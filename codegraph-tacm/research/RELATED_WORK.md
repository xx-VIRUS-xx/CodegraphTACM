# RELATED_WORK.md — Existing Systems + Differentiation

## Systems to Beat on Benchmark

### CodexGraph (NAACL 2025)
- **Paper:** arxiv.org/abs/2408.03910
- **What it does:** Extracts code graph from AST, stores in Neo4j, uses dual-agent LLM to write Cypher queries for retrieval
- **Graph layers:** 1 — AST only (CONTAINS, HAS_METHOD, HAS_FIELD, INHERITS, USES, CALLS)
- **Retrieval:** LLM writes Cypher → Neo4j returns text → LLM inserts text into context
- **Token approach:** Inserts raw retrieved code text
- **Benchmarks:** CrossCodeEval, SWE-bench, EvoCodeBench
- **Key weakness:** LLM must write correct Cypher queries — fails with weaker models. No data flow. No historical signals. No query-adaptive scoring.
- **Our advantage:** Four graphs vs one. Query-adaptive weights. Two-phase resolution. No Cypher generation required.

### Code Graph Model / CGM (NeurIPS 2025)
- **Repo:** github.com/codefuse-ai/CodeFuse-CGM
- **What it does:** Builds repository-level code graph, fine-tunes LLM with LoRA to jointly model structural + semantic information
- **Graph layers:** 1 — AST with structural + semantic annotations
- **Retrieval:** R4 chain (Rewriter → Retriever → Reranker → Reader)
- **Token approach:** Retrieved subgraph serialised to text, fed to fine-tuned model
- **Key weakness:** Requires fine-tuning — cannot use arbitrary LLM. Single graph. No historical signals.
- **Our advantage:** Zero fine-tuning required. Four graphs. Historical risk signals. Works with any LLM.

### GraphCoder (ASE 2024)
- **What it does:** Code context graph for repository-level completion via coarse-to-fine retrieval
- **Graph layers:** 1 — Code context graph (structural)
- **Retrieval:** Coarse retrieval → fine-grained re-ranking
- **Key weakness:** Completion task only. No bug localisation. No historical signals. Single graph.
- **Our advantage:** General-purpose retrieval across task types. Four graphs. Bug localisation primary task.

### CodeRAG (2025)
- **What it does:** Bigraph-based RAG — retrieves API calls, similar code, indirectly related code
- **Graph layers:** 2 — dependency bigraph + semantic similarity
- **Key weakness:** No causal (CFG/DFG) layer. No historical layer. No query-adaptive weights.
- **Our advantage:** CFG+DFG causal layer. Historical risk signals. Query-adaptive scoring.

### LlamaIndex CodeSplitter
- **What it does:** Code-aware chunking for standard RAG pipelines
- **Graph layers:** 0 — no graph, just smarter chunking
- **Key weakness:** No structural awareness. No cross-file relationships. Chunking artifacts.
- **Our advantage:** Everything.

---

## Differentiation Table

| Feature | CodexGraph | CGM | GraphCoder | CodeRAG | **Ours** |
|---|---|---|---|---|---|
| AST graph (G1) | ✓ | ✓ | ✓ | ✓ | ✓ |
| CFG/DFG graph (G2) | ✗ | ✗ | ✗ | Partial | ✓ |
| Semantic graph (G3) | ✗ | Partial | ✗ | ✓ | ✓ |
| Historical graph (G4) | ✗ | ✗ | ✗ | ✗ | ✓ |
| Query-adaptive weights | ✗ | ✗ | ✗ | ✗ | ✓ |
| Two-phase resolution | ✗ | ✗ | ✗ | ✗ | ✓ |
| Zero fine-tuning | ✓ | ✗ | ✓ | ✓ | ✓ |
| Token budget control | ✗ | ✗ | ✗ | ✗ | ✓ |
| Bug localisation | ✗ | ✗ | ✗ | ✗ | ✓ (primary) |
| Multi-language | ✗ | ✗ | ✗ | ✗ | G1 only |

---

## Benchmarks Used by Prior Work

| Benchmark | What it tests | Used by | Our plan |
|---|---|---|---|
| SWE-bench | GitHub issue → code fix | CodexGraph, CGM | Secondary (credibility) |
| SWE-bench Lite | 300-task subset | Most systems | Secondary |
| CrossCodeEval | Cross-file code completion | CodexGraph | No |
| EvoCodeBench | Code generation | CodexGraph | No |
| BugsInPy | Python bug localisation | None | **Primary** |
| Custom 50-task | Real GitHub issues | Our baseline | Yes |

---

## Agent Task

If you are an agent working on this file:
- Search arxiv for any papers published after March 2026 that use code graphs + LLMs
- Check if any new system has introduced query-adaptive graph weighting
- Check if any system has introduced two-phase skeleton/payload resolution
- Update the differentiation table if new systems found
- Flag any system that claims to beat CodexGraph on SWE-bench
