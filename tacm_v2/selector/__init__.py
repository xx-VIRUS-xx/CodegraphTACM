"""tacm_v2.selector — public API for scoring and context selection.

Importing from sub-modules still works; this module re-exports the common
entry points so downstream callers can do::

    from tacm_v2.selector import select, SelectorConfig, classify_intent
"""

from .config import SelectorConfig, DEFAULT_CONFIG
from .intent import (
    QueryIntent,
    classify_intent,
    classify_intent_with_confidence,
    blended_weights,
    INTENT_WEIGHTS,
    LAYER_BUDGETS,
)
from .scoring import NodeScorer
from .selector import (
    SelectedNode,
    SelectionResult,
    select,
    select_dynamic,
    explain_selection,
)
from .cache import get_scorer_cache, invalidate, clear_cache

__all__ = [
    # Config
    "SelectorConfig",
    "DEFAULT_CONFIG",
    # Intent
    "QueryIntent",
    "classify_intent",
    "classify_intent_with_confidence",
    "blended_weights",
    "INTENT_WEIGHTS",
    "LAYER_BUDGETS",
    # Scoring
    "NodeScorer",
    # Selection
    "SelectedNode",
    "SelectionResult",
    "select",
    "select_dynamic",
    "explain_selection",
    # Cache
    "get_scorer_cache",
    "invalidate",
    "clear_cache",
]
