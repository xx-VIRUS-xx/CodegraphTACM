"""model.py — Core data model for the TACM v2 multi-layer weighted graph.

Three abstraction layers, each a complete graph:

    Layer 0 — File      (architectural context)
    Layer 1 — Class     (structural context)
    Layer 2 — Function  (behavioral context)

Each layer has nodes and weighted edges. Weights are dynamic — computed
from what the code actually does (call frequency, inheritance distance,
import depth) not assigned arbitrarily.

Cross-layer edges connect the hierarchy:
    File  --[CONTAINS]--> Class      weight = 1.0
    File  --[CONTAINS]--> Function   weight = 1.0 (top-level functions)
    Class --[CONTAINS]--> Function   weight = 1.0

Within-layer edges carry meaning:
    Function --[CALLS]-----------> Function   weight = call_frequency / max_freq (normalised)
    Class    --[INHERITS]--------> Class      weight = 1.0 direct, 0.5 transitive
    File     --[IMPORTS_FROM]----> File       weight = 1.0 direct, 0.5 transitive
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


# ---------------------------------------------------------------------------
# Layer enum — every node knows which abstraction level it lives at
# ---------------------------------------------------------------------------

class Layer(int, Enum):
    FILE     = 0   # coarsest — one node per source file
    CLASS    = 1   # mid — one node per class definition
    FUNCTION = 2   # finest — one node per function/method


# ---------------------------------------------------------------------------
# Token cost estimates per layer
# These are used by the selector to allocate budget across layers.
# A File node serialises as its path + import list + contained class/fn names.
# A Class node serialises as its signature + method signatures.
# A Function node serialises as its full source body.
# ---------------------------------------------------------------------------

LAYER_TOKEN_ESTIMATES = {
    Layer.FILE:     25,    # "file requests/auth.py — imports: [hashlib] — contains: [HTTPDigestAuth]"
    Layer.CLASS:   60,    # "class HTTPDigestAuth(AuthBase) — methods: [__init__, __call__, handle_401]"
    Layer.FUNCTION: 150,  # full body, median function in psf/requests
}


# ---------------------------------------------------------------------------
# Node
# ---------------------------------------------------------------------------

@dataclass
class LNode:
    """A node in the layered graph.

    Wraps a crg GraphNode, adds layer identity and pre-computed signals
    used by the selector. Immutable after construction.
    """
    # Identity
    node_id:        str          # crg qualified_name — stable unique key
    layer:          Layer
    name:           str          # unqualified name
    file_path:      str
    line_start:     int
    line_end:       int

    # Containment — which nodes own this one (populated by GraphBuilder)
    parent_id:      Optional[str] = None   # direct container's node_id

    # Pre-computed signals (populated by GraphBuilder)
    in_degree:      int   = 0    # number of edges pointing INTO this node
    out_degree:     int   = 0    # number of edges pointing OUT of this node
    call_fan_in:    int   = 0    # how many distinct functions call this one
    call_fan_out:   int   = 0    # how many distinct functions this one calls
    is_test:        bool  = False

    # Token cost — actual measured from source, not estimate
    token_cost:     int   = 0

    @property
    def total_degree(self) -> int:
        return self.in_degree + self.out_degree

    @property
    def layer_name(self) -> str:
        return self.layer.name.lower()


# ---------------------------------------------------------------------------
# Edge
# ---------------------------------------------------------------------------

class EdgeKind(str, Enum):
    # Within-layer
    CALLS        = "CALLS"          # Function → Function
    INHERITS     = "INHERITS"       # Class → Class
    IMPORTS_FROM = "IMPORTS_FROM"   # File → File

    # Cross-layer (containment)
    CONTAINS     = "CONTAINS"       # File→Class, File→Function, Class→Function

    # Cross-layer (testing)
    TESTED_BY    = "TESTED_BY"      # Function ← Test


@dataclass
class LEdge:
    """A weighted directed edge in the layered graph.

    Weight semantics by edge kind:

    CALLS:        normalised call frequency [0, 1].
                  raw = count of (src, tgt) duplicate edges in crg.
                  normalised = raw / max_calls_in_graph.
                  A function that calls another 10× gets weight 1.0 if 10
                  is the global max; a single call gets weight 0.1.

    INHERITS:     inheritance distance.
                  1.0 = direct parent.
                  0.5 = grandparent (added during transitive closure).

    IMPORTS_FROM: import depth.
                  1.0 = directly imported.
                  0.5 = transitively imported (added during closure).

    CONTAINS:     always 1.0 — containment is binary.

    TESTED_BY:    always 1.0 — coverage is binary at this level.
    """
    source_id:  str
    target_id:  str
    kind:       EdgeKind
    weight:     float          # [0, 1] — see semantics above
    raw_count:  int   = 1      # raw crg edge count before normalisation


# ---------------------------------------------------------------------------
# The layered graph — what GraphBuilder produces
# ---------------------------------------------------------------------------

@dataclass
class LayeredGraph:
    """The full multi-layer weighted graph for one repository.

    Nodes and edges are stored in flat dicts keyed by node_id for O(1) lookup.
    Adjacency is stored separately for fast traversal.
    """
    # All nodes across all layers
    nodes: dict[str, LNode] = field(default_factory=dict)

    # All edges
    edges: list[LEdge] = field(default_factory=list)

    # Adjacency index — built once after all edges are added
    # out_adj[node_id] = list of LEdge leaving that node
    # in_adj[node_id]  = list of LEdge entering that node
    out_adj: dict[str, list[LEdge]] = field(default_factory=dict)
    in_adj:  dict[str, list[LEdge]] = field(default_factory=dict)

    def add_node(self, node: LNode) -> None:
        self.nodes[node.node_id] = node

    def add_edge(self, edge: LEdge) -> None:
        self.edges.append(edge)
        self.out_adj.setdefault(edge.source_id, []).append(edge)
        self.in_adj.setdefault(edge.target_id, []).append(edge)

    def nodes_at_layer(self, layer: Layer) -> list[LNode]:
        return [n for n in self.nodes.values() if n.layer == layer]

    def neighbors_out(self, node_id: str, kind: EdgeKind | None = None) -> list[LNode]:
        """Nodes this node points to, optionally filtered by edge kind."""
        edges = self.out_adj.get(node_id, [])
        if kind is not None:
            edges = [e for e in edges if e.kind == kind]
        return [self.nodes[e.target_id] for e in edges if e.target_id in self.nodes]

    def neighbors_in(self, node_id: str, kind: EdgeKind | None = None) -> list[LNode]:
        """Nodes pointing to this node, optionally filtered by edge kind."""
        edges = self.in_adj.get(node_id, [])
        if kind is not None:
            edges = [e for e in edges if e.kind == kind]
        return [self.nodes[e.source_id] for e in edges if e.source_id in self.nodes]

    def get_edge(self, source_id: str, target_id: str, kind: EdgeKind | None = None) -> LEdge | None:
        for e in self.out_adj.get(source_id, []):
            if e.target_id == target_id and (kind is None or e.kind == kind):
                return e
        return None

    @property
    def stats(self) -> dict:
        layer_counts = {l.name: 0 for l in Layer}
        for n in self.nodes.values():
            layer_counts[n.layer.name] += 1
        edge_counts = {}
        for e in self.edges:
            edge_counts[e.kind.value] = edge_counts.get(e.kind.value, 0) + 1
        return {"nodes": layer_counts, "edges": edge_counts}
