# Using TACM on Any Repository

A step-by-step guide to run TACM (Topology-Aware Context Manager) on your own repository for code retrieval, bug localization, or context-aware code search.

---

## Prerequisites

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.10+ | Runtime |
| Git | 2.x | Clone repos, checkout commits |
| Docker | 20+ | Neo4j container (v3 only) |
| tree-sitter | (bundled) | Multi-language parsing via crg |

### Install dependencies

```bash
# Clone the TACM repository
git clone <tacm-repo-url>
cd CodegraphTACM

# Create & activate virtual environment
python -m venv .venv

# Windows
.\.venv\Scripts\Activate.ps1

# Linux/macOS
source .venv/bin/activate

# Install core dependencies
pip install -r requirements.txt    # if available
pip install neo4j                  # for TACM v3

# Install code-review-graph (crg) — the parser that builds the code graph
pip install code-review-graph
```

---

## Quick Start (3 commands)

```bash
# 1. Clone your target repo
git clone https://github.com/USER/REPO.git

# 2. Build the code graph
python -c "
from code_review_graph.incremental import get_db_path, full_build
from code_review_graph.graph import GraphStore
from pathlib import Path

repo = Path('REPO')
store = GraphStore(get_db_path(repo))
full_build(repo, store)
store.close()
print('Graph built!')
"

# 3. Run TACM retrieval
python -c "
from tacm_v2.graph.builder import build_graph
from tacm_v2.selector.selector import select

graph = build_graph('REPO')
result = select(graph, 'your natural language query here', token_budget=4000)
print(result.context_text())
"
```

---

## Detailed Usage

### Step 1: Parse a Repository with crg

crg (code-review-graph) is the tree-sitter powered parser that extracts:
- **File** nodes — one per source file
- **Class** nodes — one per class/struct definition
- **Function** nodes — one per function/method
- **Test** nodes — detected test functions
- **Edges** — CALLS, CONTAINS, INHERITS, IMPORTS_FROM, TESTED_BY

```python
from pathlib import Path
from code_review_graph.graph import GraphStore
from code_review_graph.incremental import get_db_path, full_build

repo_path = Path("/path/to/your/repo")

# crg stores its graph in a SQLite database at .crg/graph.db inside the repo
db_path = get_db_path(repo_path)
store = GraphStore(db_path)

# full_build parses all source files and extracts nodes + edges
full_build(repo_path, store)

# Check what was parsed
nodes = store.get_nodes_by_kind(["Function"])
print(f"Found {len(nodes)} functions")

edges = store.get_all_edges()
print(f"Found {len(edges)} edges")

store.close()
```

**Supported languages:** Python, JavaScript/TypeScript, Java, Go, Rust, C/C++, Ruby, Swift, Kotlin

### Step 2: Build the TACM Layered Graph

The `GraphBuilder` transforms crg's flat graph into a weighted, 3-layer graph:

```python
from tacm_v2.graph.builder import build_graph

# One-line convenience function
graph = build_graph("/path/to/your/repo")

# What you get:
print(f"Nodes: {len(graph.nodes)}")
print(f"Edges: {len(graph.edges)}")
print(f"  Files:     {len(graph.nodes_at_layer(Layer.FILE))}")
print(f"  Classes:   {len(graph.nodes_at_layer(Layer.CLASS))}")
print(f"  Functions: {len(graph.nodes_at_layer(Layer.FUNCTION))}")
```

The builder automatically:
- Normalizes CALLS edge weights by call frequency
- Adds transitive INHERITS edges (grandparent at weight 0.5)
- Adds transitive IMPORTS_FROM edges
- Resolves short-name call targets (e.g., `"send"` → `module::Class::send`)
- Computes per-node fan-in/fan-out/degree signals

### Step 3: Query with TACM

#### Basic retrieval (fixed layer budgets)

```python
from tacm_v2.selector.selector import select

result = select(
    graph,
    query="authentication fails when session cookie expires",
    token_budget=4000,    # total context window tokens
)

# The context to inject into your LLM prompt
context = result.context_text()
print(f"Intent: {result.intent}")
print(f"Tokens used: {result.total_tokens}/{result.budget}")
print(f"Layers: {result.layer_counts}")
print(context)
```

#### Dynamic cross-layer selection

```python
from tacm_v2.selector.selector import select_dynamic

result = select_dynamic(
    graph,
    query="why does the parser crash on UTF-8 input?",
    token_budget=4000,
)
```

`select_dynamic` lets all nodes compete globally after seeding a minimal structure, avoiding budget waste on less relevant layers.

#### Override intent classification

```python
result = select(graph, query="...", token_budget=4000, intent="bug")
# Force BUG intent: 75% budget → functions, 20% → classes, 5% → files
```

Intents: `"bug"`, `"structure"`, `"explain"`

### Step 4: Use Context Providers (ready-made)

The `context_providers.py` module provides drop-in retrieval functions:

```python
from context_providers import (
    bm25_context,         # BM25-only baseline
    tacm_context,         # TACM v2 (fixed budgets)
    tacm_dynamic_context, # TACM v2 (cross-layer)
    tacm_l4_context,      # TACM + Layer 04 (variable context)
)

# All return a string ready for LLM injection
context = tacm_context(graph, query="your query", budget=4000)
```

---

## TACM v3: Neo4j Active Memory

For persistent memory across queries with full graph algorithm support.

### Setup Neo4j

```bash
# Start Neo4j with Graph Data Science plugin
docker-compose up -d

# Wait for container to be healthy
docker-compose ps
# Visit http://localhost:7474 to verify (neo4j / tacm_graph_2026)
```

### Use the Orchestrator

```python
from tacm_v2.neo4j_memory.orchestrator import ActiveMemoryOrchestrator

# Connect to Neo4j
orch = ActiveMemoryOrchestrator.connect()

# Ingest your repo (one-time)
from tacm_v2.graph.builder import build_graph
graph = build_graph("/path/to/your/repo")
orch.ingest_repo("my-project", graph)

# Start a session (memory persists within session)
session_id = orch.start_session("my-project")

# Query 1 — no memory yet, pure signal scoring
result = orch.retrieve(
    "why does the cache invalidation fail?",
    budget=4000,
)
print(result.context_text)
print(f"Communities covered: {result.communities_covered}")

# Agent finds the bug → write back to graph
orch.confirm_bug(
    ["myproject::cache::invalidate_entry"],
    description="Race condition in TTL check",
)

# Query 2 — memory signals now active
# Previously explored nodes get recency_boost
# Confirmed bug node gets hot_spot_boost
# Its unexplored neighbors get exploration_momentum
result2 = orch.retrieve(
    "how is the TTL computed for cache entries?",
    budget=4000,
)

# Agent rules out some functions
orch.rule_out(["myproject::cache::serialize", "myproject::cache::compress"])

# Query 3 — ruled-out nodes are penalized, momentum drives to new areas
result3 = orch.retrieve("what validates the cache key format?", budget=4000)

# End session
orch.end_session()
orch.close()
```

### Introspection

```python
# See what memory accumulated
history = orch.get_session_history()

# Historical bug hot spots across all sessions
hot_spots = orch.get_hot_spots(top_k=10)

# Explain why a specific function was selected
explanation = orch.explain_selection("myproject::cache::invalidate_entry")
# Returns: graph_signals (pagerank, betweenness, community),
#          memory_signals (recency, hot_spot, momentum),
#          findings (past bugs, fixes)

# Call chain between two functions
chain = orch.get_call_chain("myproject::api::handle_request",
                             "myproject::cache::invalidate_entry")

# Find structurally similar functions
similar = orch.get_similar_functions("myproject::cache::invalidate_entry")
```

---

## Benchmark Evaluation

To evaluate TACM on a benchmark dataset (BugsInPy / SWE-bench format):

```bash
# Retrieval-only, all conditions
python zero_cost_runner.py --retriever all --no-exec --python-only

# Single retriever
python zero_cost_runner.py --retriever tacm --no-exec

# Limit to first N instances
python zero_cost_runner.py --retriever tacm --no-exec --limit 10

# With diagnostic traces
python zero_cost_runner.py --retriever tacm --no-exec --trace
```

**Available retrievers:** `bm25`, `minilm`, `codesearch`, `hybrid`, `hybrid-cs`, `tacm`, `tacm-rerank`, `all`

### Benchmark JSON Format

To create your own benchmark, provide a JSON file with this structure:

```json
[
  {
    "id": 1,
    "repo": "owner/repo",
    "instance_id": "unique_id",
    "base_commit": "abc123...",
    "language": "Python",
    "query": "Description of the bug or task...",
    "patch": "diff --git a/... unified diff of the fix",
    "fail_to_pass": ["test::path::test_name"],
    "execution_instructions": {
      "clone": "git clone https://github.com/owner/repo.git",
      "checkout_buggy": "git checkout abc123",
      "run_failing_tests": ["test::path::test_name"]
    }
  }
]
```

```bash
python zero_cost_runner.py --dataset my_benchmark.json --retriever tacm --no-exec
```

### Metrics

| Metric | Description |
|--------|-------------|
| **Fn-Hit@K** | Is the ground-truth function in the top-K? (K=1,5,10) |
| **Fn-MRR** | Mean reciprocal rank of first correct function |
| **Ctx%** | Is the GT function in the final budget-constrained context? |
| **File-Hit@K** | Is the GT file in the top-K? (secondary) |

---

## Architecture at a Glance

```
Your Repo
   ↓
crg parse (tree-sitter)
   ↓
SQLite GraphStore (nodes + edges)
   ↓
GraphBuilder → LayeredGraph (FILE / CLASS / FUNCTION)
   ↓                              ↓ (v3 only)
TACM v2 Selector              Neo4j ingest
   ↓                              ↓
Intent classification         GDS algorithms
   ↓                          (PageRank, Louvain, betweenness)
Signal fusion scoring              ↓
(BM25 + fan_in/out +          Active memory
 complexity + test_cover)     (sessions, findings, patterns)
   ↓                              ↓
Greedy budget selection       Memory-augmented 10-signal scorer
   ↓                              ↓
Context string → LLM         Context string → LLM → feedback → Neo4j
```

---

## Tips

- **Token budget:** 4000 tokens is a good default. Increase to 6000–8000 for larger repos.
- **Intent override:** If the auto-classifier picks wrong, pass `intent="bug"` explicitly.
- **Test exclusion:** Tests are excluded by default (`exclude_tests=True`). Set to `False` if you need test functions in context.
- **Large repos:** crg parsing scales linearly. For repos with 10k+ files, expect 30–60s parse time.
- **Graph caching:** The crg SQLite DB persists at `.crg/graph.db` inside the repo. Subsequent runs reuse it unless files changed.
- **Neo4j memory:** Active memory is most valuable for multi-query workflows (debugging sessions, code review). For single-shot retrieval, v2 is sufficient.
