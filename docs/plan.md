# 🚀 TACM v3 — Neo4j Active Memory Code Retrieval System

## 📌 Overview

This document describes the **TACM v3** architecture — a Neo4j-backed
active memory system for code retrieval that extends the proven TACM v2
pipeline with:

* **Neo4j Knowledge Graph** — persistent, server-side graph store
* **Real-time GDS algorithms** — PageRank, Louvain, betweenness centrality
* **Persistent cross-query memory** — exploration history, relevance decay
* **Dynamic knowledge graph updates** — agent writes findings back
* **Intent-aware signal fusion** — 10-signal weighted scoring

### Evolution: v2 → v3

TACM v2 used an in-memory `LayeredGraph` backed by crg SQLite. It achieved:
- thefuck MRR: 0.451 (TACM), 0.563 (TACM-rerank)
- scrapy MRR: 0.356–0.370

TACM v3 replaces the in-memory graph with Neo4j and adds active memory —
the system learns from the agent's exploration history across queries.

---

# 🧠 1. Knowledge Graph Design (Neo4j)

## 🔷 Code Nodes (3-layer model)

```cypher
(:File {
  node_id, name, file_path, language, repo,
  in_degree, out_degree, token_cost,
  // Active memory signals (accumulated):
  exploration_count, bug_count, last_explored, last_bug
})

(:Class {
  node_id, name, file_path, parent_id, language, repo,
  in_degree, out_degree, call_fan_in, call_fan_out,
  is_test, token_cost,
  exploration_count, bug_count, last_explored
})

(:Function {
  node_id, name, file_path, parent_id, language, repo,
  line_start, line_end,
  in_degree, out_degree, call_fan_in, call_fan_out,
  is_test, token_cost,
  // GDS-computed signals (server-side):
  pagerank, betweenness, community_id,
  // Active memory signals:
  exploration_count, bug_count, ruled_out_count,
  patch_count, last_explored, last_bug
})
```

## 🔗 Code Relationships

```cypher
(:Function)-[:CALLS {weight, raw_count}]->(:Function)
(:Class)-[:INHERITS {weight}]->(:Class)         // 1.0 direct, 0.5 transitive
(:File)-[:IMPORTS_FROM {weight}]->(:File)        // 1.0 direct, 0.5 transitive
(:File)-[:CONTAINS]->(:Class|:Function)          // always 1.0
(:Function)-[:TESTED_BY]->(:Function)            // always 1.0
```

## 🧠 Active Memory Nodes

```cypher
(:Session {session_id, repo, started_at, ended_at, query_count})
  -[:HAS_QUERY]->
(:QueryEvent {query_id, query_text, intent, timestamp})
  -[:EXPLORED]->(:Function)         // agent looked at this
  -[:CONFIRMED_BUG]->(:Function)    // confirmed defect
  -[:RULED_OUT]->(:Function)        // eliminated
  -[:PATCH_TARGET]->(:Function)     // fix location

(:Finding {finding_id, type, description, confidence, timestamp})
  -[:ABOUT]->(:Function)            // code node this is about
  -[:CAUSED_BY]->(:Finding)         // causal chain
  -[:RELATED_TO]->(:Finding)        // lateral associations
```

Finding types: `BUG`, `ROOT_CAUSE`, `SIDE_EFFECT`, `FIX`, `PATTERN`

---

# 🔎 2. BM25 Retrieval (Pure Python)

BM25 runs locally (no Elasticsearch) with cascading query expansion:

```python
# Three query variants, take max per node:
1. Raw query
2. camelCase/snake_case split ("GetNewCommand" → "get new command")
3. Graph-expanded (class name → member function names)
```

Full-text index on Neo4j (`code_fulltext`) for future hybrid search.

---

# ⚡ 3. Real-time Graph Algorithms (Neo4j GDS)

All computed server-side via GDS library:

```cypher
// PageRank — replaces pure-Python power iteration
CALL gds.pageRank.write('calls_graph', {
  dampingFactor: 0.85,
  maxIterations: 50,
  relationshipWeightProperty: 'weight',
  writeProperty: 'pagerank'
})

// Louvain communities — detects functional module clusters
CALL gds.louvain.write('calls_graph', {
  relationshipWeightProperty: 'weight',
  writeProperty: 'community_id'
})

// Betweenness centrality — identifies bridge functions
CALL gds.betweenness.write('calls_graph', {
  writeProperty: 'betweenness'
})
```

Additional capabilities:
- **Shortest call path** between any two functions
- **K-hop neighborhood expansion** (server-side, ranked by connection strength)
- **Jaccard similarity** on call neighborhoods (find structurally similar functions)

---

# 🧬 4. Memory-Augmented Signal Fusion

## 🔢 10-Signal Scoring Vector

```python
signals = [
    "bm25",           # cascading BM25 relevance
    "fan_in",         # weighted call in-degree (ambiguity-discounted)
    "fan_out",        # call out-degree (orchestrators)
    "complexity",     # token_cost normalized
    "test_cover",     # has TESTED_BY edge?
    "pagerank",       # GDS PageRank (server-side)
    "betweenness",    # GDS betweenness centrality
    "recency_boost",  # exponential decay from last exploration
    "hot_spot_boost", # log-scaled historical bug count
    "momentum",       # exploration gap in hot neighborhoods
]
```

## 🧮 Intent-Aware Weight Vectors

```
                 bm25  fan_in fan_out cmplx  test   PR    btwn  recen  hot   mom
BUG:            0.35   0.15   0.05   0.10   0.00  0.10  0.05  0.08  0.07  0.05
STRUCTURE:      0.40   0.05   0.15   0.00   0.05  0.10  0.10  0.05  0.03  0.07
EXPLAIN:        0.30   0.10   0.20   0.03   0.02  0.10  0.10  0.05  0.03  0.07
```

## Memory Signal Details

```python
# Recency: exponential decay from last exploration
recency = 2 ** (-hours_ago / half_life)   # half_life = 2 hours

# Hot spot: log-scaled bug count
hot_spot = min(1.0, log2(1 + bug_count) / 3.0)

# Ruled-out penalty: grows with repeated rule-outs
penalty = min(0.3, 0.1 * ruled_out_count)

# Exploration momentum: unexplored node surrounded by explored neighbors
momentum = min(0.5, 0.1 * explored_neighbor_count)
```

---

# 🔄 5. Query Pipeline

```
User Query
   ↓
Intent Classification (BUG / STRUCTURE / EXPLAIN)
   ↓
Load memory signals from Neo4j  ←─── cross-query history
   ↓
BM25 cascading (3 variants) + GDS graph signals (cached)
   ↓
10-signal intent-weighted fusion scoring
   ↓
Community-diversity greedy selection
   ↓
Record query + exploration → Neo4j memory  ───→ persisted
   ↓
Selected context → LLM
   ↓
Agent feedback (confirm_bug / rule_out / mark_fix)  ───→ Neo4j
```

---

# 🧠 6. Active Memory Lifecycle

```python
# Session start
orch = ActiveMemoryOrchestrator.connect()
orch.ingest_repo("thefuck", graph)
session_id = orch.start_session("thefuck")

# Query 1: memory is empty, pure signal scoring 
ctx1 = orch.retrieve("fish shell crash on alias resolution", budget=4000)

# Agent explores, finds the bug
orch.confirm_bug(["thefuck::shells::fish::get_aliases"],
                 description="missing encoding param")

# Query 2: memory signals now active
#   - get_aliases has recency_boost (just explored)
#   - get_aliases has hot_spot_boost (confirmed bug)
#   - neighbors get exploration_momentum (gap filling)
#   - previously ruled-out nodes get penalty
ctx2 = orch.retrieve("how is the alias cache structured?", budget=4000)
```

---

# ⚡ 7. Performance Targets

| Component           | Expected Impact   |
| ------------------- | ----------------- |
| GDS PageRank        | +0.02–0.05 MRR    |
| Community diversity | +0.01–0.03 MRR    |
| Betweenness signal  | +0.01–0.03 MRR    |
| Active memory       | +0.05–0.15 MRR    |
| Cross-query memory  | +0.03–0.08 MRR    |

### 🎯 Targets:

* thefuck MRR: **0.55–0.70** (from 0.451 baseline)
* scrapy MRR: **0.40–0.55** (from 0.356 baseline)
* Multi-query session MRR: **0.60+** (memory compounds)

---

# 🏗 8. Infrastructure

```yaml
# docker-compose.yml
services:
  neo4j:
    image: neo4j:5.26-community
    ports: ["7474:7474", "7687:7687"]
    environment:
      NEO4J_PLUGINS: '["graph-data-science"]'
    volumes: [neo4j_data:/data]
```

Dependencies: `neo4j` Python driver, Neo4j GDS plugin.

---

# 🏁 9. Module Structure

```
tacm_v2/neo4j_memory/
├── __init__.py          # package docstring
├── store.py             # Neo4j graph store (ingest, export, schema)
├── algorithms.py        # GDS algorithms (PageRank, Louvain, betweenness, paths)
├── memory.py            # Cross-query active memory (sessions, exploration, signals)
├── findings.py          # Dynamic knowledge graph updates (bugs, fixes, patterns)
├── scorer.py            # Memory-augmented 10-signal scorer
└── orchestrator.py      # End-to-end pipeline (retrieve, feedback, introspection)
```

---

# 🚀 10. Next Steps

* [ ] Run `docker-compose up -d` and verify Neo4j + GDS are operational
* [ ] Ingest thefuck + scrapy graphs into Neo4j
* [ ] Run Experiment 05: TACM-v3 (memory-augmented) vs v2 vs baselines
* [ ] Ablate memory signals (which dimensions help most?)
* [ ] Multi-query session evaluation (bug localization across 3+ queries)
* [ ] Evaluate cross-repo transfer (do findings from thefuck help scrapy?)

---
