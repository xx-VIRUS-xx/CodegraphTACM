# TACM Agent Brief — Start Here

## What This Project Is

We are building a **context selection layer** for LLM coding agents called TACM
(Token-Addressable Context Memory). The core thesis is simple:

> The winner in AI coding tools will be the one that controls context selection,
> not the one with the biggest model.

Most tools today — including the best ones — dump raw code into the LLM's context
window and let the model figure it out. We are building the layer that decides
*which code*, *how much of it*, and *in what form* the LLM should see — given a
fixed token budget.

---

## What We Are NOT Building

We are not building a new AST parser. We are not building another code graph
tool. `code-review-graph` (https://github.com/tirth8205/code-review-graph)
already does structural graph extraction well — MIT licensed, MCP interface,
19 languages. We are using it as our G1 (structural graph layer).

G1 setup: `pip install code-review-graph`, run `code-review-graph build` on
the target repo, then `code-review-graph serve` to expose the MCP interface.
`get_review_context_tool` is the only G1 call TACM makes.

We are building what sits on top of it — the part nobody has built.

---

## The One Problem Nobody Has Solved

`code-review-graph` returns a context payload with ~38% average precision.
That means 62% of what it sends to the LLM is noise — impacted nodes that
are not actually relevant to the query. The LLM has to wade through all of it.

Nobody is doing budget-aware, scored context selection. That is the gap.

---

## The Core Idea — TACM Resolver

Given the raw output from `code-review-graph`, the TACM Resolver does this:

```
code-review-graph output (raw nodes + edges)
        +
Token Budget (e.g. 800 tokens)
        +
Query Intent (what kind of task — review, debug, refactor, explain)
        │
        ▼
Score every node:
    score(node) = w1×structural + w2×semantic + w3×historical
    value(node) = score(node) / node.token_cost

        │
        ▼
Greedy fill to budget:
    select highest value/token nodes until budget exhausted

        │
        ▼
Return: minimum-token, maximum-relevance context slice
```

The LLM only ever sees the selected slice. Never raw graph dumps.

---

## The Four Graph Layers (Long Term Vision)

| Graph | Name | Signal | Status |
|-------|------|--------|--------|
| G1 | Structural | AST nodes, call edges, imports | USE code-review-graph |
| G2 | Causal | Control flow, data flow | Not built |
| G3 | Semantic | Embedding similarity | Not built |
| G4 | Historical | Git churn, bug frequency | Not built |

**Right now, only G1 matters.** G2, G3, G4 come after the Resolver is proven.

---

## Current State — Honest Assessment

| Component | Status | Notes |
|-----------|--------|-------|
| G1 (structural graph) | Ready — use code-review-graph | `pip install code-review-graph` |
| TACM Resolver | Not built | This is the first thing to build |
| Score function | Not built | Start simple — see below |
| Budget filler | Not built | Greedy is fine for now |
| Experiment 01 | Not run | This must run before anything else |
| Benchmarks | Empty | No numbers yet |

---

## The First Task — Experiment 01

**Before building anything else, run this experiment.**

### Goal
Prove that TACM Resolver improves on raw code-review-graph output.

### Setup
1. Install code-review-graph on `psf/requests` library
2. Call `get_review_context_tool` on 10 real bug issues
3. Record the raw output — nodes, token count, what's included
4. Run the TACM Resolver on that same output with an 800 token budget
5. Compare: does the scored, budget-filled slice contain the ground-truth
   buggy function more often? At higher rank?

### What "ground truth" means
For each bug issue, the ground truth is the function(s) modified in the
fixing commit. Binary — is that function in the selected context or not?

### Metrics to collect

| Metric | Naive crg output | TACM Resolver | Delta |
|--------|-----------------|---------------|-------|
| GT Present (%) | ? | ? | ? |
| MRR | ? | ? | ? |
| Tokens used | ? | ? | ? |
| Precision@5 | ? | ? | ? |

### Success criteria
- TACM MRR >= crg baseline MRR + 0.1
- TACM tokens used <= crg baseline tokens used
- GT Present rate >= crg baseline

If any one of these is true, continue building. If none are true, understand
why before going further.

---

## The Resolver — Build This First

```python
# resolver.py — skeleton to implement

from dataclasses import dataclass
from typing import List

@dataclass
class ScoredNode:
    node_id: str
    source_text: str
    token_cost: int        # len(source_text) // 4
    degree: int            # number of edges in graph
    in_blast_radius: bool  # from crg impact analysis
    has_test: bool         # from crg TESTED_BY edges
    score: float = 0.0
    value: float = 0.0     # score / token_cost


def score_node(node: ScoredNode, query_intent: str = "review") -> float:
    # Phase 1: ignore query_intent entirely
    # Score purely on structural signals from code-review-graph
    w_degree = 0.4
    w_blast  = 0.4
    w_test   = 0.2

    return (
        w_degree * min(node.degree / 10, 1.0) +
        w_blast  * float(node.in_blast_radius) +
        w_test   * float(node.has_test)
    )


def resolve(nodes: List[ScoredNode], token_budget: int) -> List[ScoredNode]:
    # Score and rank
    for node in nodes:
        node.score = score_node(node)
        node.value = node.score / max(node.token_cost, 1)

    ranked = sorted(nodes, key=lambda n: n.value, reverse=True)

    # Greedy fill
    selected = []
    remaining = token_budget
    for node in ranked:
        if node.token_cost <= remaining:
            selected.append(node)
            remaining -= node.token_cost

    return selected
```

This is the entire Resolver for Experiment 01. Do not add complexity until
the experiment results justify it.

---

## What code-review-graph Gives You (G1 Input)

Install and run:
```bash
pip install code-review-graph
code-review-graph build   # on psf/requests repo
code-review-graph serve   # start MCP server
```

The `get_review_context_tool` returns:
- `changed_nodes` — functions/classes that changed
- `impacted_nodes` — blast radius (BFS traversal)
- `edges` — relationships between nodes
- `source_snippets` — extracted line ranges
- `review_guidance` — pre-computed heuristics (test gaps, wide blast radius)

These are your raw inputs to the Resolver. Map them to `ScoredNode` objects
and run `resolve()`.

---

## Key Decision: Why Greedy Fill, Not Knapsack

The optimal budget packing is a 0/1 knapsack problem (NP-hard). Greedy
(sort by value/cost, fill until budget exhausted) gives a good approximation
in O(n log n) and is fast enough for real-time use. Revisit this only if
experimental results show greedy is leaving significant value on the table.

---

## What Good Looks Like

A Resolver that takes code-review-graph's 38% precision payload and returns
a budget-constrained slice with 60%+ precision — using the same or fewer
tokens — is a publishable, demonstrable result.

That number — precision improvement within a fixed token budget — is the
entire research claim at this stage.

---

## Agent Rules

- Do not build G2, G3, or G4 until Experiment 01 results are in hand
- Do not modify the score function until you have baseline numbers to compare against
- Do not add query intent classification until single-intent scoring is validated
- The Resolver is ~200 lines of Python. Keep it that way for now
- Every change should be motivated by an experimental result, not intuition
- If something is unclear, ask — do not assume and build in the wrong direction

---

## Immediate Next Steps

1. `pip install code-review-graph`, clone `psf/requests`, run `code-review-graph build`
2. Call `get_review_context_tool` on one test query — print raw output, understand schema
3. Build `tacm/crg_adapter.py` — map crg output → `ScoredNode` objects
4. Build `tacm/resolver.py` — `score_node()` + `resolve()` as specced above
5. Run `resolve()` on the raw crg output with 800 token budget
6. Manually check: is the ground-truth buggy function in the selected slice?
7. Record results in the metrics table above
8. Report back before building anything else
