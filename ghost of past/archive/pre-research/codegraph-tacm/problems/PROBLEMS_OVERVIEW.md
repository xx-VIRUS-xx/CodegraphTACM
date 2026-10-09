# PROBLEMS_OVERVIEW.md — All Problems + Questions

## Status Key
- 🔴 CRITICAL — blocks all downstream work
- 🟠 HIGH — blocks specific components
- 🟡 MEDIUM — important but not blocking
- ✅ RESOLVED — answer decided
- ❓ OPEN — needs exploration

---

## Research Problems

| ID | Title | Severity | Blocks | Status |
|---|---|---|---|---|
| P01 | Pointer Resolution | 🔴 | All | ✅ |
| P02 | Cross-file Symbol Resolution | 🔴 | G1, G2, G3 | ❓ |
| P03 | Inter-procedural DFG at Scale | 🟠 | G2 | ❓ |
| P04 | Address Stability Under Change | 🟠 | TACM | ❓ |
| P05 | Graph 4 Data Availability | 🟠 | G4 | ❓ |
| P06 | Token Budget Allocation | 🟡 | TACM | ✅ dissolved |
| P07 | Benchmark Fairness | 🟡 | Paper | ❓ |
| P08 | Formalising Starting Point Quality | 🟡 | Paper | ❓ |
| P09 | Query Intent Classifier Design | 🔴 | TACM Resolver | ❓ |
| P10 | Cross-graph Score Normalisation | 🟠 | TACM Resolver | ❓ |
| P11 | Payload Serialisation Format | 🟠 | TACM → LLM | ❓ |

## Open Questions

| ID | Title | Status |
|---|---|---|
| Q01 | Elasticsearch vs Redis + Qdrant | ✅ ES wins |
| Q02 | How to tune weight vector (w1-w4) | ❓ |
| Q03 | Primary benchmark dataset for bug localisation | ❓ |
| Q04 | tree-sitter vs Python ast for G2 | ✅ hybrid |
| Q05 | Git extraction without shell dependencies | ❓ |
| Q06 | Greedy vs knapsack for budget fill | ❓ |

---

## Priority Resolution Order

Tackle in this sequence — each unblocks the next:

```
P01 ✅ → P09 → P02 → P10 → P04 → P03 → P11 → P05 → Q02 → Q06 → P07 → P08 → Q03 → Q05
```

---

## Agent Instructions

Each problem has its own file at `problems/P##_title.md`.

Each file contains:
- Problem statement
- Why it matters
- Known approaches with pros/cons
- Current best thinking
- Specific questions for an agent to answer
- Acceptance criteria for "resolved"

Read the individual file before working on any problem.
Do not attempt to solve multiple problems in one session.
Update the Status column in this file when a problem is resolved.
