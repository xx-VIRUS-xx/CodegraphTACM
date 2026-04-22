"""cache.py — Per-graph memoisation of query-independent signals.

Two signals do **not** depend on the query:

  * PageRank over the FUNCTION-layer CALLS subgraph
  * (name, file_path) counts used by the fan_in discount

Before this module, both were recomputed on every call to
:class:`NodeScorer`. PageRank alone was 50 power-iterations over every
FUNCTION node on every query — dominated scorer runtime in benchmarks.

We key the cache on ``id(graph)`` (not the object itself — ``LayeredGraph``
is not hashable). :func:`clear_cache` is exposed for test teardown.

This module also exposes :func:`personalized_pagerank` — a query-dependent
PPR that re-uses the cached adjacency (``PPRGraphIndex``). Teleport
probability mass is placed on BM25 seed nodes instead of uniformly across
all nodes, so PPR scores become a query-aware structural relevance signal.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..graph.model import LayeredGraph, LNode

from .config import DEFAULT_CONFIG, SelectorConfig


@dataclass
class PPRGraphIndex:
    """Precomputed CALLS adjacency over non-test FUNCTION nodes.

    Built once per graph and reused by every PPR query. Holds only the
    shape of the call graph — no query state — so it is safe to cache.
    """
    node_ids:  list[str]                                   # stable node order
    index_of:  dict[str, int]                              # node_id -> index
    out_links: list[list[int]]                             # idx -> list of target idx
    in_links:  list[list[tuple[int, float]]]               # idx -> [(src_idx, weight)]
    out_weight_sum: list[float]                            # sum of outgoing weights per idx


@dataclass
class ScorerCache:
    """Per-graph cache of query-independent signals."""
    pagerank:    dict[str, float]                 # node_id -> pagerank in [0, 1]
    name_counts: dict[tuple[str, str | None], int]
    ppr_index:   PPRGraphIndex


# Module-level store. Keyed by (id(graph), config) — ``SelectorConfig`` is
# frozen so it is hashable. Cleared explicitly by tests.
_caches: dict[tuple[int, SelectorConfig], ScorerCache] = {}


def get_scorer_cache(
    graph: "LayeredGraph",
    config: SelectorConfig = DEFAULT_CONFIG,
) -> ScorerCache:
    """Return the cached :class:`ScorerCache`, building it if absent.

    Keyed on ``(id(graph), config)``. Callers that mutate the graph after
    first use must call :func:`clear_cache` or :func:`invalidate` to avoid
    stale signals. Different configs (e.g. different ``pagerank_alpha``)
    get their own cache slot.
    """
    key = (id(graph), config)
    cached = _caches.get(key)
    if cached is not None:
        return cached

    cached = _build_cache(graph, config)
    _caches[key] = cached
    return cached


def invalidate(graph: "LayeredGraph") -> None:
    """Drop all cached entries for a single graph (across all configs)."""
    gid = id(graph)
    stale = [k for k in _caches if k[0] == gid]
    for k in stale:
        _caches.pop(k, None)


def clear_cache() -> None:
    """Drop all cached signals. Use in test teardown."""
    _caches.clear()


# ---------------------------------------------------------------------------
# Builders
# ---------------------------------------------------------------------------

def _build_cache(
    graph: "LayeredGraph",
    config: SelectorConfig,
) -> ScorerCache:
    name_counts: dict[tuple[str, str | None], int] = Counter(
        (n.name, n.file_path) for n in graph.nodes.values()
        if n.layer.name == "FUNCTION"
    )
    pagerank = _compute_pagerank_full(graph, config)
    ppr_index = _build_ppr_index(graph)
    return ScorerCache(
        pagerank=pagerank,
        name_counts=name_counts,
        ppr_index=ppr_index,
    )


def _build_ppr_index(graph: "LayeredGraph") -> PPRGraphIndex:
    """Build the index-based adjacency used by PPR power iteration.

    Switching from dict-of-ids to list-of-ints is worth roughly an order of
    magnitude in inner-loop speed — PPR runs per query, so this matters.
    The index only covers non-test FUNCTION nodes, matching the default
    selector path.
    """
    from ..graph.model import EdgeKind  # local import to avoid cycles

    fn_nodes = [
        n for n in graph.nodes.values()
        if n.layer.name == "FUNCTION" and not n.is_test
    ]
    node_ids = [n.node_id for n in fn_nodes]
    index_of = {nid: i for i, nid in enumerate(node_ids)}

    out_links: list[list[int]] = [[] for _ in node_ids]
    in_links:  list[list[tuple[int, float]]] = [[] for _ in node_ids]
    out_weight_sum: list[float] = [0.0 for _ in node_ids]

    for i, nid in enumerate(node_ids):
        for e in graph.out_adj.get(nid, []):
            if e.kind != EdgeKind.CALLS:
                continue
            j = index_of.get(e.target_id)
            if j is None:
                continue
            out_links[i].append(j)
            in_links[j].append((i, e.weight))
            out_weight_sum[i] += e.weight

    return PPRGraphIndex(
        node_ids=node_ids,
        index_of=index_of,
        out_links=out_links,
        in_links=in_links,
        out_weight_sum=out_weight_sum,
    )


def personalized_pagerank(
    index: PPRGraphIndex,
    seed_weights: dict[str, float],
    alpha: float = 0.85,
    max_iter: int = 20,
    tol: float = 1e-4,
) -> dict[str, float]:
    """Personalized PageRank with a query-dependent teleport vector.

    Standard PageRank teleports uniformly to ``1/N`` on every step. PPR
    teleports to a query-specific distribution over **seed nodes** —
    typically the top-K BM25 hits. Random walks therefore preferentially
    explore the call-graph neighborhood of those seeds, surfacing
    structurally important functions that are one or two hops away from
    the lexical match.

    Args:
        index:        Precomputed :class:`PPRGraphIndex` over the CALLS graph.
        seed_weights: ``{node_id: weight}`` — teleport mass for each seed.
                      Weights are auto-normalised to sum to 1. Seeds not in
                      the index are silently dropped.
        alpha:        Damping factor. Higher → longer random walks.
        max_iter:     Power-iteration cap.
        tol:          L1 early-stop threshold on rank delta.

    Returns:
        ``{node_id: score}`` over every node in the index, normalised to
        ``[0, 1]``. Nodes not in the index do not appear in the result.
    """
    N = len(index.node_ids)
    if N == 0:
        return {}

    # Build teleport vector from seeds, falling back to uniform if nothing
    # matched — this keeps the algorithm well-defined for queries with no
    # seed support (PPR then behaves like vanilla PageRank).
    teleport = [0.0] * N
    total = 0.0
    for nid, w in seed_weights.items():
        if w <= 0:
            continue
        idx = index.index_of.get(nid)
        if idx is None:
            continue
        teleport[idx] += w
        total += w

    if total > 0:
        inv = 1.0 / total
        teleport = [t * inv for t in teleport]
    else:
        uniform = 1.0 / N
        teleport = [uniform] * N

    rank = list(teleport)  # initialise from teleport — converges faster than uniform
    out_links = index.out_links
    in_links = index.in_links
    out_weight_sum = index.out_weight_sum

    for _ in range(max_iter):
        dangling_sum = 0.0
        for i in range(N):
            if not out_links[i]:
                dangling_sum += rank[i]

        new_rank = [0.0] * N
        dangling_share = alpha * dangling_sum
        for i in range(N):
            incoming = 0.0
            for src, w in in_links[i]:
                ws = out_weight_sum[src]
                if ws > 0:
                    incoming += rank[src] * (w / ws)
            # (1 - alpha) * teleport[i] is the PPR "reset" mass — this is
            # what makes PPR query-dependent. Dangling nodes redistribute
            # their rank via the teleport vector as well (standard PPR).
            new_rank[i] = (
                (1 - alpha) * teleport[i]
                + alpha * incoming
                + dangling_share * teleport[i]
            )

        delta = 0.0
        for i in range(N):
            delta += abs(new_rank[i] - rank[i])
        rank = new_rank
        if delta < tol:
            break

    max_val = max(rank) if rank else 1.0
    if max_val > 0:
        inv = 1.0 / max_val
        return {index.node_ids[i]: rank[i] * inv for i in range(N)}
    return {index.node_ids[i]: rank[i] for i in range(N)}


def _compute_pagerank_full(
    graph: "LayeredGraph",
    config: SelectorConfig,
) -> dict[str, float]:
    """PageRank over the non-test FUNCTION-layer CALLS subgraph.

    The historical scorer computed PageRank after excluding test nodes
    (they come in via the ``exclude_tests=True`` path in the selectors).
    We bake that exclusion into the cache so switching from per-query to
    cached PageRank is a no-op for the default code path.

    Early-stops when the L1 delta falls below ``config.pagerank_tol``.
    """
    from ..graph.model import EdgeKind  # local import to avoid cycles

    fn_nodes = [
        n for n in graph.nodes.values()
        if n.layer.name == "FUNCTION" and not n.is_test
    ]
    node_ids = {n.node_id for n in fn_nodes}
    if not fn_nodes:
        return {}

    out_links: dict[str, list[str]] = {}
    in_links: dict[str, list[tuple[str, float]]] = {n.node_id: [] for n in fn_nodes}

    for node in fn_nodes:
        targets = [
            (e.target_id, e.weight)
            for e in graph.out_adj.get(node.node_id, [])
            if e.kind == EdgeKind.CALLS and e.target_id in node_ids
        ]
        out_links[node.node_id] = [t for t, _ in targets]
        for t, w in targets:
            in_links[t].append((node.node_id, w))

    N = len(fn_nodes)
    rank = {n.node_id: 1.0 / N for n in fn_nodes}

    alpha = config.pagerank_alpha
    tol = config.pagerank_tol
    for _ in range(config.pagerank_max_iter):
        new_rank: dict[str, float] = {}
        dangling_sum = sum(
            rank[nid] for nid in node_ids if not out_links.get(nid)
        )
        for node in fn_nodes:
            nid = node.node_id
            incoming = sum(
                rank[src] * w / max(1, len(out_links.get(src, [])))
                for src, w in in_links.get(nid, [])
            )
            new_rank[nid] = (
                (1 - alpha) / N + alpha * (incoming + dangling_sum / N)
            )
        # L1 delta for early stopping
        delta = sum(abs(new_rank[k] - rank[k]) for k in rank)
        rank = new_rank
        if delta < tol:
            break

    max_val = max(rank.values()) if rank else 1.0
    if max_val > 0:
        return {k: v / max_val for k, v in rank.items()}
    return rank
