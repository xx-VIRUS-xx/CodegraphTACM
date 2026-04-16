# BENCHMARK_PLAN.md — Full Evaluation Design

## Primary Benchmark: Bug Localisation (BugsInPy)

### Dataset
BugsInPy — github.com/soarsmu/BugsInPy
- 493 real Python bugs from 17 projects
- Ground truth: buggy files + line ranges (derive function-level from G1)
- Use: 50 bugs (representative sample across projects)

### Task
Given: bug report text (natural language)
Goal: rank the buggy function highest in retrieved context

### Metric
MRR (Mean Reciprocal Rank) — primary
P@5 (Precision at 5) — secondary
Token cost per query — efficiency metric

---

## Secondary Benchmark: SWE-bench Lite

### Dataset
SWE-bench Lite — 300 tasks
Use: first 50 tasks (consistent with prior work)

### Task
Given: GitHub issue text
Goal: generate a correct fix (pass unit tests)

### Metric
% Resolved (Pass@1) — primary SWE-bench metric

---

## Systems to Compare

| System | Implementation |
|---|---|
| No retrieval (LLM only) | Direct GPT-4o call, no context |
| Naive RAG | LlamaIndex VectorStoreIndex, top-5 chunks |
| BM25 only | rank_bm25 on code tokens |
| G1 only | AST graph + BM25, no scoring |
| G1 + G2 | + causal signals |
| G1 + G2 + G3 | + semantic signals |
| G1 + G2 + G3 + G4 | Full four-graph system |
| Full system + adaptive weights | + query intent classifier |

Last row = our complete system. Each row tests one addition.

---

## Fixed Variables (all systems)

- LLM: GPT-4o (gpt-4o-2024-08-06)
- Temperature: 0.0
- Context budget: 800 tokens
- Max generation: 512 tokens

---

## Results Table Template

| System | BugsInPy MRR | BugsInPy P@5 | SWE% | Tokens/query | Build time |
|---|---|---|---|---|---|
| No retrieval | | | | 0 | — |
| Naive RAG | | | | | |
| BM25 only | | | | | |
| G1 only | | | | | |
| G1+G2 | | | | | |
| G1+G2+G3 | | | | | |
| G1+G2+G3+G4 | | | | | |
| Full + adaptive | | | | | |
