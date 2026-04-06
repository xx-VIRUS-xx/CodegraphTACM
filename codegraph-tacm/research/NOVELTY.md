# NOVELTY.md — Three Novel Claims

## Claim 1 — Four-Graph Signal Fusion with Query-Adaptive Weights

**What:** The resolver assigns a weight vector (w1, w2, w3, w4) to the four graph layers dynamically based on the query type. Bug queries boost causal (w2) and historical (w4). Similarity queries boost semantic (w3). History queries boost historical (w4) exclusively.

**Why novel:** Every existing system uses a single graph layer with uniform retrieval. None weight multiple graph signals per query type.

**How to validate:** Ablation study. Compare:
- G1 only (AST) — baseline
- G1 + G2 (AST + Causal)
- G1 + G2 + G3 (+ Semantic)
- G1 + G2 + G3 + G4 (full system)
- Full system with static equal weights vs query-adaptive weights

Each step should show measurable improvement on the benchmark.

**Formal statement:**
```
score(node, query) = w1(q)×G1(node) + w2(q)×G2(node)
                   + w3(q)×G3(node, query) + w4(q)×G4(node)

where w_i(q) are learned or heuristic functions of query intent q
and Σ w_i = 1 for all q
```

---

## Claim 2 — Two-Phase Skeleton/Payload Resolution

**What:** Resolution happens in two phases:
- Phase 1 (Skeleton): fetch only node IDs + scores from all four graphs. ~5 tokens per node. Fast, cheap.
- Phase 2 (Payload): fetch full text payload for selected nodes only. Only nodes that pass the budget filter get expanded.

**Why novel:** All existing systems resolve in one phase — fetch the subgraph, serialise it to text, insert it. They have no intermediate skeleton representation.

**Why it matters:**
- The skeleton phase makes the "pointer" concept architecturally real — node IDs exist as stable internal addresses between phases
- Skeleton fetch can scan thousands of candidates cheaply
- Payload fetch is expensive but only called for the ~10 nodes that actually get included
- Total cost: (N × 5 tokens for skeleton) + (K × 50 tokens for payload) where N=1000, K=10
- vs single-phase: immediately fetches full text for top-K candidates only (misses better candidates deeper in the graph)

**How to validate:** Compare retrieval precision of two-phase vs single-phase at same total token budget.

---

## Claim 3 — Addressable Reasoning Traces (Future / V2)

**What:** After each resolved query, TACM stores the reasoning pattern — which nodes were retrieved, which graph signals were highest, what weight vector was used — as an addressable trace. Future similar queries bootstrap from prior reasoning.

**Why novel:** No existing system accumulates retrieval experience. Every query starts from scratch against the raw code graph.

**Why it matters:**
- Repeated queries about the same codebase get progressively cheaper and more accurate
- The system learns which areas of a codebase are "hotspots" for a given team's query patterns
- Reasoning traces are the Memory Layer that GPT identified as missing

**Status:** Not yet designed in detail. Belongs in V2 after Phase 1 benchmark.

---

## What Is NOT Novel (Be Honest in the Paper)

- Using a code graph for LLM retrieval — CodexGraph, CGM, GraphCoder all do this
- AST parsing for code structure extraction — standard
- BM25 + embedding hybrid retrieval — standard
- Token budget management — LlamaIndex does a version of this
- Graph traversal for subgraph extraction — standard graph algorithms

The novelty is specifically: (1) four-graph fusion, (2) query-adaptive weights, (3) two-phase resolution. Everything else is infrastructure.
