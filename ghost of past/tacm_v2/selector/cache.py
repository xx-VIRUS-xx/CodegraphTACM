"""cache.py — Per-graph memoisation of query-independent signals.

Two signals do **not** depend on the query:

  * PageRank over the FUNCTION-layer CALLS subgraph
  * (name, file_path) counts used by the fan_in discount

Before this module, both were recomputed on every call to
:class:`NodeScorer`. PageRank alone was 50 power-iterations over every
FUNCTION node on every query — dominated scorer runtime in benchmarks.

We key the cache on ``id(graph)`` (not the object itself — ``LayeredGraph``
is not hashable). :func:`clear_cache` is exposed for test teardown.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..graph.model import LayeredGraph, LNode

from .config import DEFAULT_CONFIG, SelectorConfig


@dataclass
class ScorerCache:
    """Per-graph cache of query-independent signals."""
    pagerank:    dict[str, float]                 # node_id -> pagerank in [0, 1]
    name_counts: dict[tuple[str, str | None], int]


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
    return ScorerCache(pagerank=pagerank, name_counts=name_counts)


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
