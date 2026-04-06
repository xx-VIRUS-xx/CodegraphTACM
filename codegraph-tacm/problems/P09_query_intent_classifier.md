# P09 — Query Intent Classifier Design
**Severity:** 🔴 CRITICAL | **Status:** ❓ OPEN | **Blocks:** TACM Resolver

## Problem
The resolver needs to assign (w1, w2, w3, w4) per query. These weights depend on query *intent*. The classifier maps query text → intent class → weight vector.

## Intent Classes + Weight Profiles

| Intent | w1 (Syntax) | w2 (Causal) | w3 (Semantic) | w4 (Historical) | Example queries |
|---|---|---|---|---|---|
| bug_localisation | 0.2 | 0.4 | 0.2 | 0.4 | "why does X crash", "what causes Y error" |
| similarity_search | 0.3 | 0.1 | 0.5 | 0.1 | "find functions like X", "similar to parse()" |
| history_query | 0.1 | 0.1 | 0.1 | 0.7 | "what changed in X", "who modified Y" |
| explanation | 0.4 | 0.3 | 0.2 | 0.1 | "what does X do", "explain this function" |
| dependency | 0.4 | 0.4 | 0.1 | 0.1 | "what calls X", "what does X depend on" |
| completion | 0.5 | 0.3 | 0.2 | 0.0 | "what should come after", "complete this" |

Note: weights shown are heuristic starting points. Final values from Q02 (weight tuning).

## Classifier Options

### Option A — Rule-based keyword matching (START HERE)
```python
INTENT_PATTERNS = {
    "bug_localisation": ["crash", "fail", "error", "bug", "broken", "exception", "why does"],
    "similarity_search": ["similar", "like", "find functions", "equivalent", "same as"],
    "history_query":     ["changed", "modified", "who wrote", "when was", "commit"],
    "explanation":       ["what does", "explain", "how does", "describe"],
    "dependency":        ["calls", "depends", "imports", "uses", "callers of"],
    "completion":        ["complete", "what comes next", "implement", "write"],
}

def classify(query: str) -> str:
    query_lower = query.lower()
    scores = {intent: sum(1 for kw in kws if kw in query_lower)
              for intent, kws in INTENT_PATTERNS.items()}
    return max(scores, key=scores.get) or "explanation"
```
- ✅ No training data needed
- ✅ Interpretable
- ✅ Fast (microseconds)
- ❌ Misses paraphrases ("doesn't work" = bug_localisation)

### Option B — Embedding similarity to intent templates
```python
INTENT_TEMPLATES = {
    "bug_localisation": "why does this function fail and crash with an error",
    "similarity_search": "find functions similar to this one",
    ...
}
# Embed query, embed templates, return closest intent
```
- ✅ Handles paraphrases better
- ✅ Soft weights possible (blend two intents)
- ❌ Requires embedding model (latency + cost)

### Option C — Small trained classifier
Fine-tune DistilBERT on labelled (query, intent) pairs.
- ✅ Most accurate
- ❌ Needs labelled training data
- ❌ Adds model dependency

## Agent Task
1. Implement Option A (rule-based) fully
2. Collect 50 real code-related queries from GitHub issues, Stack Overflow
3. Manually label each query with intent class
4. Measure Option A accuracy on this dataset
5. If accuracy < 70%, test Option B on same dataset
6. Recommend: which classifier for v1?

## Acceptance Criteria
- Classification accuracy ≥ 75% on 50-query test set
- Classification latency ≤ 5ms
- Handles "unknown" intent gracefully (falls back to equal weights)
- Weight vectors sum to 1.0 for all intent classes
