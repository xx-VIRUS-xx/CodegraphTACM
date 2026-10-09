"""intent.py — Query intent classification and per-intent weight vectors.

Shared by selector.py and scoring.py to avoid circular imports.

Public surface:
  * :class:`QueryIntent`       — string constants for each intent label
  * :func:`classify_intent`    — legacy entry point, returns a label string
  * :func:`classify_intent_with_confidence` — returns (label, confidence, scores)
  * :func:`blended_weights`    — weight vector that interpolates the top 2
                                 intents when the classifier is not confident
  * ``INTENT_WEIGHTS``, ``LAYER_BUDGETS`` — per-intent constants
"""

from __future__ import annotations
import re


class QueryIntent:
    STRUCTURE = "structure"
    BUG       = "bug"
    EXPLAIN   = "explain"


_STRUCTURE_KEYWORDS = {
    "structure", "architecture", "overview", "organized", "organisation",
    "layout", "design", "module", "package", "depend", "dependency",
    "import", "hierarchy", "relationship", "connected", "uses",
    "structured", "map", "diagram",
}
_STRUCTURE_PHRASES = [
    "how is", "how are", "structured", "laid out", "organized",
    "what is the structure", "give me an overview", "show the structure",
]

_BUG_KEYWORDS = {
    "bug", "error", "fail", "failing", "broken", "crash", "exception",
    "wrong", "incorrect", "issue", "problem", "why", "raises",
    "traceback", "fix", "regression", "not", "doesn",
}
_BUG_PHRASES = ["not working", "not sent", "not get", "doesn't work", "fails when"]

_EXPLAIN_KEYWORDS = {
    "explain", "describe", "understand", "walk",
}
_EXPLAIN_PHRASES = [
    "what does", "how does", "what is", "show me", "tell me",
    "how do", "explain how", "explain what",
]

# Phrases that neutralise BUG signal — "no error", "without bug", etc.
# A hit here subtracts from bug_hits before the winner is picked.
_BUG_NEGATION_PHRASES = [
    "no error", "no bug", "no exception", "without error", "without bug",
    "not a bug", "not an error", "no crash", "no failure",
]


def _raw_scores(query: str) -> dict[str, int]:
    """Shared keyword + phrase counting used by both classifier entry points."""
    q = query.lower()
    tokens = set(re.findall(r"[a-z]+", q))

    bug_hits       = len(tokens & _BUG_KEYWORDS)
    structure_hits = len(tokens & _STRUCTURE_KEYWORDS)
    explain_hits   = len(tokens & _EXPLAIN_KEYWORDS)

    for phrase in _STRUCTURE_PHRASES:
        if phrase in q:
            structure_hits += 2
    for phrase in _BUG_PHRASES:
        if phrase in q:
            bug_hits += 2
    for phrase in _EXPLAIN_PHRASES:
        if phrase in q:
            explain_hits += 2

    # Negation cancels noisy BUG hits ("no error", "without failure").
    # Bounded at 0 so we never produce a negative score.
    for phrase in _BUG_NEGATION_PHRASES:
        if phrase in q:
            bug_hits = max(0, bug_hits - 2)

    return {
        QueryIntent.BUG:       bug_hits,
        QueryIntent.STRUCTURE: structure_hits,
        QueryIntent.EXPLAIN:   explain_hits,
    }


def classify_intent(query: str) -> str:
    """Return the best-matching intent label (legacy entry point).

    When no keyword fires at all, falls back to :data:`QueryIntent.BUG` —
    this preserves the behaviour the regression tests depend on.
    """
    scores = _raw_scores(query)
    best = max(scores, key=lambda k: scores[k])
    return best if scores[best] > 0 else QueryIntent.BUG


def classify_intent_with_confidence(
    query: str,
) -> tuple[str, float, dict[str, int]]:
    """Return ``(label, confidence, raw_scores)``.

    ``confidence`` is the margin between the top and second-top intent,
    normalised by the total score, in ``[0, 1]``:

      * 1.0  → the winning intent dominates (all hits are its own)
      * 0.0  → top two are tied, or no hits fired at all
    """
    scores = _raw_scores(query)
    ranked = sorted(scores.items(), key=lambda kv: -kv[1])
    top_label, top_score = ranked[0]
    second_score = ranked[1][1] if len(ranked) > 1 else 0

    if top_score <= 0:
        return QueryIntent.BUG, 0.0, scores

    total = sum(v for _, v in ranked) or 1
    confidence = (top_score - second_score) / total
    return top_label, confidence, scores


# Weight vectors per intent: (bm25, fan_in, fan_out, complexity, test_cover)
INTENT_WEIGHTS: dict[str, tuple[float, float, float, float, float]] = {
    QueryIntent.BUG:       (0.50, 0.25, 0.10, 0.15, 0.00),
    QueryIntent.STRUCTURE: (0.60, 0.10, 0.20, 0.00, 0.10),
    QueryIntent.EXPLAIN:   (0.45, 0.15, 0.30, 0.05, 0.05),
}

# Layer budget fractions per intent: (file_frac, class_frac, function_frac)
LAYER_BUDGETS: dict[str, tuple[float, float, float]] = {
    QueryIntent.STRUCTURE: (0.30, 0.50, 0.20),
    QueryIntent.BUG:       (0.05, 0.20, 0.75),
    QueryIntent.EXPLAIN:   (0.10, 0.35, 0.55),
}


def blended_weights(
    query: str,
    confidence_threshold: float = 0.30,
) -> tuple[str, tuple[float, float, float, float, float]]:
    """Return ``(primary_intent, weights)`` with optional top-2 blending.

    When the classifier's confidence is below ``confidence_threshold``,
    the weights for the top and second intents are linearly mixed, with
    the primary intent keeping the larger share. When confidence is high,
    returns the crisp :data:`INTENT_WEIGHTS` entry unchanged.

    Callers who do not want blending should continue to use
    :func:`classify_intent` and index :data:`INTENT_WEIGHTS` directly.
    """
    label, confidence, scores = classify_intent_with_confidence(query)

    if confidence >= confidence_threshold or scores[label] == 0:
        return label, INTENT_WEIGHTS[label]

    ranked = sorted(scores.items(), key=lambda kv: -kv[1])
    second_label = ranked[1][0] if len(ranked) > 1 else label
    if second_label == label or scores[second_label] <= 0:
        return label, INTENT_WEIGHTS[label]

    # Primary keeps (0.5 + confidence/2); secondary gets the rest.
    primary_share = 0.5 + confidence * 0.5
    secondary_share = 1.0 - primary_share
    w_primary   = INTENT_WEIGHTS[label]
    w_secondary = INTENT_WEIGHTS[second_label]
    blended = tuple(
        primary_share * w_primary[i] + secondary_share * w_secondary[i]
        for i in range(5)
    )
    return label, blended  # type: ignore[return-value]
