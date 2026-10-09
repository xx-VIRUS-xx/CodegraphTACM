# ABLATION_PLAN.md — Testing Each Graph's Contribution

## Purpose
Prove that each graph layer contributes independently.
Removing any single graph should degrade performance measurably.
This is required for Claim 1 in NOVELTY.md.

## Ablation Matrix

Run all 8 combinations on BugsInPy (50 bugs):

| Run | G1 | G2 | G3 | G4 | Weights |
|---|---|---|---|---|---|
| 1 | ✓ | ✗ | ✗ | ✗ | — |
| 2 | ✓ | ✓ | ✗ | ✗ | equal |
| 3 | ✓ | ✗ | ✓ | ✗ | equal |
| 4 | ✓ | ✗ | ✗ | ✓ | equal |
| 5 | ✓ | ✓ | ✓ | ✗ | equal |
| 6 | ✓ | ✓ | ✗ | ✓ | equal |
| 7 | ✓ | ✓ | ✓ | ✓ | equal |
| 8 | ✓ | ✓ | ✓ | ✓ | adaptive |

Run 8 vs Run 7 tests Claim 2 (adaptive weights outperform static).
Each run vs Run 1 tests that graph's individual contribution.

## Expected Pattern
Each graph should add measurable MRR improvement over the previous.
If G4 adds nothing, the historical risk claim is not supported.

## Adaptive Weight Ablation

For Run 8, also test:
- Static equal weights (0.25, 0.25, 0.25, 0.25)
- Hand-tuned presets per intent (from P09)
- Grid-searched presets (from Q02)

Shows progressive improvement from weighting strategy.
