"""zero_cost_runner.py — End-to-end retrieval + solve benchmark.

Mirrors the Exp 04 conditions (bm25, minilm, codesearch, hybrid, hybrid-cs,
tacm, tacm-rerank) but runs against executable_benchmark.json (SWE-bench Lite
style instances with real test infrastructure).

Pipeline per instance:
    Query → Retriever → Top-K files → GT hit check
    If hit → apply GT patch → run tests → SOLVED

Usage:
    # Retrieval-only, all conditions, Python only:
    python3 zero_cost_runner.py --retriever all --no-exec --python-only

    # Single retriever, full solve pipeline:
    python3 zero_cost_runner.py --retriever tacm
    python3 zero_cost_runner.py --retriever bm25

    # Limit to N instances:
    python3 zero_cost_runner.py --retriever tacm --no-exec --limit 10

Available retrievers: bm25, minilm, codesearch, hybrid, hybrid-cs, tacm, tacm-rerank, all
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

# Suppress HuggingFace tokenizer parallelism warnings when forking
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
TOP_K = 5
TIMEOUT = 120


# ---------------------------------------------------------------------------
# Shell utils
# ---------------------------------------------------------------------------

def _run(cmd: str, cwd=None) -> tuple[int, str, str]:
    try:
        result = subprocess.run(
            cmd, shell=True, cwd=cwd,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            timeout=TIMEOUT,
        )
        return result.returncode, result.stdout.decode(errors="replace"), result.stderr.decode(errors="replace")
    except subprocess.TimeoutExpired:
        return -1, "", "TIMEOUT"


def _clone(repo: str, workdir: str) -> tuple[int, str, str]:
    return _run(f"git clone --depth=50 https://github.com/{repo}.git", cwd=workdir)


def _checkout(repo_path: Path, commit: str) -> None:
    _run(f"git fetch --depth=50 origin {commit}", cwd=repo_path)
    _run("git reset --hard", cwd=repo_path)
    _run("git clean -fd", cwd=repo_path)
    _run(f"git checkout {commit}", cwd=repo_path)


# ---------------------------------------------------------------------------
# Patch helpers
# ---------------------------------------------------------------------------

def _apply_patch(repo_path: Path, patch_str: str) -> bool:
    p = repo_path / "temp.patch"
    p.write_text(patch_str)
    code, _, _ = _run(f"git apply --whitespace=fix {p}", cwd=repo_path)
    return code == 0


def _extract_gt_files(patch_str: str) -> list[str]:
    return [
        line.removeprefix("+++ b/").strip()
        for line in patch_str.split("\n")
        if line.startswith("+++ b/")
    ]


def _retrieval_hit(retrieved: list[str], gt_files: list[str]) -> bool:
    for gt in gt_files:
        for f in retrieved:
            if f.replace("\\", "/").endswith(gt.replace("\\", "/")):
                return True
    return False


# ---------------------------------------------------------------------------
# Test command builder
# ---------------------------------------------------------------------------

def _parse_test_ids(raw: str) -> list[str]:
    """fail_to_pass is sometimes a JSON-encoded list, sometimes a plain string."""
    raw = raw.strip()
    if raw.startswith("["):
        try:
            ids = json.loads(raw)
            if isinstance(ids, list):
                return [str(x) for x in ids]
        except json.JSONDecodeError:
            pass
    return [raw]


def _pytest_cmd(test_ids: list[str]) -> str:
    escaped = " ".join(f'"{t}"' for t in test_ids)
    return f"python3 -m pytest {escaped} -x -q --tb=no 2>&1"


def _fail_cmd(instance: dict) -> str:
    return _pytest_cmd(_parse_test_ids(instance["execution_instructions"]["run_failing_tests"]))


def _verify_cmd(instance: dict) -> str:
    raw = instance.get("fail_to_pass", instance["execution_instructions"]["run_failing_tests"])
    return _pytest_cmd(_parse_test_ids(raw))


# ---------------------------------------------------------------------------
# Shared: build TACM graph from a freshly-cloned repo
# ---------------------------------------------------------------------------

def _build_tacm_graph(repo_path: Path):
    """
    Run crg parse on repo_path and return (graph, fn_nodes).
    fn_nodes = non-test FUNCTION layer nodes.
    Raises on any failure — callers should catch and fall back.
    """
    from code_review_graph.graph import GraphStore
    from code_review_graph.incremental import get_db_path, full_build
    from tacm_v2.graph.builder import GraphBuilder
    from tacm_v2.graph.model import Layer

    db_path = get_db_path(repo_path)
    store = GraphStore(db_path)
    try:
        full_build(repo_path, store)
        graph = GraphBuilder(store).build()
    finally:
        store.close()

    fn_nodes = [
        n for n in graph.nodes.values()
        if n.layer == Layer.FUNCTION and not n.is_test
    ]
    return graph, fn_nodes


# ---------------------------------------------------------------------------
# Shared: read node source (same logic as bench_v2._read_source)
# ---------------------------------------------------------------------------

def _read_source(file_path: str, line_start: int, line_end: int) -> str:
    if not (file_path and line_start and line_end):
        return ""
    try:
        lines = Path(file_path).read_text(errors="replace").splitlines()
        return "\n".join(lines[max(0, line_start - 1): min(len(lines), line_end)])
    except OSError:
        return ""


# ---------------------------------------------------------------------------
# Shared: node → relative file path
# ---------------------------------------------------------------------------

def _node_files(nodes, repo_path: Path, top_k: int) -> list[str]:
    """Deduplicate to file level, return top_k relative paths."""
    seen: set[str] = set()
    result: list[str] = []
    for n in nodes:
        fp = getattr(n, "file_path", None)
        if not fp or fp in seen:
            continue
        seen.add(fp)
        try:
            rel = str(Path(fp).relative_to(repo_path))
        except ValueError:
            rel = fp
        result.append(rel)
        if len(result) >= top_k:
            break
    return result


# ---------------------------------------------------------------------------
# BM25 (function-level, matching bench_v2.bm25_rank_nodes)
# ---------------------------------------------------------------------------

def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zA-Z_]\w*", text.lower())


def _bm25_rank(nodes, query: str) -> list:
    """Return fn_nodes sorted by BM25 score descending."""
    prod = [n for n in nodes if not n.is_test]
    if not prod:
        return []
    q_tokens = _tokenize(query)
    if not q_tokens:
        return prod

    corpus_texts = [
        _read_source(n.file_path or "", n.line_start or 0, n.line_end or 0) or n.name
        for n in prod
    ]
    corpus = [_tokenize(t) for t in corpus_texts]
    N = len(corpus)
    k1, b = 1.5, 0.75

    df: dict[str, int] = {}
    for doc in corpus:
        for term in set(doc):
            df[term] = df.get(term, 0) + 1

    idf = {
        t: math.log((N - df.get(t, 0) + 0.5) / (df.get(t, 0) + 0.5) + 1)
        for t in q_tokens
    }
    avgdl = sum(len(d) for d in corpus) / N if N else 1.0

    scores = []
    for doc in corpus:
        dl = len(doc)
        tf_map: dict[str, int] = {}
        for term in doc:
            tf_map[term] = tf_map.get(term, 0) + 1
        s = sum(
            idf.get(t, 0.0) * (
                tf_map.get(t, 0) * (k1 + 1) /
                (tf_map.get(t, 0) + k1 * (1 - b + b * dl / avgdl))
            )
            for t in q_tokens
        )
        scores.append(s)

    return [n for _, n in sorted(zip(scores, prod), key=lambda x: -x[0])]


# ---------------------------------------------------------------------------
# Dense embedding helpers
# ---------------------------------------------------------------------------

_ST_MODEL_CACHE: dict[str, object] = {}


def _get_st_model(model_name: str):
    if model_name not in _ST_MODEL_CACHE:
        from sentence_transformers import SentenceTransformer
        print(f"  [loading model {model_name}...]")
        _ST_MODEL_CACHE[model_name] = SentenceTransformer(model_name)
    return _ST_MODEL_CACHE[model_name]


def _build_st_index(nodes, model_name: str) -> tuple | None:
    try:
        model = _get_st_model(model_name)
        corpus = [
            (n, _read_source(n.file_path or "", n.line_start or 0, n.line_end or 0) or n.name)
            for n in nodes if not n.is_test
        ]
        if not corpus:
            return None
        node_list = [n for n, _ in corpus]
        texts = [t for _, t in corpus]
        vecs = model.encode(texts, batch_size=64, show_progress_bar=False, normalize_embeddings=True)
        return node_list, vecs, model
    except Exception as e:
        print(f"    [embedding index failed: {e}]")
        return None


def _dense_rank(query: str, index: tuple) -> list:
    """Return nodes sorted by cosine similarity descending."""
    import numpy as np
    node_list, vecs, model = index
    q_vec = model.encode([query], normalize_embeddings=True)[0]
    sims = vecs @ q_vec
    order = list(int(i) for i in np.argsort(-sims))
    return [node_list[i] for i in order]


def _rrf_rank(ranked_a: list, ranked_b: list, k: int = 60) -> list:
    """Reciprocal Rank Fusion of two ranked node lists."""
    scores: dict[int, float] = {}
    for rank, n in enumerate(ranked_a, 1):
        nid = id(n)
        scores[nid] = scores.get(nid, 0.0) + 1.0 / (k + rank)
    for rank, n in enumerate(ranked_b, 1):
        nid = id(n)
        scores[nid] = scores.get(nid, 0.0) + 1.0 / (k + rank)

    # collect all unique nodes preserving first-seen order reference
    seen: dict[int, object] = {}
    for n in ranked_a + ranked_b:
        if id(n) not in seen:
            seen[id(n)] = n

    return sorted(seen.values(), key=lambda n: -scores.get(id(n), 0.0))


# ---------------------------------------------------------------------------
# OpenAI helpers (for tacm-rerank)
# ---------------------------------------------------------------------------

def _load_openai_key() -> str:
    key = os.environ.get("OPENAI_API_KEY", "")
    if not key:
        env_path = ROOT / ".env"
        if env_path.exists():
            for line in env_path.read_text().splitlines():
                if line.startswith("OPENAI_API_KEY="):
                    key = line.split("=", 1)[1].strip()
                    break
    if not key:
        raise RuntimeError("OPENAI_API_KEY not found")
    return key


def _llm_rerank(query: str, candidates: list, top_n: int = 20, delay: float = 2.5) -> list:
    """Rerank top-N candidates with gpt-4o-mini. Falls back to TACM order on error."""
    try:
        from openai import OpenAI
        client = OpenAI(api_key=_load_openai_key())
    except Exception:
        return candidates

    pool = candidates[:top_n]
    if not pool:
        return candidates

    lines = []
    for i, node in enumerate(pool, 1):
        src = _read_source(node.file_path or "", node.line_start or 0,
                           min(node.line_end or 0, (node.line_start or 0) + 4))
        first_line = src.strip().splitlines()[0][:120] if src.strip() else ""
        lines.append(
            f"{i}. {node.node_id}\n"
            f"   file: {node.file_path or ''}\n"
            f"   code: {first_line}"
        )

    prompt = (
        f"Bug report: {query}\n\n"
        f"Which of these {len(pool)} functions is most likely to contain the bug?\n"
        f"Return ONLY a comma-separated list of numbers, ranked most to least likely.\n"
        f"Example: 3,1,7,2,...\n\n"
        + "\n".join(lines)
        + "\n\nRanking:"
    )

    try:
        time.sleep(delay)
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=80,
            temperature=0.0,
        )
        raw = resp.choices[0].message.content.strip()
        indices = []
        for tok in re.split(r"[,\s]+", raw):
            tok = tok.strip().rstrip(".")
            if tok.isdigit():
                idx = int(tok) - 1
                if 0 <= idx < len(pool) and idx not in indices:
                    indices.append(idx)

        if not indices:
            return candidates

        reranked = [pool[i] for i in indices]
        seen_set = set(indices)
        for i, n in enumerate(pool):
            if i not in seen_set:
                reranked.append(n)
        reranked.extend(candidates[top_n:])
        return reranked
    except Exception:
        return candidates


# ---------------------------------------------------------------------------
# Per-condition retrieval: returns ranked fn_nodes
# ---------------------------------------------------------------------------

def _retrieve(condition: str, query: str, graph, fn_nodes: list) -> list:
    """
    Run the named retrieval condition and return fn_nodes ranked best-first.
    graph and fn_nodes come from _build_tacm_graph().
    """
    if condition == "bm25":
        return _bm25_rank(fn_nodes, query)

    if condition == "minilm":
        idx = _build_st_index(fn_nodes, "sentence-transformers/all-MiniLM-L6-v2")
        return _dense_rank(query, idx) if idx else _bm25_rank(fn_nodes, query)

    if condition == "codesearch":
        idx = _build_st_index(fn_nodes, "flax-sentence-embeddings/st-codesearch-distilroberta-base")
        return _dense_rank(query, idx) if idx else _bm25_rank(fn_nodes, query)

    if condition == "hybrid":
        bm25_ranked = _bm25_rank(fn_nodes, query)
        idx = _build_st_index(fn_nodes, "sentence-transformers/all-MiniLM-L6-v2")
        if idx:
            dense_ranked = _dense_rank(query, idx)
            return _rrf_rank(bm25_ranked, dense_ranked)
        return bm25_ranked

    if condition == "hybrid-cs":
        bm25_ranked = _bm25_rank(fn_nodes, query)
        idx = _build_st_index(fn_nodes, "flax-sentence-embeddings/st-codesearch-distilroberta-base")
        if idx:
            dense_ranked = _dense_rank(query, idx)
            return _rrf_rank(bm25_ranked, dense_ranked)
        return bm25_ranked

    if condition == "tacm":
        from tacm_v2.layers.serializers import serialize
        from tacm_v2.selector.intent import classify_intent
        from tacm_v2.selector.scoring import NodeScorer
        intent = classify_intent(query)
        all_nodes = [n for n in graph.nodes.values() if not n.is_test]
        texts = {n.node_id: serialize(n, graph) for n in all_nodes}
        scorer = NodeScorer(graph, query, intent, texts)
        scores = scorer.score_all(fn_nodes)
        return sorted(fn_nodes, key=lambda n: -scores[n.node_id])

    if condition == "tacm-rerank":
        from tacm_v2.layers.serializers import serialize
        from tacm_v2.selector.intent import classify_intent
        from tacm_v2.selector.scoring import NodeScorer
        intent = classify_intent(query)
        all_nodes = [n for n in graph.nodes.values() if not n.is_test]
        texts = {n.node_id: serialize(n, graph) for n in all_nodes}
        scorer = NodeScorer(graph, query, intent, texts)
        scores = scorer.score_all(fn_nodes)
        tacm_ranked = sorted(fn_nodes, key=lambda n: -scores[n.node_id])
        return _llm_rerank(query, tacm_ranked[:40])

    raise ValueError(f"Unknown condition: {condition}")


# ---------------------------------------------------------------------------
# Core: single instance × single condition
# ---------------------------------------------------------------------------

def _run_condition(
    condition: str,
    instance: dict,
    repo_path: Path,
    gt_files: list[str],
    top_k: int,
    no_exec: bool,
    graph,
    fn_nodes: list,
) -> dict:
    """
    Retrieve under one condition, check hit, optionally apply patch + run tests.
    graph and fn_nodes are built once per instance and shared across conditions.
    Returns a result dict.
    """
    result = dict(
        condition=condition,
        retrieval_hit=False,
        patch_applied=False,
        tests_passed=False,
        solved=False,
        skip_reason=None,
    )

    try:
        ranked = _retrieve(condition, instance["query"], graph, fn_nodes)
    except Exception as e:
        print(f"    [{condition}] retrieval failed: {e}")
        result["skip_reason"] = "retrieval_failed"
        return result

    retrieved_files = _node_files(ranked, repo_path, top_k)
    hit = _retrieval_hit(retrieved_files, gt_files)
    result["retrieval_hit"] = hit

    status = "HIT " if hit else "MISS"
    print(f"    [{condition}] {status}  top-files: {retrieved_files[:3]}")

    if no_exec or not hit:
        return result

    # Apply patch + verify
    if not _apply_patch(repo_path, instance["patch"]):
        print(f"    [{condition}] patch failed")
        result["patch_applied"] = False
        return result
    result["patch_applied"] = True

    rc, _, _ = _run(_verify_cmd(instance), cwd=repo_path)
    passed = rc == 0
    result["tests_passed"] = passed
    result["solved"] = passed
    print(f"    [{condition}] {'SOLVED' if passed else 'tests still failing'}")

    return result


# ---------------------------------------------------------------------------
# Instance runner
# ---------------------------------------------------------------------------

def run_instance(
    instance: dict,
    conditions: list[str],
    no_exec: bool,
    top_k: int,
) -> list[dict]:
    """Clone once, run all conditions, return list of per-condition result dicts."""
    iid = instance.get("instance_id", str(instance.get("id", "?")))
    print(f"\n--- {iid} [{instance.get('language','?')}] ---")

    gt_files = _extract_gt_files(instance.get("patch", ""))
    if not gt_files:
        print("  ⚠  No GT files in patch — skipping")
        return [dict(instance_id=iid, repo=instance["repo"],
                     language=instance.get("language", "?"),
                     condition=c, retrieval_hit=False, patch_applied=False,
                     tests_passed=False, solved=False,
                     skip_reason="no_gt_files") for c in conditions]

    print(f"  GT files: {gt_files}")

    base_result = dict(instance_id=iid, repo=instance["repo"], language=instance.get("language", "?"))

    with tempfile.TemporaryDirectory() as tmpdir:
        rc, _, err = _clone(instance["repo"], tmpdir)
        if rc != 0:
            print(f"  ⚠  Clone failed: {err[:120]}")
            return [{**base_result, "condition": c, "retrieval_hit": False,
                     "patch_applied": False, "tests_passed": False,
                     "solved": False, "skip_reason": "clone_failed"} for c in conditions]

        repo_name = instance["repo"].split("/")[-1]
        repo_path = Path(tmpdir) / repo_name
        _checkout(repo_path, instance["base_commit"])

        if not no_exec:
            # Sanity: pre-patch tests should fail
            rc_fail, _, _ = _run(_fail_cmd(instance), cwd=repo_path)
            if rc_fail == 0:
                print("  ⚠  Tests already passing before patch — skipping")
                return [{**base_result, "condition": c, "retrieval_hit": False,
                         "patch_applied": False, "tests_passed": False,
                         "solved": False, "skip_reason": "already_passing"} for c in conditions]
            print("  ✓  Pre-patch sanity: tests failing as expected")

        # Build graph once — shared across all conditions
        try:
            graph, fn_nodes = _build_tacm_graph(repo_path)
        except Exception as e:
            print(f"  ⚠  Graph build failed: {e}")
            return [{**base_result, "condition": c, "retrieval_hit": False,
                     "patch_applied": False, "tests_passed": False,
                     "solved": False, "skip_reason": "graph_build_failed"} for c in conditions]

        if not fn_nodes:
            print("  ⚠  No function nodes parsed")
            return [{**base_result, "condition": c, "retrieval_hit": False,
                     "patch_applied": False, "tests_passed": False,
                     "solved": False, "skip_reason": "no_fn_nodes"} for c in conditions]

        print(f"  ✓  Graph: {len(fn_nodes)} function nodes")

        condition_results = []
        for condition in conditions:
            r = _run_condition(condition, instance, repo_path, gt_files, top_k, no_exec, graph, fn_nodes)
            condition_results.append({**base_result, **r})

            # Reset repo between conditions if patch was applied
            if r.get("patch_applied"):
                _run("git checkout -- .", cwd=repo_path)

    return condition_results


# ---------------------------------------------------------------------------
# Benchmark runner + summary
# ---------------------------------------------------------------------------

def run_benchmark(
    dataset_path: str,
    conditions: list[str],
    no_exec: bool = False,
    python_only: bool = False,
    limit: int | None = None,
    top_k: int = TOP_K,
) -> None:
    with open(dataset_path) as f:
        dataset = json.load(f)

    if python_only:
        dataset = [x for x in dataset if x.get("language", "") == "Python"]
        print(f"  (python-only filter: {len(dataset)} instances)")

    if limit:
        dataset = dataset[:limit]

    all_results: list[dict] = []
    for instance in dataset:
        results = run_instance(instance, conditions, no_exec, top_k)
        all_results.extend(results)

    # ---- Per-condition summary ----
    print(f"\n{'='*60}")
    print(f"Dataset : {dataset_path}  |  Mode: {'retrieval-only' if no_exec else 'full solve'}")
    print(f"{'='*60}")
    print(f"{'Condition':<16} {'N':>4} {'Skipped':>7} {'Hit@K':>7}" + ("  Solved" if not no_exec else ""))
    print(f"{'-'*60}")

    for cond in conditions:
        rows = [r for r in all_results if r["condition"] == cond]
        valid = [r for r in rows if r["skip_reason"] is None]
        skipped = len(rows) - len(valid)
        n = len(valid)
        hits = sum(1 for r in valid if r["retrieval_hit"])
        hit_pct = f"{hits/n:.1%}" if n else "—"
        line = f"{cond:<16} {n:>4} {skipped:>7} {hit_pct:>7}"
        if not no_exec:
            solved = sum(1 for r in valid if r["solved"])
            line += f"  {solved/n:.1%}" if n else "  —"
        print(line)

    print(f"{'='*60}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

ALL_CONDITIONS = ["bm25", "minilm", "codesearch", "hybrid", "hybrid-cs", "tacm", "tacm-rerank"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zero-cost retrieval + solve benchmark")
    parser.add_argument(
        "--retriever", default="bm25",
        help=f"Condition(s) to run. 'all' = all conditions. Comma-separated or space-separated. Choices: {ALL_CONDITIONS + ['all']}",
    )
    parser.add_argument(
        "--dataset", default="executable_benchmark.json",
        help="Path to benchmark JSON (default: executable_benchmark.json)",
    )
    parser.add_argument(
        "--no-exec", action="store_true",
        help="Retrieval-only — skip patch application and test execution",
    )
    parser.add_argument(
        "--python-only", action="store_true",
        help="Skip non-Python instances",
    )
    parser.add_argument(
        "--limit", type=int, default=None,
        help="Only run first N instances",
    )
    parser.add_argument(
        "--top-k", type=int, default=TOP_K,
        help=f"Files to retrieve per query (default: {TOP_K})",
    )
    args = parser.parse_args()

    # Parse conditions
    raw = args.retriever
    if raw == "all":
        conditions = ALL_CONDITIONS
    else:
        conditions = [c.strip() for c in raw.replace(",", " ").split()]

    for c in conditions:
        if c not in ALL_CONDITIONS:
            parser.error(f"Unknown retriever '{c}'. Valid: {ALL_CONDITIONS + ['all']}")

    run_benchmark(
        dataset_path=args.dataset,
        conditions=conditions,
        no_exec=args.no_exec,
        python_only=args.python_only,
        limit=args.limit,
        top_k=args.top_k,
    )
