# 🚀 Graph + BM25 + Embedding Hybrid Retrieval System for Code

## 📌 Overview

This document describes a production-grade **code retrieval architecture** combining:

* Knowledge Graph (Neo4j)
* BM25 + Vector Search (Elasticsearch)
* Signal Fusion Ranking

This system is designed to outperform standalone embedding or keyword-based retrieval systems by leveraging **structure + semantics + signals**.

---

# 🧠 1. Knowledge Graph Design (Neo4j)

## 🔷 Node Types

```cypher
(:File {
  path,
  language,
  repo,
  last_modified
})

(:Class {
  name,
  file_path,
  docstring
})

(:Function {
  name,
  signature,
  file_path,
  docstring,
  start_line,
  end_line
})

(:Variable {
  name,
  type,
  scope
})
```

---

## 🔗 Relationships

```cypher
(:File)-[:CONTAINS]->(:Class)
(:File)-[:CONTAINS]->(:Function)

(:Class)-[:HAS_METHOD]->(:Function)
(:Class)-[:INHERITS]->(:Class)

(:Function)-[:CALLS]->(:Function)
(:Function)-[:USES]->(:Variable)
(:Function)-[:RETURNS]->(:Variable)

(:File)-[:IMPORTS]->(:File)
(:Function)-[:DEFINED_IN]->(:File)
```

---

## ⚡ Weighted Edges

```cypher
(:Function)-[:CALLS {weight: 0.8}]->(:Function)
(:Function)-[:USES {weight: 0.5}]->(:Variable)
```

---

## 📊 Precomputed Graph Signals

```cypher
SET f.call_count = size((f)-[:CALLS]->())
SET f.in_degree = size(()-[:CALLS]->(f))
SET f.pagerank = algo.pageRank(...)
```

---

# 🔎 2. Elasticsearch Index Design

## 📦 Mapping

```json
{
  "mappings": {
    "properties": {
      "node_id": { "type": "keyword" },
      "type": { "type": "keyword" },
      "name": { "type": "text" },
      "code": { "type": "text" },
      "docstring": { "type": "text" },
      "file_path": { "type": "keyword" },

      "embedding": {
        "type": "dense_vector",
        "dims": 768,
        "index": true,
        "similarity": "cosine"
      },

      "pagerank": { "type": "float" },
      "call_count": { "type": "integer" },
      "depth_level": { "type": "integer" }
    }
  }
}
```

---

## ⚡ Stage 1: BM25 Retrieval

```json
{
  "size": 100,
  "query": {
    "multi_match": {
      "query": "user authentication logic",
      "fields": ["name^3", "docstring^2", "code"]
    }
  }
}
```

---

## 🔁 Stage 2: Vector Reranking

```json
{
  "script_score": {
    "query": { "match_all": {} },
    "script": {
      "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
      "params": {
        "query_vector": [ ... ]
      }
    }
  }
}
```

---

# 🔁 3. Graph Expansion

```cypher
MATCH (f:Function)
WHERE f.node_id IN $top_ids

MATCH (f)-[r*1..2]-(neighbors)
RETURN neighbors, relationships(r)
LIMIT 200
```

* Limit traversal depth to **2 hops**
* Filter edge types if needed

---

# 🧬 4. Signal Fusion Ranking

## 🔢 Normalize Scores

```python
bm25_score = normalize(bm25)
embedding_score = normalize(cosine_sim)
pagerank_score = normalize(pagerank)
call_score = normalize(call_count)
```

---

## 🧮 Final Ranking Formula

```python
final_score =
    0.35 * bm25_score +
    0.30 * embedding_score +
    0.20 * pagerank_score +
    0.10 * call_score +
    0.05 * depth_boost
```

---

## 🎯 Depth Boost

```python
if type == "Function":
    depth_boost = 1.0
elif type == "Class":
    depth_boost = 0.7
else:
    depth_boost = 0.5
```

---

# 🔄 5. Query Pipeline

```
User Query
   ↓
BM25 (Elasticsearch) → top 100
   ↓
Graph Expansion (Neo4j)
   ↓
Merge candidates
   ↓
Embedding similarity (rerank)
   ↓
Signal fusion scoring
   ↓
Top K results
```

---

# ⚡ 6. Latency Optimization

* Run Elasticsearch + Neo4j in **parallel**
* Cache:

  * query embeddings
  * graph neighborhoods
* Limit candidate size (100–200)

**Target latency:** < 80 ms

---

# 📊 7. Expected Performance Gains

| Component        | Impact         |
| ---------------- | -------------- |
| Graph expansion  | +0.05–0.10 MRR |
| Hybrid retrieval | +0.05–0.15 MRR |
| Reranking        | +0.10–0.20 MRR |

### 🎯 Target Metrics:

* MRR: **0.45–0.60**
* Significant H@1 improvement

---

# 🏁 Final Summary

This system combines:

* Structural understanding (graph)
* Exact matching (BM25)
* Semantic understanding (embeddings)
* Intelligent ranking (signal fusion)

👉 Result: **State-of-the-art code retrieval system**

---

# 🚀 Next Steps

* Build ingestion pipeline (code → graph + ES)
* Add query classification (intent-aware retrieval)
* Implement evaluation loop (optimize MRR / H@1)

---
