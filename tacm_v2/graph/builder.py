"""builder.py — Builds a LayeredGraph from a crg GraphStore.

Reads what crg already parsed (File/Class/Function nodes + all edge kinds),
computes dynamic edge weights, and produces a LayeredGraph.

Dynamic weight computation:

    CALLS weight:
        crg stores one edge per call-site. If function A calls B three times
        (in a loop, in branches, etc.), there are 3 duplicate (A→B) edges.
        weight = count(A→B) / global_max_call_count
        This makes "A calls B 10 times" weight=1.0 and "A calls B once"
        weight=0.1, reflecting how tightly coupled A is to B.

    IMPORTS_FROM weight:
        1.0 for direct imports (A imports B directly).
        Transitive closure added at 0.5 (A imports C which imports B → A→B at 0.5).
        Captures indirect dependency for the File layer traversal.

    INHERITS weight:
        1.0 for direct parent.
        0.5 for grandparent (transitive, one step removed).
        Deeper ancestry is not added — too noisy at class level.

    CONTAINS weight:
        Always 1.0. Containment is structural, not variable.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Optional

from code_review_graph.graph import GraphStore, GraphNode
from code_review_graph.incremental import get_db_path

from .model import (
    Layer, LayeredGraph, LNode, LEdge, EdgeKind, LAYER_TOKEN_ESTIMATES
)


# ---------------------------------------------------------------------------
# Source reading — same as v1, needed for token_cost
# ---------------------------------------------------------------------------

def _read_source(file_path: str, line_start: Optional[int], line_end: Optional[int]) -> str:
    if not (file_path and line_start and line_end):
        return ""
    try:
        lines = Path(file_path).read_text(errors="replace").splitlines()
        return "\n".join(lines[max(0, line_start - 1): min(len(lines), line_end)])
    except OSError:
        return ""


def _token_cost(source: str, layer: Layer) -> int:
    if source:
        return max(1, len(source) // 4)
    return LAYER_TOKEN_ESTIMATES[layer]


# ---------------------------------------------------------------------------
# crg kind → Layer mapping
# ---------------------------------------------------------------------------

_CRG_KIND_TO_LAYER: dict[str, Layer] = {
    "File":     Layer.FILE,
    "Class":    Layer.CLASS,
    "Function": Layer.FUNCTION,
    "Test":     Layer.FUNCTION,  # tests live at function layer
}


# ---------------------------------------------------------------------------
# Builder
# ---------------------------------------------------------------------------

class GraphBuilder:
    """Reads a crg GraphStore and produces a LayeredGraph with dynamic weights."""

    def __init__(self, store: GraphStore):
        self._store = store

    def build(self) -> LayeredGraph:
        graph = LayeredGraph()

        self._add_nodes(graph)
        self._add_edges(graph)
        self._compute_degrees(graph)

        return graph

    # ------------------------------------------------------------------
    # Node construction
    # ------------------------------------------------------------------

    def _add_nodes(self, graph: LayeredGraph) -> None:
        for crg_kind, layer in _CRG_KIND_TO_LAYER.items():
            for crg_node in self._store.get_nodes_by_kind([crg_kind]):
                source = _read_source(crg_node.file_path, crg_node.line_start, crg_node.line_end)
                node = LNode(
                    node_id   = crg_node.qualified_name,
                    layer     = layer,
                    name      = crg_node.name,
                    file_path = crg_node.file_path,
                    line_start= crg_node.line_start or 0,
                    line_end  = crg_node.line_end or 0,
                    is_test   = crg_node.is_test,
                    token_cost= _token_cost(source, layer),
                )
                graph.add_node(node)

        # Build a name → node_id index for short-name CALLS resolution.
        # crg stores many call targets as unqualified names (e.g. "send", "Session").
        # We resolve these to the best matching node in the graph by short name.
        # If multiple nodes share the same short name, we keep all matches
        # (ambiguity is resolved by edge weight later).
        self._name_index: dict[str, list[str]] = defaultdict(list)
        for node_id, node in graph.nodes.items():
            self._name_index[node.name].append(node_id)

    # ------------------------------------------------------------------
    # Edge construction with dynamic weights
    # ------------------------------------------------------------------

    def _add_edges(self, graph: LayeredGraph) -> None:
        all_edges = self._store.get_all_edges()

        # --- CALLS: count frequency per (src, tgt) pair ---
        call_counts: Counter = Counter(
            (e.source_qualified, e.target_qualified)
            for e in all_edges if e.kind == "CALLS"
        )
        max_calls = max(call_counts.values()) if call_counts else 1

        for (src, tgt), count in call_counts.items():
            if src not in graph.nodes:
                continue
            # Resolve target: try exact qualified name first, then short name index.
            # crg stores many call targets as unqualified names ("send", "Session").
            targets: list[str] = []
            if tgt in graph.nodes:
                targets = [tgt]
            else:
                short = tgt.split("::")[-1]
                candidates = self._name_index.get(short, [])
                # Only resolve to nodes inside this repo (have "::" in their id)
                targets = [c for c in candidates if "::" in c]

            for resolved_tgt in targets:
                if resolved_tgt != src:  # no self-loops
                    graph.add_edge(LEdge(
                        source_id = src,
                        target_id = resolved_tgt,
                        kind      = EdgeKind.CALLS,
                        weight    = count / max_calls,
                        raw_count = count,
                    ))

        # --- CONTAINS: always 1.0, also sets parent_id on child ---
        for e in all_edges:
            if e.kind != "CONTAINS":
                continue
            if e.source_qualified in graph.nodes and e.target_qualified in graph.nodes:
                graph.add_edge(LEdge(
                    source_id = e.source_qualified,
                    target_id = e.target_qualified,
                    kind      = EdgeKind.CONTAINS,
                    weight    = 1.0,
                ))
                # Set parent on child node
                child = graph.nodes.get(e.target_qualified)
                if child is not None:
                    child.parent_id = e.source_qualified

        # --- INHERITS: 1.0 direct, then transitive closure at 0.5 ---
        direct_inherits: set[tuple[str, str]] = set()
        for e in all_edges:
            if e.kind != "INHERITS":
                continue
            if e.source_qualified in graph.nodes and e.target_qualified in graph.nodes:
                graph.add_edge(LEdge(
                    source_id = e.source_qualified,
                    target_id = e.target_qualified,
                    kind      = EdgeKind.INHERITS,
                    weight    = 1.0,
                ))
                direct_inherits.add((e.source_qualified, e.target_qualified))

        # Transitive: if A→B and B→C exist, add A→C at 0.5 (if not already direct)
        for (child, parent) in list(direct_inherits):
            for (p2, grandparent) in direct_inherits:
                if p2 == parent and (child, grandparent) not in direct_inherits:
                    if child in graph.nodes and grandparent in graph.nodes:
                        if graph.get_edge(child, grandparent, EdgeKind.INHERITS) is None:
                            graph.add_edge(LEdge(
                                source_id = child,
                                target_id = grandparent,
                                kind      = EdgeKind.INHERITS,
                                weight    = 0.5,
                            ))

        # --- IMPORTS_FROM: 1.0 direct, transitive at 0.5 ---
        direct_imports: set[tuple[str, str]] = set()
        for e in all_edges:
            if e.kind != "IMPORTS_FROM":
                continue
            if e.source_qualified in graph.nodes and e.target_qualified in graph.nodes:
                if graph.get_edge(e.source_qualified, e.target_qualified, EdgeKind.IMPORTS_FROM) is None:
                    graph.add_edge(LEdge(
                        source_id = e.source_qualified,
                        target_id = e.target_qualified,
                        kind      = EdgeKind.IMPORTS_FROM,
                        weight    = 1.0,
                    ))
                direct_imports.add((e.source_qualified, e.target_qualified))

        for (a, b) in list(direct_imports):
            for (b2, c) in direct_imports:
                if b2 == b and (a, c) not in direct_imports and a != c:
                    if a in graph.nodes and c in graph.nodes:
                        if graph.get_edge(a, c, EdgeKind.IMPORTS_FROM) is None:
                            graph.add_edge(LEdge(
                                source_id = a,
                                target_id = c,
                                kind      = EdgeKind.IMPORTS_FROM,
                                weight    = 0.5,
                            ))

        # --- TESTED_BY: always 1.0 ---
        for e in all_edges:
            if e.kind != "TESTED_BY":
                continue
            if e.source_qualified in graph.nodes and e.target_qualified in graph.nodes:
                graph.add_edge(LEdge(
                    source_id = e.source_qualified,
                    target_id = e.target_qualified,
                    kind      = EdgeKind.TESTED_BY,
                    weight    = 1.0,
                ))

    # ------------------------------------------------------------------
    # Degree computation — run after all edges are added
    # ------------------------------------------------------------------

    def _compute_degrees(self, graph: LayeredGraph) -> None:
        for node_id, node in graph.nodes.items():
            out_edges = graph.out_adj.get(node_id, [])
            in_edges  = graph.in_adj.get(node_id, [])
            node.out_degree = len(out_edges)
            node.in_degree  = len(in_edges)

            # call-specific fan signals (excluding test and contains edges)
            node.call_fan_out = sum(
                1 for e in out_edges if e.kind == EdgeKind.CALLS
            )
            node.call_fan_in = sum(
                1 for e in in_edges if e.kind == EdgeKind.CALLS
            )


# ---------------------------------------------------------------------------
# Convenience — open store and build in one call
# ---------------------------------------------------------------------------

def build_graph(repo_root: str | Path) -> LayeredGraph:
    """Build a LayeredGraph from the crg graph at repo_root."""
    root = Path(repo_root).resolve()
    store = GraphStore(get_db_path(root))
    try:
        return GraphBuilder(store).build()
    finally:
        store.close()
