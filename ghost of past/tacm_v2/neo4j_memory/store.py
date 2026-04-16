"""store.py — Neo4j graph store replacing crg GraphStore + in-memory LayeredGraph.

Design principles:
  - Every node and edge from the LayeredGraph model is stored in Neo4j
  - Graph algorithms (PageRank, Louvain, betweenness) run server-side via GDS
  - Cross-query memory is stored as (:Session) and (:QueryEvent) nodes
  - Agent findings are written back as (:Finding) nodes with edges to code nodes
  - The LayeredGraph interface is preserved for backward compatibility
"""

from __future__ import annotations

import os
import time
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Optional

from neo4j import GraphDatabase, Driver, Session as Neo4jSession

from ..graph.model import (
    Layer, LayeredGraph, LNode, LEdge, EdgeKind, LAYER_TOKEN_ESTIMATES,
)


# ---------------------------------------------------------------------------
# Connection config
# ---------------------------------------------------------------------------

@dataclass
class Neo4jConfig:
    uri: str = "bolt://localhost:7687"
    user: str = "neo4j"
    password: str = "tacm_graph_2026"
    database: str = "neo4j"

    @classmethod
    def from_env(cls) -> "Neo4jConfig":
        return cls(
            uri=os.environ.get("NEO4J_URI", "bolt://localhost:7687"),
            user=os.environ.get("NEO4J_USER", "neo4j"),
            password=os.environ.get("NEO4J_PASSWORD", "tacm_graph_2026"),
            database=os.environ.get("NEO4J_DATABASE", "neo4j"),
        )


# ---------------------------------------------------------------------------
# Schema bootstrap — constraints + indexes
# ---------------------------------------------------------------------------

_SCHEMA_CYPHER = [
    # Uniqueness constraints
    "CREATE CONSTRAINT file_id IF NOT EXISTS FOR (n:File) REQUIRE n.node_id IS UNIQUE",
    "CREATE CONSTRAINT class_id IF NOT EXISTS FOR (n:Class) REQUIRE n.node_id IS UNIQUE",
    "CREATE CONSTRAINT function_id IF NOT EXISTS FOR (n:Function) REQUIRE n.node_id IS UNIQUE",
    "CREATE CONSTRAINT session_id IF NOT EXISTS FOR (n:Session) REQUIRE n.session_id IS UNIQUE",
    "CREATE CONSTRAINT query_id IF NOT EXISTS FOR (n:QueryEvent) REQUIRE n.query_id IS UNIQUE",
    "CREATE CONSTRAINT finding_id IF NOT EXISTS FOR (n:Finding) REQUIRE n.finding_id IS UNIQUE",

    # Full-text index for BM25 search
    """
    CREATE FULLTEXT INDEX code_fulltext IF NOT EXISTS
    FOR (n:File|Class|Function)
    ON EACH [n.name, n.serialized_text]
    """,

    # Composite index for fast layer queries
    "CREATE INDEX layer_idx IF NOT EXISTS FOR (n:File) ON (n.repo)",
    "CREATE INDEX class_layer_idx IF NOT EXISTS FOR (n:Class) ON (n.repo)",
    "CREATE INDEX fn_layer_idx IF NOT EXISTS FOR (n:Function) ON (n.repo)",
]


# ---------------------------------------------------------------------------
# Neo4j Graph Store
# ---------------------------------------------------------------------------

class Neo4jGraphStore:
    """Persistent graph store backed by Neo4j.

    Provides:
      - Ingest from existing LayeredGraph or crg GraphStore
      - Real-time graph algorithm execution via GDS
      - Cross-query memory (session tracking)
      - Dynamic knowledge graph updates (findings)
      - Export back to LayeredGraph for backward compatibility
    """

    def __init__(self, config: Optional[Neo4jConfig] = None):
        self._config = config or Neo4jConfig.from_env()
        self._driver: Driver = GraphDatabase.driver(
            self._config.uri,
            auth=(self._config.user, self._config.password),
        )
        self._ensure_schema()

    def close(self) -> None:
        self._driver.close()

    def __enter__(self) -> "Neo4jGraphStore":
        return self

    def __exit__(self, *exc) -> None:
        self.close()

    @contextmanager
    def _session(self):
        with self._driver.session(database=self._config.database) as s:
            yield s

    def _ensure_schema(self) -> None:
        with self._session() as s:
            for cypher in _SCHEMA_CYPHER:
                try:
                    s.run(cypher.strip())
                except Exception:
                    pass  # constraint already exists

    # ------------------------------------------------------------------
    # Ingest — load a LayeredGraph into Neo4j
    # ------------------------------------------------------------------

    def ingest_graph(self, graph: LayeredGraph, repo: str) -> None:
        """Bulk-load a LayeredGraph into Neo4j. Idempotent via MERGE."""
        self._ingest_nodes(graph, repo)
        self._ingest_edges(graph)

    def _ingest_nodes(self, graph: LayeredGraph, repo: str) -> None:
        layer_label = {Layer.FILE: "File", Layer.CLASS: "Class", Layer.FUNCTION: "Function"}

        # Batch by layer for efficient UNWIND
        for layer, label in layer_label.items():
            nodes = graph.nodes_at_layer(layer)
            if not nodes:
                continue

            batch = [
                {
                    "node_id": n.node_id,
                    "name": n.name,
                    "file_path": n.file_path,
                    "line_start": n.line_start,
                    "line_end": n.line_end,
                    "parent_id": n.parent_id or "",
                    "language": n.language,
                    "in_degree": n.in_degree,
                    "out_degree": n.out_degree,
                    "call_fan_in": n.call_fan_in,
                    "call_fan_out": n.call_fan_out,
                    "is_test": n.is_test,
                    "token_cost": n.token_cost,
                    "repo": repo,
                }
                for n in nodes
            ]

            cypher = f"""
            UNWIND $batch AS row
            MERGE (n:{label} {{node_id: row.node_id}})
            SET n += row
            """
            with self._session() as s:
                s.run(cypher, batch=batch)

    def _ingest_edges(self, graph: LayeredGraph) -> None:
        # Group edges by kind for batch insert
        by_kind: dict[EdgeKind, list[dict]] = {}
        for edge in graph.edges:
            by_kind.setdefault(edge.kind, []).append({
                "source_id": edge.source_id,
                "target_id": edge.target_id,
                "weight": edge.weight,
                "raw_count": edge.raw_count,
            })

        # Map EdgeKind to Neo4j relationship type
        rel_type = {
            EdgeKind.CALLS: "CALLS",
            EdgeKind.INHERITS: "INHERITS",
            EdgeKind.IMPORTS_FROM: "IMPORTS_FROM",
            EdgeKind.CONTAINS: "CONTAINS",
            EdgeKind.TESTED_BY: "TESTED_BY",
        }

        for kind, edges in by_kind.items():
            rtype = rel_type[kind]
            cypher = f"""
            UNWIND $edges AS row
            MATCH (src {{node_id: row.source_id}})
            MATCH (tgt {{node_id: row.target_id}})
            MERGE (src)-[r:{rtype}]->(tgt)
            SET r.weight = row.weight, r.raw_count = row.raw_count
            """
            with self._session() as s:
                s.run(cypher, edges=edges)

    # ------------------------------------------------------------------
    # Export — reconstruct a LayeredGraph from Neo4j (backward compat)
    # ------------------------------------------------------------------

    def export_graph(self, repo: str) -> LayeredGraph:
        """Read the full graph for a repo back into a LayeredGraph."""
        graph = LayeredGraph()

        label_to_layer = {"File": Layer.FILE, "Class": Layer.CLASS, "Function": Layer.FUNCTION}

        with self._session() as s:
            # Nodes
            for label, layer in label_to_layer.items():
                result = s.run(
                    f"MATCH (n:{label} {{repo: $repo}}) RETURN n",
                    repo=repo,
                )
                for record in result:
                    props = dict(record["n"])
                    node = LNode(
                        node_id=props["node_id"],
                        layer=layer,
                        name=props.get("name", ""),
                        file_path=props.get("file_path", ""),
                        line_start=props.get("line_start", 0),
                        line_end=props.get("line_end", 0),
                        parent_id=props.get("parent_id") or None,
                        language=props.get("language", ""),
                        in_degree=props.get("in_degree", 0),
                        out_degree=props.get("out_degree", 0),
                        call_fan_in=props.get("call_fan_in", 0),
                        call_fan_out=props.get("call_fan_out", 0),
                        is_test=props.get("is_test", False),
                        token_cost=props.get("token_cost", 0),
                    )
                    graph.add_node(node)

            # Edges
            kind_map = {
                "CALLS": EdgeKind.CALLS,
                "INHERITS": EdgeKind.INHERITS,
                "IMPORTS_FROM": EdgeKind.IMPORTS_FROM,
                "CONTAINS": EdgeKind.CONTAINS,
                "TESTED_BY": EdgeKind.TESTED_BY,
            }
            for rtype, ekind in kind_map.items():
                result = s.run(f"""
                    MATCH (src)-[r:{rtype}]->(tgt)
                    WHERE src.repo = $repo
                    RETURN src.node_id AS src, tgt.node_id AS tgt,
                           r.weight AS weight, r.raw_count AS raw_count
                """, repo=repo)
                for record in result:
                    graph.add_edge(LEdge(
                        source_id=record["src"],
                        target_id=record["tgt"],
                        kind=ekind,
                        weight=record["weight"] or 1.0,
                        raw_count=record["raw_count"] or 1,
                    ))

        # Recompute degrees from edges
        for node_id, node in graph.nodes.items():
            out_e = graph.out_adj.get(node_id, [])
            in_e = graph.in_adj.get(node_id, [])
            node.out_degree = len(out_e)
            node.in_degree = len(in_e)
            node.call_fan_out = sum(1 for e in out_e if e.kind == EdgeKind.CALLS)
            node.call_fan_in = sum(1 for e in in_e if e.kind == EdgeKind.CALLS)

        return graph

    # ------------------------------------------------------------------
    # Clear repo data
    # ------------------------------------------------------------------

    def clear_repo(self, repo: str) -> None:
        """Remove all nodes and edges for a repo. Use with care."""
        with self._session() as s:
            s.run("""
                MATCH (n {repo: $repo})
                DETACH DELETE n
            """, repo=repo)
