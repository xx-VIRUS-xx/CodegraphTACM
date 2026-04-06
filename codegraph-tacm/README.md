# CodeGraph-TACM — Master Reference

## What This Project Is

A code intelligence system that constructs a **minimum-token, maximum-relevance context payload** for LLM queries about codebases. Instead of stuffing raw source into prompts, it builds four graph signal layers, scores every candidate code node across all four, and hands the LLM only what it actually needs.

**Core thesis:**
> The winner in AI coding tools will be the one that controls context selection, not the one with the biggest model. CodeGraph-TACM is the context selection layer.

---

## The Four Graph Solution

Four graph layers. None of them touch the LLM directly. They are pure signal sources for the TACM Resolver.

| Graph | Name | What it captures | Implementation |
|---|---|---|---|
| G1 | Syntax / AST | What's written — functions, classes, calls, imports | Python `ast` module — **BUILT** (`ast_parser.py`) |
| G2 | Causal / CPG | What flows and branches — CFG + DFG | Python `ast` — **NOT BUILT** |
| G3 | Semantic | What's similar — embedding cosine similarity | sentence-transformers + Elasticsearch kNN — **NOT BUILT** |
| G4 | Historical | What's been risky — Git churn, bug frequency | GitPython — **NOT BUILT** |

---

## The TACM Resolver Pipeline

```
User Query + Token Budget
        │
        ▼
Query Intent Classifier
(assigns dynamic weights w1, w2, w3, w4 per query type)
        │
        ▼
Phase 1: Skeleton Fetch
(node IDs + scores from all four graphs — ~5 tokens/node)
        │
        ▼
Scorer
score(node) = w1×G1 + w2×G2 + w3×G3 + w4×G4
value(node) = score(node) / node.token_cost
        │
        ▼
Phase 2: Payload Fetch
(resolve selected nodes to full text — signatures, docstrings, deps)
        │
        ▼
Budget Filler
(greedy fill: highest value/token_cost until budget exhausted)
        │
        ▼
Payload Serialiser
(structured XML/JSON — the ONLY thing the LLM ever sees)
        │
        ▼
LLM Call
```

**Key design rule:** The LLM never sees raw pointers, node IDs, or graph structures. It receives resolved natural text only.

---

## Repository Structure

```
codegraph-tacm/
│
├── README.md                    ← this file
│
├── research/
│   ├── THESIS.md                ← one-sentence thesis + full research claim
│   ├── RELATED_WORK.md          ← existing systems + differentiation table
│   └── NOVELTY.md               ← three novel claims, precisely stated
│
├── problems/
│   ├── PROBLEMS_OVERVIEW.md     ← all 11 problems + 6 questions indexed
│   ├── P01_pointer_resolution.md
│   ├── P02_cross_file_symbols.md
│   ├── P03_interprocedural_dfg.md
│   ├── P04_address_stability.md
│   ├── P05_graph4_data.md
│   ├── P06_budget_allocation.md
│   ├── P07_benchmark_fairness.md
│   ├── P08_starting_point_metric.md
│   ├── P09_query_intent_classifier.md
│   ├── P10_score_normalisation.md
│   ├── P11_payload_serialisation.md
│   ├── Q01_elasticsearch_vs_redis.md
│   ├── Q02_weight_tuning.md
│   ├── Q03_bug_localisation_dataset.md
│   ├── Q04_treesitter_vs_ast.md
│   ├── Q05_git_extraction.md
│   └── Q06_greedy_vs_knapsack.md
│
├── architecture/
│   ├── DECISIONS.md             ← all 6 architecture decisions + rationale
│   ├── STACK.md                 ← technology choices + justification
│   ├── DATA_MODELS.md           ← CGINode, CGIEdge, TACMAddress schemas
│   └── TACM_DEEP.md             ← two-phase resolution + reasoning traces
│
└── experiments/
    ├── BENCHMARK_PLAN.md        ← what to measure, how, against what
    ├── EXPERIMENT_01.md         ← Graph 1 only vs naive RAG (run this first)
    └── ABLATION_PLAN.md         ← how to test each graph's contribution
```

---

## Current Status

| Component | Status | File |
|---|---|---|
| G1 AST Parser | ✅ Built + tested | `ast_parser.py` |
| G2 Causal Graph | ❌ Not built | — |
| G3 Semantic Graph | ❌ Not built | — |
| G4 Historical Graph | ❌ Not built | — |
| TACM Resolver | ❌ Not built | — |
| Query Intent Classifier | ❌ Not built | — |
| Benchmark | ❌ Not run | — |

**Next action:** Run Experiment 01 before building anything else. See `experiments/EXPERIMENT_01.md`.

---

## Three Audiences

| Audience | What they need | What you have now |
|---|---|---|
| Academic (EMNLP/NAACL) | Benchmark numbers + novel claim | Architecture + G1 |
| Hiring managers ($100k+) | Working demo + GitHub repo | ast_parser.py |
| Investors (seed) | Cost reduction proof | Architecture story |

---

## Agent Instructions

If you are an AI agent working on this project:
- Each problem file in `problems/` is self-contained — read only that file to work on that problem
- Each experiment file in `experiments/` has explicit success criteria
- Do not modify `research/THESIS.md` without updating `research/NOVELTY.md` too
- The canonical architecture is in `architecture/DECISIONS.md` — check it before proposing changes
- All code should target Python 3.10+ and use type hints throughout
