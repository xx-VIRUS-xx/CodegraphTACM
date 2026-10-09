"""memory.py — Persistent cross-query active memory.

This is the core innovation: the graph remembers what happened across queries.

Data model:
  (:Session {session_id, repo, started_at, ended_at})
    -[:HAS_QUERY]-> (:QueryEvent {query_id, query_text, intent, timestamp})
       -[:EXPLORED]-> (:Function)      -- agent looked at this node
       -[:CONFIRMED_BUG]-> (:Function) -- agent confirmed bug here
       -[:RULED_OUT]-> (:Function)     -- agent eliminated this node
       -[:PATCH_TARGET]-> (:Function)  -- agent patched this node

Each code node accumulates signals from multiple queries over time:
  - exploration_count:  how many times agents have looked at this node
  - bug_count:          how many times confirmed as bug location
  - last_explored:      timestamp of last exploration
  - relevance_decay:    exponential decay of historical relevance

Memory-augmented scoring:
  When scoring nodes for a new query, the memory layer adds:
  - recency_boost:      recently explored nodes get a boost (temporal locality)
  - hot_spot_boost:      nodes with high bug_count get a boost (known trouble spots)
  - cold_penalty:        never-explored nodes in hot zones get penalized less
  - exploration_momentum: nodes partially explored get a boost to continue investigation
"""

from __future__ import annotations

import time
import uuid
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class QueryMemory:
    """Memory signals for a single code node accumulated across queries."""
    node_id: str
    exploration_count: int = 0
    bug_count: int = 0
    ruled_out_count: int = 0
    last_explored: float = 0.0
    last_bug: float = 0.0


class ActiveMemory:
    """Persistent cross-query memory backed by Neo4j.

    Tracks what the agent has explored, confirmed, and ruled out
    across multiple queries within a session. Memory signals feed
    into the scoring pipeline as additional dimensions.
    """

    def __init__(self, store: "Neo4jGraphStore"):
        self._store = store
        self._session_id: Optional[str] = None

    # ------------------------------------------------------------------
    # Session lifecycle
    # ------------------------------------------------------------------

    def start_session(self, repo: str) -> str:
        """Begin a new exploration session. Returns session_id."""
        self._session_id = f"session_{uuid.uuid4().hex[:12]}"
        with self._store._session() as s:
            s.run("""
                CREATE (sess:Session {
                    session_id: $sid,
                    repo: $repo,
                    started_at: datetime(),
                    query_count: 0
                })
            """, sid=self._session_id, repo=repo)
        return self._session_id

    def end_session(self) -> None:
        """Close the current session."""
        if not self._session_id:
            return
        with self._store._session() as s:
            s.run("""
                MATCH (sess:Session {session_id: $sid})
                SET sess.ended_at = datetime()
            """, sid=self._session_id)
        self._session_id = None

    def resume_session(self, session_id: str) -> None:
        """Resume a previously started session."""
        self._session_id = session_id

    # ------------------------------------------------------------------
    # Query event recording
    # ------------------------------------------------------------------

    def record_query(
        self,
        query: str,
        intent: str,
        explored_ids: list[str],
    ) -> str:
        """Record a query event and link to explored nodes."""
        if not self._session_id:
            raise RuntimeError("No active session — call start_session() first")

        query_id = f"q_{uuid.uuid4().hex[:12]}"

        with self._store._session() as s:
            # Create QueryEvent and link to Session
            s.run("""
                MATCH (sess:Session {session_id: $sid})
                CREATE (q:QueryEvent {
                    query_id: $qid,
                    query_text: $query,
                    intent: $intent,
                    timestamp: datetime(),
                    explored_count: $count
                })
                CREATE (sess)-[:HAS_QUERY]->(q)
                SET sess.query_count = sess.query_count + 1
            """, sid=self._session_id, qid=query_id,
                 query=query, intent=intent, count=len(explored_ids))

            # Link to explored nodes and update their memory signals
            if explored_ids:
                s.run("""
                    MATCH (q:QueryEvent {query_id: $qid})
                    UNWIND $node_ids AS nid
                    MATCH (n {node_id: nid})
                    MERGE (q)-[:EXPLORED]->(n)
                    SET n.exploration_count = coalesce(n.exploration_count, 0) + 1,
                        n.last_explored = datetime()
                """, qid=query_id, node_ids=explored_ids)

        return query_id

    # ------------------------------------------------------------------
    # Agent feedback — recording findings
    # ------------------------------------------------------------------

    def confirm_bug(self, query_id: str, node_ids: list[str], description: str = "") -> None:
        """Agent confirms these nodes contain the bug."""
        with self._store._session() as s:
            s.run("""
                MATCH (q:QueryEvent {query_id: $qid})
                UNWIND $node_ids AS nid
                MATCH (n {node_id: nid})
                MERGE (q)-[:CONFIRMED_BUG]->(n)
                SET n.bug_count = coalesce(n.bug_count, 0) + 1,
                    n.last_bug = datetime()
            """, qid=query_id, node_ids=node_ids)

            if description:
                s.run("""
                    MATCH (q:QueryEvent {query_id: $qid})
                    SET q.bug_description = $desc
                """, qid=query_id, desc=description)

    def rule_out(self, query_id: str, node_ids: list[str]) -> None:
        """Agent rules out these nodes — not the bug location."""
        with self._store._session() as s:
            s.run("""
                MATCH (q:QueryEvent {query_id: $qid})
                UNWIND $node_ids AS nid
                MATCH (n {node_id: nid})
                MERGE (q)-[:RULED_OUT]->(n)
                SET n.ruled_out_count = coalesce(n.ruled_out_count, 0) + 1
            """, qid=query_id, node_ids=node_ids)

    def mark_patch_target(self, query_id: str, node_ids: list[str]) -> None:
        """Agent marks these nodes as the location it will patch."""
        with self._store._session() as s:
            s.run("""
                MATCH (q:QueryEvent {query_id: $qid})
                UNWIND $node_ids AS nid
                MATCH (n {node_id: nid})
                MERGE (q)-[:PATCH_TARGET]->(n)
                SET n.patch_count = coalesce(n.patch_count, 0) + 1
            """, qid=query_id, node_ids=node_ids)

    # ------------------------------------------------------------------
    # Memory-augmented scoring signals
    # ------------------------------------------------------------------

    def get_memory_signals(
        self,
        node_ids: list[str],
        decay_half_life_hours: float = 2.0,
    ) -> dict[str, dict[str, float]]:
        """Compute memory-based scoring signals for a set of nodes.

        Returns {node_id: {signal_name: value}} with signals:
          - recency_boost:   exponential decay from last exploration
          - hot_spot_boost:   scaled by historical bug_count
          - ruled_out_penalty: penalty for nodes previously ruled out
          - exploration_momentum: boost for partially-explored neighborhoods
        """
        with self._store._session() as s:
            result = s.run("""
                UNWIND $node_ids AS nid
                MATCH (n {node_id: nid})
                OPTIONAL MATCH (n)<-[:EXPLORED]-(q:QueryEvent)
                WITH n, nid,
                     count(q) AS explore_count,
                     max(q.timestamp) AS last_explore
                OPTIONAL MATCH (n)<-[:CONFIRMED_BUG]-(q2:QueryEvent)
                WITH n, nid, explore_count, last_explore,
                     count(q2) AS bug_count
                OPTIONAL MATCH (n)<-[:RULED_OUT]-(q3:QueryEvent)
                WITH n, nid, explore_count, last_explore, bug_count,
                     count(q3) AS ruled_count
                // Compute neighbor exploration density
                OPTIONAL MATCH (n)-[:CALLS]-(neighbor)
                WHERE neighbor.exploration_count > 0
                WITH nid, explore_count, last_explore, bug_count, ruled_count,
                     count(neighbor) AS explored_neighbors,
                     coalesce(n.exploration_count, 0) AS self_explore
                RETURN nid AS node_id,
                       explore_count,
                       last_explore,
                       bug_count,
                       ruled_count,
                       explored_neighbors,
                       self_explore
            """, node_ids=node_ids)

            signals: dict[str, dict[str, float]] = {}
            now = time.time()

            for r in result:
                nid = r["node_id"]
                explore_count = r["explore_count"] or 0
                bug_count = r["bug_count"] or 0
                ruled_count = r["ruled_count"] or 0
                explored_neighbors = r["explored_neighbors"] or 0

                # Recency: exponential decay
                recency = 0.0
                if r["last_explore"] is not None:
                    try:
                        last_ts = r["last_explore"].to_native().timestamp()
                        hours_ago = max(0, (now - last_ts) / 3600)
                        recency = 2.0 ** (-hours_ago / decay_half_life_hours)
                    except (AttributeError, TypeError):
                        pass

                # Hot spot: log-scaled bug count
                hot_spot = 0.0
                if bug_count > 0:
                    import math
                    hot_spot = min(1.0, math.log2(1 + bug_count) / 3.0)

                # Ruled out: penalty that grows with repeated rule-outs
                ruled_penalty = min(0.3, 0.1 * ruled_count)

                # Exploration momentum: if many neighbors are explored but
                # this node isn't, it's in a "gap" — boost it
                momentum = 0.0
                if explored_neighbors > 0 and explore_count == 0:
                    momentum = min(0.5, 0.1 * explored_neighbors)
                elif explored_neighbors > 0 and explore_count > 0:
                    # Continuing investigation — smaller boost
                    momentum = min(0.2, 0.05 * explored_neighbors)

                signals[nid] = {
                    "recency_boost": recency,
                    "hot_spot_boost": hot_spot,
                    "ruled_out_penalty": ruled_penalty,
                    "exploration_momentum": momentum,
                }

            # Fill missing nodes with zero signals
            for nid in node_ids:
                if nid not in signals:
                    signals[nid] = {
                        "recency_boost": 0.0,
                        "hot_spot_boost": 0.0,
                        "ruled_out_penalty": 0.0,
                        "exploration_momentum": 0.0,
                    }

            return signals

    # ------------------------------------------------------------------
    # Session history queries
    # ------------------------------------------------------------------

    def get_session_history(self) -> list[dict]:
        """Return all queries in the current session, ordered by time."""
        if not self._session_id:
            return []

        with self._store._session() as s:
            result = s.run("""
                MATCH (sess:Session {session_id: $sid})-[:HAS_QUERY]->(q:QueryEvent)
                OPTIONAL MATCH (q)-[:EXPLORED]->(explored)
                OPTIONAL MATCH (q)-[:CONFIRMED_BUG]->(bug)
                OPTIONAL MATCH (q)-[:RULED_OUT]->(ruled)
                WITH q,
                     collect(DISTINCT explored.node_id) AS explored_ids,
                     collect(DISTINCT bug.node_id) AS bug_ids,
                     collect(DISTINCT ruled.node_id) AS ruled_ids
                RETURN q.query_id AS query_id,
                       q.query_text AS query,
                       q.intent AS intent,
                       q.timestamp AS timestamp,
                       explored_ids, bug_ids, ruled_ids
                ORDER BY q.timestamp
            """, sid=self._session_id)
            return [dict(r) for r in result]

    def get_hot_spots(self, repo: str, top_k: int = 20) -> list[dict]:
        """Return nodes with highest historical bug_count across all sessions."""
        with self._store._session() as s:
            result = s.run("""
                MATCH (n)
                WHERE n.repo = $repo AND coalesce(n.bug_count, 0) > 0
                RETURN n.node_id AS node_id,
                       n.name AS name,
                       n.file_path AS file_path,
                       n.bug_count AS bug_count,
                       n.exploration_count AS exploration_count
                ORDER BY n.bug_count DESC
                LIMIT $top_k
            """, repo=repo, top_k=top_k)
            return [dict(r) for r in result]
