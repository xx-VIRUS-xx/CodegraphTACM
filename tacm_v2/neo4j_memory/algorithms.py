"""algorithms.py — Real-time graph algorithms via Neo4j GDS.

Runs server-side graph algorithms that would be expensive or impossible
in the pure-Python implementation:

  1. PageRank          — replaces the sparse power-iteration in scoring.py
  2. Louvain community — detects module clusters for diversity-aware selection
  3. Betweenness       — identifies bridge functions between modules
  4. Shortest path     — finds call chains between two functions
  5. Node similarity   — Jaccard similarity on call neighborhoods

All algorithms use Neo4j Graph Data Science (GDS) library projections
that are created on-demand and dropped after use.
"""

from __future__ import annotations

import uuid
from typing import Optional

from neo4j import Session as Neo4jSession


class GraphAlgorithms:
    """Executes GDS algorithms against a Neo4j-backed code graph."""

    def __init__(self, store: "Neo4jGraphStore"):
        self._store = store

    # ------------------------------------------------------------------
    # GDS projection lifecycle
    # ------------------------------------------------------------------

    def _project_calls_graph(self, session: Neo4jSession, repo: str) -> str:
        """Create a temporary GDS graph projection over the CALLS subgraph."""
        graph_name = f"tacm_calls_{uuid.uuid4().hex[:8]}"
        session.run("""
            CALL gds.graph.project(
                $graph_name,
                {
                    Function: {
                        label: 'Function',
                        properties: ['call_fan_in', 'call_fan_out', 'token_cost']
                    }
                },
                {
                    CALLS: {
                        type: 'CALLS',
                        orientation: 'NATURAL',
                        properties: ['weight']
                    }
                }
            )
        """, graph_name=graph_name)
        return graph_name

    def _project_full_graph(self, session: Neo4jSession, repo: str) -> str:
        """Create a GDS projection over all node types and edge types."""
        graph_name = f"tacm_full_{uuid.uuid4().hex[:8]}"
        session.run("""
            CALL gds.graph.project(
                $graph_name,
                ['File', 'Class', 'Function'],
                {
                    CALLS:        {type: 'CALLS',        properties: ['weight']},
                    CONTAINS:     {type: 'CONTAINS',     properties: ['weight']},
                    INHERITS:     {type: 'INHERITS',     properties: ['weight']},
                    IMPORTS_FROM: {type: 'IMPORTS_FROM', properties: ['weight']}
                }
            )
        """, graph_name=graph_name)
        return graph_name

    def _drop_projection(self, session: Neo4jSession, graph_name: str) -> None:
        try:
            session.run("CALL gds.graph.drop($name, false)", name=graph_name)
        except Exception:
            pass

    # ------------------------------------------------------------------
    # PageRank — server-side, weighted, normalized
    # ------------------------------------------------------------------

    def pagerank(
        self,
        repo: str,
        damping: float = 0.85,
        max_iterations: int = 50,
        write_property: str = "pagerank",
    ) -> dict[str, float]:
        """Run weighted PageRank over CALLS subgraph. Returns {node_id: score}.

        Scores are written back to Neo4j nodes AND returned.
        This replaces the pure-Python power-iteration in scoring.py with
        a server-side implementation that handles millions of edges efficiently.
        """
        with self._store._session() as s:
            graph_name = self._project_calls_graph(s, repo)
            try:
                # Run PageRank with weighted edges
                s.run(f"""
                    CALL gds.pageRank.write(
                        $graph_name,
                        {{
                            dampingFactor: $damping,
                            maxIterations: $max_iterations,
                            relationshipWeightProperty: 'weight',
                            writeProperty: $write_property
                        }}
                    )
                """, graph_name=graph_name, damping=damping,
                     max_iterations=max_iterations, write_property=write_property)

                # Read back results
                result = s.run(f"""
                    MATCH (n:Function)
                    WHERE n.{write_property} IS NOT NULL
                    RETURN n.node_id AS node_id, n.{write_property} AS score
                """)
                scores = {r["node_id"]: r["score"] for r in result}

                # Normalize to [0, 1]
                max_val = max(scores.values()) if scores else 1.0
                if max_val > 0:
                    scores = {k: v / max_val for k, v in scores.items()}
                return scores
            finally:
                self._drop_projection(s, graph_name)

    # ------------------------------------------------------------------
    # Louvain community detection
    # ------------------------------------------------------------------

    def louvain_communities(
        self,
        repo: str,
        write_property: str = "community_id",
    ) -> dict[str, int]:
        """Detect communities via Louvain. Returns {node_id: community_id}.

        Communities represent functional modules — groups of functions that
        call each other heavily. Used by the selector for diversity-aware
        context: selecting from multiple communities gives the LLM broader
        codebase coverage.
        """
        with self._store._session() as s:
            graph_name = self._project_calls_graph(s, repo)
            try:
                s.run("""
                    CALL gds.louvain.write(
                        $graph_name,
                        {
                            relationshipWeightProperty: 'weight',
                            writeProperty: $write_property
                        }
                    )
                """, graph_name=graph_name, write_property=write_property)

                result = s.run(f"""
                    MATCH (n:Function)
                    WHERE n.{write_property} IS NOT NULL
                    RETURN n.node_id AS node_id, n.{write_property} AS community
                """)
                return {r["node_id"]: r["community"] for r in result}
            finally:
                self._drop_projection(s, graph_name)

    # ------------------------------------------------------------------
    # Betweenness centrality — bridge detection
    # ------------------------------------------------------------------

    def betweenness(
        self,
        repo: str,
        write_property: str = "betweenness",
    ) -> dict[str, float]:
        """Betweenness centrality over CALLS subgraph.

        Identifies bridge functions that sit between modules. These are
        critical for understanding how subsystems interact — a function
        with high betweenness is on many shortest call-paths between
        other function pairs.

        Example: a `dispatch()` function that routes between subsystems
        has high betweenness even if its fan_in and fan_out are modest.
        """
        with self._store._session() as s:
            graph_name = self._project_calls_graph(s, repo)
            try:
                s.run("""
                    CALL gds.betweenness.write(
                        $graph_name,
                        {writeProperty: $write_property}
                    )
                """, graph_name=graph_name, write_property=write_property)

                result = s.run(f"""
                    MATCH (n:Function)
                    WHERE n.{write_property} IS NOT NULL
                    RETURN n.node_id AS node_id, n.{write_property} AS score
                """)
                scores = {r["node_id"]: r["score"] for r in result}

                max_val = max(scores.values()) if scores else 1.0
                if max_val > 0:
                    scores = {k: v / max_val for k, v in scores.items()}
                return scores
            finally:
                self._drop_projection(s, graph_name)

    # ------------------------------------------------------------------
    # Shortest path — call chain between two functions
    # ------------------------------------------------------------------

    def shortest_call_path(
        self,
        source_id: str,
        target_id: str,
    ) -> list[str]:
        """Find shortest call-chain path between two functions.

        Returns ordered list of node_ids from source to target.
        Used by active memory to understand how a buggy function
        is reachable from an entry point.
        """
        with self._store._session() as s:
            result = s.run("""
                MATCH (src:Function {node_id: $source}),
                      (tgt:Function {node_id: $target}),
                      path = shortestPath((src)-[:CALLS*..10]->(tgt))
                RETURN [n IN nodes(path) | n.node_id] AS chain
            """, source=source_id, target=target_id)
            record = result.single()
            return record["chain"] if record else []

    # ------------------------------------------------------------------
    # K-hop neighborhood expansion
    # ------------------------------------------------------------------

    def expand_neighborhood(
        self,
        node_ids: list[str],
        hops: int = 2,
        max_neighbors: int = 50,
    ) -> list[dict]:
        """Expand a set of seed nodes by K hops through CALLS edges.

        Returns neighbor nodes ranked by connection strength.
        This is the Neo4j-native version of the graph expansion
        described in plan.md — runs server-side instead of Python loops.
        """
        with self._store._session() as s:
            result = s.run("""
                UNWIND $seeds AS seed_id
                MATCH (seed:Function {node_id: seed_id})
                MATCH (seed)-[r:CALLS*1..$hops]-(neighbor:Function)
                WHERE NOT neighbor.node_id IN $seeds
                  AND NOT neighbor.is_test
                WITH neighbor,
                     count(DISTINCT seed_id) AS seed_connections,
                     sum(reduce(w = 1.0, rel IN r | w * rel.weight)) AS path_weight
                RETURN neighbor.node_id AS node_id,
                       neighbor.name AS name,
                       seed_connections,
                       path_weight
                ORDER BY seed_connections DESC, path_weight DESC
                LIMIT $limit
            """, seeds=node_ids, hops=hops, limit=max_neighbors)
            return [dict(r) for r in result]

    # ------------------------------------------------------------------
    # Node similarity — Jaccard on call neighborhoods
    # ------------------------------------------------------------------

    def similar_functions(
        self,
        node_id: str,
        top_k: int = 10,
    ) -> list[tuple[str, float]]:
        """Find functions with similar call neighborhoods (Jaccard).

        If function A calls {X, Y, Z} and function B calls {X, Y, W},
        their Jaccard similarity is |{X,Y}| / |{X,Y,Z,W}| = 0.5.

        Used by active memory to suggest related functions when the
        agent is exploring a bug.
        """
        with self._store._session() as s:
            result = s.run("""
                MATCH (a:Function {node_id: $node_id})-[:CALLS]->(shared)<-[:CALLS]-(b:Function)
                WHERE a <> b AND NOT b.is_test
                WITH b,
                     count(DISTINCT shared) AS intersection,
                     size([(a)-[:CALLS]->(x) | x]) AS a_out,
                     size([(b)-[:CALLS]->(y) | y]) AS b_out
                WITH b, intersection,
                     (a_out + b_out - intersection) AS union_size
                WHERE union_size > 0
                RETURN b.node_id AS node_id,
                       toFloat(intersection) / union_size AS jaccard
                ORDER BY jaccard DESC
                LIMIT $top_k
            """, node_id=node_id, top_k=top_k)
            return [(r["node_id"], r["jaccard"]) for r in result]
