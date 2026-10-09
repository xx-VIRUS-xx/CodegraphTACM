# DATA_MODELS.md — Canonical Schemas

## CGINode

```python
from dataclasses import dataclass, field
from enum import Enum

class NodeKind(str, Enum):
    FUNCTION  = "fn"
    CLASS     = "cls"
    MODULE    = "mod"
    VARIABLE  = "var"
    CONSTANT  = "const"

@dataclass
class CGINode:
    # Identity
    id:           str          # "fn:parser.py::Parser.parse"
    kind:         NodeKind
    name:         str
    qualified:    str          # "mymodule.Parser.parse"

    # Code content
    signature:    str          # "def parse(text: str) -> List[Token]:"
    docstring:    str          # first line of docstring only
    full_doc:     str          # complete docstring
    file:         str          # relative path from repo root
    line_start:   int
    line_end:     int

    # Structural metadata
    is_async:     bool = False
    is_private:   bool = False
    decorators:   list[str] = field(default_factory=list)
    return_type:  str = ""
    args:         list[str] = field(default_factory=list)
    arg_types:    dict[str, str] = field(default_factory=dict)
    raises:       list[str] = field(default_factory=list)

    # Token cost
    token_cost:   int = 0      # tokens if full payload serialised

    # G3 signal — added after embedding pass
    embedding:    list[float] | None = None

    # G4 signals — added after Git analysis pass
    commit_freq:  int   = 0    # number of commits touching this node
    churn_rate:   float = 0.0  # lines added+deleted per month (rolling 6mo)
    last_modified:int   = 0    # days since last commit
    author_count: int   = 0    # distinct Git authors
    risk_score:   float = 0.0  # composite G4 signal (normalised 0-1)
```

## CGIEdge

```python
class EdgeKind(str, Enum):
    # G1 — Syntactic edges (from AST)
    CALLS         = "calls"
    IMPORTS       = "imports"
    INHERITS      = "inherits"
    HAS_METHOD    = "has_method"
    DEFINED_IN    = "defined_in"
    DECORATES     = "decorates"
    RETURNS_TYPE  = "returns_type"
    RAISES        = "raises"

    # G2 — Causal edges (from CFG/DFG)
    DATA_FLOWS_TO          = "data_flows_to"
    CONDITIONALLY_EXECUTES = "conditionally_executes"
    RAISES_ON              = "raises_on"
    ASSIGNS_TO             = "assigns_to"
    PASSES_TO              = "passes_to"

@dataclass
class CGIEdge:
    src:     str       # source node id
    dst:     str       # destination node id
    kind:    EdgeKind
    weight:  float     # call frequency or signal strength
    lineno:  int = 0
    context: str = ""  # brief human-readable description
```

## TACMAddress

```python
@dataclass
class TACMAddress:
    address:    str      # node id — internal pointer
    payload:    str      # resolved text for LLM consumption
    token_cost: int

    # Per-graph scores (populated by resolver in Phase 1)
    g1_score:   float = 0.0
    g2_score:   float = 0.0
    g3_score:   float = 0.0
    g4_score:   float = 0.0

    # Computed by resolver
    combined_score: float = 0.0
    value:          float = 0.0   # combined_score / token_cost
```

## QueryResult

```python
@dataclass
class QueryResult:
    query:          str
    intent:         str                           # classified intent class
    weights:        tuple[float,float,float,float] # (w1,w2,w3,w4)
    selected_nodes: list[TACMAddress]
    total_tokens:   int
    budget:         int
    payload:        str                           # final serialised prompt for LLM
    phase1_ms:      float                         # skeleton fetch time
    phase2_ms:      float                         # payload fetch time
    candidates_scored: int                        # nodes evaluated in Phase 1
```

## Elasticsearch Index Schema (TACM Store)

```json
{
  "mappings": {
    "properties": {
      "id":           { "type": "keyword" },
      "kind":         { "type": "keyword" },
      "name":         { "type": "keyword" },
      "qualified":    { "type": "keyword" },
      "signature":    { "type": "text" },
      "docstring":    { "type": "text" },
      "file":         { "type": "keyword" },
      "token_cost":   { "type": "integer" },
      "risk_score":   { "type": "float" },
      "commit_freq":  { "type": "integer" },
      "embedding":    {
        "type": "dense_vector",
        "dims": 384,
        "index": true,
        "similarity": "cosine"
      },
      "payload":      { "type": "text", "index": false }
    }
  }
}
```

## Kuzu Graph Schema

```cypher
// Node tables
CREATE NODE TABLE FUNCTION(
    id STRING PRIMARY KEY,
    name STRING,
    file STRING,
    line_start INT64,
    line_end INT64,
    token_cost INT64,
    risk_score DOUBLE
);

CREATE NODE TABLE CLASS(id STRING PRIMARY KEY, name STRING, file STRING);
CREATE NODE TABLE MODULE(id STRING PRIMARY KEY, name STRING, file STRING);

// Edge tables (G1)
CREATE REL TABLE CALLS(FROM FUNCTION TO FUNCTION, weight DOUBLE);
CREATE REL TABLE IMPORTS(FROM MODULE TO MODULE);
CREATE REL TABLE INHERITS(FROM CLASS TO CLASS);
CREATE REL TABLE HAS_METHOD(FROM CLASS TO FUNCTION);

// Edge tables (G2)
CREATE REL TABLE DATA_FLOWS_TO(FROM FUNCTION TO FUNCTION, context STRING);
CREATE REL TABLE RAISES_ON(FROM FUNCTION TO FUNCTION, exception STRING);
```
