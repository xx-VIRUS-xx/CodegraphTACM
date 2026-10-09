# P10 — Cross-graph Score Normalisation
**Severity:** 🟠 HIGH | **Status:** ❓ OPEN | **Blocks:** TACM Resolver

## Problem
Four graphs produce scores on different scales:
- G1: PageRank centrality (0.001 – 0.15, float)
- G2: Causal path distance (0 – 10, int)  
- G3: Cosine similarity (0.0 – 1.0, float)
- G4: Risk score (0.0 – 1.0, normalised float)

Before computing `score(node) = w1×G1 + w2×G2 + w3×G3 + w4×G4`, all four must be on the same scale.

## Normalisation Options

### Option A — Min-max per graph per query batch
```python
def minmax(scores: list[float]) -> list[float]:
    lo, hi = min(scores), max(scores)
    if hi == lo: return [0.5] * len(scores)
    return [(s - lo) / (hi - lo) for s in scores]
```
- ✅ Simple, always produces [0,1] range
- ❌ Sensitive to outliers (one very high node skews everything)
- ❌ Loses relative magnitude between batches

### Option B — Z-score normalisation
```python
import statistics
def zscore(scores: list[float]) -> list[float]:
    mu = statistics.mean(scores)
    sigma = statistics.stdev(scores) or 1.0
    return [(s - mu) / sigma for s in scores]
```
- ✅ Robust to outliers
- ✅ Standard in IR — BM25 uses a variant
- ❌ Output is not bounded [0,1] — need clipping for final scoring

### Option C — Rank-based (Reciprocal Rank Fusion style)
```python
def rank_normalise(scores: list[float], k: int = 60) -> list[float]:
    ranked = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
    rrf = [0.0] * len(scores)
    for rank, idx in enumerate(ranked):
        rrf[idx] = 1.0 / (k + rank + 1)
    return rrf
```
- ✅ Completely scale-invariant
- ✅ Used by state-of-the-art hybrid retrieval (RRF)
- ✅ No sensitivity to outliers
- ❌ Loses magnitude information (rank 1 vs rank 2 treated as equal gap)

### Option D — Learned normalisation
Train a small MLP to combine raw scores. Requires labelled training data.
- ✅ Theoretically optimal
- ❌ Needs training data we don't have yet

## Agent Task
1. Implement all three options (A, B, C) as Python functions
2. Create synthetic test case: 100 nodes with known ground-truth relevance
3. For each option: compute combined score, measure rank correlation with ground truth (Spearman ρ)
4. Test robustness: add 1 extreme outlier node to each graph's scores, re-measure
5. Recommendation: which option for v1?

## Acceptance Criteria
- Chosen method produces consistent rankings across repeated runs
- Adding an outlier does not change rankings of non-outlier nodes by more than 3 positions
- Combined score correctly ranks known-relevant nodes above known-irrelevant nodes in test case

## Current Best Thinking
Option C (rank-based RRF) for v1. Scale-invariant, no outlier sensitivity, battle-tested in hybrid retrieval literature.
