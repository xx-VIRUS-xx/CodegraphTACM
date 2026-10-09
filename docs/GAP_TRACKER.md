# TACM Gap Tracker

Rule: Do not cross off any item until explicit user confirmation.

## Execution Order

- [ ] Gap 1: GT Quality / Gold Set
Goal: Build a manually verified gold subset and report both `all` and `gold-only` results.
Done criteria: gold labels + dual-metric output exist, and user confirms closure.

- [ ] Gap 2: Statistical Power
Goal: Add CI + significance reporting by default (paired tests vs key baselines).
Done criteria: one run prints leaderboard + CIs + p-values, and user confirms closure.

- [ ] Gap 3: Budget Fairness
Goal: Enforce identical token-budget packing policy across retrievers.
Done criteria: per-condition token variance is bounded, and user confirms closure.

- [ ] Gap 4: Failure Taxonomy
Goal: Auto-label misses (e.g., `right_file_wrong_fn`, `gt_not_parsed`, `gt_not_in_pool`, `ranked_outside_k`, `query_ambiguous`).
Done criteria: summary includes bucket counts/percentages, and user confirms closure.

- [ ] Gap 5: Cross-Language Robustness
Goal: Add per-language calibration and scorecards (Python/JS/Java/Rust/Go).
Done criteria: language-wise benchmarks run cleanly with clear diagnostics, and user confirms closure.

- [ ] Gap 7: Adversarial/Noisy Query Robustness
Goal: Add harder query sets (issue text, vague bug reports, stack traces).
Done criteria: robustness report exists across query styles, and user confirms closure.

- [ ] Gap 8: Retrieval -> Solve Causality
Goal: Quantify solve probability by retrieval rank/coverage bands.
Done criteria: rank-to-solve curve report exists, and user confirms closure.

- [ ] Gap 6: Online Realism (Future, done last)
Goal: Add latency, cost, cache-hit, and operational metrics.
Done criteria: production-style eval report exists, and user confirms closure.
