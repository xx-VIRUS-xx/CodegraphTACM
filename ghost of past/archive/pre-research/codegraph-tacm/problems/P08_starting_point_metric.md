# P08 — Formalising "Starting Point Quality"
**Severity:** 🟡 MEDIUM | **Status:** ❓ OPEN | **Blocks:** Paper / Metrics

## Problem
GPT's framing — "LLM starts near the answer" — is the pitch. "Near" must be a formal metric.

Without a formal metric we cannot:
- Claim the system improves starting position (not just answer quality)
- Distinguish better retrieval from better reasoning
- Run ablations that isolate retrieval quality from generation quality

## Proposed Metric: Rank of Ground Truth

For bug localisation tasks where we know the buggy function:

```
starting_position_quality = MRR(ground_truth_node, tacm_ranked_list)

MRR = (1/N) Σ (1 / rank_i)

where rank_i = position of ground-truth buggy function
               in TACM's scored node list, BEFORE the LLM call
```

This measures retrieval quality independently of the LLM.

## Secondary Metrics

**P@K (Precision at K):**
What fraction of top-K nodes are relevant to the ground-truth fix?
```
P@5 = |{relevant nodes in top 5}| / 5
```

**Token distance:**
How many tokens does the resolver allocate before including the ground-truth node?
```
token_distance = Σ token_cost(nodes ranked above ground_truth)
```
Lower = better starting position.

**Counterfactual degradation:**
How much does answer quality drop if TACM selection is replaced with random selection at same token budget?
```
counterfactual_delta = accuracy(TACM) - accuracy(random_same_budget)
```
Large delta = TACM selection is meaningful, not just token injection.

## Agent Task
1. Take 20 tasks from BugsInPy where the buggy function is known
2. Run TACM resolver on each (G1 only first)
3. For each: record rank of ground-truth buggy function in resolver's output list
4. Compute MRR, P@5, token_distance
5. Compare: does TACM ranking correlate with final answer quality?

## Acceptance Criteria
- MRR > 0.5 (ground-truth node in top 2 on average)
- P@5 > 0.6
- Counterfactual delta > 0.15 (15% quality improvement from selection vs random)
