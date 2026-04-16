# TACM_DEEP.md — Two-Phase Resolution + Reasoning Traces

## The Core Insight

Every existing system resolves queries in one shot:
```
Query → fetch text → insert text → LLM
```

This limits candidate evaluation to what you can afford to load.

Two-phase resolution separates *scoring* from *loading*:
```
Phase 1: Query → score 1000 candidates cheaply (node IDs only)
Phase 2: Load text for the best 10-20 only
```

The "pointer" is architecturally real in Phase 1 — node IDs exist as stable internal addresses between phases. The LLM never sees them.

---

## Phase 1 — Skeleton Fetch

### What Happens
1. Embed the query with sentence-transformers
2. Run ES kNN search → top-N nodes by semantic similarity (G3 signal)
3. Run Kuzu K-hop traversal from anchor nodes → structural neighbours (G1 signal)
4. Look up G2 causal score for each candidate (pre-computed at index time)
5. Look up G4 risk score for each candidate (pre-computed at index time)

### Output
List of `(node_id, g1_score, g2_score, g3_score, g4_score)` — no text content

### Cost
- ~5 tokens per node × 500 candidates = 2,500 tokens **internal only**
- These tokens never reach the LLM
- Time: 20–50ms (ES kNN + Kuzu traversal)

---

## Scoring

```python
def score(node, weights, g1, g2, g3, g4):
    # Apply RRF normalisation to each graph's scores first
    w1, w2, w3, w4 = weights
    combined = w1*g1 + w2*g2 + w3*g3 + w4*g4
    value = combined / node.token_cost
    return value

# Sort all candidates by value, descending
ranked = sorted(candidates, key=lambda c: score(c, ...), reverse=True)
```

---

## Phase 2 — Payload Fetch

### What Happens
1. Take top-K candidates by value score
2. Greedily select until token budget exhausted
3. For each selected node: ES exact lookup by node_id → full payload text
4. Serialise selected payloads to structured XML/pseudo-code

### Output
Final prompt payload — the only thing the LLM sees

### Cost
- ~50 tokens per node × 12 selected = ~600 tokens in a 800-token budget
- Time: 12 × ES GET = ~10–20ms

---

## Why This Beats Single-Phase

### Single-phase (existing systems)
```
Budget: 800 tokens
Fetch: top-10 chunks × 80 tokens = 800 tokens
Candidates evaluated: 10
```

### Two-phase (TACM)
```
Budget: 800 tokens
Phase 1: score 500 candidates × 0 LLM tokens = 500 evaluated
Phase 2: fetch best 12 nodes × ~66 tokens = 800 tokens
Candidates evaluated: 500
Better candidates surface because the scoring pool is 50x larger
```

---

## Reasoning Traces (V2 — Not Built Yet)

### Concept
After each resolved query, store the retrieval pattern as an addressable trace:

```python
@dataclass
class ReasoningTrace:
    query_hash:     str            # hash of query embedding
    intent:         str
    weights_used:   tuple[float,float,float,float]
    hot_node_ids:   list[str]      # top-10 nodes that were selected
    answer_quality: float | None   # if ground truth available
    codebase_id:    str            # which repo this was for
    timestamp:      datetime
```

### How Future Queries Use Traces
1. Embed new query
2. Find similar past queries by embedding similarity
3. If similar trace exists: pre-boost scores of that trace's hot_node_ids
4. Effectively: "last time someone asked something similar, these nodes were the answer"

### Why This Is Novel
No existing retrieval system accumulates query-resolution patterns.
Every query starts from scratch against the raw index.
Traces make the system get smarter about a specific codebase over time.

### Status
Not in scope for v1. Design when Phase 1 benchmark shows promising results.

---

## What the LLM Never Sees

```
Internal only (never in LLM prompt):
  - Node IDs / addresses ("fn:parser.py::Parser.parse")
  - Graph scores (g1=0.45, g2=0.82, ...)
  - Weight vectors (w1=0.15, w2=0.40, ...)
  - Phase 1 skeleton output
  - TACM internal data structures
  - Reasoning traces
```

## What the LLM Always Sees

```xml
<context codebase="myrepo" budget_used="387/800">
  <node kind="function" file="parser.py" risk="high">
    def parse(self, text: str) -> List[Token]:
      """Parse input text into a list of Token objects."""
      # raises: UnicodeDecodeError, ParseError
      # calls: tokenize, normalize_string
  </node>
  <node kind="function" file="tokenizer.py" risk="low">
    def tokenize(text: str) -> List[str]:
      """Split text into raw string tokens."""
  </node>
</context>
<query>Why does parse() fail on Unicode input?</query>
```

Natural text. Code stubs. Source attribution. Nothing unusual for any LLM.
