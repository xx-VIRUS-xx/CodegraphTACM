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


def _score_hybrid_full(node: ScoredNode, hs_lo: float = 0.010, hs_hi: float = 0.018) -> float:
    """Strategy E: hybrid_search relevance + structural signals.

    Key design decisions vs original:

    1. hybrid_score normalised as RANK signal not absolute value.
       Scores are linearly ramped from hs_lo (noise floor) to hs_hi (full credit).
       These bounds are computed per-query from the actual score distribution
       (see resolve() which passes hs_lo/hs_hi via partial application).
       Default fallback: [0.010, 0.018] for RRF-style scores.

    2. Degree computed on production edges only (non-test callers).
       Test functions have high degree within test infrastructure. We want
       degree = how many *production* functions call or depend on this node.
       Proxy: use degree but cap at 15 (most production fns have 2-15 edges).

    3. blast_radius only for TOP search hits, not all hits.
       All direct search hits get in_blast_radius=True in the adapter, but
       with multi-keyword search this means 40+ nodes. Reserve the bonus for
       nodes with hybrid_score above the top-30% of the candidate pool.
       This is approximated here by requiring hs >= hs_hi * 0.7.

    Weights (sum to 1.0):
      w_hybrid  = 0.55  — primary signal: query relevance
      w_degree  = 0.25  — structural: production connectivity
      w_test    = 0.10  — test coverage (positive signal for functions WITH tests)
      w_blast   = 0.10  — blast radius (narrow: only strong search hits)
    """
    hs = node.hybrid_score
    ramp_range = max(hs_hi - hs_lo, 1e-6)
    h = max(0.0, min(1.0, (hs - hs_lo) / ramp_range))

    # Degree: cap at 15 for production functions (tests inflate this)
    d = min(node.degree / 15, 1.0) if not node.is_test else 0.0

    # Blast radius: only reward strong search hits (top ~30% by score)
    blast_threshold = max(hs_lo, hs_hi * 0.7)
    blast = float(node.in_blast_radius and hs >= blast_threshold)

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
    "hybrid_full":          _score_hybrid_full,  # hs_lo/hs_hi computed per-call in resolve()
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
    candidates = [n for n in nodes if not (exclude_tests and n.is_test)]

    # For hybrid_full, compute per-call ramp bounds from actual score distribution.
    # hybrid_score values vary widely across codebases (0.002–3.0 depending on FTS5
    # hit density). A fixed ramp saturates the signal for high-scoring corpora.
    # Strategy: use min as noise floor, max as full-credit threshold, with a floor
    # guard so zero-score nodes (semantic-only expansions) always get h=0.
    if strategy == "hybrid_full" and candidates:
        hs_nonzero = sorted([n.hybrid_score for n in candidates if n.hybrid_score > 0])
        if len(hs_nonzero) >= 4:
            hs_lo = hs_nonzero[0]  # minimum nonzero score = noise floor
            hs_hi = hs_nonzero[-1]  # maximum score = full credit
            # Guard: avoid degenerate ramp when all scores are equal
            if hs_hi <= hs_lo:
                hs_hi = hs_lo * 2.0
        else:
            hs_lo, hs_hi = 0.010, 0.018
        import functools
        scorer = functools.partial(_score_hybrid_full, hs_lo=hs_lo, hs_hi=hs_hi)
    else:
        scorer = _SCORERS[strategy]

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

    Uses full 2D DP table for correct backtracking. At n<=200 items and
    budget<=32000, the table is <=6.4M cells — trivially fast (<50ms).
    The 1D rolling-array approach cannot backtrack correctly when multiple
    items share the same (cost, value), producing wrong selections.
    """
    items = [(n, _effective_cost(n, strategy)) for n in candidates if _effective_cost(n, strategy) <= budget]
    if not items:
        return []

    n = len(items)
    int_scores = [round(node.score * 1000) for node, _ in items]
    costs = [cost for _, cost in items]

    # Full 2D table: dp[i][w] = max score using items 0..i-1 with capacity w
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        w_i = costs[i - 1]
        v_i = int_scores[i - 1]
        for w in range(budget + 1):
            dp[i][w] = dp[i - 1][w]
            if w >= w_i:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - w_i] + v_i)

    # Backtrack
    selected_nodes: list[ScoredNode] = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_nodes.append(items[i - 1][0])
            w -= costs[i - 1]

    selected_nodes.sort(key=lambda n: n.score, reverse=True)
    return selected_nodes


def _effective_cost(node: ScoredNode, strategy: Strategy) -> int:
    if strategy == "structural_truncated":
        line_count = node.line_end - node.line_start + 1 if node.line_end > node.line_start else 0
        if line_count > TRUNCATION_LINE_THRESHOLD:
            return TRUNCATION_TOKEN_CAP
    return node.token_cost
