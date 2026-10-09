"""findings.py — Dynamic knowledge graph updates.

The agent writes findings back into the graph as it works:

  (:Finding {finding_id, type, description, confidence, timestamp})
     -[:ABOUT]-> (:Function)     -- the code node this finding is about
     -[:CAUSED_BY]-> (:Finding)  -- causal chain between findings
     -[:RELATED_TO]-> (:Finding) -- lateral associations

Finding types:
  - BUG:         confirmed defect location
  - ROOT_CAUSE:  the underlying cause (may differ from symptom location)
  - SIDE_EFFECT: a function affected by the bug but not the cause
  - FIX:         the applied fix location
  - PATTERN:     a recurring pattern across bugs (e.g., "missing null check")

This creates a growing knowledge base that:
  1. Feeds into memory scoring (hot spots, patterns)
  2. Enables cross-bug analysis (which functions keep breaking?)
  3. Provides the agent with historical context on similar past bugs
"""

from __future__ import annotations

import uuid
from enum import Enum
from dataclasses import dataclass
from typing import Optional


class FindingType(str, Enum):
    BUG = "BUG"
    ROOT_CAUSE = "ROOT_CAUSE"
    SIDE_EFFECT = "SIDE_EFFECT"
    FIX = "FIX"
    PATTERN = "PATTERN"


@dataclass
class Finding:
    finding_id: str
    finding_type: FindingType
    description: str
    confidence: float  # [0, 1]
    node_ids: list[str]  # code nodes this is about
    caused_by: Optional[str] = None  # another finding_id
    related_to: list[str] = None  # other finding_ids

    def __post_init__(self):
        if self.related_to is None:
            self.related_to = []


class FindingsStore:
    """Manages agent findings written back to the Neo4j graph."""

    def __init__(self, store: "Neo4jGraphStore"):
        self._store = store

    # ------------------------------------------------------------------
    # Write findings
    # ------------------------------------------------------------------

    def record_finding(self, finding: Finding) -> str:
        """Write a finding to Neo4j and link to code nodes."""
        with self._store._session() as s:
            # Create finding node
            s.run("""
                CREATE (f:Finding {
                    finding_id: $fid,
                    type: $ftype,
                    description: $desc,
                    confidence: $conf,
                    timestamp: datetime()
                })
            """, fid=finding.finding_id, ftype=finding.finding_type.value,
                 desc=finding.description, conf=finding.confidence)

            # Link to code nodes
            if finding.node_ids:
                s.run("""
                    MATCH (f:Finding {finding_id: $fid})
                    UNWIND $node_ids AS nid
                    MATCH (n {node_id: nid})
                    CREATE (f)-[:ABOUT]->(n)
                """, fid=finding.finding_id, node_ids=finding.node_ids)

            # Causal chain
            if finding.caused_by:
                s.run("""
                    MATCH (f:Finding {finding_id: $fid})
                    MATCH (cause:Finding {finding_id: $cause_id})
                    CREATE (f)-[:CAUSED_BY]->(cause)
                """, fid=finding.finding_id, cause_id=finding.caused_by)

            # Related findings
            if finding.related_to:
                s.run("""
                    MATCH (f:Finding {finding_id: $fid})
                    UNWIND $related AS rid
                    MATCH (rel:Finding {finding_id: rid})
                    CREATE (f)-[:RELATED_TO]->(rel)
                """, fid=finding.finding_id, related=finding.related_to)

        return finding.finding_id

    def create_finding(
        self,
        finding_type: FindingType,
        description: str,
        node_ids: list[str],
        confidence: float = 0.8,
        caused_by: Optional[str] = None,
    ) -> str:
        """Convenience: create and record a finding in one call."""
        f = Finding(
            finding_id=f"f_{uuid.uuid4().hex[:12]}",
            finding_type=finding_type,
            description=description,
            confidence=confidence,
            node_ids=node_ids,
            caused_by=caused_by,
        )
        return self.record_finding(f)

    # ------------------------------------------------------------------
    # Query findings
    # ------------------------------------------------------------------

    def get_findings_for_node(self, node_id: str) -> list[dict]:
        """All findings about a specific code node."""
        with self._store._session() as s:
            result = s.run("""
                MATCH (f:Finding)-[:ABOUT]->(n {node_id: $nid})
                OPTIONAL MATCH (f)-[:CAUSED_BY]->(cause:Finding)
                RETURN f.finding_id AS finding_id,
                       f.type AS type,
                       f.description AS description,
                       f.confidence AS confidence,
                       f.timestamp AS timestamp,
                       cause.finding_id AS caused_by
                ORDER BY f.timestamp DESC
            """, nid=node_id)
            return [dict(r) for r in result]

    def get_causal_chain(self, finding_id: str) -> list[dict]:
        """Walk the CAUSED_BY chain from a finding to its root cause."""
        with self._store._session() as s:
            result = s.run("""
                MATCH path = (f:Finding {finding_id: $fid})-[:CAUSED_BY*0..10]->(root)
                WHERE NOT (root)-[:CAUSED_BY]->()
                UNWIND nodes(path) AS finding
                MATCH (finding)-[:ABOUT]->(n)
                RETURN finding.finding_id AS finding_id,
                       finding.type AS type,
                       finding.description AS description,
                       collect(n.node_id) AS node_ids
            """, fid=finding_id)
            return [dict(r) for r in result]

    def get_patterns(self, repo: str, min_occurrences: int = 2) -> list[dict]:
        """Find recurring bug patterns — functions that keep breaking.

        Returns nodes that have multiple BUG findings, grouped by
        the types of bugs found there.
        """
        with self._store._session() as s:
            result = s.run("""
                MATCH (f:Finding {type: 'BUG'})-[:ABOUT]->(n)
                WHERE n.repo = $repo
                WITH n, count(f) AS bug_count,
                     collect(f.description) AS descriptions
                WHERE bug_count >= $min_occ
                RETURN n.node_id AS node_id,
                       n.name AS name,
                       n.file_path AS file_path,
                       bug_count,
                       descriptions
                ORDER BY bug_count DESC
            """, repo=repo, min_occ=min_occurrences)
            return [dict(r) for r in result]

    def find_similar_bugs(self, node_id: str) -> list[dict]:
        """Find past bugs in structurally similar functions.

        Uses the CALLS neighborhood to find functions that share
        callers/callees with the target node and have had bugs.
        """
        with self._store._session() as s:
            result = s.run("""
                MATCH (target {node_id: $nid})-[:CALLS]-(neighbor)-[:CALLS]-(similar)
                WHERE target <> similar
                MATCH (f:Finding {type: 'BUG'})-[:ABOUT]->(similar)
                WITH similar, f, count(DISTINCT neighbor) AS shared_neighbors
                RETURN similar.node_id AS node_id,
                       similar.name AS name,
                       f.description AS bug_description,
                       shared_neighbors,
                       f.confidence AS confidence
                ORDER BY shared_neighbors DESC
                LIMIT 10
            """, nid=node_id)
            return [dict(r) for r in result]
