# Q02 — How to Tune Weight Vector (w1, w2, w3, w4)
**Status:** ❓ OPEN | **Blocks:** TACM Resolver

## Problem
Once the Query Intent Classifier assigns an intent class, the actual numeric weight values (w1, w2, w3, w4) for that class must be determined.

## Options

### Option A — Hand-tuned presets (START HERE)
Define a weight table manually based on domain intuition:
```python
WEIGHT_PRESETS = {
    "bug_localisation":  (0.15, 0.40, 0.20, 0.35),  # (w1,w2,w3,w4) — boost causal+historical
    "similarity_search": (0.25, 0.10, 0.55, 0.10),  # boost semantic
    "history_query":     (0.10, 0.10, 0.10, 0.70),  # boost historical
    "explanation":       (0.40, 0.30, 0.20, 0.10),  # boost syntax+causal
    "dependency":        (0.35, 0.40, 0.15, 0.10),  # boost syntax+causal
    "completion":        (0.50, 0.30, 0.15, 0.05),  # boost syntax
}
```
- ✅ No training data needed
- ✅ Interpretable and adjustable
- ❌ Suboptimal — human intuition ≠ data-driven optimum

### Option B — Grid search on validation set
Try all combinations of weights at 0.1 increments (subject to Σ=1).
Evaluate each on a held-out labelled query set.
- ✅ Semi-principled, no model training
- ❌ Combinatorial: 4 weights at 0.1 intervals = ~286 combinations per intent class
- For 6 intent classes = 1,716 experiments (feasible with GPT-4o mini judge)

### Option C — Bayesian optimisation
Use a Bayesian optimiser (optuna, scikit-optimize) to efficiently search the weight space.
- ✅ More efficient than grid search
- ✅ Finds optima in fewer evaluations
- ❌ Still requires labelled evaluation set

## Agent Task
1. Implement Option A with the preset table above
2. Build a 30-query evaluation set: 5 queries per intent class, with known ground-truth node
3. For each query: run resolver with Option A weights, measure MRR
4. Try manual variations: ±0.1 on each weight for the worst-performing intent class
5. Report: which intent class benefits most from weight tuning?

## Acceptance Criteria
- Baseline (equal weights 0.25 each) MRR established
- Option A presets improve MRR by ≥5% over equal weights
- Identify which weight (w1–w4) has highest sensitivity for each intent class
