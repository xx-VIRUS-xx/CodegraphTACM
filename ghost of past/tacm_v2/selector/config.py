"""config.py — Single source of truth for selector tuning knobs.

Previously these constants lived scattered across ``scoring.py`` and
``selector.py`` as inline magic numbers. Centralising them here gives us:

  * one place to tune,
  * serialisable config for ablation experiments,
  * safe defaults that exactly reproduce the pre-config behaviour so the
    regression guards in ``tests/test_regression.py`` still hold.

Nothing in this module is allowed to change the defaults silently.
If you need different behaviour, pass a non-default :class:`SelectorConfig`
into :class:`~tacm_v2.selector.scoring.NodeScorer` and the selectors.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class SelectorConfig:
    """All tunable parameters for scoring and selection.

    Defaults are the values previously hard-coded in the codebase.
    Do not change defaults without updating the regression guards.
    """

    # --- Overflow (both select and select_dynamic) ---
    max_overflow_ratio:     float = 0.5
    overflow_score_floor:   float = 0.25

    # --- Containment bonus ---
    containment_bonus:      float = 0.15

    # --- Neighborhood bonus (post-score) ---
    neighborhood_scale_strong: float = 0.08   # when BM25 signal is strong
    neighborhood_scale_weak:   float = 0.15   # when BM25 signal is weak

    # --- PageRank bonus ---
    pagerank_scale_strong:  float = 0.06
    pagerank_scale_weak:    float = 0.12
    pagerank_alpha:         float = 0.85
    pagerank_max_iter:      int   = 50
    pagerank_tol:           float = 0.0       # 0.0 → always run max_iter (reproduces legacy)

    # --- Adaptive BM25 weighting ---
    bm25_weak_threshold:    float = 0.01      # mean normalised BM25 below this → weak
    bm25_shed_fraction:     float = 0.5       # fraction of w_bm25 redistributed

    # --- Cascading BM25 (previously dead code; enabled by default) ---
    use_cascading_bm25:     bool  = True
    cascading_expansion_cap: int  = 12        # max expansion terms appended

    # --- Identifier-match signals (FUNCTION nodes only) ---
    # Rewards functions whose *name* or *qualified name* token-matches the
    # query, independent of long-body BM25 dilution. Primary lever for
    # within-file disambiguation.
    name_match_scale:       float = 0.20
    # Rewards functions whose file path contains a query token. Helps
    # recover cases where the query mentions a filename/module explicitly.
    path_match_scale:       float = 0.10
    # Minimum token length counted for name/path matching.
    identifier_min_length:  int   = 3

    # --- Diversity penalty (select_dynamic only) ---
    diversity_sibling_free: int   = 1         # first N siblings are free
    diversity_file_free:    int   = 2         # first N file-mates are free
    diversity_sibling_step: float = 0.04
    diversity_file_step:    float = 0.03
    diversity_sibling_cap:  float = 0.12
    diversity_file_cap:     float = 0.12
    diversity_total_cap:    float = 0.18

    # --- Intent classification ---
    intent_blend_threshold: float = 0.30      # top-1 margin below this → blend top-2
    intent_default_on_zero: str   = "bug"     # when no keyword hits at all

    def as_dict(self) -> dict:
        """JSON-serialisable view of the config (for experiment logs)."""
        return asdict(self)


# The canonical default used throughout the codebase.
# Do not mutate; construct a new SelectorConfig when you need overrides.
DEFAULT_CONFIG = SelectorConfig()
