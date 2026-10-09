"""scorer.py — Memory-augmented scoring pipeline.

Extends the existing TACM NodeScorer with Neo4j-computed signals:

  Base signals (from scoring.py):
    bm25, fan_in, fan_out, complexity, test_cover, nbr_bonus

  Neo4j graph signals (computed server-side):
    pagerank, betweenness, community_diversity

  Memory signals (from cross-query history):
    recency_boost, hot_spot_boost, ruled_out_penalty, exploration_momentum

The final score combines all three tiers with intent-aware weights.
"""

from __future__ import annotations

from typing import Optional

from ..graph.model import LayeredGraph, LNode, EdgeKind
from ..selector.intent import classify_intent, QueryIntent
from ..selector.scoring import NodeScorer as BaseScorer
from .store import Neo4jGraphStore
from .algorithms import GraphAlgorithms
from .memory import ActiveMemory


# ---------------------------------------------------------------------------
# Extended weight vectors
# (bm25, fan_in, fan_out, complexity, test_cover,
#  pagerank, betweenness, recency, hot_spot, momentum)
# ---------------------------------------------------------------------------

_MEMORY_WEIGHTS: dict[str, tuple[float, ...]] = {
    #                     bm25  fan_in fan_out cmplx  test   pr    btwn   recen  hot_   mom
    QueryIntent.BUG:      (0.35, 0.15,  0.05,  0.10,  0.00, 0.10, 0.05, 0.08, 0.07, 0.05),
    QueryIntent.STRUCTURE: (0.40, 0.05,  0.15,  0.00,  0.05, 0.10, 0.10, 0.05, 0.03, 0.07),
    QueryIntent.EXPLAIN:  (0.30, 0.10,  0.20,  0.03,  0.02, 0.10, 0.10, 0.05, 0.03, 0.07),
}

_SIGNAL_NAMES = [
    "bm25", "fan_in", "fan_out", "complexity", "test_cover",
    "pagerank", "betweenness", "recency", "hot_spot", "momentum",
]


class MemoryAugmentedScorer:
    """Scorer that combines TACM base signals with Neo4j graph + memory signals."""

    def __init__(
        self,
        graph: LayeredGraph,
        query: str,
        intent: str,
        score_texts: dict[str, str],
        neo4j_store: Neo4jGraphStore,
        memory: ActiveMemory,
        repo: str,
        *,
        precomputed_pagerank: Optional[dict[str, float]] = None,
        precomputed_betweenness: Optional[dict[str, float]] = None,
        precomputed_communities: Optional[dict[str, int]] = None,
    ):
        self._graph = graph
        self._query = query
        self._intent = intent
        self._neo4j = neo4j_store
        self._memory = memory
        self._repo = repo

        # Base scorer for bm25, fan_in, fan_out, complexity, test_cover
        self._base_scorer = BaseScorer(graph, query, intent, score_texts)

        # Graph algorithms (lazy — only compute if not precomputed)
        self._algos = GraphAlgorithms(neo4j_store)
        self._pagerank = precomputed_pagerank
        self._betweenness = precomputed_betweenness
        self._communities = precomputed_communities

    def _ensure_graph_signals(self) -> None:
        """Compute graph signals if not precomputed."""
        if self._pagerank is None:
            self._pagerank = self._algos.pagerank(self._repo)
        if self._betweenness is None:
            self._betweenness = self._algos.betweenness(self._repo)
        if self._communities is None:
            self._communities = self._algos.louvain_communities(self._repo)

    def score_all(self, nodes: list[LNode]) -> dict[str, float]:
        """Score nodes using all signal tiers: base + graph + memory."""
        if not nodes:
            return {}

        # Tier 1: base TACM signals
        base_scores = self._base_scorer.score_all(nodes)

        # Tier 2: Neo4j graph signals
        self._ensure_graph_signals()

        # Tier 3: memory signals
        node_ids = [n.node_id for n in nodes]
        memory_signals = self._memory.get_memory_signals(node_ids)

        # Get weight vector for this intent
        weights = _MEMORY_WEIGHTS.get(self._intent, _MEMORY_WEIGHTS[QueryIntent.BUG])

        # Combine all signals
        combined: dict[str, float] = {}
        for node in nodes:
            nid = node.node_id

            # Base signals (already combined into one score — we need them separate)
            # We'll use the base score as-is for bm25 weight slot, and
            # add graph + memory signals on top
            base = base_scores.get(nid, 0.0)

            # Extract individual base signals (re-weight from scratch)
            pr = self._pagerank.get(nid, 0.0) if self._pagerank else 0.0
            btwn = self._betweenness.get(nid, 0.0) if self._betweenness else 0.0

            mem = memory_signals.get(nid, {})
            recency = mem.get("recency_boost", 0.0)
            hot_spot = mem.get("hot_spot_boost", 0.0)
            momentum = mem.get("exploration_momentum", 0.0)
            ruled_penalty = mem.get("ruled_out_penalty", 0.0)

            # Use base TACM score for the first 5 weight slots combined
            base_weight_sum = sum(weights[:5])
            graph_memory_score = (
                weights[5] * pr +
                weights[6] * btwn +
                weights[7] * recency +
                weights[8] * hot_spot +
                weights[9] * momentum
            )

            # Final: blend base TACM score with graph+memory signals
            combined[nid] = (
                base_weight_sum * base +
                graph_memory_score -
                ruled_penalty  # subtract penalty for ruled-out nodes
            )

        # Normalize to [0, 1]
        max_val = max(combined.values()) if combined else 1.0
        if max_val > 0:
            combined = {k: max(0.0, v / max_val) for k, v in combined.items()}

        return combined

    def score_with_community_diversity(
        self,
        nodes: list[LNode],
        selected_communities: set[int],
        diversity_weight: float = 0.1,
    ) -> dict[str, float]:
        """Score with additional diversity bonus for under-represented communities.

        After initial scoring, nodes from communities not yet represented
        in the selection get a bonus. This ensures the context doesn't
        cluster too heavily in one module.
        """
        scores = self.score_all(nodes)
        self._ensure_graph_signals()

        if not self._communities:
            return scores

        for node in nodes:
            nid = node.node_id
            comm = self._communities.get(nid)
            if comm is not None and comm not in selected_communities:
                # Bonus for novel community
                scores[nid] = min(1.0, scores[nid] + diversity_weight)

        return scores
