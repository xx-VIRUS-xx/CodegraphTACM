# DECISIONS.md — Architecture Decisions

All six architecture decisions. Treat these as locked unless a specific problem forces a revisit.

## D1 — Deployment Unit: Python Library
`pip install codegraph-tacm`
Serves all three audiences. Foundation for future service. Open-source GitHub repo.

## D2 — Indexing Trigger: Manual → CI
`codegraph index ./repo` for prototype.
Design schema for incremental on-commit updates (V2). Do not build CI integration before benchmark.

## D3 — Query Interface: Natural Language + RAG Drop-in
Natural language as primary interface.
LlamaIndex-compatible retriever interface as adoption layer.
Agent tool-call interface as Phase 2 (after benchmark).

## D4 — Cross-file Scope: Full Repo, Honest DFG
Index full repository (required for SWE-bench).
G2 explicitly scoped to module-cluster level DFG — state this clearly in the paper.

## D5 — Language Support: G1 Any, G2-G4 Python
tree-sitter for G1 structural parsing in any language.
Python ast for G2 (CFG/DFG), G3, G4 — Python only, maximum depth.

## D6 — Primary Benchmark: Bug Localisation + SWE-bench
Bug localisation (BugsInPy) as primary novel result.
SWE-bench Lite as secondary credibility comparison.
Drop code completion as a benchmark task.
