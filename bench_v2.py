"""bench_v2.py — TACM-v2 benchmark against retrieval systems + ablations.

Systems compared:
  BM25-Body         — BM25Okapi on full function body (lexical ceiling)
  RepoMap           — Aider tree-sitter + PageRank (most deployed structural retriever)
  Dense-MiniLM      — all-MiniLM-L6-v2 cosine similarity (Cursor/Continue default)
  Dense-CodeSearch  — st-codesearch-distilroberta-base (CodeSearchNet-trained)
  Dense-Voyage      — voyage-code-3 (Continue.dev recommended, Voyage AI)
  Dense-OpenAI      — text-embedding-3-small (OpenAI API)
  Hybrid-MiniLM     — BM25 + MiniLM via RRF (Agentless/Moatless style)
  Hybrid-CodeSearch — BM25 + CodeSearch via RRF (strongest open hybrid)
  TACM-v2           — Multi-layer graph + intent scoring + containment bonus
  TACM-NoCB         — Ablation: TACM-v2 without containment bonus
  TACM-FixedBudget  — Ablation: TACM-v2 with equal budget per layer (no intent split)
  TACM-BM25Only     — Ablation: TACM-v2 with BM25 signal only (no graph signals)

Evaluation design:
  Query source  : git commit message from bug.info fixed_commit_id.
                  Tasks with no valid commit message are DROPPED (no GT fallback).
  GT matching   : STRICT = file-path suffix + function name. LENIENT = name only.
  Candidate pool: all systems rank over the same non-test function set.
  Retrieval task: top-K unlimited rank (apples-to-apples across all systems).
  Packing task  : TACM-v2 token budget (budget-constrained selection).

Multi-level GT:
  FUNCTION level — hit the specific function changed in the patch (primary metric)
  FILE level     — hit the file containing the fix (measures module-routing quality)
  CLASS level    — hit the class containing the fix (measures structural coherence)
  These three together prove TACM is an all-rounder, not just a function ranker.

API keys (set as env vars or export before running):
  VOYAGE_API_KEY   — for voyage-code-3
  OPENAI_API_KEY   — for text-embedding-3-small

Usage:
    python3 bench_v2.py --project thefuck --repo ./thefuck --max 30 --budget 4000
    python3 bench_v2.py --project scrapy  --repo ./scrapy  --max 30 --budget 800 4000
    python3 bench_v2.py --all
"""

from __future__ import annotations

import argparse
import math
import os
import random
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "archive" / "pre-research"))

BUGSINPY_ROOT = ROOT / "BugsInPy"

# API keys from environment
VOYAGE_API_KEY = os.environ.get("VOYAGE_API_KEY", "")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")


# ---------------------------------------------------------------------------
# BugsInPy task loading
# ---------------------------------------------------------------------------

@dataclass
class Task:
    bug_id: str
    project: str
    patch_path: Path
    fixed_commit: str
    gt_functions: list[str]   # "ClassName.method" or "function_name"
    gt_files: list[str]       # "thefuck/rules/pip_unknown_command.py"
    gt_classes: list[str]     # "ClassName" extracted from patch context
    query: str                # from commit message only — no GT leakage


_HUNK_RE  = re.compile(r"^@@ .+ @@(.*)$")
_DEF_RE   = re.compile(r"^[ +\-]?(\s*)def\s+(\w+)\s*\(")
_CLASS_RE = re.compile(r"^[ +\-]?(\s*)class\s+(\w+)[\s:(]")
_FILE_RE  = re.compile(r"^\+\+\+ b/(.+)$")


def _extract_gt_from_patch(patch_text: str) -> tuple[list[str], list[str], list[str]]:
    """Extract (gt_functions, gt_files, gt_classes) from unified diff.

    gt_functions: qualified names like "ClassName.method_name" or "function_name"
    gt_files: file paths like "thefuck/rules/pip_unknown_command.py"
    gt_classes: class names that contain the changed functions
    """
    gt_functions: list[str] = []
    gt_files: list[str] = []
    gt_classes: list[str] = []
    seen_fns: set[str] = set()
    seen_cls: set[str] = set()
    current_file = ""
    context_stack: list[tuple[int, str, bool]] = []
    in_hunk = False

    for line in patch_text.splitlines():
        fm = _FILE_RE.match(line)
        if fm:
            current_file = fm.group(1)
            if current_file.endswith(".py"):
                gt_files.append(current_file)
            context_stack = []
            in_hunk = False
            continue

        if _HUNK_RE.match(line):
            in_hunk = True
            continue

        cm = _CLASS_RE.match(line)
        if cm and not line.startswith("---"):
            indent = len(cm.group(1))
            while context_stack and context_stack[-1][0] >= indent:
                context_stack.pop()
            context_stack.append((indent, cm.group(2), True))

        dm = _DEF_RE.match(line)
        if dm and not line.startswith("---"):
            indent = len(dm.group(1))
            while context_stack and context_stack[-1][0] >= indent:
                context_stack.pop()
            fn_name = dm.group(2)
            context_stack.append((indent, fn_name, False))

        if in_hunk and line.startswith(("-", "+")) and not line.startswith(("---", "+++")):
            classes = [n for (_, n, is_cls) in context_stack if is_cls]
            fns     = [n for (_, n, is_cls) in context_stack if not is_cls]
            if fns:
                fn = fns[-1]
                gt = f"{classes[-1]}.{fn}" if classes else fn
                if gt not in seen_fns:
                    seen_fns.add(gt)
                    gt_functions.append(gt)
                # Track classes touched by the patch
                for cls in classes:
                    if cls not in seen_cls:
                        seen_cls.add(cls)
                        gt_classes.append(cls)

    return gt_functions, list(dict.fromkeys(gt_files)), gt_classes


def _commit_msg(repo_root: Path, commit: str) -> str:
    if not commit:
        return ""
    try:
        r = subprocess.run(
            ["git", "log", "--format=%B", "-1", commit],
            cwd=repo_root, capture_output=True, text=True, timeout=10,
        )
        for line in r.stdout.splitlines():
            line = line.strip()
            if line:
                return line
    except Exception:
        pass
    return ""


def _parse_fixed_commit(bug_dir: Path) -> str:
    """Parse fixed_commit_id from bug.info (format: fixed_commit_id="abc123")."""
    info_f = bug_dir / "bug.info"
    if not info_f.exists():
        return ""
    for line in info_f.read_text().splitlines():
        if line.startswith("fixed_commit_id="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    return ""


def load_tasks(
    project: str,
    repo_root: Path,
    max_bugs: int = 30,
    skip_no_query: bool = True,
) -> list[Task]:
    """Load BugsInPy tasks. skip_no_query=True drops tasks where commit message
    lookup fails — prevents GT-name fallback from leaking ground truth."""
    proj_dir = BUGSINPY_ROOT / "projects" / project / "bugs"
    if not proj_dir.exists():
        print(f"  BugsInPy dir not found: {proj_dir}")
        return []

    tasks: list[Task] = []
    skipped_no_gt = 0
    skipped_no_query = 0
    bug_nums = sorted(int(d.name) for d in proj_dir.iterdir() if d.name.isdigit())

    for num in bug_nums[:max_bugs]:
        bug_dir = proj_dir / str(num)
        patch_f = bug_dir / "bug_patch.txt"
        if not patch_f.exists():
            continue

        patch_text = patch_f.read_text(errors="replace")
        gt_fns, gt_files, gt_classes = _extract_gt_from_patch(patch_text)
        if not gt_fns:
            skipped_no_gt += 1
            continue

        fixed_commit = _parse_fixed_commit(bug_dir)
        query = _commit_msg(repo_root, fixed_commit)

        if skip_no_query and not query:
            skipped_no_query += 1
            continue

        tasks.append(Task(
            bug_id=f"{project}-{num}",
            project=project,
            patch_path=patch_f,
            fixed_commit=fixed_commit,
            gt_functions=gt_fns,
            gt_files=gt_files,
            gt_classes=gt_classes,
            query=query,
        ))

    if skipped_no_gt:
        print(f"  Skipped {skipped_no_gt} tasks: no GT extracted from patch")
    if skipped_no_query:
        print(f"  Skipped {skipped_no_query} tasks: no commit message (query would leak GT)")
    return tasks


# ---------------------------------------------------------------------------
# GT matching — strict and lenient, across all three levels
# ---------------------------------------------------------------------------

def _node_matches_gt_strict(
    node_id: str,
    node_file: str,
    gt_fn: str,
    gt_files: list[str],
) -> bool:
    """Strict match: function short name AND file path suffix must both agree.

    No basename fallback — both checks require the full relative path suffix.
    This is intentionally conservative: a match in scrapy/http/response.py
    does not match scrapy/tests/http/response.py even if the basename is the same.
    """
    gt_fn_short = gt_fn.split(".")[-1]
    node_fn_part = node_id.split("::")[-1] if "::" in node_id else node_id
    node_fn_short = node_fn_part.split(".")[-1]

    if gt_fn_short != node_fn_short:
        return False

    node_path = node_file or (node_id.split("::")[0] if "::" in node_id else "")
    for gt_file in gt_files:
        if node_path.endswith(gt_file) or node_path.endswith(gt_file.replace("/", os.sep)):
            return True
    return False


def _node_matches_gt_lenient(node_id: str, gt_fn: str) -> bool:
    """Lenient match: short function name only."""
    gt_fn_short = gt_fn.split(".")[-1]
    node_fn_part = node_id.split("::")[-1] if "::" in node_id else node_id
    node_fn_short = node_fn_part.split(".")[-1]
    return gt_fn_short == node_fn_short


def _file_matches_gt(node_file: str, gt_files: list[str]) -> bool:
    """FILE-level match: node's file path ends with the GT relative path.
    No basename fallback — same strictness as _node_matches_gt_strict."""
    if not node_file or not gt_files:
        return False
    for gt_file in gt_files:
        if node_file.endswith(gt_file) or node_file.endswith(gt_file.replace("/", os.sep)):
            return True
    return False


def _class_matches_gt(node_id: str, gt_classes: list[str]) -> bool:
    """CLASS-level match: node's class name matches any GT class."""
    if not gt_classes:
        return False
    # node_id may be like "/path/file.py::ClassName" or "/path/file.py::ClassName.method"
    part = node_id.split("::")[-1] if "::" in node_id else node_id
    # For CLASS nodes, part is "ClassName"; for FUNCTION nodes in a class, part is "ClassName.method"
    parts = part.split(".")
    # Check both the full part and the first component (class name)
    for gt_cls in gt_classes:
        if parts[0] == gt_cls or part == gt_cls:
            return True
    return False


def _match_ranked_nodes(
    gt_fns: list[str],
    gt_files: list[str],
    gt_classes: list[str],
    ranked_ids: list[tuple[str, str]],  # (node_id, file_path)
    top_k: int,
) -> tuple[int | None, int | None, int | None, int | None]:
    """Return (strict_fn_rank, lenient_fn_rank, file_rank, class_rank), all 1-based or None."""
    strict_rank = None
    lenient_rank = None
    file_rank = None
    class_rank = None

    for rank, (nid, nfile) in enumerate(ranked_ids[:top_k], 1):
        for gt_fn in gt_fns:
            if strict_rank is None and _node_matches_gt_strict(nid, nfile, gt_fn, gt_files):
                strict_rank = rank
            if lenient_rank is None and _node_matches_gt_lenient(nid, gt_fn):
                lenient_rank = rank
        if file_rank is None and _file_matches_gt(nfile, gt_files):
            file_rank = rank
        if class_rank is None and gt_classes and _class_matches_gt(nid, gt_classes):
            class_rank = rank
        if strict_rank and lenient_rank and file_rank and (not gt_classes or class_rank):
            break

    return strict_rank, lenient_rank, file_rank, class_rank


# ---------------------------------------------------------------------------
# BM25-Body baseline
# ---------------------------------------------------------------------------

def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def _read_source(file_path: str, line_start: int, line_end: int) -> str:
    try:
        lines = Path(file_path).read_text(errors="replace").splitlines()
        return "\n".join(lines[max(0, line_start - 1): line_end])
    except OSError:
        return ""


def bm25_rank_nodes(nodes, query: str) -> list[tuple[str, str]]:
    """BM25 on full function body. Returns [(node_id, file_path)] sorted by score."""
    prod = [n for n in nodes if not n.is_test]
    if not prod:
        return []

    q_tokens = _tokenize(query)
    if not q_tokens:
        return [(n.qualified_name, n.file_path or "") for n in prod]

    corpus_texts = [
        _read_source(n.file_path, n.line_start or 0, n.line_end or 0) or n.name
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

    ranked = sorted(zip(scores, prod), key=lambda x: -x[0])
    return [(n.qualified_name, n.file_path or "") for _, n in ranked]


# ---------------------------------------------------------------------------
# Dense embedding retrievers
# ---------------------------------------------------------------------------

_embed_cache: dict[str, dict] = {}


def _corpus_texts(flat_nodes) -> list[tuple[str, str, str]]:
    """Returns [(node_id, file_path, text)] for all non-test function nodes."""
    return [
        (n.qualified_name, n.file_path or "",
         _read_source(n.file_path, n.line_start or 0, n.line_end or 0) or n.name)
        for n in flat_nodes if not n.is_test
    ]


def _build_minilm_index(flat_nodes, repo_key: str) -> tuple | None:
    slug = "minilm"
    if repo_key in _embed_cache and slug in _embed_cache[repo_key]:
        return _embed_cache[repo_key][slug]
    try:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        corpus = _corpus_texts(flat_nodes)
        ids    = [(nid, fpath) for nid, fpath, _ in corpus]
        texts  = [t for _, _, t in corpus]
        vecs   = model.encode(texts, batch_size=64, show_progress_bar=False,
                               normalize_embeddings=True)
        result = (ids, vecs, model)
        _embed_cache.setdefault(repo_key, {})[slug] = result
        return result
    except Exception as e:
        print(f"  [MiniLM] build failed: {e}")
        return None


def _build_codesearch_index(flat_nodes, repo_key: str) -> tuple | None:
    slug = "codesearch"
    if repo_key in _embed_cache and slug in _embed_cache[repo_key]:
        return _embed_cache[repo_key][slug]
    try:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer("flax-sentence-embeddings/st-codesearch-distilroberta-base")
        corpus = _corpus_texts(flat_nodes)
        ids    = [(nid, fpath) for nid, fpath, _ in corpus]
        texts  = [t for _, _, t in corpus]
        vecs   = model.encode(texts, batch_size=32, show_progress_bar=False,
                               normalize_embeddings=True)
        result = (ids, vecs, model)
        _embed_cache.setdefault(repo_key, {})[slug] = result
        return result
    except Exception as e:
        print(f"  [CodeSearch] build failed: {e}")
        return None


def _build_voyage_index(flat_nodes, repo_key: str) -> tuple | None:
    """voyage-code-3 via Voyage AI API. Batched to respect rate limits."""
    slug = "voyage"
    if repo_key in _embed_cache and slug in _embed_cache[repo_key]:
        return _embed_cache[repo_key][slug]
    if not VOYAGE_API_KEY:
        return None
    try:
        import voyageai
        import numpy as np
        client = voyageai.Client(api_key=VOYAGE_API_KEY)
        corpus = _corpus_texts(flat_nodes)
        ids    = [(nid, fpath) for nid, fpath, _ in corpus]
        texts  = [t for _, _, t in corpus]

        # Voyage API batch limit: 128 texts or 120k tokens per request
        BATCH = 64
        all_vecs = []
        for i in range(0, len(texts), BATCH):
            batch = texts[i:i+BATCH]
            resp = client.embed(batch, model="voyage-code-3", input_type="document")
            all_vecs.extend(resp.embeddings)

        mat = np.array(all_vecs, dtype="float32")
        # Normalize for cosine similarity
        norms = np.linalg.norm(mat, axis=1, keepdims=True)
        mat = mat / np.maximum(norms, 1e-9)

        result = (ids, mat, client)
        _embed_cache.setdefault(repo_key, {})[slug] = result
        return result
    except Exception as e:
        print(f"  [Voyage] build failed: {e}")
        return None


def _build_openai_index(flat_nodes, repo_key: str) -> tuple | None:
    """text-embedding-3-small via OpenAI API. Batched."""
    slug = "openai"
    if repo_key in _embed_cache and slug in _embed_cache[repo_key]:
        return _embed_cache[repo_key][slug]
    if not OPENAI_API_KEY:
        return None
    try:
        from openai import OpenAI
        import numpy as np
        client = OpenAI(api_key=OPENAI_API_KEY)
        corpus = _corpus_texts(flat_nodes)
        ids    = [(nid, fpath) for nid, fpath, _ in corpus]
        texts  = [t for _, _, t in corpus]

        # Truncate to OpenAI 8191 token limit (approx 32k chars)
        texts = [t[:32000] for t in texts]

        BATCH = 100
        all_vecs = []
        for i in range(0, len(texts), BATCH):
            batch = texts[i:i+BATCH]
            resp = client.embeddings.create(input=batch, model="text-embedding-3-small")
            all_vecs.extend([d.embedding for d in resp.data])

        mat = np.array(all_vecs, dtype="float32")
        norms = np.linalg.norm(mat, axis=1, keepdims=True)
        mat = mat / np.maximum(norms, 1e-9)

        result = (ids, mat, client)
        _embed_cache.setdefault(repo_key, {})[slug] = result
        return result
    except Exception as e:
        print(f"  [OpenAI] build failed: {e}")
        return None


def _dense_rank_st(query: str, index_tuple: tuple) -> list[tuple[str, str]]:
    """SentenceTransformer cosine ranking."""
    import numpy as np
    if index_tuple is None:
        return []
    ids, mat, model = index_tuple
    q_vec = model.encode([query], normalize_embeddings=True)[0]
    sims  = mat @ q_vec
    order = np.argsort(-sims)
    return [ids[i] for i in order]


def _dense_rank_voyage(query: str, index_tuple: tuple) -> list[tuple[str, str]]:
    """Voyage AI query-side embedding + cosine ranking."""
    import numpy as np
    if index_tuple is None:
        return []
    ids, mat, client = index_tuple
    resp = client.embed([query], model="voyage-code-3", input_type="query")
    q_vec = np.array(resp.embeddings[0], dtype="float32")
    q_vec = q_vec / max(np.linalg.norm(q_vec), 1e-9)
    sims  = mat @ q_vec
    order = np.argsort(-sims)
    return [ids[i] for i in order]


def _dense_rank_openai(query: str, index_tuple: tuple) -> list[tuple[str, str]]:
    """OpenAI query-side embedding + cosine ranking."""
    import numpy as np
    if index_tuple is None:
        return []
    ids, mat, client = index_tuple
    resp = client.embeddings.create(input=[query[:32000]], model="text-embedding-3-small")
    q_vec = np.array(resp.data[0].embedding, dtype="float32")
    q_vec = q_vec / max(np.linalg.norm(q_vec), 1e-9)
    sims  = mat @ q_vec
    order = np.argsort(-sims)
    return [ids[i] for i in order]


def _hybrid_rrf_rank(
    bm25_ranked: list[tuple[str, str]],
    dense_ranked: list[tuple[str, str]],
    k: int = 60,
) -> list[tuple[str, str]]:
    """Reciprocal Rank Fusion: 1/(k+rank_bm25) + 1/(k+rank_dense)."""
    from collections import defaultdict
    scores: dict[str, float] = defaultdict(float)
    id_to_pair: dict[str, tuple[str, str]] = {}
    for rank, (nid, fpath) in enumerate(bm25_ranked, 1):
        scores[nid] += 1.0 / (k + rank)
        id_to_pair[nid] = (nid, fpath)
    for rank, (nid, fpath) in enumerate(dense_ranked, 1):
        scores[nid] += 1.0 / (k + rank)
        id_to_pair[nid] = (nid, fpath)
    return [id_to_pair[nid] for nid, _ in sorted(scores.items(), key=lambda x: -x[1])]


# ---------------------------------------------------------------------------
# Aider RepoMap baseline
# ---------------------------------------------------------------------------

_repomap_instances: dict[str, object] = {}


def _get_repomap(repo_root: Path):
    key = str(repo_root)
    if key not in _repomap_instances:
        try:
            from aider.repomap import RepoMap
            from aider.io import InputOutput
            from unittest.mock import MagicMock
            io = InputOutput()
            mock_model = MagicMock()
            mock_model.token_count.side_effect = lambda t: max(1, len(t) // 4)
            _repomap_instances[key] = RepoMap(
                map_tokens=4000, root=str(repo_root),
                io=io, main_model=mock_model, verbose=False,
            )
        except ImportError:
            _repomap_instances[key] = None
    return _repomap_instances[key]


_IS_TEST_FILE = re.compile(r"(^|[/\\])tests?[/\\]|[/\\]test_|_test\.py$", re.IGNORECASE)


def repomap_rank_nodes(repo_root: Path, query: str) -> list[tuple[str, str]]:
    """RepoMap ranked function defs. Returns [(fn_name, rel_file)] in rank order.
    Excludes test files to match TACM-v2/BM25 candidate pool."""
    rm = _get_repomap(repo_root)
    if rm is None:
        return []
    py_files = [
        str(f) for f in repo_root.rglob("*.py")
        if ".git" not in str(f) and not _IS_TEST_FILE.search(str(f))
    ]
    q_idents = set(re.findall(r"[a-z_][a-z0-9_]*", query.lower()))
    try:
        tags = list(rm.get_ranked_tags(
            chat_fnames=[], other_fnames=py_files,
            mentioned_fnames=set(), mentioned_idents=q_idents,
        ))
    except Exception:
        return []
    return [
        (t.name, t.rel_fname)
        for t in tags if getattr(t, "kind", "") == "def"
    ]


def _gt_match_repomap(
    gt_fns: list[str],
    gt_files: list[str],
    gt_classes: list[str],
    ranked: list[tuple[str, str]],
    top_k: int,
) -> tuple[int | None, int | None, int | None, int | None]:
    """Match RepoMap (name, rel_path). Returns (strict_fn, lenient_fn, file, class)."""
    strict_rank = lenient_rank = file_rank = class_rank = None
    for rank, (name, rel_path) in enumerate(ranked[:top_k], 1):
        for gt_fn in gt_fns:
            gt_short = gt_fn.split(".")[-1]
            if lenient_rank is None and name == gt_short:
                lenient_rank = rank
            if strict_rank is None and name == gt_short:
                for gt_file in gt_files:
                    if rel_path.endswith(gt_file) or Path(rel_path).name == Path(gt_file).name:
                        strict_rank = rank
                        break
        if file_rank is None and gt_files:
            for gt_file in gt_files:
                if rel_path.endswith(gt_file) or Path(rel_path).name == Path(gt_file).name:
                    file_rank = rank
                    break
        if class_rank is None and gt_classes:
            for gt_cls in gt_classes:
                if name == gt_cls:
                    class_rank = rank
                    break
        if strict_rank and lenient_rank and file_rank and (not gt_classes or class_rank):
            break
    return strict_rank, lenient_rank, file_rank, class_rank


# ---------------------------------------------------------------------------
# TACM-v2 result matching — multi-level
# ---------------------------------------------------------------------------

def _gt_match_v2(
    gt_fns: list[str],
    gt_files: list[str],
    gt_classes: list[str],
    selected_nodes,
    top_k: int,
) -> tuple[int | None, int | None, int | None, int | None]:
    """Match TACM-v2 SelectedNode list across all three layers.

    FUNCTION rank: top-K over FUNCTION layer nodes only (primary metric)
    FILE rank    : top-K over FILE layer nodes
    CLASS rank   : top-K over CLASS layer nodes
    Returns (strict_fn_rank, lenient_fn_rank, file_rank, class_rank).
    """
    # FUNCTION-level
    fn_nodes = [(sn.node.node_id, sn.node.file_path or "")
                for sn in selected_nodes if sn.layer.name == "FUNCTION"]
    strict_rank, lenient_rank, _, _ = _match_ranked_nodes(
        gt_fns, gt_files, gt_classes, fn_nodes, top_k
    )

    # FILE-level: did any selected FILE node point to the right file?
    file_rank = None
    for rank, sn in enumerate(
        [sn for sn in selected_nodes if sn.layer.name == "FILE"], 1
    ):
        if rank > top_k:
            break
        node_file = sn.node.file_path or ""
        if _file_matches_gt(node_file, gt_files):
            file_rank = rank
            break

    # CLASS-level: did any selected CLASS node match a GT class?
    class_rank = None
    if gt_classes:
        for rank, sn in enumerate(
            [sn for sn in selected_nodes if sn.layer.name == "CLASS"], 1
        ):
            if rank > top_k:
                break
            if _class_matches_gt(sn.node.node_id, gt_classes):
                class_rank = rank
                break

    return strict_rank, lenient_rank, file_rank, class_rank


# ---------------------------------------------------------------------------
# TACM-v2 ablation variants
# ---------------------------------------------------------------------------

def _select_no_containment_bonus(graph, query: str, token_budget: int):
    """TACM-v2 without containment bonus — ablation 1."""
    from tacm_v2.selector.intent import classify_intent, LAYER_BUDGETS
    from tacm_v2.selector.scoring import NodeScorer
    from tacm_v2.selector.selector import SelectedNode, SelectionResult, _count_tokens
    from tacm_v2.graph.model import Layer
    from tacm_v2.layers.serializers import serialize

    intent = classify_intent(query)
    file_frac, class_frac, fn_frac = LAYER_BUDGETS[intent]
    file_budget  = int(token_budget * file_frac)
    class_budget = int(token_budget * class_frac)
    fn_budget    = token_budget - file_budget - class_budget

    all_nodes = [n for n in graph.nodes.values() if not n.is_test]
    texts = {n.node_id: serialize(n, graph) for n in all_nodes}
    scorer = NodeScorer(graph, query, intent, texts)

    selected = []
    layer_counts = {}
    for layer, budget in [(Layer.FILE, file_budget), (Layer.CLASS, class_budget), (Layer.FUNCTION, fn_budget)]:
        if budget <= 0:
            continue
        nodes = [n for n in graph.nodes_at_layer(layer) if not n.is_test]
        if not nodes:
            continue
        scores = scorer.score_all(nodes)
        # NO containment bonus applied here
        node_scores = sorted([(scores[n.node_id], n) for n in nodes], key=lambda x: -x[0])
        remaining = budget
        count = 0
        for score, node in node_scores:
            text = texts[node.node_id]
            cost = _count_tokens(text)
            if cost <= remaining:
                selected.append(SelectedNode(node=node, layer=layer, text=text,
                                             token_cost=cost, score=score, intent=intent))
                remaining -= cost
                count += 1
        layer_counts[layer.name] = count

    return SelectionResult(nodes=selected, total_tokens=sum(n.token_cost for n in selected),
                           budget=token_budget, intent=intent, layer_counts=layer_counts)


def _select_fixed_budget(graph, query: str, token_budget: int):
    """TACM-v2 with equal 33%/33%/33% budget split — ablation 2 (no intent routing)."""
    from tacm_v2.selector.intent import classify_intent
    from tacm_v2.selector.scoring import NodeScorer
    from tacm_v2.selector.selector import SelectedNode, SelectionResult, _count_tokens
    from tacm_v2.graph.model import Layer
    from tacm_v2.layers.serializers import serialize

    intent = classify_intent(query)
    third = token_budget // 3
    file_budget  = third
    class_budget = third
    fn_budget    = token_budget - file_budget - class_budget

    all_nodes = [n for n in graph.nodes.values() if not n.is_test]
    texts = {n.node_id: serialize(n, graph) for n in all_nodes}
    scorer = NodeScorer(graph, query, intent, texts)

    selected = []
    selected_ids: set[str] = set()
    layer_counts = {}
    CONTAINMENT_BONUS = 0.15

    for layer, budget in [(Layer.FILE, file_budget), (Layer.CLASS, class_budget), (Layer.FUNCTION, fn_budget)]:
        if budget <= 0:
            continue
        nodes = [n for n in graph.nodes_at_layer(layer) if not n.is_test]
        if not nodes:
            continue
        scores = scorer.score_all(nodes)
        for node in nodes:
            if node.parent_id and node.parent_id in selected_ids:
                scores[node.node_id] = min(1.0, scores[node.node_id] + CONTAINMENT_BONUS)
        node_scores = sorted([(scores[n.node_id], n) for n in nodes], key=lambda x: -x[0])
        remaining = budget
        count = 0
        for score, node in node_scores:
            text = texts[node.node_id]
            cost = _count_tokens(text)
            if cost <= remaining:
                selected.append(SelectedNode(node=node, layer=layer, text=text,
                                             token_cost=cost, score=score, intent=intent))
                selected_ids.add(node.node_id)
                remaining -= cost
                count += 1
        layer_counts[layer.name] = count

    return SelectionResult(nodes=selected, total_tokens=sum(n.token_cost for n in selected),
                           budget=token_budget, intent=intent, layer_counts=layer_counts)


def _select_bm25_only(graph, query: str, token_budget: int):
    """TACM-v2 with BM25-only scoring (fan_in=fan_out=complexity=test_cover=0) — ablation 3."""
    from tacm_v2.selector.intent import classify_intent, LAYER_BUDGETS
    from tacm_v2.selector.scoring import NodeScorer
    from tacm_v2.selector.selector import SelectedNode, SelectionResult, _count_tokens
    from tacm_v2.graph.model import Layer
    from tacm_v2.layers.serializers import serialize

    intent = classify_intent(query)
    file_frac, class_frac, fn_frac = LAYER_BUDGETS[intent]
    file_budget  = int(token_budget * file_frac)
    class_budget = int(token_budget * class_frac)
    fn_budget    = token_budget - file_budget - class_budget

    all_nodes = [n for n in graph.nodes.values() if not n.is_test]
    texts = {n.node_id: serialize(n, graph) for n in all_nodes}

    # Override: BM25-only weights — zero out all graph signals
    bm25_only_weights = {"bm25": 1.0, "fan_in": 0.0, "fan_out": 0.0,
                         "complexity": 0.0, "test_cover": 0.0}
    scorer = NodeScorer(graph, query, intent, texts, weight_override=bm25_only_weights)

    selected = []
    selected_ids: set[str] = set()
    layer_counts = {}
    CONTAINMENT_BONUS = 0.15

    for layer, budget in [(Layer.FILE, file_budget), (Layer.CLASS, class_budget), (Layer.FUNCTION, fn_budget)]:
        if budget <= 0:
            continue
        nodes = [n for n in graph.nodes_at_layer(layer) if not n.is_test]
        if not nodes:
            continue
        scores = scorer.score_all(nodes)
        for node in nodes:
            if node.parent_id and node.parent_id in selected_ids:
                scores[node.node_id] = min(1.0, scores[node.node_id] + CONTAINMENT_BONUS)
        node_scores = sorted([(scores[n.node_id], n) for n in nodes], key=lambda x: -x[0])
        remaining = budget
        count = 0
        for score, node in node_scores:
            text = texts[node.node_id]
            cost = _count_tokens(text)
            if cost <= remaining:
                selected.append(SelectedNode(node=node, layer=layer, text=text,
                                             token_cost=cost, score=score, intent=intent))
                selected_ids.add(node.node_id)
                remaining -= cost
                count += 1
        layer_counts[layer.name] = count

    return SelectionResult(nodes=selected, total_tokens=sum(n.token_cost for n in selected),
                           budget=token_budget, intent=intent, layer_counts=layer_counts)


# ---------------------------------------------------------------------------
# Metrics with bootstrap CI
# ---------------------------------------------------------------------------

def mrr(ranks: list[int | None]) -> float:
    n = len(ranks)
    return sum(1 / r for r in ranks if r is not None) / n if n else 0.0


def hit_pct(ranks: list[int | None]) -> float:
    n = len(ranks)
    return 100 * sum(1 for r in ranks if r is not None) / n if n else 0.0


def bootstrap_ci(
    ranks: list[int | None],
    fn=mrr,
    n_boot: int = 2000,
    ci: float = 0.95,
) -> tuple[float, float]:
    if not ranks:
        return 0.0, 0.0
    rng = random.Random(42)
    n = len(ranks)
    boot_vals = [fn([rng.choice(ranks) for _ in range(n)]) for _ in range(n_boot)]
    boot_vals.sort()
    lo = boot_vals[int((1 - ci) / 2 * n_boot)]
    hi = boot_vals[int((1 + ci) / 2 * n_boot)]
    return lo, hi


def paired_bootstrap_p(
    ranks_a: list[int | None],
    ranks_b: list[int | None],
    fn=mrr,
    n_boot: int = 5000,
) -> float:
    """One-sided paired bootstrap p-value: P(MRR_a > MRR_b) under H0: no difference.

    Permutes the sign of per-task differences to simulate H0. Returns the fraction
    of bootstrap samples where the permuted difference exceeds the observed difference.
    A small p-value (e.g. p<0.05) means the observed advantage of A over B is
    unlikely under H0.

    Paired on per-task reciprocal ranks: delta_i = rr(a_i) - rr(b_i).
    """
    assert len(ranks_a) == len(ranks_b), "Paired test requires same-length lists"
    rr = lambda r: (1.0 / r) if r is not None else 0.0
    diffs = [rr(a) - rr(b) for a, b in zip(ranks_a, ranks_b)]
    observed = sum(diffs) / len(diffs)

    rng = random.Random(42)
    n = len(diffs)
    count_exceeds = 0
    for _ in range(n_boot):
        # Under H0, each difference's sign is equally likely to flip
        perm_diff = sum(d * rng.choice((1, -1)) for d in diffs) / n
        if perm_diff >= observed:
            count_exceeds += 1
    return count_exceeds / n_boot


# ---------------------------------------------------------------------------
# Main benchmark
# ---------------------------------------------------------------------------

def run_benchmark(
    project: str,
    repo_root: Path,
    budgets: list[int],
    max_bugs: int = 30,
    top_k: int = 10,
    show_pertask: bool = True,
) -> dict:
    """Run benchmark and return result dict for aggregation."""
    from code_review_graph.graph import GraphStore
    from code_review_graph.incremental import get_db_path
    from tacm_v2.graph.builder import GraphBuilder
    from tacm_v2.selector.selector import select

    print(f"\n=== {project}  @ {repo_root} ===")

    tasks = load_tasks(project, repo_root, max_bugs=max_bugs, skip_no_query=True)
    if not tasks:
        print("  No usable tasks (need valid commit-message queries).")
        return {}

    print(f"  Tasks with valid NL query: {len(tasks)}")
    tasks_with_classes = sum(1 for t in tasks if t.gt_classes)
    print(f"  Tasks with GT classes: {tasks_with_classes}/{len(tasks)}")

    # Build TACM-v2 graph
    print("  Building LayeredGraph...", end=" ", flush=True)
    store = GraphStore(get_db_path(repo_root))
    try:
        graph = GraphBuilder(store).build()
    finally:
        store.close()

    fn_prod = sum(1 for n in graph.nodes.values() if n.layer.name == "FUNCTION" and not n.is_test)
    cls_prod = sum(1 for n in graph.nodes.values() if n.layer.name == "CLASS")
    file_prod = sum(1 for n in graph.nodes.values() if n.layer.name == "FILE")
    print(f"  {fn_prod} prod functions, {cls_prod} classes, {file_prod} files")

    # Flat nodes for BM25
    from code_review_graph.graph import GraphStore as GS
    store2 = GS(get_db_path(repo_root))
    flat_nodes = [n for n in store2.get_nodes_by_kind(["Function"]) if not n.is_test]
    store2.close()

    # Warm up RepoMap
    print("  Building RepoMap index...", end=" ", flush=True)
    _get_repomap(repo_root)
    _ = repomap_rank_nodes(repo_root, "test")
    print("ok")

    repo_key = str(repo_root)

    # Build embedding indexes
    print("  Building MiniLM index...", end=" ", flush=True)
    minilm_idx = _build_minilm_index(flat_nodes, repo_key)
    print("ok" if minilm_idx else "FAILED")

    print("  Building CodeSearch index...", end=" ", flush=True)
    codebert_idx = _build_codesearch_index(flat_nodes, repo_key)
    print("ok" if codebert_idx else "FAILED")

    print("  Building Voyage index...", end=" ", flush=True)
    voyage_idx = _build_voyage_index(flat_nodes, repo_key)
    print("ok" if voyage_idx else "SKIPPED (no key)")

    print("  Building OpenAI index...", end=" ", flush=True)
    openai_idx = _build_openai_index(flat_nodes, repo_key)
    print("ok" if openai_idx else "SKIPPED (no key)")

    results: dict = {}

    # Pre-compute BM25 rankings once (budget-independent)
    bm25_cache: dict[str, list] = {}
    for task in tasks:
        bm25_cache[task.bug_id] = bm25_rank_nodes(flat_nodes, task.query)

    for budget in budgets:
        # All rank slots: _s = strict fn, _l = lenient fn, _f = file, _c = class
        rank_keys = [
            "bm25", "rm", "mini", "cs", "voyage", "oai",
            "hmini", "hcs", "v2", "v2_nocb", "v2_fixed", "v2_bm25only"
        ]
        ranks: dict[str, dict] = {k: {"s": [], "l": [], "f": [], "c": []} for k in rank_keys}

        per_task_rows = []

        for task in tasks:
            q = task.query
            bm25_ranked = bm25_cache[task.bug_id]

            # BM25-Body
            bs, bl, bf, bc = _match_ranked_nodes(task.gt_functions, task.gt_files, task.gt_classes, bm25_ranked, top_k)

            # RepoMap
            rm_ranked = repomap_rank_nodes(repo_root, q)
            rs, rl, rf, rc = _gt_match_repomap(task.gt_functions, task.gt_files, task.gt_classes, rm_ranked, top_k)

            # Dense-MiniLM
            mini_ranked = _dense_rank_st(q, minilm_idx) if minilm_idx else []
            ms, ml, mf, mc = _match_ranked_nodes(task.gt_functions, task.gt_files, task.gt_classes, mini_ranked, top_k)

            # Dense-CodeSearch
            cs_ranked = _dense_rank_st(q, codebert_idx) if codebert_idx else []
            css, csl, csf, csc = _match_ranked_nodes(task.gt_functions, task.gt_files, task.gt_classes, cs_ranked, top_k)

            # Dense-Voyage
            voy_ranked = _dense_rank_voyage(q, voyage_idx) if voyage_idx else []
            voys, voyl, voyf, voyc = _match_ranked_nodes(task.gt_functions, task.gt_files, task.gt_classes, voy_ranked, top_k)

            # Dense-OpenAI
            oai_ranked = _dense_rank_openai(q, openai_idx) if openai_idx else []
            oais, oail, oaif, oaic = _match_ranked_nodes(task.gt_functions, task.gt_files, task.gt_classes, oai_ranked, top_k)

            # Hybrid-MiniLM
            hm_ranked = _hybrid_rrf_rank(bm25_ranked, mini_ranked) if mini_ranked else bm25_ranked
            hms, hml, hmf, hmc = _match_ranked_nodes(task.gt_functions, task.gt_files, task.gt_classes, hm_ranked, top_k)

            # Hybrid-CodeSearch
            hcs_ranked = _hybrid_rrf_rank(bm25_ranked, cs_ranked) if cs_ranked else bm25_ranked
            hcss, hcsl, hcsf, hcsc = _match_ranked_nodes(task.gt_functions, task.gt_files, task.gt_classes, hcs_ranked, top_k)

            # TACM-v2 (full)
            sel = select(graph, q, token_budget=budget)
            vs, vl, vf, vc = _gt_match_v2(task.gt_functions, task.gt_files, task.gt_classes, sel.nodes, top_k)

            # TACM-v2 ablation: no containment bonus
            sel_nocb = _select_no_containment_bonus(graph, q, budget)
            nocb_s, nocb_l, nocb_f, nocb_c = _gt_match_v2(task.gt_functions, task.gt_files, task.gt_classes, sel_nocb.nodes, top_k)

            # TACM-v2 ablation: fixed budget (no intent routing)
            sel_fixed = _select_fixed_budget(graph, q, budget)
            fix_s, fix_l, fix_f, fix_c = _gt_match_v2(task.gt_functions, task.gt_files, task.gt_classes, sel_fixed.nodes, top_k)

            # TACM-v2 ablation: BM25-only signals
            sel_bm25only = _select_bm25_only(graph, q, budget)
            bo_s, bo_l, bo_f, bo_c = _gt_match_v2(task.gt_functions, task.gt_files, task.gt_classes, sel_bm25only.nodes, top_k)

            for key, (s, l, f, c) in [
                ("bm25",      (bs, bl, bf, bc)),
                ("rm",        (rs, rl, rf, rc)),
                ("mini",      (ms, ml, mf, mc)),
                ("cs",        (css, csl, csf, csc)),
                ("voyage",    (voys, voyl, voyf, voyc)),
                ("oai",       (oais, oail, oaif, oaic)),
                ("hmini",     (hms, hml, hmf, hmc)),
                ("hcs",       (hcss, hcsl, hcsf, hcsc)),
                ("v2",        (vs, vl, vf, vc)),
                ("v2_nocb",   (nocb_s, nocb_l, nocb_f, nocb_c)),
                ("v2_fixed",  (fix_s, fix_l, fix_f, fix_c)),
                ("v2_bm25only", (bo_s, bo_l, bo_f, bo_c)),
            ]:
                ranks[key]["s"].append(s)
                ranks[key]["l"].append(l)
                ranks[key]["f"].append(f)
                ranks[key]["c"].append(c)

            per_task_rows.append((task, bs, rs, ms, css, voys, oais, hms, hcss, vs, nocb_s, fix_s, bo_s))

        def ci(key, dim="s"): return bootstrap_ci(ranks[key][dim])
        def m(key, dim="s"):  return mrr(ranks[key][dim])
        def h(key, dim="s"):  return hit_pct(ranks[key][dim])

        results[budget] = {
            "n": len(tasks),
            "bm25_mrr": m("bm25"),  "rm_mrr":   m("rm"),
            "mini_mrr": m("mini"),  "cs_mrr":   m("cs"),
            "voy_mrr":  m("voyage"),"oai_mrr":  m("oai"),
            "hmini_mrr":m("hmini"), "hcs_mrr":  m("hcs"),
            "v2_mrr":   m("v2"),
            "v2_nocb_mrr":  m("v2_nocb"),
            "v2_fixed_mrr": m("v2_fixed"),
            "v2_bm25only_mrr": m("v2_bm25only"),
        }

        # ---- Primary table: FUNCTION-level strict MRR ----
        print(f"\n  budget={budget}  n={len(tasks)}  top-{top_k}  [FUNCTION-STRICT MRR]")
        print(f"  {'System':<22} {'Hit%':>5}  {'MRR':>6}  {'95% CI':>16}  {'vs BM25':>8}  {'p vs BM25':>9}  {'p vs MiniLM':>11}")
        print(f"  {'-'*88}")
        baselines = [
            ("BM25-Body",         "bm25"),
            ("RepoMap",           "rm"),
            ("Dense-MiniLM",      "mini"),
            ("Dense-CodeSearch",  "cs"),
            ("Dense-Voyage",      "voyage"),
            ("Dense-OpenAI",      "oai"),
            ("Hybrid-MiniLM",     "hmini"),
            ("Hybrid-CodeSearch", "hcs"),
            ("TACM-v2",           "v2"),
        ]
        for label, key in baselines:
            mrr_s = m(key); ci_s = ci(key); delta = mrr_s - m("bm25")
            # Paired bootstrap p-values: H0 = this system is no better than BM25/MiniLM
            p_bm25  = paired_bootstrap_p(ranks[key]["s"], ranks["bm25"]["s"])
            p_mini  = paired_bootstrap_p(ranks[key]["s"], ranks["mini"]["s"])
            skipped = " [no key]" if key in ("voyage", "oai") and not any(ranks[key]["s"]) else ""
            print(f"  {label:<22} {h(key):>4.0f}%  {mrr_s:>6.4f}  "
                  f"[{ci_s[0]:.4f},{ci_s[1]:.4f}]  {delta:>+8.4f}  "
                  f"{p_bm25:>9.3f}  {p_mini:>11.3f}{skipped}")

        # ---- Ablation table with significance vs full TACM-v2 ----
        print(f"\n  [ABLATIONS vs TACM-v2 full]")
        print(f"  {'System':<22} {'Hit%':>5}  {'MRR':>6}  {'Δ vs v2':>8}  {'p(v2>this)':>10}  Description")
        print(f"  {'-'*82}")
        ablations = [
            ("TACM-v2",          "v2",          "full system"),
            ("TACM-NoCB",        "v2_nocb",     "no containment bonus"),
            ("TACM-FixedBudget", "v2_fixed",    "equal 33/33/33 layer split"),
            ("TACM-BM25Only",    "v2_bm25only", "BM25 signal only, no graph"),
        ]
        v2_mrr = m("v2")
        for label, key, desc in ablations:
            mrr_s = m(key); delta = mrr_s - v2_mrr
            # p-value that full TACM-v2 beats this ablation
            p_abl = paired_bootstrap_p(ranks["v2"]["s"], ranks[key]["s"])
            print(f"  {label:<22} {h(key):>4.0f}%  {mrr_s:>6.4f}  {delta:>+8.4f}  {p_abl:>10.3f}  {desc}")

        # ---- Multi-level table ----
        # NOTE on interpretation:
        #   For flat retrievers (BM25, dense, hybrid): file/class columns show what fraction
        #   of their TOP-K *function* results happen to be in the GT file/class.
        #   This measures "file/class attribution" — implicitly derived from fn ranking.
        #
        #   For TACM-v2: file/class columns show actual FILE-layer and CLASS-layer node
        #   selection hit rates — an explicit structural routing decision.
        #
        #   These are different things. The comparison shows TACM's structural routing
        #   quality relative to flat retrievers' implicit file/class coverage, not a
        #   direct apples-to-apples retrieval race at the file/class level.
        print(f"\n  [MULTI-LEVEL HIT@{top_k}]")
        print(f"  Flat systems: file/class cols = fn results attributed to GT file/class")
        print(f"  TACM-v2:      file/class cols = explicit FILE/CLASS layer node hits")
        print(f"  {'System':<22} {'File%':>6} {'Class%':>7} {'Fn%':>5}  "
              f"File-MRR  Class-MRR   Fn-MRR")
        print(f"  {'-'*72}")
        ml_systems = baselines + [("TACM-NoCB", "v2_nocb")]
        for label, key in ml_systems:
            fh  = h(key, "f");  ch  = h(key, "c");  sh  = h(key, "s")
            fm  = m(key, "f");  cm  = m(key, "c");  sm  = m(key, "s")
            print(f"  {label:<22} {fh:>5.0f}%  {ch:>6.0f}%  {sh:>4.0f}%  "
                  f"{fm:>8.4f}  {cm:>9.4f}  {sm:>8.4f}")

        if len(tasks) < 10:
            print(f"  WARNING: n={len(tasks)} — too small for reliable conclusions.")

        if show_pertask:
            print(f"\n  Per-task [FUNCTION-STRICT] top-{top_k}:")
            print(f"  {'ID':<20} {'BM25':>5} {'RM':>4} {'Mini':>5} {'CS':>4} "
                  f"{'Voy':>4} {'OAI':>4} {'HMini':>6} {'HCS':>5} "
                  f"{'V2':>4} {'NoCB':>5} {'Fix':>4} {'BOnly':>5}  GT")
            print(f"  {'-'*100}")
            for row in per_task_rows:
                task, bs, rs, ms, css, voys, oais, hms, hcss, vs, nocb_s, fix_s, bo_s = row
                def fmt(r): return f"#{r}" if r else "miss"
                gt_short = ", ".join(task.gt_functions[:2])
                print(f"  {task.bug_id:<20} {fmt(bs):>5} {fmt(rs):>4} {fmt(ms):>5} "
                      f"{fmt(css):>4} {fmt(voys):>4} {fmt(oais):>4} {fmt(hms):>6} "
                      f"{fmt(hcss):>5} {fmt(vs):>4} {fmt(nocb_s):>5} {fmt(fix_s):>4} "
                      f"{fmt(bo_s):>5}  {gt_short}")

    return results


def run_all(budgets: list[int], max_bugs: int, top_k: int) -> None:
    """Run all repos and print aggregate."""
    configs = [
        ("thefuck", ROOT / "thefuck"),
        ("scrapy",  ROOT / "scrapy"),
        ("tornado", ROOT / "tornado"),
    ]

    all_results: list[dict] = []
    for project, repo_root in configs:
        if not repo_root.exists():
            print(f"Skipping {project} — repo not found at {repo_root}")
            continue
        r = run_benchmark(project, repo_root, budgets=budgets,
                          max_bugs=max_bugs, top_k=top_k, show_pertask=False)
        if r:
            all_results.append({"project": project, **r})

    print("\n" + "="*70)
    print("AGGREGATE (macro-average MRR across projects)")
    print("="*70)
    for budget in budgets:
        vals = [r[budget] for r in all_results if budget in r]
        if not vals:
            continue
        total_n = sum(v["n"] for v in vals)
        print(f"\n  budget={budget}  projects={len(vals)}  total_n={total_n}")

        # Function-level strict MRR
        print(f"\n  [FUNCTION-STRICT]")
        systems = [
            ("BM25-Body",        "bm25_mrr"),
            ("RepoMap",          "rm_mrr"),
            ("Dense-MiniLM",     "mini_mrr"),
            ("Dense-CodeSearch", "cs_mrr"),
            ("Dense-Voyage",     "voy_mrr"),
            ("Dense-OpenAI",     "oai_mrr"),
            ("Hybrid-MiniLM",    "hmini_mrr"),
            ("Hybrid-CodeSearch","hcs_mrr"),
            ("TACM-v2",          "v2_mrr"),
            ("TACM-NoCB",        "v2_nocb_mrr"),
            ("TACM-FixedBudget", "v2_fixed_mrr"),
            ("TACM-BM25Only",    "v2_bm25only_mrr"),
        ]
        bm25_macro = sum(v["bm25_mrr"] for v in vals) / len(vals)
        for label, key in systems:
            macro = sum(v[key] for v in vals) / len(vals)
            delta = macro - bm25_macro
            print(f"    {label:<22}  MRR={macro:.4f}  Δ={delta:+.4f}")


def main():
    parser = argparse.ArgumentParser(description="TACM-v2 BugsInPy benchmark")
    parser.add_argument("--project", help="thefuck | scrapy | tornado")
    parser.add_argument("--repo", type=Path)
    parser.add_argument("--all", action="store_true", help="Run all repos")
    parser.add_argument("--max", type=int, default=30)
    parser.add_argument("--budget", type=int, nargs="+", default=[4000])
    parser.add_argument("--topk", type=int, default=10)
    parser.add_argument("--no-pertask", action="store_true")
    args = parser.parse_args()

    if args.all:
        run_all(args.budget, args.max, args.topk)
    elif args.project and args.repo:
        run_benchmark(
            project=args.project,
            repo_root=args.repo.resolve(),
            budgets=args.budget,
            max_bugs=args.max,
            top_k=args.topk,
            show_pertask=not args.no_pertask,
        )
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
