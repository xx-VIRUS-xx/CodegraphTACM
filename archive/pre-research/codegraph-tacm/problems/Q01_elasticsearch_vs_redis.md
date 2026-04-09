# Q01 — Elasticsearch vs Redis + Qdrant
**Status:** ✅ RESOLVED

## Decision
**Use Elasticsearch for both TACM address store and G3 semantic search.**

Final stack: **Elasticsearch + Kuzu** (2 services, not 4).

## Rationale
- Prabhat has deep ES expertise from Izoologic (50M+ darkweb records)
- ES 8.x native kNN replaces Qdrant
- ES exact key lookup replaces Redis (2–5ms vs 0.5ms — irrelevant at research scale)
- ES BM25 replaces rank_bm25 library
- Kuzu handles G1/G2 graph traversal (Cypher queries) — ES cannot replace a graph DB

## What ES Handles
- G3 semantic search (kNN on node embeddings)
- TACM address store (exact lookup by node ID)
- BM25 text search on signatures + docstrings
- Filtering by file, kind, token_cost, risk_score

## What Kuzu Handles
- Multi-hop graph traversal (MATCH queries)
- G1 structural relationships (CALLS, IMPORTS, INHERITS)
- G2 causal relationships (DATA_FLOWS_TO, CONDITIONALLY_EXECUTES)

## Closed. No further action needed.
