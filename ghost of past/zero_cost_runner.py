"""zero_cost_runner.py — Function-level retrieval benchmark.

Evaluates retrieval quality at **function granularity**: did the retriever
put the exact GT function(s) changed in the patch into its top-K?

This is the correct metric for a zero-LLM-call context retriever whose job
is to hand a small coding agent the precise functions it needs — not just
the right file.  File-level hit is tracked as a secondary reference metric.

Primary metrics:
    Fn-Hit@K   — did any GT function appear in the top-K ranked functions?
    Fn-MRR     — mean reciprocal rank of the first GT function hit
    Tokens     — total tokens consumed by top-K context (efficiency)

Secondary metrics:
    File-Hit@K — did a GT file appear (legacy, for reference)

Pipeline per instance:
    Query → Retriever → Ranked functions → GT function match
    If --exec and fn-hit → apply GT patch → run tests → SOLVED

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
import random
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
SEED = 42          # pinned across runs; controls random / numpy / torch
BOOTSTRAP_N = 2000 # paired-bootstrap samples for CIs and p-values


def _pin_seeds(seed: int = SEED) -> None:
    """Pin every RNG we can reach so dense retrievers are deterministic.

    Embedding models (MiniLM, CodeSearch) are otherwise run-to-run noisy
    because of nondeterministic matmul ordering on some BLAS backends.
    Called once at benchmark start *and* re-called before each dense
    index build so a seed set by one retriever doesn't leak into another.
    """
    random.seed(seed)
    os.environ.setdefault("PYTHONHASHSEED", str(seed))
    try:
        import numpy as np
        np.random.seed(seed)
    except Exception:
        pass
    try:
        import torch
        torch.manual_seed(seed)
        torch.use_deterministic_algorithms(False)  # too strict for SBERT
    except Exception:
        pass


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


# ---------------------------------------------------------------------------
# Function-level GT extraction from unified diff
# ---------------------------------------------------------------------------

_HUNK_RE  = re.compile(r"^@@ .+ @@(.*)$")
_FILE_RE  = re.compile(r"^\+\+\+ b/(.+)$")

# Hunk header context: git puts the enclosing function/class after @@
# e.g. "@@ -242,7 +242,7 @@ def _cstack(left, right):"
# Covers Python, Java, JS/TS, Rust, Go, C/C++, Ruby, Kotlin, Swift
_HUNK_CTX_FN_PATTERNS = [
    re.compile(r"def\s+(\w+)\s*\("),                          # Python
    re.compile(r"fn\s+(\w+)\s*[\(<]"),                         # Rust
    re.compile(r"func\s+(?:\([^)]*\)\s*)?(\w+)\s*\("),        # Go (incl. method receiver)
    re.compile(r"(?:function|async\s+function)\s+(\w+)\s*\("), # JS/TS
    re.compile(r"(?:public|private|protected|static|final|abstract|override|suspend|internal)\s+[\w<>\[\]?,\s]*\s+(\w+)\s*\("),  # Java/Kotlin/C# (requires access modifier)
    re.compile(r"(?:export\s+)?(?:default\s+)?(?:async\s+)?(\w+)\s*(?:=|:)\s*(?:function|\([^)]*\)\s*=>)"),  # JS arrow/assigned
]
_HUNK_CTX_CLASS_RE = re.compile(r"class\s+(\w+)[\s:({\[]")
_HUNK_CTX_STRUCT_RE = re.compile(r"(?:struct|impl|enum|trait|interface)\s+(\w+)")

# Content line parsers — multi-language
_DEF_PATTERNS = [
    (re.compile(r"^[ +\-]?(\s*)def\s+(\w+)\s*\("), "python"),
    (re.compile(r"^[ +\-]?(\s*)fn\s+(\w+)\s*[\(<]"), "rust"),
    (re.compile(r"^[ +\-]?(\s*)func\s+(?:\([^)]*\)\s*)?(\w+)\s*\("), "go"),
    (re.compile(r"^[ +\-]?(\s*)(?:function|async\s+function)\s+(\w+)\s*\("), "js"),
    (re.compile(r"^[ +\-]?(\s*)(?:public|private|protected|static|final|abstract|override|suspend|internal)\s+[\w<>\[\]?,\s]*\s+(\w+)\s*\("), "java"),
]
_CLASS_RE = re.compile(r"^[ +\-]?(\s*)(?:class|struct|impl|enum|trait|interface)\s+(\w+)[\s:({\[]")


def _extract_gt_functions(patch_str: str) -> tuple[list[str], list[str], list[str]]:
    """Extract (gt_functions, gt_files, gt_classes) from unified diff.

    gt_functions: qualified names like "ClassName.method_name" or "function_name"
    gt_files:     file paths like "astropy/modeling/separable.py"
    gt_classes:   class names that contain the changed functions

    Handles two sources of function names:
    1. `def` lines that appear as actual diff content (+/- or context lines)
    2. Hunk headers: `@@ ... @@ def func_name(...)` — git embeds the nearest
       enclosing function/class definition here. Most SWE-bench patches modify
       code *inside* an existing function without touching the `def` line, so
       the hunk header is often the only place the function name appears.
    """
    gt_functions: list[str] = []
    gt_files: list[str] = []
    gt_classes: list[str] = []
    seen_fns: set[str] = set()
    seen_cls: set[str] = set()
    context_stack: list[tuple[int, str, bool]] = []  # (indent, name, is_class)
    in_hunk = False
    hunk_has_content_def = False  # tracks if hunk had a def in its diff lines

    for line in patch_str.splitlines():
        fm = _FILE_RE.match(line)
        if fm:
            fpath = fm.group(1)
            gt_files.append(fpath)
            context_stack = []
            in_hunk = False
            continue

        hm = _HUNK_RE.match(line)
        if hm:
            in_hunk = True
            hunk_has_content_def = False
            # Parse hunk header context to seed the stack.
            hunk_ctx = hm.group(1).strip() if hm.group(1) else ""
            if hunk_ctx:
                context_stack = []
                # Check for class/struct/impl
                hc = _HUNK_CTX_CLASS_RE.search(hunk_ctx)
                if not hc:
                    hc = _HUNK_CTX_STRUCT_RE.search(hunk_ctx)
                if hc:
                    context_stack.append((0, hc.group(1), True))
                # Check for function across languages
                hd = None
                for pat in _HUNK_CTX_FN_PATTERNS:
                    hd = pat.search(hunk_ctx)
                    if hd:
                        break
                if hd:
                    context_stack.append((4 if hc else 0, hd.group(1), False))
            continue

        cm = _CLASS_RE.match(line)
        if cm and not line.startswith("---"):
            indent = len(cm.group(1))
            while context_stack and context_stack[-1][0] >= indent:
                context_stack.pop()
            context_stack.append((indent, cm.group(2), True))

        # Try multi-language def patterns
        dm = None
        for pat, _lang in _DEF_PATTERNS:
            dm = pat.match(line)
            if dm:
                break
        if dm and not line.startswith("---"):
            indent = len(dm.group(1))
            while context_stack and context_stack[-1][0] >= indent:
                context_stack.pop()
            fn_name = dm.group(2)
            context_stack.append((indent, fn_name, False))
            if in_hunk:
                hunk_has_content_def = True

        if in_hunk and line.startswith(("-", "+")) and not line.startswith(("---", "+++")):
            classes = [n for (_, n, is_cls) in context_stack if is_cls]
            fns     = [n for (_, n, is_cls) in context_stack if not is_cls]
            if fns:
                fn = fns[-1]
                gt = f"{classes[-1]}.{fn}" if classes else fn
                if gt not in seen_fns:
                    seen_fns.add(gt)
                    gt_functions.append(gt)
                for cls in classes:
                    if cls not in seen_cls:
                        seen_cls.add(cls)
                        gt_classes.append(cls)

    return gt_functions, list(dict.fromkeys(gt_files)), gt_classes


# ---------------------------------------------------------------------------
# GT matching helpers
# ---------------------------------------------------------------------------

def _fn_matches_gt_strict(
    node_id: str,
    node_file: str,
    gt_fn: str,
    gt_files: list[str],
) -> bool:
    """Strict match: function short name AND file path suffix must both agree."""
    gt_fn_short = gt_fn.split(".")[-1]
    node_fn_part = node_id.split("::")[-1] if "::" in node_id else node_id
    node_fn_short = node_fn_part.split(".")[-1]
    if gt_fn_short != node_fn_short:
        return False
    node_path = node_file or (node_id.split("::")[0] if "::" in node_id else "")
    for gt_file in gt_files:
        if node_path.replace("\\", "/").endswith(gt_file.replace("\\", "/")):
            return True
    return False


def _fn_matches_gt_lenient(node_id: str, gt_fn: str) -> bool:
    """Lenient match: short function name only."""
    gt_fn_short = gt_fn.split(".")[-1]
    node_fn_part = node_id.split("::")[-1] if "::" in node_id else node_id
    node_fn_short = node_fn_part.split(".")[-1]
    return gt_fn_short == node_fn_short


def _file_matches_gt(node_file: str, gt_files: list[str]) -> bool:
    """File-level match: node's file path ends with GT relative path."""
    if not node_file or not gt_files:
        return False
    for gt_file in gt_files:
        if node_file.replace("\\", "/").endswith(gt_file.replace("\\", "/")):
            return True
    return False


def _classify_miss(
    match: dict,
    gt_fns: list[str],
    gt_files: list[str],
    fn_nodes: list,
    top_k: int,
) -> str:
    """Label the retrieval outcome with a single bucket (Gap 4).

    Buckets:
      hit                  — strict match inside top-K
      right_file_wrong_fn  — file match inside top-K, no fn match
      ranked_outside_k     — strict fn match exists but rank > top_k
      gt_not_in_pool       — GT fn does not appear anywhere in fn_nodes
                             (e.g. parser skipped it, it lives in a test file,
                              or the patch touches a non-function line only)
      no_gt_fn             — no function-level GT could be extracted at all
                             (only file-level GT available)
      miss_other           — GT in pool, lenient match somewhere, strict miss
                             (usually a path-suffix mismatch)
    """
    if not gt_fns:
        return "no_gt_fn"
    if match["strict_rank"] is not None and match["strict_rank"] <= top_k:
        return "hit"
    if match["strict_rank"] is not None:
        return "ranked_outside_k"
    # No strict hit anywhere. Is the GT even in the candidate pool?
    gt_short = {gt.split(".")[-1] for gt in gt_fns}
    gt_files_norm = [gf.replace("\\", "/") for gf in gt_files]
    in_pool = False
    for n in fn_nodes:
        nfile = (getattr(n, "file_path", "") or "").replace("\\", "/")
        nid = getattr(n, "node_id", "") or ""
        nshort = nid.split("::")[-1].split(".")[-1]
        if nshort not in gt_short:
            continue
        if any(nfile.endswith(gf) for gf in gt_files_norm):
            in_pool = True
            break
    if not in_pool:
        return "gt_not_in_pool"
    if match["file_rank"] is not None and match["file_rank"] <= top_k:
        return "right_file_wrong_fn"
    return "miss_other"


def _match_ranked_functions(
    ranked_nodes: list,
    gt_fns: list[str],
    gt_files: list[str],
    top_k: int,
) -> dict:
    """Match ranked function nodes against GT. Returns metrics dict.

    Ranks are computed over the **full ranked list** (true MRR semantics).
    The ``top_k`` argument is only used to compute ``top_k_tokens`` and the
    Hit@K boolean derived upstream (``fn_hit = strict_rank <= top_k``).

    Returns:
        strict_rank:  1-based rank of first strict fn match in full list, or None
        lenient_rank: 1-based rank of first lenient fn match in full list, or None
        file_rank:    1-based rank of first file match in full list, or None
        top_k_tokens: total tokens in the top-K nodes (for efficiency metric)
    """
    strict_rank = None
    lenient_rank = None
    file_rank = None
    top_k_tokens = 0

    for rank, node in enumerate(ranked_nodes, 1):
        nid = getattr(node, "node_id", getattr(node, "qualified_name", ""))
        nfile = getattr(node, "file_path", "") or ""
        tcost = getattr(node, "token_cost", 0)
        if rank <= top_k:
            top_k_tokens += tcost

        for gt_fn in gt_fns:
            if strict_rank is None and _fn_matches_gt_strict(nid, nfile, gt_fn, gt_files):
                strict_rank = rank
            if lenient_rank is None and _fn_matches_gt_lenient(nid, gt_fn):
                lenient_rank = rank
        if file_rank is None and _file_matches_gt(nfile, gt_files):
            file_rank = rank

        if strict_rank and lenient_rank and file_rank and rank >= top_k:
            break

    return {
        "strict_rank": strict_rank,
        "lenient_rank": lenient_rank,
        "file_rank": file_rank,
        "top_k_tokens": top_k_tokens,
    }


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


# Per-instance embedding index cache. Keyed on (id(fn_nodes), model_name)
# so the same index is reused across conditions (minilm / hybrid /
# hybrid-cs / codesearch) within one instance instead of rebuilt 4×.
# Cleared between instances so stale indexes from the previous repo
# don't leak in.
_INDEX_CACHE: dict[tuple[int, str], tuple] = {}


def _clear_index_cache() -> None:
    _INDEX_CACHE.clear()


def _build_st_index(nodes, model_name: str) -> tuple | None:
    cache_key = (id(nodes), model_name)
    if cache_key in _INDEX_CACHE:
        return _INDEX_CACHE[cache_key]
    try:
        _pin_seeds()  # re-pin before every build so order-of-retrievers doesn't matter
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
        index = (node_list, vecs, model)
        _INDEX_CACHE[cache_key] = index
        return index
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

    if condition in ("tacm", "tacm-ppr"):
        from tacm_v2.graph.model import Layer
        from tacm_v2.layers.serializers import serialize, serialize_function_for_scoring
        from tacm_v2.selector.intent import classify_intent
        from tacm_v2.selector.scoring import NodeScorer
        from tacm_v2.selector.config import SelectorConfig, DEFAULT_CONFIG
        intent = classify_intent(query)
        all_nodes = [n for n in graph.nodes.values() if not n.is_test]
        # Use the same (agent_text, scoring_text) split as selector.select() —
        # scoring on agent-facing text alone under-reports TACM because
        # serialize_function_for_scoring includes docstring+signature context
        # that production uses.
        agent_texts = {n.node_id: serialize(n, graph) for n in all_nodes}
        score_texts = {
            n.node_id: (
                serialize_function_for_scoring(n, graph)
                if n.layer == Layer.FUNCTION else agent_texts[n.node_id]
            )
            for n in all_nodes
        }
        # tacm-ppr flips on Personalized PageRank — BM25 top-K seed the teleport
        # vector so the structural signal becomes query-aware. Everything else
        # is identical to the `tacm` path.
        cfg = (
            SelectorConfig(ppr_enabled=True)
            if condition == "tacm-ppr"
            else DEFAULT_CONFIG
        )
        scorer = NodeScorer(graph, query, intent, score_texts, config=cfg)
        scores = scorer.score_all(fn_nodes)
        return sorted(fn_nodes, key=lambda n: -scores[n.node_id])

    if condition == "tacm-rerank":
        from tacm_v2.graph.model import Layer
        from tacm_v2.layers.serializers import serialize, serialize_function_for_scoring
        from tacm_v2.selector.intent import classify_intent
        from tacm_v2.selector.scoring import NodeScorer
        intent = classify_intent(query)
        all_nodes = [n for n in graph.nodes.values() if not n.is_test]
        agent_texts = {n.node_id: serialize(n, graph) for n in all_nodes}
        score_texts = {
            n.node_id: (
                serialize_function_for_scoring(n, graph)
                if n.layer == Layer.FUNCTION else agent_texts[n.node_id]
            )
            for n in all_nodes
        }
        scorer = NodeScorer(graph, query, intent, score_texts)
        scores = scorer.score_all(fn_nodes)
        tacm_ranked = sorted(fn_nodes, key=lambda n: -scores[n.node_id])
        return _llm_rerank(query, tacm_ranked[:40])

    raise ValueError(f"Unknown condition: {condition}")


# ---------------------------------------------------------------------------
# TACM Trace — per-instance diagnostic HTML
# ---------------------------------------------------------------------------

_TRACE_DIR = ROOT / "tacm_traces"

def _generate_tacm_trace(
    instance_id: str,
    query: str,
    condition: str,
    graph,
    fn_nodes: list,
    ranked_nodes: list,
    gt_fns: list[str],
    gt_files: list[str],
    top_k: int,
    match_result: dict,
) -> str:
    """Build a per-instance diagnostic HTML trace and write it to disk.

    Returns the path of the generated HTML file.
    """
    from tacm_v2.layers.serializers import serialize
    from tacm_v2.selector.intent import classify_intent, INTENT_WEIGHTS, LAYER_BUDGETS
    from tacm_v2.selector.scoring import (
        NodeScorer, compute_bm25, compute_fan_in, compute_fan_out,
        compute_complexity, compute_test_cover, compute_neighborhood_bonus,
        compute_pagerank,
    )
    from tacm_v2.graph.model import Layer, EdgeKind
    from collections import Counter

    intent = classify_intent(query)
    weights_tuple = INTENT_WEIGHTS[intent]
    weight_names = ["bm25", "fan_in", "fan_out", "complexity", "test_cover"]
    weights = dict(zip(weight_names, weights_tuple))
    layer_budgets = dict(zip(["file", "class", "function"], LAYER_BUDGETS[intent]))

    all_nodes_list = [n for n in graph.nodes.values() if not n.is_test]
    texts = {n.node_id: serialize(n, graph) for n in all_nodes_list}
    scorer = NodeScorer(graph, query, intent, texts)

    name_counts = Counter(
        (n.name, n.file_path) for n in graph.nodes.values()
        if n.layer.name == "FUNCTION"
    )

    # Per-signal scoring for all fn_nodes
    bm25     = compute_bm25(query, fn_nodes, texts)
    fan_in   = compute_fan_in(fn_nodes, graph, name_counts)
    fan_out  = compute_fan_out(fn_nodes, graph)
    cmplx    = compute_complexity(fn_nodes)
    test_cov = compute_test_cover(fn_nodes, graph)
    nbr      = compute_neighborhood_bonus(fn_nodes, graph, scorer.score_all(fn_nodes))
    pr       = compute_pagerank(fn_nodes, graph)

    # GT sets for quick lookup
    gt_fn_shorts = {fn.split(".")[-1] for fn in gt_fns}
    gt_file_set  = {f.replace("\\", "/") for f in gt_files}

    def _is_gt(node) -> str:
        """Returns 'strict', 'lenient', or '' to classify GT match."""
        nid = getattr(node, "node_id", "")
        nfile = getattr(node, "file_path", "") or ""
        for gt_fn in gt_fns:
            if _fn_matches_gt_strict(nid, nfile, gt_fn, gt_files):
                return "strict"
        for gt_fn in gt_fns:
            if _fn_matches_gt_lenient(nid, gt_fn):
                return "lenient"
        return ""

    def _short(nid: str) -> str:
        return nid.split("::")[-1] if "::" in nid else nid.split("/")[-1]

    def _short_file(fp: str) -> str:
        p = Path(fp)
        parts = p.parts
        return str(Path(*parts[-3:])) if len(parts) >= 3 else fp

    # Build ranked list data (top 30)
    ranked_data = []
    for rank, node in enumerate(ranked_nodes[:30], 1):
        nid = node.node_id
        nfile = node.file_path or ""
        gt_tag = _is_gt(node)
        ranked_data.append({
            "rank": rank,
            "id": nid,
            "short": _short(nid),
            "file": _short_file(nfile),
            "line": node.line_start or 0,
            "tokens": node.token_cost,
            "in_topk": rank <= top_k,
            "gt": gt_tag,
            "signals": {
                "bm25":       round(bm25.get(nid, 0), 4),
                "fan_in":     round(fan_in.get(nid, 0), 4),
                "fan_out":    round(fan_out.get(nid, 0), 4),
                "complexity": round(cmplx.get(nid, 0), 4),
                "test_cover": round(test_cov.get(nid, 0), 4),
                "nbr_bonus":  round(nbr.get(nid, 0), 4),
                "pagerank":   round(pr.get(nid, 0), 4),
            },
        })

    # Where are the GT functions in the full ranking?
    gt_positions = []
    for rank, node in enumerate(ranked_nodes, 1):
        gt_tag = _is_gt(node)
        if gt_tag:
            gt_positions.append({
                "rank": rank,
                "id": node.node_id,
                "short": _short(node.node_id),
                "file": _short_file(node.file_path or ""),
                "gt": gt_tag,
                "bm25": round(bm25.get(node.node_id, 0), 4),
            })

    # Neighbor edges for top-K nodes
    edges_data = []
    top_k_ids = {ranked_nodes[i].node_id for i in range(min(top_k, len(ranked_nodes)))}
    for nid in top_k_ids:
        for e in graph.out_adj.get(nid, []):
            if e.kind == EdgeKind.CALLS and e.target_id in graph.nodes:
                tgt = graph.nodes[e.target_id]
                edges_data.append({
                    "src": _short(nid), "tgt": _short(e.target_id),
                    "kind": "CALLS", "tgt_gt": _is_gt(tgt) if hasattr(tgt, 'node_id') else "",
                })
        for e in graph.in_adj.get(nid, []):
            if e.kind == EdgeKind.CALLS and e.source_id in graph.nodes:
                src_node = graph.nodes[e.source_id]
                edges_data.append({
                    "src": _short(e.source_id), "tgt": _short(nid),
                    "kind": "CALLS", "tgt_gt": "",
                })

    trace_data = {
        "instance_id": instance_id,
        "query": query,
        "condition": condition,
        "intent": intent,
        "weights": weights,
        "layer_budgets": layer_budgets,
        "gt_fns": gt_fns,
        "gt_files": gt_files,
        "top_k": top_k,
        "total_fn_nodes": len(fn_nodes),
        "match_result": match_result,
        "ranked": ranked_data,
        "gt_positions": gt_positions,
        "edges": edges_data[:200],
        "stats": {
            "files":     sum(1 for n in graph.nodes.values() if n.layer == Layer.FILE),
            "classes":   sum(1 for n in graph.nodes.values() if n.layer == Layer.CLASS),
            "functions": len(fn_nodes),
        },
    }

    _TRACE_DIR.mkdir(exist_ok=True)
    safe_id = re.sub(r"[^\w\-]", "_", instance_id)
    out_path = _TRACE_DIR / f"{safe_id}_{condition}.html"

    html = _TRACE_HTML_TEMPLATE.replace("__TRACE_DATA__", json.dumps(trace_data, indent=None))
    out_path.write_text(html, encoding="utf-8")
    return str(out_path)


_TRACE_HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>TACM Trace — __INSTANCE_ID__</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',system-ui,sans-serif;background:#0d1117;color:#c9d1d9;padding:20px}
.container{max-width:1400px;margin:0 auto}
h1{color:#58a6ff;font-size:1.5em}
h2{color:#58a6ff;font-size:1.15em;margin:22px 0 10px;border-bottom:1px solid #21262d;padding-bottom:6px}
h3{color:#8b949e;font-size:0.95em;margin:12px 0 6px}
.subtitle{color:#8b949e;font-size:0.85em;margin-bottom:18px}
.card{background:#161b22;border:1px solid #21262d;border-radius:8px;padding:14px;margin-bottom:14px}
.grid{display:grid;gap:14px}
.g2{grid-template-columns:1fr 1fr}
.g3{grid-template-columns:1fr 1fr 1fr}
.g4{grid-template-columns:1fr 1fr 1fr 1fr}
.badge{display:inline-block;padding:2px 8px;border-radius:12px;font-size:0.78em;font-weight:600}
.b-bug{background:#f8514930;color:#f85149}
.b-structure{background:#58a6ff30;color:#58a6ff}
.b-explain{background:#3fb95030;color:#3fb950}
.b-hit{background:#3fb95025;color:#3fb950;border:1px solid #3fb95050}
.b-miss{background:#f8514925;color:#f85149;border:1px solid #f8514950}
.b-gt-strict{background:#da362930;color:#ff7b72}
.b-gt-lenient{background:#f0883e30;color:#f0883e}
.b-topk{background:#79c0ff20;color:#79c0ff}

.verdict{font-size:1.8em;font-weight:700;margin:10px 0}
.verdict.hit{color:#3fb950}
.verdict.miss{color:#f85149}

.wb{display:flex;align-items:center;gap:8px;margin:3px 0}
.wb .l{width:85px;font-size:0.82em;text-align:right;color:#8b949e}
.wb .bg{flex:1;height:16px;background:#21262d;border-radius:3px;overflow:hidden;position:relative}
.wb .fill{height:100%;border-radius:3px}
.wb .val{position:absolute;right:5px;top:0;line-height:16px;font-size:0.72em}

table{width:100%;border-collapse:collapse;font-size:0.82em}
th{text-align:left;padding:5px 7px;border-bottom:2px solid #21262d;color:#8b949e;font-weight:600;position:sticky;top:0;background:#161b22}
td{padding:4px 7px;border-bottom:1px solid #21262d}
tr:hover td{background:#1c2128}
tr.gt-strict td{background:#da362912!important}
tr.gt-lenient td{background:#f0883e10!important}
tr.topk-row td{border-left:3px solid #79c0ff}
.sc{font-family:'Cascadia Code',monospace;font-size:0.8em}
.mb{display:inline-block;height:9px;border-radius:2px;margin-right:1px;vertical-align:middle}

.gt-box{background:#161b22;border:1px solid #21262d;border-radius:8px;padding:12px;margin-top:8px}
.gt-fn{color:#ff7b72;font-family:'Cascadia Code',monospace;font-size:0.85em}
.gt-file{color:#8b949e;font-size:0.8em}
.gt-rank{font-weight:700;margin-left:8px}
.gt-rank.found{color:#3fb950}
.gt-rank.notfound{color:#f85149}

.signal-legend{display:flex;gap:12px;flex-wrap:wrap;margin:8px 0;font-size:0.78em}
.signal-legend span{display:flex;align-items:center;gap:4px}
.signal-legend .dot{width:10px;height:10px;border-radius:2px}
</style>
</head>
<body>
<div class="container">

<h1>TACM Diagnostic Trace</h1>
<div class="subtitle" id="sub"></div>

<!-- Verdict -->
<div class="card" style="text-align:center">
  <div id="verdict-text" class="verdict"></div>
  <div id="verdict-detail" style="color:#8b949e;font-size:0.9em"></div>
</div>

<!-- Row 1: Intent + Weights + GT -->
<div class="grid g3">
  <div class="card">
    <h3>Intent & Weights</h3>
    <div style="margin:8px 0"><span id="intent-badge" class="badge"></span></div>
    <div id="weights-bars"></div>
  </div>
  <div class="card">
    <h3>Ground Truth Functions</h3>
    <div id="gt-fns"></div>
  </div>
  <div class="card">
    <h3>GT in Ranking</h3>
    <div id="gt-positions"></div>
  </div>
</div>

<!-- Row 2: Ranked table -->
<h2>Ranked Functions (Top 30)</h2>
<div class="signal-legend">
  <span><span class="dot" style="background:#58a6ff"></span>BM25</span>
  <span><span class="dot" style="background:#f0883e"></span>Fan-In</span>
  <span><span class="dot" style="background:#d2a8ff"></span>Fan-Out</span>
  <span><span class="dot" style="background:#f85149"></span>Complexity</span>
  <span><span class="dot" style="background:#3fb950"></span>Test-Cover</span>
  <span><span class="dot" style="background:#db61a2"></span>Nbr-Bonus</span>
  <span><span class="dot" style="background:#f778ba"></span>PageRank</span>
</div>
<div class="card" style="max-height:600px;overflow-y:auto">
  <table><thead id="rank-head"></thead><tbody id="rank-body"></tbody></table>
</div>

<!-- Row 3: Signal comparison for GT vs top-1 -->
<h2>Signal Deep-Dive: GT vs Top Ranked</h2>
<div class="grid g2" id="compare-panels"></div>

</div>

<script>
const D = __TRACE_DATA__;

// Subtitle
document.getElementById('sub').textContent =
  `Instance: ${D.instance_id}  |  Query: "${D.query}"  |  Condition: ${D.condition}  |  ${D.total_fn_nodes} functions`;

// Verdict
const v = document.getElementById('verdict-text');
const vd = document.getElementById('verdict-detail');
if (D.match_result.strict_rank) {
  v.className = 'verdict hit';
  v.textContent = `FN-HIT @ rank ${D.match_result.strict_rank}`;
  vd.textContent = `GT function found in top-${D.top_k}. ` +
    `File rank: ${D.match_result.file_rank || 'n/a'}. Tokens: ${D.match_result.top_k_tokens}`;
} else {
  v.className = 'verdict miss';
  v.textContent = 'FN-MISS';
  const closest = D.gt_positions.length ? D.gt_positions[0] : null;
  vd.textContent = closest
    ? `Closest GT "${closest.short}" at rank ${closest.rank} (needed ≤${D.top_k}). BM25=${closest.bm25}`
    : 'No GT function found in ranking at all.';
}

// Intent
const ib = document.getElementById('intent-badge');
ib.textContent = D.intent.toUpperCase();
ib.className = 'badge b-' + D.intent;

// Weights
const wDiv = document.getElementById('weights-bars');
const wColors = {bm25:'#58a6ff',fan_in:'#f0883e',fan_out:'#d2a8ff',complexity:'#f85149',test_cover:'#3fb950'};
for (const [k, val] of Object.entries(D.weights)) {
  const pct = (val * 100).toFixed(0);
  wDiv.innerHTML += `<div class="wb"><div class="l">${k}</div><div class="bg"><div class="fill" style="width:${pct}%;background:${wColors[k]}"></div><div class="val">${pct}%</div></div></div>`;
}

// GT functions
const gtDiv = document.getElementById('gt-fns');
D.gt_fns.forEach(fn => {
  gtDiv.innerHTML += `<div style="margin:4px 0"><span class="gt-fn">${fn}</span></div>`;
});
D.gt_files.forEach(f => {
  gtDiv.innerHTML += `<div><span class="gt-file">📄 ${f}</span></div>`;
});

// GT positions in ranking
const gpDiv = document.getElementById('gt-positions');
if (!D.gt_positions.length) {
  gpDiv.innerHTML = '<div style="color:#f85149;font-weight:600">No GT functions found in ranking!</div>';
} else {
  D.gt_positions.forEach(p => {
    const cls = p.rank <= D.top_k ? 'found' : 'notfound';
    const tag = p.rank <= D.top_k ? '✓ IN TOP-K' : `✗ outside (need ≤${D.top_k})`;
    gpDiv.innerHTML += `<div style="margin:4px 0"><span class="gt-fn">${p.short}</span><span class="gt-rank ${cls}"> rank ${p.rank} ${tag}</span><br><span class="gt-file">${p.file} | bm25=${p.bm25}</span></div>`;
  });
}

// Signal mini-bar helper
function sbar(v, color, maxW) {
  const w = Math.max(1, v * maxW);
  return `<span class="mb" style="width:${w}px;background:${color}" title="${v}"></span>`;
}

// Ranked table
document.getElementById('rank-head').innerHTML =
  '<tr><th>#</th><th>Function</th><th>File</th><th>Tok</th><th>BM25</th><th>Fan-In</th><th>Fan-Out</th><th>Cmplx</th><th>Test</th><th>Nbr</th><th>PR</th><th>Tag</th></tr>';
const tbody = document.getElementById('rank-body');
D.ranked.forEach(r => {
  let cls = '';
  if (r.gt === 'strict') cls = 'gt-strict';
  else if (r.gt === 'lenient') cls = 'gt-lenient';
  if (r.in_topk) cls += ' topk-row';
  const s = r.signals;
  let tags = '';
  if (r.in_topk) tags += '<span class="badge b-topk">TOP-K</span> ';
  if (r.gt === 'strict') tags += '<span class="badge b-gt-strict">GT</span>';
  else if (r.gt === 'lenient') tags += '<span class="badge b-gt-lenient">GT~</span>';

  tbody.innerHTML += `<tr class="${cls}">
    <td>${r.rank}</td>
    <td title="${r.id}">${r.short}</td>
    <td style="color:#8b949e;font-size:0.78em">${r.file}:${r.line}</td>
    <td>${r.tokens}</td>
    <td class="sc">${sbar(s.bm25,'#58a6ff',55)} ${s.bm25.toFixed(3)}</td>
    <td class="sc">${sbar(s.fan_in,'#f0883e',55)} ${s.fan_in.toFixed(3)}</td>
    <td class="sc">${sbar(s.fan_out,'#d2a8ff',55)} ${s.fan_out.toFixed(3)}</td>
    <td class="sc">${sbar(s.complexity,'#f85149',55)} ${s.complexity.toFixed(3)}</td>
    <td class="sc">${sbar(s.test_cover,'#3fb950',55)} ${s.test_cover.toFixed(3)}</td>
    <td class="sc">${sbar(s.nbr_bonus,'#db61a2',55)} ${s.nbr_bonus.toFixed(3)}</td>
    <td class="sc">${sbar(s.pagerank,'#f778ba',55)} ${s.pagerank.toFixed(3)}</td>
    <td>${tags}</td>
  </tr>`;
});

// Compare: GT vs Top-1
const cp = document.getElementById('compare-panels');
function makeCompareCard(title, data, highlight) {
  if (!data) return '<div class="card" style="color:#8b949e">N/A</div>';
  const s = data.signals;
  let html = `<div class="card"><h3>${title}: ${data.short}</h3><div style="font-size:0.78em;color:#8b949e;margin-bottom:8px">${data.file}:${data.line}</div>`;
  const sigs = [
    ['BM25', s.bm25, '#58a6ff'], ['Fan-In', s.fan_in, '#f0883e'], ['Fan-Out', s.fan_out, '#d2a8ff'],
    ['Complexity', s.complexity, '#f85149'], ['Test-Cover', s.test_cover, '#3fb950'],
    ['Nbr-Bonus', s.nbr_bonus, '#db61a2'], ['PageRank', s.pagerank, '#f778ba'],
  ];
  sigs.forEach(([name, val, color]) => {
    const pct = (val * 100).toFixed(1);
    html += `<div class="wb"><div class="l">${name}</div><div class="bg"><div class="fill" style="width:${pct}%;background:${color}"></div><div class="val">${val.toFixed(4)}</div></div></div>`;
  });
  html += '</div>';
  return html;
}

const top1 = D.ranked.length ? D.ranked[0] : null;
const gtEntry = D.ranked.find(r => r.gt === 'strict') || D.ranked.find(r => r.gt === 'lenient');
cp.innerHTML = makeCompareCard('Top-1 Ranked', top1, false) + makeCompareCard('Ground Truth', gtEntry, true);
</script>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Core: single instance × single condition
# ---------------------------------------------------------------------------

def _run_condition(
    condition: str,
    instance: dict,
    repo_path: Path,
    gt_fns: list[str],
    gt_files: list[str],
    top_k: int,
    no_exec: bool,
    graph,
    fn_nodes: list,
    trace: bool = False,
) -> dict:
    """
    Retrieve under one condition, evaluate function-level GT match,
    optionally apply patch + run tests.
    Returns a result dict with function-level metrics as primary.
    """
    iid = instance.get("instance_id", str(instance.get("id", "?")))
    result = dict(
        condition=condition,
        fn_hit=False,
        fn_strict_rank=None,
        fn_lenient_rank=None,
        file_hit=False,
        file_rank=None,
        top_k_tokens=0,
        retrieval_ms=None,
        miss_bucket=None,
        patch_applied=False,
        tests_passed=False,
        solved=False,
        skip_reason=None,
    )

    try:
        t0 = time.perf_counter()
        ranked = _retrieve(condition, instance["query"], graph, fn_nodes)
        result["retrieval_ms"] = (time.perf_counter() - t0) * 1000.0
    except Exception as e:
        print(f"    [{condition}] retrieval failed: {e}")
        result["skip_reason"] = "retrieval_failed"
        return result

    # Function-level matching (primary metric)
    match = _match_ranked_functions(ranked, gt_fns, gt_files, top_k)
    result["fn_strict_rank"] = match["strict_rank"]
    result["fn_lenient_rank"] = match["lenient_rank"]
    result["file_rank"] = match["file_rank"]
    result["top_k_tokens"] = match["top_k_tokens"]
    # Hit@K derived from full-list ranks so MRR and Hit@K stay consistent.
    result["fn_hit"] = (
        match["strict_rank"] is not None and match["strict_rank"] <= top_k
    )
    result["file_hit"] = (
        match["file_rank"] is not None and match["file_rank"] <= top_k
    )
    result["miss_bucket"] = _classify_miss(
        match=match, gt_fns=gt_fns, gt_files=gt_files,
        fn_nodes=fn_nodes, top_k=top_k,
    )

    # Generate diagnostic trace for TACM conditions
    if trace and condition.startswith("tacm"):
        try:
            trace_path = _generate_tacm_trace(
                iid, instance["query"], condition,
                graph, fn_nodes, ranked, gt_fns, gt_files,
                top_k, match,
            )
            print(f"    [{condition}] trace → {trace_path}")
        except Exception as e:
            print(f"    [{condition}] trace generation failed: {e}")

    # Display
    fn_status = f"FN-HIT@{match['strict_rank']}" if match["strict_rank"] else "FN-MISS"
    file_tag = f"file@{match['file_rank']}" if match["file_rank"] else "file-miss"
    tok_tag = f"{match['top_k_tokens']}tok"
    print(f"    [{condition}] {fn_status}  {file_tag}  {tok_tag}")

    if no_exec or not result["fn_hit"]:
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
    trace: bool = False,
) -> list[dict]:
    """Clone once, run all conditions, return list of per-condition result dicts."""
    iid = instance.get("instance_id", str(instance.get("id", "?")))
    print(f"\n--- {iid} [{instance.get('language','?')}] ---")

    gt_fns, gt_files, gt_classes = _extract_gt_functions(instance.get("patch", ""))
    if not gt_fns:
        # Fall back to file-level only if no functions extracted
        gt_files_fallback = _extract_gt_files(instance.get("patch", ""))
        if not gt_files_fallback:
            print("  ⚠  No GT in patch — skipping")
            return [dict(instance_id=iid, repo=instance["repo"],
                         language=instance.get("language", "?"),
                         condition=c, fn_hit=False, fn_strict_rank=None,
                         fn_lenient_rank=None, file_hit=False, file_rank=None,
                         top_k_tokens=0, patch_applied=False,
                         tests_passed=False, solved=False,
                         skip_reason="no_gt") for c in conditions]
        print(f"  ⚠  No GT functions — file-only GT: {gt_files_fallback}")
        gt_files = gt_files_fallback

    print(f"  GT functions: {gt_fns[:5]}{'...' if len(gt_fns) > 5 else ''}")
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
            r = _run_condition(condition, instance, repo_path, gt_fns, gt_files, top_k, no_exec, graph, fn_nodes, trace=trace)
            condition_results.append({**base_result, **r})

            # Reset repo between conditions if patch was applied
            if r.get("patch_applied"):
                _run("git checkout -- .", cwd=repo_path)

    return condition_results


# ---------------------------------------------------------------------------
# Benchmark runner + summary
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Statistics — paired bootstrap for MRR/Hit/Solved
# ---------------------------------------------------------------------------

def _bootstrap_ci(values: list[float], n_boot: int = BOOTSTRAP_N,
                  alpha: float = 0.05) -> tuple[float, float]:
    """Two-sided percentile bootstrap CI on the mean of ``values``."""
    if not values:
        return (0.0, 0.0)
    rng = random.Random(SEED)
    n = len(values)
    samples = []
    for _ in range(n_boot):
        s = sum(values[rng.randrange(n)] for _ in range(n)) / n
        samples.append(s)
    samples.sort()
    lo = samples[int((alpha / 2) * n_boot)]
    hi = samples[int((1 - alpha / 2) * n_boot)]
    return (lo, hi)


def _paired_bootstrap_p(a: list[float], b: list[float],
                        n_boot: int = BOOTSTRAP_N) -> float:
    """One-sided p-value that ``a`` beats ``b`` on the paired mean.

    ``a`` and ``b`` are aligned per-instance (same index = same task).
    H0: mean(a) <= mean(b). Lower p means stronger evidence that a > b.
    Returns 1.0 when lengths don't match (misaligned pairs → treat as null).
    """
    if len(a) != len(b) or not a:
        return 1.0
    rng = random.Random(SEED)
    diffs = [a[i] - b[i] for i in range(len(a))]
    observed = sum(diffs) / len(diffs)
    if observed <= 0:
        # Not even directionally better — no need to bootstrap.
        return 1.0
    # Resample diffs under H0 (center at zero) and count how often the
    # resampled mean equals or exceeds the observed lift.
    centered = [d - observed for d in diffs]
    n = len(centered)
    hits = 0
    for _ in range(n_boot):
        s = sum(centered[rng.randrange(n)] for _ in range(n)) / n
        if s >= observed:
            hits += 1
    return hits / n_boot


def _paired_vectors(
    all_results: list[dict],
    cond_a: str,
    cond_b: str,
    metric: str,
) -> tuple[list[float], list[float]]:
    """Build per-instance paired vectors for two conditions over a metric.

    Only instance_ids where BOTH conditions produced a non-skip result are
    included — this guarantees the paired bootstrap sees aligned pairs.
    """
    def _metric(r: dict) -> float:
        if metric == "mrr":
            rnk = r.get("fn_strict_rank")
            return (1.0 / rnk) if rnk else 0.0
        if metric == "hit":
            return 1.0 if r.get("fn_hit") else 0.0
        if metric == "solved":
            return 1.0 if r.get("solved") else 0.0
        raise ValueError(metric)

    by_iid: dict[str, dict[str, dict]] = {}
    for r in all_results:
        iid = r.get("instance_id", "?")
        by_iid.setdefault(iid, {})[r["condition"]] = r

    a, b = [], []
    for iid, conds in by_iid.items():
        ra, rb = conds.get(cond_a), conds.get(cond_b)
        if not ra or not rb:
            continue
        if ra.get("skip_reason") or rb.get("skip_reason"):
            continue
        a.append(_metric(ra))
        b.append(_metric(rb))
    return a, b


def _results_to_path(dataset_path: str) -> Path:
    stem = Path(dataset_path).stem
    ts = time.strftime("%Y%m%d_%H%M%S")
    out_dir = ROOT / "agent_results"
    out_dir.mkdir(exist_ok=True)
    return out_dir / f"zero_cost_{stem}_{ts}.json"


def run_benchmark(
    dataset_path: str,
    conditions: list[str],
    no_exec: bool = False,
    python_only: bool = False,
    limit: int | None = None,
    top_k: int = TOP_K,
    trace: bool = False,
) -> None:
    _pin_seeds()

    with open(dataset_path) as f:
        dataset = json.load(f)

    if python_only:
        dataset = [x for x in dataset if x.get("language", "") == "Python"]
        print(f"  (python-only filter: {len(dataset)} instances)")

    if limit:
        dataset = dataset[:limit]

    all_results: list[dict] = []
    for instance in dataset:
        _clear_index_cache()  # fresh cache per instance
        results = run_instance(instance, conditions, no_exec, top_k, trace=trace)
        all_results.extend(results)

    # Persist raw results for offline reanalysis
    out_path = _results_to_path(dataset_path)
    try:
        with open(out_path, "w") as f:
            json.dump({
                "seed": SEED,
                "top_k": top_k,
                "dataset": dataset_path,
                "conditions": conditions,
                "no_exec": no_exec,
                "python_only": python_only,
                "results": all_results,
            }, f, indent=2, default=str)
        print(f"\nRaw results → {out_path}")
    except Exception as e:
        print(f"\n[warn] could not write results JSON: {e}")

    # Baselines for the p-value columns
    ref_bm25 = "bm25" if "bm25" in conditions else None
    ref_tacm = "tacm" if "tacm" in conditions else None

    # ---- Per-condition summary ----
    print(f"\n{'='*108}")
    print(f"Dataset : {dataset_path}  |  Mode: {'retrieval-only' if no_exec else 'full solve'}  |  Seed: {SEED}")
    print(f"Top-K   : {top_k}  |  Bootstrap: {BOOTSTRAP_N}")
    print(f"{'='*108}")
    header = (f"{'Condition':<14} {'N':>3} {'Skip':>4}  "
              f"{'Hit%':>5} {'MRR':>6} {'MRR 95% CI':>17} "
              f"{'p>bm25':>7} {'p>tacm':>7} {'p50ms':>6} {'File%':>5} {'Tok':>5}")
    if not no_exec:
        header += f" {'Solve%':>6}"
    print(header)
    print("-" * len(header))

    for cond in conditions:
        rows = [r for r in all_results if r["condition"] == cond]
        valid = [r for r in rows if r.get("skip_reason") is None]
        skipped = len(rows) - len(valid)
        n = len(valid)

        # PRIMARY: MRR with bootstrap CI
        mrr_vec = [
            (1.0 / r["fn_strict_rank"]) if r.get("fn_strict_rank") else 0.0
            for r in valid
        ]
        mrr = sum(mrr_vec) / n if n else 0.0
        ci_lo, ci_hi = _bootstrap_ci(mrr_vec)

        # Hit%
        hit_pct = sum(1 for r in valid if r.get("fn_hit")) / n if n else 0.0

        # Paired p-values on MRR vs the baselines
        if ref_bm25 and cond != ref_bm25:
            a, b = _paired_vectors(all_results, cond, ref_bm25, "mrr")
            p_bm25 = _paired_bootstrap_p(a, b)
            p_bm25_str = f"{p_bm25:.3f}"
        else:
            p_bm25_str = "—"

        if ref_tacm and cond != ref_tacm:
            a, b = _paired_vectors(all_results, cond, ref_tacm, "mrr")
            p_tacm = _paired_bootstrap_p(a, b)
            p_tacm_str = f"{p_tacm:.3f}"
        else:
            p_tacm_str = "—"

        # Latency — median is more honest than mean for one-shot retrievers
        lat = sorted(r["retrieval_ms"] for r in valid if r.get("retrieval_ms") is not None)
        p50 = lat[len(lat) // 2] if lat else 0.0

        # File-level + tokens (legacy reference)
        file_pct = sum(1 for r in valid if r.get("file_hit")) / n if n else 0.0
        tok = sum(r.get("top_k_tokens", 0) for r in valid) / n if n else 0.0

        line = (f"{cond:<14} {n:>3} {skipped:>4}  "
                f"{hit_pct:>4.0%} {mrr:>6.4f} [{ci_lo:.3f},{ci_hi:.3f}] "
                f"{p_bm25_str:>7} {p_tacm_str:>7} "
                f"{p50:>5.0f}m {file_pct:>4.0%} {tok:>5.0f}")
        if not no_exec:
            solved = sum(1 for r in valid if r.get("solved")) / n if n else 0.0
            line += f" {solved:>5.0%}"
        print(line)

    print("-" * len(header))

    # ---- Failure taxonomy per condition (Gap 4) ----
    print("\nMiss taxonomy (% of valid rows per condition):")
    buckets = ["hit", "right_file_wrong_fn", "ranked_outside_k",
               "gt_not_in_pool", "no_gt_fn", "miss_other"]
    head = f"{'Condition':<14} " + " ".join(f"{b:>20}" for b in buckets)
    print(head)
    print("-" * len(head))
    for cond in conditions:
        valid = [r for r in all_results
                 if r["condition"] == cond and r.get("skip_reason") is None]
        total = len(valid) or 1
        counts = {b: 0 for b in buckets}
        for r in valid:
            counts[r.get("miss_bucket") or "miss_other"] = counts.get(
                r.get("miss_bucket") or "miss_other", 0) + 1
        cells = " ".join(f"{counts[b] / total:>19.0%} " for b in buckets)
        print(f"{cond:<14} {cells}")

    print(f"\n{'='*108}")
    print("Stats legend:")
    print("  MRR 95% CI : percentile bootstrap on per-instance reciprocal ranks")
    print("  p>bm25     : paired-bootstrap one-sided p-value that this retriever beats BM25 on MRR")
    print("  p>tacm     : same, but against TACM (only meaningful for TACM variants)")
    print("  p50ms      : median retrieval latency (graph build excluded, pure ranking cost)")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

ALL_CONDITIONS = ["bm25", "minilm", "codesearch", "hybrid", "hybrid-cs", "tacm", "tacm-ppr", "tacm-rerank"]

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
    parser.add_argument(
        "--trace", action="store_true",
        help="Generate per-instance HTML diagnostic traces for TACM conditions (saved to tacm_traces/)",
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
        trace=args.trace,
    )
