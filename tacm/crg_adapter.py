"""crg_adapter.py — maps code-review-graph GraphNode/GraphEdge objects to TACM ScoredNode.

Uses the full crg capability set:
- hybrid_search(): FTS5 BM25 + RRF (replaces naive LIKE search)
- callers_of traversal: expands hits with graph-aware caller context (1-hop and 2-hop)
- TESTED_BY edges: direct test coverage signal
- signature field: included in FTS5 index for better matching
- G3: semantic embedding similarity (SemanticIndex) — 5th scoring signal
- G4-A: LLM query rewriting — decomposes NL bug report into targeted sub-queries
- G4-B: 2-hop caller traversal with score decay
- BM25-Body: BM25Okapi on full function source text (closes Gap 1: FTS5 only indexes name/sig)
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import TYPE_CHECKING

from code_review_graph.graph import GraphStore, GraphNode
from code_review_graph.incremental import get_db_path
from code_review_graph.search import hybrid_search

if TYPE_CHECKING:
    from .resolver import ScoredNode

# G3: semantic index is built lazily and cached per db_path
_semantic_cache: dict[str, object] = {}  # db_path -> SemanticIndex | None

# BM25-Body: cached per db_path to avoid rebuilding corpus on every query
_bm25_cache: dict[str, object] = {}  # db_path -> _BM25BodyIndex | None


def _tokenize_bm25(text: str) -> list[str]:
    """Simple lowercase word-boundary tokenizer for BM25."""
    return re.findall(r"[a-z0-9]+", text.lower())


class _BM25BodyIndex:
    """BM25Okapi index over full function source text for all prod nodes."""

    def __init__(self, nodes: list, source_texts: list[str]):
        from rank_bm25 import BM25Okapi
        self.nodes = nodes
        corpus = [_tokenize_bm25(t) for t in source_texts]
        self.bm25 = BM25Okapi(corpus)

    def query(self, query: str, top_k: int = 40) -> dict[str, float]:
        """Return {qualified_name: normalized_score} for top_k BM25 body hits.

        Scores are normalized to [0, 1.0] — caller rescales to FTS5 range.
        """
        q_tokens = _tokenize_bm25(query)
        if not q_tokens:
            return {}
        raw = self.bm25.get_scores(q_tokens)
        max_score = float(max(raw)) if len(raw) > 0 else 1.0
        if max_score <= 0:
            return {}
        pairs = sorted(zip(raw, self.nodes), key=lambda x: -x[0])
        result = {}
        for score, node in pairs[:top_k]:
            if score <= 0:
                break
            result[node.qualified_name] = score / max_score  # normalized [0, 1]
        return result


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


def _get_bm25_index(store: GraphStore) -> "_BM25BodyIndex | None":
    """Lazily build BM25Okapi index over full function source text. Returns None if rank_bm25 unavailable."""
    db_key = store.db_path
    if db_key not in _bm25_cache:
        try:
            all_prod = store.get_nodes_by_kind(["Function"])
            prod_nodes = [n for n in all_prod if not n.is_test]
            source_texts = [
                _read_source(n.file_path, n.line_start, n.line_end) or n.name
                for n in prod_nodes
            ]
            _bm25_cache[db_key] = _BM25BodyIndex(prod_nodes, source_texts)
        except ImportError:
            _bm25_cache[db_key] = None
        except Exception as exc:
            import logging
            logging.getLogger(__name__).warning("BM25-Body index build failed: %s", exc)
            _bm25_cache[db_key] = None
    return _bm25_cache[db_key]


def query_to_scored_nodes(
    store: GraphStore,
    query: str,
    repo_root: Path,
    max_candidates: int = 120,
    token_budget: int = 4000,
    use_semantic: bool = True,
    use_bm25_body: bool = True,
    use_rewriter: bool = False,
    two_hop: bool = True,
    use_reranker: bool = False,
    use_cochange: bool = False,
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

    # --- Phase 0: G4-F file routing for large corpora ---
    # For corpora > FILE_ROUTER_MIN_NODES, restrict FTS5 + semantic search to
    # the top-K most relevant files. Reduces noise from unrelated subsystems.
    _file_filter: set[str] | None = None
    if token_budget < FULL_CORPUS_BUDGET_THRESHOLD:
        try:
            from .file_router import get_file_router, FILE_ROUTER_MIN_NODES
            all_prod_check = store.get_nodes_by_kind(["Function"])
            all_prod_check = [n for n in all_prod_check if not n.is_test]
            if len(all_prod_check) >= FILE_ROUTER_MIN_NODES:
                router = get_file_router(store, all_prod_check)
                if router is not None:
                    _file_filter = router.route(query)
        except Exception as exc:
            import logging
            logging.getLogger(__name__).warning("File router failed: %s", exc)

    # --- Phase 1: hybrid search (FTS5 BM25 + RRF) ---
    # G4-A: if use_rewriter=True, decompose the NL bug report into targeted sub-queries
    # phrased as implementation actions (e.g. "rebuild auth header on redirect" instead of
    # "cookies not sent after redirect"). Each sub-query hits FTS5 independently.
    # Without rewriter: split into individual keywords as before.
    from .query_rewriter import rewrite_query_if_enabled
    sub_queries = rewrite_query_if_enabled(query, use_rewriter=use_rewriter)

    score_by_qn: dict[str, float] = {}

    for sq in sub_queries:
        # Per-keyword search within each sub-query
        keywords = [w for w in sq.split() if len(w) > 2]
        for kw in keywords:
            for h in hybrid_search(store, kw, limit=20):
                qn = h["qualified_name"]
                score_by_qn[qn] = max(score_by_qn.get(qn, 0.0), h["score"])
        # Also try the full sub-query as a phrase
        for h in hybrid_search(store, sq, limit=10):
            qn = h["qualified_name"]
            score_by_qn[qn] = max(score_by_qn.get(qn, 0.0), h["score"])

    # Always also try the original full query
    for h in hybrid_search(store, query, limit=10):
        qn = h["qualified_name"]
        score_by_qn[qn] = max(score_by_qn.get(qn, 0.0), h["score"])

    # BM25-Body: search full function source text (closes Gap 1 — FTS5 only indexes name/sig).
    # Top-K BM25 hits are merged into score_by_qn via max so body-vocabulary nodes
    # can enter the direct pool even when FTS5 misses them entirely (Mode B rescue at G1).
    # BM25 scores are scaled to match the FTS5 score range so they compete fairly in the
    # ramp normalization. Without scaling, FTS5 exact-name hits (score ~3.0) dominate the
    # ramp ceiling, compressing all BM25-body hits to h < 0.5.
    if use_bm25_body:
        try:
            bm25_idx = _get_bm25_index(store)
            if bm25_idx is not None:
                bm25_hits = bm25_idx.query(query, top_k=40)
                # Scale BM25 scores to FTS5 range: bm25_normalized is in [0,1],
                # re-scale to [0, fts_max] so top BM25 hits are on par with top FTS5 hits.
                # Scale BM25 body scores to 70% of FTS5 max score.
                # This lets body-only Mode B nodes compete with graph traversal
                # nodes while preserving FTS5 name/sig hits as the primary signal.
                # At 100%, BM25 over-dominates and hurts precision on clean queries.
                fts_max = max(score_by_qn.values()) if score_by_qn else 1.0
                bm25_scale = fts_max * 1.00  # bm25_norm is in [0, 1]
                for qn, bm25_norm in bm25_hits.items():
                    score_by_qn[qn] = max(score_by_qn.get(qn, 0.0), bm25_norm * bm25_scale)
        except Exception as exc:
            import logging
            logging.getLogger(__name__).warning("BM25-Body search failed: %s", exc)

    direct_qns: set[str] = set(score_by_qn.keys())

    # Fetch full GraphNode objects for direct hits — production functions only.
    # Test nodes inflate degree counts and dominate hybrid_score for keyword
    # queries that match test function names (e.g. "test_session_cookies").
    direct_nodes = store._batch_get_nodes(direct_qns)
    direct_nodes = [n for n in direct_nodes if n.kind == "Function" and not n.is_test]
    # G4-F: filter to routed files if file router is active
    if _file_filter is not None:
        direct_nodes = [n for n in direct_nodes if n.file_path in _file_filter]
        direct_qns = {n.qualified_name for n in direct_nodes}

    # --- Phase 2: callers_of expansion (G4-B: up to 2-hop with score decay) ---
    # Hop-1: direct callers of FTS5 hits inherit parent_hs * 0.5
    # Hop-2: callers of hop-1 nodes inherit hop1_hs * 0.25 (only if two_hop=True)
    # Score decay ensures hop-2 nodes rank below hop-1 and well below direct hits.
    caller_parent_score: dict[str, float] = {}  # caller_qn -> max inherited score

    def _expand_callers(source_nodes: list, parent_scores: dict[str, float], decay: float) -> set[str]:
        """Return qns of callers of source_nodes, updating caller_parent_score."""
        found: set[str] = set()
        for n in source_nodes:
            parent_hs = parent_scores.get(n.qualified_name, 0.0) * decay
            if parent_hs < 0.001:
                continue  # not worth expanding zero-score nodes
            for e in store.get_edges_by_target(n.qualified_name):
                if e.kind == "CALLS" and "::" in e.source_qualified:
                    qn = e.source_qualified
                    found.add(qn)
                    caller_parent_score[qn] = max(caller_parent_score.get(qn, 0.0), parent_hs)
            for e in store.search_edges_by_target_name(n.name, kind="CALLS"):
                if "::" in e.source_qualified:
                    qn = e.source_qualified
                    found.add(qn)
                    caller_parent_score[qn] = max(caller_parent_score.get(qn, 0.0), parent_hs)
        return found

    # Hop 1 — cap at 40 to leave room for semantic nodes
    hop1_qns = _expand_callers(direct_nodes, score_by_qn, decay=0.5) - direct_qns
    hop1_nodes = store._batch_get_nodes(hop1_qns)
    hop1_nodes = [n for n in hop1_nodes if n.kind in ("Function", "Test")]
    # Sort by inherited score so we keep the best hop-1 nodes if capped
    hop1_nodes.sort(key=lambda n: -caller_parent_score.get(n.qualified_name, 0.0))
    hop1_nodes = hop1_nodes[:40]

    # Hop 2 (optional) — cap tightly, only highest-score entries
    hop2_nodes: list = []
    if two_hop:
        hop1_scores = {n.qualified_name: caller_parent_score.get(n.qualified_name, 0.0)
                       for n in hop1_nodes}
        hop2_qns = _expand_callers(hop1_nodes, hop1_scores, decay=0.5) - direct_qns - hop1_qns
        hop2_nodes_raw = store._batch_get_nodes(hop2_qns)
        hop2_nodes = [n for n in hop2_nodes_raw if n.kind in ("Function", "Test")]
        hop2_nodes.sort(key=lambda n: -caller_parent_score.get(n.qualified_name, 0.0))
        hop2_nodes = hop2_nodes[:20]  # strict cap — hop-2 is speculative

    caller_nodes = hop1_nodes + hop2_nodes

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
                caller_qns_so_far = {n.qualified_name for n in caller_nodes}
                sem_qns = set(sem_hits.keys()) - direct_qns - caller_qns_so_far
                sem_nodes = store._batch_get_nodes(sem_qns)
                sem_nodes = [n for n in sem_nodes if n.kind == "Function" and not n.is_test]
                # Inject as additional direct candidates (they got here via semantics, not FTS)
                direct_nodes = direct_nodes + sem_nodes
                direct_qns |= {n.qualified_name for n in sem_nodes}
        except Exception as exc:
            import logging
            logging.getLogger(__name__).warning("G3 semantic scoring failed: %s", exc)

    # --- Phase 2c: G4-E co-change expansion ---
    # Expand candidate pool with functions that historically co-change with FTS5 hits.
    # Helps find structurally related functions that share no call edge.
    if use_cochange:
        try:
            from .cochange import get_cochange_index
            cc_idx = get_cochange_index(repo_root, store.db_path)
            if cc_idx is not None:
                hit_names = [qn.split("::")[-1] for qn in direct_qns]
                cc_partners = cc_idx.expand(hit_names, top_k=10)
                cc_partner_qns: set[str] = set()
                for partner in cc_partners:
                    # Find nodes matching this name in the store
                    for h in hybrid_search(store, partner, limit=5):
                        pqn = h["qualified_name"]
                        if pqn not in direct_qns and pqn not in {n.qualified_name for n in caller_nodes}:
                            cc_partner_qns.add(pqn)
                            # Score: low but non-zero so they enter the pool
                            score_by_qn[pqn] = max(score_by_qn.get(pqn, 0.0), 0.05)
                cc_nodes = store._batch_get_nodes(cc_partner_qns)
                cc_nodes = [n for n in cc_nodes if n.kind == "Function" and not n.is_test]
                direct_nodes = direct_nodes + cc_nodes
                direct_qns |= {n.qualified_name for n in cc_nodes}
        except Exception as exc:
            import logging
            logging.getLogger(__name__).warning("Co-change expansion failed: %s", exc)

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

    # --- Phase 4: G4-D cross-encoder re-ranking (optional, expensive) ---
    # Re-ranks top-20 candidates using Claude to jointly score (query, function).
    # Only use when latency/cost is acceptable — ~1-3K tokens per query.
    if use_reranker and scored:
        try:
            from .reranker import rerank
            # Sort by current score before re-ranking so top-K is meaningful
            scored.sort(key=lambda n: -n.hybrid_score)
            scored = rerank(query, scored)
        except Exception as exc:
            import logging
            logging.getLogger(__name__).warning("Reranker failed: %s", exc)

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
