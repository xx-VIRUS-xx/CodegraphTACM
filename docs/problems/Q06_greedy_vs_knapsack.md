# Q06 — Greedy vs Knapsack for Budget Fill
**Status:** ❓ OPEN | **Blocks:** TACM Resolver

## Problem
The budget filler selects nodes to include in the final payload. Greedy (sort by value/cost, take until full) is simple but may not be optimal.

**Example where greedy fails:**
```
Budget: 100 tokens
Node A: score=0.9, cost=60 tokens  → value/cost = 0.015
Node B: score=0.7, cost=45 tokens  → value/cost = 0.0156  ← greedy picks this first
Node C: score=0.6, cost=40 tokens  → value/cost = 0.015

Greedy: picks B (45 tokens), then can't fit A (60) or C (40) → total score: 0.7
Optimal: picks B + C (85 tokens) → total score: 1.3
Or: picks A + C (100 tokens) → total score: 1.5  ← BEST
```

## Options

### Option A — Greedy (value/token_cost ratio)
```python
def greedy_fill(nodes, budget):
    ranked = sorted(nodes, key=lambda n: n.value/n.cost, reverse=True)
    selected, used = [], 0
    for node in ranked:
        if used + node.cost <= budget:
            selected.append(node)
            used += node.cost
    return selected
```
- ✅ O(n log n) — extremely fast
- ✅ Approximately optimal in practice (empirically within 5% of optimal)
- ❌ Not theoretically optimal

### Option B — 0/1 Knapsack DP
```python
def knapsack_fill(nodes, budget):
    n = len(nodes)
    dp = [[0]*(budget+1) for _ in range(n+1)]
    for i, node in enumerate(nodes, 1):
        for w in range(budget+1):
            dp[i][w] = dp[i-1][w]
            if node.cost <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-node.cost] + node.score)
    # backtrack to find selected items
    ...
```
- ✅ Provably optimal
- O(n × budget) — with n=200 nodes, budget=800 tokens: 160,000 operations
- ✅ Tractable at our scale
- ❌ More complex code

### Option C — Beam search
Try top-K partial selections at each step, keep best K beams.
- ✅ Between greedy and DP in quality and speed
- ❌ Adds complexity without clear advantage over DP at our scale

## Agent Task
1. Implement both Option A (greedy) and Option B (knapsack DP)
2. Generate synthetic test: 200 nodes with random scores and costs (5–100 tokens each), budget=800
3. Run both: measure selected total score, time taken
4. How often does greedy match optimal? What is the average quality gap?
5. At what node count does knapsack become too slow (>100ms)?
6. Recommendation: greedy for speed or knapsack for optimality?

## Acceptance Criteria
- Greedy quality gap ≤ 5% vs optimal on synthetic test
- If greedy gap > 5%: use knapsack DP
- Decision made with data, not intuition
