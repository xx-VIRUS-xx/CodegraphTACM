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

    # --- Personalized PageRank (query-dependent) ---
    # When enabled, runs PPR per query with BM25 top-K as seeds. Replaces
    # the cached vanilla PageRank bonus as the structural signal channel.
    # Off by default to keep regression guards stable; turn on to measure lift.
    ppr_enabled:            bool  = False
    ppr_seed_k:             int   = 20        # how many BM25 top hits seed teleport
    ppr_alpha:              float = 0.85
    ppr_max_iter:           int   = 20        # 20 is ample with seeded init
    ppr_tol:                float = 1e-4
    ppr_scale_strong:       float = 0.12      # dominant structural signal when BM25 is strong
    ppr_scale_weak:         float = 0.20      # lean harder on structure when BM25 is weak

    # --- Adaptive PPR by seed-neighborhood density ---
    # PPR's random walks only help when BM25 seeds have a non-trivial call
    # neighborhood to explore. On shallow-library queries (e.g. flask/xarray
    # GT is a top-level function) the seeds have near-zero fan-out and PPR
    # mass gets stuck on the teleport vector, which is effectively BM25 —
    # but with added noise from rank normalisation that can demote the true
    # target. Analyzer on the 2026-04-22 SWE-bench run showed Hybrid beat
    # TACM-PPR on flask/xarray/sklearn (shallow repos) while TACM-PPR beat
    # Hybrid on pylint/seaborn (call-graph-rich). We scale the PPR bonus
    # continuously between [density_min_scale, 1.0] of its configured value
    # based on the average out-degree of the seed set: low density → damp,
    # high density → keep full weight.
    ppr_density_enabled:        bool  = True
    ppr_density_min_scale:      float = 0.0    # when seed out-degree ≈ 0, shed full PPR weight
    ppr_density_saturation:     float = 6.0    # seed avg out-degree at which to use full weight

    # --- Adaptive BM25 weighting ---
    bm25_weak_threshold:    float = 0.01      # mean normalised BM25 below this → weak
    bm25_shed_fraction:     float = 0.5       # fraction of w_bm25 redistributed

    # --- Cascading BM25 (previously dead code; enabled by default) ---
    use_cascading_bm25:     bool  = True
    cascading_expansion_cap: int  = 12        # max expansion terms appended

    # --- Aggressive query-side identifier expansion (Experiment 06) ---
    # When enabled, extracts code-like identifiers from the raw query
    # (CamelCase, snake_case, dotted paths, backtick/quoted tokens) and
    # emits both the original and identifier-split forms as additional
    # BM25 variants. Also enables an "identifier-exact" side signal that
    # rewards FUNCTION nodes whose *name tokens* contain any query-extracted
    # identifier token verbatim — escaping BM25 body-dilution on Hit@1.
    # Off by default so regression guards hold.
    identifier_expansion_enabled: bool  = False
    identifier_exact_scale:       float = 0.25   # bonus weight for exact identifier match

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
