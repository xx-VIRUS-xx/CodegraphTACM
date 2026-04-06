"""crg_adapter.py — maps code-review-graph GraphNode/GraphEdge objects to TACM ScoredNode.

Uses the full crg capability set:
- hybrid_search(): FTS5 BM25 + RRF (replaces naive LIKE search)
- callers_of traversal: expands hits with graph-aware caller context
- TESTED_BY edges: direct test coverage signal
- signature field: included in FTS5 index for better matching
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from code_review_graph.graph import GraphStore, GraphNode
from code_review_graph.incremental import get_db_path
from code_review_graph.search import hybrid_search

if TYPE_CHECKING:
    from .resolver import ScoredNode


def _degree(store: GraphStore, qualified_name: str) -> int:
    out = store.get_edges_by_source(qualified_name)
    into = store.get_edges_by_target(qualified_name)
    return len(out) + len(into)


def _has_test(store: GraphStore, qualified_name: str) -> bool:
    edges = store.get_edges_by_target(qualified_name)
    return any(e.kind == "TESTED_BY" for e in edges)


TRUNCATION_LINE_THRESHOLD = 40   # functions longer than this get a summary payload
TRUNCATION_TOKEN_CAP      = 120  # tokens for signature + first docstring line

def _token_cost(source_text: str, line_start: int | None = None, line_end: int | None = None) -> int:
    if source_text:
        return max(1, len(source_text) // 4)
    if line_start and line_end:
        return max(1, (line_end - line_start + 1) * 8)
    return 20


def _read_source(file_path: str, line_start: int | None, line_end: int | None) -> str:
    if not (file_path and line_start and line_end):
        return ""
    try:
        lines = Path(file_path).read_text(errors="replace").splitlines()
        return "\n".join(lines[max(0, line_start - 1): min(len(lines), line_end)])
    except OSError:
        return ""


def _truncated_source(file_path: str, line_start: int | None, line_end: int | None) -> str:
    """Return signature + docstring only for oversized functions.

    For a function too large to fit in a tight budget, we still want it
    in the selected set — the LLM can see its signature, docstring, and
    first few lines, which is enough to identify it as the bug location.
    Full body is omitted; the LLM can request it separately.
    """
    if not (file_path and line_start and line_end):
        return ""
    try:
        lines = Path(file_path).read_text(errors="replace").splitlines()
        body = lines[max(0, line_start - 1): min(len(lines), line_end)]
        # Keep: def line + decorator lines before it + up to 8 lines of docstring/body
        result = []
        for line in body[:12]:
            result.append(line)
            # Stop after closing triple-quote if we're in a docstring
            stripped = line.strip()
            if len(result) > 3 and stripped in ('"""', "'''", '"""', "'''"):
                break
        result.append("    # ... (truncated, function continues)")
        return "\n".join(result)
    except OSError:
        return ""


def _graph_node_to_scored(
    store: GraphStore,
    n: GraphNode,
    in_blast_radius: bool,
    hybrid_score: float = 0.0,
) -> "ScoredNode":
    from .resolver import ScoredNode
    source_text = _read_source(n.file_path, n.line_start, n.line_end)
    return ScoredNode(
        node_id=n.qualified_name,
        name=n.name,
        file_path=n.file_path,
        source_text=source_text,
        token_cost=_token_cost(source_text, n.line_start, n.line_end),
        degree=_degree(store, n.qualified_name),
        in_blast_radius=in_blast_radius,
        has_test=_has_test(store, n.qualified_name),
        is_test=n.is_test,
        line_start=n.line_start or 0,
        line_end=n.line_end or 0,
        hybrid_score=hybrid_score,
    )


def query_to_scored_nodes(
    store: GraphStore,
    query: str,
    repo_root: Path,
    max_candidates: int = 80,
) -> list["ScoredNode"]:
    """Build a scored candidate pool using crg's full capability set.

    1. hybrid_search(): FTS5 BM25 + optional embeddings merged via RRF.
       Includes signature text in the FTS index — better than name-only LIKE.
    2. callers_of expansion: for each direct hit, add its callers (1 hop)
       so the resolver can reward high-connectivity context nodes.
    3. in_blast_radius=True for direct hits (they are the "changed" nodes
       conceptually), False for caller expansions.
    4. hybrid_score passed through so the resolver can use it as a 4th signal.
    """
    from .resolver import ScoredNode

    # --- Phase 1: hybrid search (FTS5 BM25 + RRF) ---
    # FTS5 wraps the whole query as a phrase ("word1 word2") — fails for multi-word
    # natural-language queries. Run one hybrid_search per keyword + the full query,
    # accumulate scores with max-merge. This uses FTS5 BM25 + kind boosting properly.
    keywords = [w for w in query.split() if len(w) > 2]
    score_by_qn: dict[str, float] = {}

    for kw in keywords:
        for h in hybrid_search(store, kw, limit=20):
            qn = h["qualified_name"]
            score_by_qn[qn] = max(score_by_qn.get(qn, 0.0), h["score"])

    # Also try full query (works if the query happens to be a function name or short phrase)
    for h in hybrid_search(store, query, limit=10):
        qn = h["qualified_name"]
        score_by_qn[qn] = max(score_by_qn.get(qn, 0.0), h["score"])

    direct_qns: set[str] = set(score_by_qn.keys())

    # Fetch full GraphNode objects for direct hits — production functions only.
    # Test nodes inflate degree counts and dominate hybrid_score for keyword
    # queries that match test function names (e.g. "test_session_cookies").
    # The resolver's exclude_tests=True handles selection, but keeping tests
    # in the candidate pool inflates scores and crowds out production nodes.
    direct_nodes = store._batch_get_nodes(direct_qns)
    direct_nodes = [n for n in direct_nodes if n.kind == "Function" and not n.is_test]

    # --- Phase 2: callers_of expansion (graph traversal, 1 hop) ---
    # Use store.get_edges_by_target with CALLS filter — same as crg callers_of tool.
    # This surfaces the functions that CALL our matched functions, which are
    # often the actual bug location (a caller passing bad args, not the callee).
    caller_qns: set[str] = set()
    for n in direct_nodes:
        for e in store.get_edges_by_target(n.qualified_name):
            if e.kind == "CALLS" and "::" in e.source_qualified:
                caller_qns.add(e.source_qualified)
    # Also expand one hop via name-based CALLS (crg stores unqualified targets)
    for n in direct_nodes:
        for e in store.search_edges_by_target_name(n.name, kind="CALLS"):
            if "::" in e.source_qualified:
                caller_qns.add(e.source_qualified)

    caller_qns -= direct_qns  # don't double-add
    caller_nodes = store._batch_get_nodes(caller_qns)
    caller_nodes = [n for n in caller_nodes if n.kind in ("Function", "Test")]

    # Cap total
    all_graph_nodes = (direct_nodes + caller_nodes)[:max_candidates]

    # --- Phase 3: build ScoredNode list ---
    scored: list[ScoredNode] = []
    for n in all_graph_nodes:
        is_direct = n.qualified_name in direct_qns
        line_count = (n.line_end or 0) - (n.line_start or 0) + 1
        if line_count > TRUNCATION_LINE_THRESHOLD:
            # Large function: store truncated payload so it fits in tight budgets.
            # The resolver scores it on full structural signals; the payload sent
            # to the LLM is sig+docstring only. Full body retrievable on demand.
            source_text = _truncated_source(n.file_path, n.line_start, n.line_end)
        else:
            source_text = _read_source(n.file_path, n.line_start, n.line_end)
        scored.append(ScoredNode(
            node_id=n.qualified_name,
            name=n.name,
            file_path=n.file_path,
            source_text=source_text,
            token_cost=_token_cost(source_text, n.line_start, n.line_end),
            degree=_degree(store, n.qualified_name),
            in_blast_radius=is_direct,
            has_test=_has_test(store, n.qualified_name),
            is_test=n.is_test,
            line_start=n.line_start or 0,
            line_end=n.line_end or 0,
            hybrid_score=score_by_qn.get(n.qualified_name, 0.0),
        ))

    return scored


def get_blast_radius_nodes(
    store: GraphStore,
    changed_files: list[str],
    repo_root: Path,
    max_depth: int = 2,
) -> list["ScoredNode"]:
    """Return ScoredNodes for the blast radius of changed_files (review/PR path)."""
    from .resolver import ScoredNode

    abs_files = [str(repo_root / f) for f in changed_files]
    impact = store.get_impact_radius(abs_files, max_depth=max_depth)

    all_graph_nodes = impact["changed_nodes"] + impact["impacted_nodes"]
    changed_qns = {n.qualified_name for n in impact["changed_nodes"]}

    edge_counts: dict[str, int] = {}
    for e in impact["edges"]:
        edge_counts[e.source_qualified] = edge_counts.get(e.source_qualified, 0) + 1
        edge_counts[e.target_qualified] = edge_counts.get(e.target_qualified, 0) + 1

    tested_qns = {e.source_qualified for e in impact["edges"] if e.kind == "TESTED_BY"}

    scored: list[ScoredNode] = []
    for n in all_graph_nodes:
        if n.kind not in ("Function", "Test"):
            continue
        source_text = _read_source(n.file_path, n.line_start, n.line_end)
        scored.append(ScoredNode(
            node_id=n.qualified_name,
            name=n.name,
            file_path=n.file_path,
            source_text=source_text,
            token_cost=_token_cost(source_text, n.line_start, n.line_end),
            degree=edge_counts.get(n.qualified_name, 0),
            in_blast_radius=(n.qualified_name not in changed_qns),
            has_test=(n.qualified_name in tested_qns),
            is_test=n.is_test,
            line_start=n.line_start or 0,
            line_end=n.line_end or 0,
            hybrid_score=0.0,
        ))

    return scored


def open_store(repo_root: str | Path) -> tuple[GraphStore, Path]:
    root = Path(repo_root).resolve()
    return GraphStore(get_db_path(root)), root
