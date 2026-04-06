"""resolver.py — TACM Resolver with four scoring strategies for benchmarking.

Strategy A: Structural     — degree + blast_radius + test (original brief spec)
Strategy B: ValDensity     — structural score / sqrt(token_cost)
Strategy C: DegreeOnly     — pure connectivity, no other signals
Strategy D: Strct+Trunc    — structural + truncate oversized nodes to fit budget
Strategy E: HybridFull     — structural + crg hybrid_score (FTS5 BM25 relevance)
                             This is the primary strategy: graph signals + query relevance.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


Strategy = Literal["structural", "value_density", "degree_only", "structural_truncated", "hybrid_full"]

TRUNCATION_LINE_THRESHOLD = 40
TRUNCATION_TOKEN_CAP = 120


@dataclass
class ScoredNode:
    node_id: str
    name: str
    file_path: str
    source_text: str
    token_cost: int
    degree: int
    in_blast_radius: bool
    has_test: bool
    is_test: bool = False
    line_start: int = 0
    line_end: int = 0
    hybrid_score: float = 0.0   # FTS5 BM25+RRF score from crg hybrid_search
    score: float = 0.0
    value: float = 0.0


# ---------------------------------------------------------------------------
# Scoring functions
# ---------------------------------------------------------------------------

def _score_structural(node: ScoredNode) -> float:
    """Strategy A: G1 structural signals only. Weights sum to 1.0."""
    return (
        0.4 * min(node.degree / 10, 1.0)
        + 0.4 * float(node.in_blast_radius)
        + 0.2 * float(node.has_test)
    )


def _score_value_density(node: ScoredNode) -> float:
    """Strategy B: structural score normalised by sqrt(token_cost)."""
    return _score_structural(node) / max(node.token_cost ** 0.5, 1.0)


def _score_degree_only(node: ScoredNode) -> float:
    """Strategy C: pure degree (connectivity), no other signals."""
    return min(node.degree / 10, 1.0)


def _score_structural_truncated(node: ScoredNode) -> float:
    """Strategy D: structural (truncation applied in resolve(), score same as A)."""
    return _score_structural(node)


def _score_hybrid_full(node: ScoredNode) -> float:
    """Strategy E: hybrid_search relevance + structural signals.

    Key design decisions vs original:

    1. hybrid_score normalised as RANK signal not absolute value.
       RRF scores cluster 0.014–0.025 — dividing by 0.02 gives 0.7–1.0 for
       everything, making it useless as a discriminator. Instead treat it as
       a relative rank: nodes above 0.018 (top ~30%) get full credit,
       below 0.010 (noise) get zero. Linear ramp between.

    2. Degree computed on production edges only (non-test callers).
       Test functions have high degree within test infrastructure. We want
       degree = how many *production* functions call or depend on this node.
       Proxy: use degree but cap at 15 (most production fns have 2-15 edges).

    3. blast_radius only for TOP search hits, not all hits.
       All direct search hits get in_blast_radius=True in the adapter, but
       with multi-keyword search this means 40+ nodes. Reserve the bonus for
       nodes with hybrid_score above the median of the candidate pool.
       This is approximated here by requiring hs > 0.016.

    Weights (sum to 1.0):
      w_hybrid  = 0.55  — primary signal: query relevance
      w_degree  = 0.25  — structural: production connectivity
      w_test    = 0.10  — test coverage (positive signal for functions WITH tests)
      w_blast   = 0.10  — blast radius (narrow: only strong search hits)
    """
    # Hybrid score: linear ramp [0.010, 0.018] → [0.0, 1.0]
    hs = node.hybrid_score
    h = max(0.0, min(1.0, (hs - 0.010) / (0.018 - 0.010)))

    # Degree: cap at 15 for production functions (tests inflate this)
    d = min(node.degree / 15, 1.0) if not node.is_test else 0.0

    # Blast radius: only reward strong search hits
    blast = float(node.in_blast_radius and hs >= 0.016)

    return (
        0.55 * h
        + 0.25 * d
        + 0.10 * float(node.has_test)
        + 0.10 * blast
    )


_SCORERS = {
    "structural":           _score_structural,
    "value_density":        _score_value_density,
    "degree_only":          _score_degree_only,
    "structural_truncated": _score_structural_truncated,
    "hybrid_full":          _score_hybrid_full,
}


# ---------------------------------------------------------------------------
# Resolver
# ---------------------------------------------------------------------------

def resolve(
    nodes: list[ScoredNode],
    token_budget: int,
    strategy: Strategy = "hybrid_full",
    exclude_tests: bool = True,
    use_knapsack: bool = True,
) -> list[ScoredNode]:
    """Score nodes then select the highest-total-score set within token_budget.

    use_knapsack=True (default): 0/1 knapsack DP — finds the provably optimal
    subset. At n<=200 nodes and budget<=8000 tokens, the DP table is trivially
    fast (<5ms). Greedy value/cost ranking is wrong for retrieval: it buries
    high-score expensive nodes (e.g. prepare_url at 666 tokens) behind cheap
    low-relevance noise.

    use_knapsack=False: greedy value/cost fill (original behaviour, kept for
    comparison in benchmarks).
    """
    scorer = _SCORERS[strategy]
    candidates = [n for n in nodes if not (exclude_tests and n.is_test)]

    for node in candidates:
        node.score = scorer(node)
        cost = _effective_cost(node, strategy)
        node.value = node.score / max(cost, 1)  # kept for reference / greedy path

    if use_knapsack:
        return _knapsack(candidates, token_budget, strategy)
    else:
        return _greedy(candidates, token_budget, strategy)


def _greedy(candidates: list[ScoredNode], budget: int, strategy: Strategy) -> list[ScoredNode]:
    # Rank by score (relevance), not value/cost (packing efficiency).
    # Value-density ranking deprioritises high-score expensive nodes in favour
    # of cheap low-noise nodes — correct for portfolio packing, wrong for
    # retrieval where the GT is one specific function.
    ranked = sorted(candidates, key=lambda n: n.score, reverse=True)
    selected: list[ScoredNode] = []
    remaining = budget
    for node in ranked:
        cost = _effective_cost(node, strategy)
        if cost <= remaining:
            selected.append(node)
            remaining -= cost
    return selected


def _knapsack(candidates: list[ScoredNode], budget: int, strategy: Strategy) -> list[ScoredNode]:
    """0/1 knapsack DP. Returns the subset maximising total score within budget.

    Scores are scaled to integers (×1000) for the DP table.
    Items whose cost exceeds the budget are excluded upfront.
    """
    items = [(n, _effective_cost(n, strategy)) for n in candidates if _effective_cost(n, strategy) <= budget]
    if not items:
        return []

    n = len(items)
    # Scale scores to integers (DP requires integer values)
    int_scores = [round(node.score * 1000) for node, _ in items]
    costs = [cost for _, cost in items]

    # dp[i][w] = max total int_score using first i items with weight <= w
    # Use 1-D rolling array to save memory
    dp = [0] * (budget + 1)
    for i in range(n):
        w_i = costs[i]
        v_i = int_scores[i]
        for w in range(budget, w_i - 1, -1):
            dp[w] = max(dp[w], dp[w - w_i] + v_i)

    # Backtrack to find which items were selected
    selected_nodes: list[ScoredNode] = []
    w = budget
    for i in range(n - 1, -1, -1):
        w_i = costs[i]
        v_i = int_scores[i]
        if w >= w_i and dp[w] == dp[w - w_i] + v_i:
            selected_nodes.append(items[i][0])
            w -= w_i

    # Return in score-descending order
    selected_nodes.sort(key=lambda n: n.score, reverse=True)
    return selected_nodes


def _effective_cost(node: ScoredNode, strategy: Strategy) -> int:
    if strategy == "structural_truncated":
        line_count = node.line_end - node.line_start + 1 if node.line_end > node.line_start else 0
        if line_count > TRUNCATION_LINE_THRESHOLD:
            return TRUNCATION_TOKEN_CAP
    return node.token_cost
