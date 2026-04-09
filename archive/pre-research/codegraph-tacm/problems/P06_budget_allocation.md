# P06 — Token Budget Allocation
**Severity:** 🟡 MEDIUM | **Status:** ✅ DISSOLVED

## Resolution
This problem does not exist.

The four graphs are pure signal layers. They do not consume token budget.
Only the TACM Resolver output consumes budget.

The resolver has a single budget constraint applied to its output:
```
Σ token_cost(selected_nodes) ≤ user_budget
```

There is no allocation between graphs because graphs produce scores, not tokens.

## What This Means
The budget problem reduces to:
1. Score every candidate node: `score(n) = w1×G1(n) + w2×G2(n) + w3×G3(n) + w4×G4(n)`
2. Compute value: `value(n) = score(n) / token_cost(n)`
3. Sort by value descending
4. Greedily select until budget exhausted

See `problems/Q06_greedy_vs_knapsack.md` for whether greedy is optimal here.

## Closed. No further action needed.
