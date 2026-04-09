"""intent.py — Query intent classification and per-intent weight vectors.

Shared by selector.py and scoring.py to avoid circular imports.
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


def classify_intent(query: str) -> str:
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

    scores = {
        QueryIntent.BUG:       bug_hits,
        QueryIntent.STRUCTURE: structure_hits,
        QueryIntent.EXPLAIN:   explain_hits,
    }
    best = max(scores, key=lambda k: scores[k])
    return best if scores[best] > 0 else QueryIntent.BUG


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
