"""crg_adapter.py — maps code-review-graph GraphNode/GraphEdge objects to TACM ScoredNode.

Uses the full crg capability set:
- hybrid_search(): FTS5 BM25 + RRF (replaces naive LIKE search)
- callers_of traversal: expands hits with graph-aware caller context
- TESTED_BY edges: direct test coverage signal
- signature field: included in FTS5 index for better matching
- G3: semantic embedding similarity (SemanticIndex) — 5th scoring signal
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from code_review_graph.graph import GraphStore, GraphNode
from code_review_graph.incremental import get_db_path
from code_review_graph.search import hybrid_search

if TYPE_CHECKING:
    from .resolver import ScoredNode

# G3: semantic index is built lazily and cached per db_path
_semantic_cache: dict[str, object] = {}  # db_path -> SemanticIndex | None


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


FULL_CORPUS_BUDGET_THRESHOLD = 8000  # At budgets >= this, bypass FTS5 cap and score all nodes

# G3: semantic score weight when blending with FTS5 hybrid_score.
# Semantic can raise a zero-FTS node (Mode B rescue) but cannot override a strong FTS hit.
SEMANTIC_WEIGHT = 0.8   # semantic_score * this is used as the floor
SEMANTIC_TOP_K = 40     # how many top-semantic hits to include in candidate expansion


def _get_semantic_index(store: GraphStore):
    """Lazily build or load the semantic index for this store's DB. Returns None if unavailable."""
    from .semantic import SemanticIndex
    db_key = store.db_path
    if db_key not in _semantic_cache:
        all_prod = store.get_nodes_by_kind(["Function"])
        prod_nodes = [n for n in all_prod if not n.is_test]
        _semantic_cache[db_key] = SemanticIndex.build(store.db_path, prod_nodes)
    return _semantic_cache[db_key]


def query_to_scored_nodes(
    store: GraphStore,
    query: str,
    repo_root: Path,
    max_candidates: int = 80,
    token_budget: int = 4000,
    use_semantic: bool = True,
) -> list["ScoredNode"]:
    """Build a scored candidate pool using crg's full capability set.

    1. hybrid_search(): FTS5 BM25 + optional embeddings merged via RRF.
       Includes signature text in the FTS index — better than name-only LIKE.
    2. callers_of expansion: for each direct hit, add its callers (1 hop)
       so the resolver can reward high-connectivity context nodes.
    3. in_blast_radius=True for direct hits (they are the "changed" nodes
       conceptually), False for caller expansions.
    4. hybrid_score passed through so the resolver can use it as a 4th signal.

    At token_budget >= FULL_CORPUS_BUDGET_THRESHOLD (8k): bypass FTS5 cap and
    return all production nodes scored by degree + hybrid signal. This prevents
    the 32k-budget regression where Naive RAG wins by brute-force covering nodes
    that FTS5 never retrieves.
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
    direct_nodes = store._batch_get_nodes(direct_qns)
    direct_nodes = [n for n in direct_nodes if n.kind == "Function" and not n.is_test]

    # --- Phase 2: callers_of expansion (graph traversal, 1 hop) ---
    # Also track the max parent hybrid_score so caller nodes can inherit
    # partial credit — prevents graph-traversed nodes scoring zero when
    # the direct hit had a strong FTS5 signal.
    caller_qns: set[str] = set()
    caller_parent_score: dict[str, float] = {}  # caller_qn -> max parent hs

    for n in direct_nodes:
        parent_hs = score_by_qn.get(n.qualified_name, 0.0)
        for e in store.get_edges_by_target(n.qualified_name):
            if e.kind == "CALLS" and "::" in e.source_qualified:
                caller_qns.add(e.source_qualified)
                caller_parent_score[e.source_qualified] = max(
                    caller_parent_score.get(e.source_qualified, 0.0), parent_hs
                )
    for n in direct_nodes:
        parent_hs = score_by_qn.get(n.qualified_name, 0.0)
        for e in store.search_edges_by_target_name(n.name, kind="CALLS"):
            if "::" in e.source_qualified:
                caller_qns.add(e.source_qualified)
                caller_parent_score[e.source_qualified] = max(
                    caller_parent_score.get(e.source_qualified, 0.0), parent_hs
                )

    caller_qns -= direct_qns
    caller_nodes = store._batch_get_nodes(caller_qns)
    caller_nodes = [n for n in caller_nodes if n.kind in ("Function", "Test")]

    # --- Phase 2b: G3 semantic expansion ---
    # Build semantic scores for all nodes, add top-K semantic hits to the candidate pool.
    # This rescues Mode B nodes: functions never hit by FTS5 due to lexical gap.
    # semantic_score is blended with fts_score: final = max(fts, semantic * SEMANTIC_WEIGHT).
    semantic_score_by_qn: dict[str, float] = {}
    if use_semantic:
        try:
            sem_idx = _get_semantic_index(store)
            if sem_idx is not None:
                sem_hits = sem_idx.query(query, top_k=SEMANTIC_TOP_K)
                semantic_score_by_qn = sem_hits
                # Add semantic top hits to the candidate pool (Mode B rescue)
                sem_qns = set(sem_hits.keys()) - direct_qns - caller_qns
                sem_nodes = store._batch_get_nodes(sem_qns)
                sem_nodes = [n for n in sem_nodes if n.kind == "Function" and not n.is_test]
                # Inject as additional direct candidates (they got here via semantics, not FTS)
                direct_nodes = direct_nodes + sem_nodes
                direct_qns |= {n.qualified_name for n in sem_nodes}
        except Exception as exc:
            import logging
            logging.getLogger(__name__).warning("G3 semantic scoring failed: %s", exc)

    if token_budget >= FULL_CORPUS_BUDGET_THRESHOLD:
        # At large budgets: use full corpus only for small repos (< 2000 prod nodes)
        # where the full corpus is manageable and FTS80 would miss Mode B functions.
        # For large repos (e.g. SQLAlchemy at 15k nodes), full corpus degrades quality
        # because most nodes have no hybrid signal and degree becomes the only
        # discriminator — which is too noisy at this scale.
        all_prod = store.get_nodes_by_kind(["Function"])
        all_prod = [n for n in all_prod if not n.is_test]
        if len(all_prod) <= 2000:
            all_graph_nodes = all_prod
        else:
            # Large repo: expand FTS candidates proportional to budget
            expanded = min(len(all_prod), max_candidates * (token_budget // 4000))
            all_graph_nodes = (direct_nodes + caller_nodes)[:expanded]
    else:
        all_graph_nodes = (direct_nodes + caller_nodes)[:max_candidates]

    # --- Phase 3: build ScoredNode list ---
    scored: list[ScoredNode] = []
    for n in all_graph_nodes:
        is_direct = n.qualified_name in direct_qns
        line_count = (n.line_end or 0) - (n.line_start or 0) + 1
        if line_count > TRUNCATION_LINE_THRESHOLD:
            source_text = _truncated_source(n.file_path, n.line_start, n.line_end)
        else:
            source_text = _read_source(n.file_path, n.line_start, n.line_end)
        # Blend FTS5 score with semantic score (G3):
        # - FTS hits: fts_score dominates, semantic adds a small floor
        # - Mode B nodes (FTS miss): semantic_score * SEMANTIC_WEIGHT lifts them
        fts_score = score_by_qn.get(
            n.qualified_name,
            caller_parent_score.get(n.qualified_name, 0.0) * 0.5,
        )
        sem_score = semantic_score_by_qn.get(n.qualified_name, 0.0) * SEMANTIC_WEIGHT
        blended_hs = max(fts_score, sem_score)

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
            hybrid_score=blended_hs,
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
