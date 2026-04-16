# STACK.md — Technology Choices

## Storage

| Component | Technology | Why |
|---|---|---|
| G1 + G2 graph traversal | **Kuzu** (embedded graph DB) | No-ops, embedded, Cypher queries |
| G3 semantic search + TACM store | **Elasticsearch 8.x** | Native kNN, BM25, exact lookup, Prabhat's expertise from Izoologic |
| G4 signals | Elasticsearch | Same instance as TACM store |

## Processing

| Component | Technology | Why |
|---|---|---|
| G1 AST parsing | Python `ast` module | Already built in ast_parser.py |
| G2 CFG/DFG | Python `ast` module | Same visitor pattern as G1 |
| G3 embeddings | `sentence-transformers` BAAI/bge-small-en-v1.5 | Fast, 384 dims, good quality |
| G4 Git signals | `GitPython` | Pure Python, no shell deps |
| Cross-file resolution | import maps (v1), `jedi` (v2) | See P02 |

## Query Pipeline

| Component | Technology | Why |
|---|---|---|
| Intent classification | Rule-based keywords (v1) | No deps, fast, interpretable |
| Score normalisation | Rank-based RRF | Scale-invariant, battle-tested in hybrid retrieval |
| Budget fill | Greedy (v1), Knapsack DP if gap > 5% | See Q06 |
| Payload serialisation | XML hybrid format | See P11 |

## Minimal Service Dependencies

```
Prototype stack:
  Python 3.10+
  kuzu                   # embedded graph DB — no server
  elasticsearch          # local Docker or Elastic Cloud
  sentence-transformers  # for G3 embeddings
  gitpython              # for G4 Git signals
  jedi                   # v2 only, for cross-file resolution
```

## What We Explicitly Decided Not To Use

| Tool | Replaced by | Reason |
|---|---|---|
| Redis | Elasticsearch | ES handles exact lookup + kNN in one service |
| Qdrant | Elasticsearch 8.x kNN | Same as above |
| Neo4j | Kuzu | Kuzu is embedded — zero operational overhead |
| LangChain | Direct implementation | Too much abstraction over what we're measuring |
| Fine-tuned models | Any LLM via API | Zero fine-tuning is a core design constraint |
| rank_bm25 library | Elasticsearch BM25 | ES handles this natively |
