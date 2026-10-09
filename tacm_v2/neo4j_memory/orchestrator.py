"""orchestrator.py — End-to-end Neo4j active memory pipeline.

This is the main entry point for the Neo4j-backed TACM system.
It replaces the context_providers.py functions with a unified pipeline:

  1. Load/build graph → Neo4j
  2. Run GDS algorithms (PageRank, Louvain, betweenness) — cached per repo
  3. Start/resume active memory session
  4. Score nodes with memory-augmented scorer
  5. Select context with community-aware diversity
  6. Record query + exploration in memory
  7. Accept agent feedback (confirm_bug, rule_out, mark_fix)
  8. Serialize context for the LLM

Usage:
    orch = ActiveMemoryOrchestrator.connect()
    orch.ingest_repo("thefuck", graph)
    session_id = orch.start_session("thefuck")

    # First query
    ctx = orch.retrieve("why does thefuck crash on fish shell?", budget=4000)

    # Agent finds the bug
    orch.confirm_bug(ctx.query_id, ["thefuck::shells::fish::get_aliases"])

    # Second query — memory from first query influences scoring
    ctx2 = orch.retrieve("how is the shell detection logic structured?", budget=4000)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from ..graph.model import LayeredGraph, Layer, LNode
from ..graph.builder import build_graph
from ..layers.serializers import serialize
from ..selector.intent import classify_intent
from .store import Neo4jGraphStore, Neo4jConfig
from .algorithms import GraphAlgorithms
from .memory import ActiveMemory
from .findings import FindingsStore, FindingType
from .scorer import MemoryAugmentedScorer


@dataclass
class RetrievalResult:
    """Result of a memory-augmented retrieval."""
    context_text: str
    query_id: str
    intent: str
    selected_nodes: list[dict]
    total_tokens: int
    budget: int
    communities_covered: set[int]
    memory_signals_summary: dict[str, float]


def _count_tokens(text: str) -> int:
    return max(1, len(text) // 4)


class ActiveMemoryOrchestrator:
    """Unified pipeline combining Neo4j graph store, GDS algorithms,
    active memory, and findings into one retrieval system.
    """

    def __init__(self, store: Neo4jGraphStore):
        self._store = store
        self._algos = GraphAlgorithms(store)
        self._memory = ActiveMemory(store)
        self._findings = FindingsStore(store)

        # Cached graph algorithm results per repo
        self._cached_pagerank: dict[str, dict[str, float]] = {}
        self._cached_betweenness: dict[str, dict[str, float]] = {}
        self._cached_communities: dict[str, dict[str, int]] = {}

        # Currently loaded in-memory graph (for BM25/serialization)
        self._graphs: dict[str, LayeredGraph] = {}
        self._current_repo: Optional[str] = None
        self._last_query_id: Optional[str] = None

    @classmethod
    def connect(cls, config: Optional[Neo4jConfig] = None) -> "ActiveMemoryOrchestrator":
        """Create orchestrator with Neo4j connection."""
        store = Neo4jGraphStore(config)
        return cls(store)

    def close(self) -> None:
        self._store.close()

    def __enter__(self) -> "ActiveMemoryOrchestrator":
        return self

    def __exit__(self, *exc) -> None:
        self.close()

    # ------------------------------------------------------------------
    # Repo lifecycle
    # ------------------------------------------------------------------

    def ingest_repo(
        self,
        repo: str,
        graph: Optional[LayeredGraph] = None,
        repo_root: Optional[str] = None,
    ) -> None:
        """Ingest a repository into Neo4j.

        Either pass an existing LayeredGraph or a repo_root path to
        build one from crg.
        """
        if graph is None:
            if repo_root is None:
                raise ValueError("Provide either graph or repo_root")
            graph = build_graph(repo_root)

        self._store.ingest_graph(graph, repo)
        self._graphs[repo] = graph

        # Pre-compute and cache graph algorithms
        self._refresh_algorithms(repo)

    def _refresh_algorithms(self, repo: str) -> None:
        """Run GDS algorithms and cache results."""
        self._cached_pagerank[repo] = self._algos.pagerank(repo)
        self._cached_betweenness[repo] = self._algos.betweenness(repo)
        self._cached_communities[repo] = self._algos.louvain_communities(repo)

    def _ensure_graph(self, repo: str) -> LayeredGraph:
        if repo not in self._graphs:
            self._graphs[repo] = self._store.export_graph(repo)
        return self._graphs[repo]

    # ------------------------------------------------------------------
    # Session lifecycle
    # ------------------------------------------------------------------

    def start_session(self, repo: str) -> str:
        """Start a new active memory session for a repo."""
        self._current_repo = repo
        return self._memory.start_session(repo)

    def resume_session(self, session_id: str, repo: str) -> None:
        """Resume an existing session."""
        self._current_repo = repo
        self._memory.resume_session(session_id)

    def end_session(self) -> None:
        self._memory.end_session()

    # ------------------------------------------------------------------
    # Retrieval — the main entry point
    # ------------------------------------------------------------------

    def retrieve(
        self,
        query: str,
        budget: int = 4000,
        repo: Optional[str] = None,
        intent: Optional[str] = None,
        exclude_tests: bool = True,
    ) -> RetrievalResult:
        """Memory-augmented context retrieval.

        Pipeline:
          1. Classify intent
          2. Build memory-augmented scorer (base + graph + memory signals)
          3. Score all nodes
          4. Greedy selection with community diversity
          5. Record query in active memory
          6. Return context
        """
        repo = repo or self._current_repo
        if not repo:
            raise ValueError("No repo specified — call start_session() first")

        graph = self._ensure_graph(repo)

        if intent is None:
            intent = classify_intent(query)

        # Prepare texts
        all_nodes = [
            n for n in graph.nodes.values()
            if not (exclude_tests and n.is_test)
        ]
        agent_texts = {n.node_id: serialize(n, graph) for n in all_nodes}

        # Score texts for BM25 (function bodies for scoring)
        from ..layers.serializers import serialize_function_for_scoring
        score_texts = {
            n.node_id: (
                serialize_function_for_scoring(n, graph)
                if n.layer == Layer.FUNCTION
                else agent_texts[n.node_id]
            )
            for n in all_nodes
        }

        # Memory-augmented scorer
        scorer = MemoryAugmentedScorer(
            graph=graph,
            query=query,
            intent=intent,
            score_texts=score_texts,
            neo4j_store=self._store,
            memory=self._memory,
            repo=repo,
            precomputed_pagerank=self._cached_pagerank.get(repo),
            precomputed_betweenness=self._cached_betweenness.get(repo),
            precomputed_communities=self._cached_communities.get(repo),
        )

        # Score all nodes
        scores = scorer.score_all(all_nodes)

        # Community-aware greedy selection
        communities = self._cached_communities.get(repo, {})
        selected_ids, selected_nodes_info, total_tokens, communities_covered = \
            self._greedy_select(
                all_nodes, scores, agent_texts, communities, budget, intent,
            )

        # Build context text
        context_parts = []
        for nid in selected_ids:
            context_parts.append(agent_texts[nid])
        context_text = "\n\n".join(context_parts)

        # Record in active memory
        query_id = self._memory.record_query(query, intent, selected_ids)
        self._last_query_id = query_id

        # Memory signals summary
        mem_signals = self._memory.get_memory_signals(selected_ids[:5])
        avg_signals = {}
        if mem_signals:
            signal_keys = ["recency_boost", "hot_spot_boost", "exploration_momentum"]
            for key in signal_keys:
                vals = [m.get(key, 0.0) for m in mem_signals.values()]
                avg_signals[key] = sum(vals) / len(vals) if vals else 0.0

        return RetrievalResult(
            context_text=context_text,
            query_id=query_id,
            intent=intent,
            selected_nodes=[
                {"node_id": nid, "score": scores.get(nid, 0), "community": communities.get(nid)}
                for nid in selected_ids
            ],
            total_tokens=total_tokens,
            budget=budget,
            communities_covered=communities_covered,
            memory_signals_summary=avg_signals,
        )

    def _greedy_select(
        self,
        nodes: list[LNode],
        scores: dict[str, float],
        texts: dict[str, str],
        communities: dict[str, int],
        budget: int,
        intent: str,
    ) -> tuple[list[str], list[dict], int, set[int]]:
        """Greedy selection with community diversity."""

        # Sort by score descending
        ranked = sorted(nodes, key=lambda n: -scores.get(n.node_id, 0.0))

        selected_ids: list[str] = []
        selected_info: list[dict] = []
        total_tokens = 0
        covered_communities: set[int] = set()
        file_counts: dict[str, int] = {}

        # Diversity bonus: after 60% budget used, give bonus to uncovered communities
        diversity_threshold = budget * 0.6

        for node in ranked:
            nid = node.node_id
            text = texts.get(nid, "")
            cost = _count_tokens(text)

            if total_tokens + cost > budget:
                continue

            # After threshold, apply community diversity boost
            effective_score = scores.get(nid, 0.0)
            if total_tokens > diversity_threshold:
                comm = communities.get(nid)
                if comm is not None and comm not in covered_communities:
                    effective_score += 0.1  # diversity bonus

            # File clustering limit: don't put more than 5 nodes from one file
            fp = node.file_path or ""
            if file_counts.get(fp, 0) >= 5:
                continue

            selected_ids.append(nid)
            total_tokens += cost
            file_counts[fp] = file_counts.get(fp, 0) + 1

            comm = communities.get(nid)
            if comm is not None:
                covered_communities.add(comm)

            selected_info.append({
                "node_id": nid,
                "score": effective_score,
                "cost": cost,
                "community": comm,
            })

        return selected_ids, selected_info, total_tokens, covered_communities

    # ------------------------------------------------------------------
    # Agent feedback API
    # ------------------------------------------------------------------

    def confirm_bug(
        self,
        node_ids: list[str],
        description: str = "",
        query_id: Optional[str] = None,
    ) -> str:
        """Agent confirms these functions contain the bug."""
        qid = query_id or self._last_query_id
        if qid:
            self._memory.confirm_bug(qid, node_ids, description)
        return self._findings.create_finding(
            FindingType.BUG, description, node_ids,
        )

    def rule_out(
        self,
        node_ids: list[str],
        query_id: Optional[str] = None,
    ) -> None:
        """Agent rules out these functions."""
        qid = query_id or self._last_query_id
        if qid:
            self._memory.rule_out(qid, node_ids)

    def mark_fix(
        self,
        node_ids: list[str],
        description: str = "",
        caused_by_finding: Optional[str] = None,
        query_id: Optional[str] = None,
    ) -> str:
        """Agent marks the fix location."""
        qid = query_id or self._last_query_id
        if qid:
            self._memory.mark_patch_target(qid, node_ids)
        return self._findings.create_finding(
            FindingType.FIX, description, node_ids,
            caused_by=caused_by_finding,
        )

    def record_pattern(
        self,
        description: str,
        node_ids: list[str],
        related_findings: Optional[list[str]] = None,
    ) -> str:
        """Record a recurring bug pattern."""
        f = FindingsStore(self._store)
        from .findings import Finding
        finding = Finding(
            finding_id=f"pat_{__import__('uuid').uuid4().hex[:12]}",
            finding_type=FindingType.PATTERN,
            description=description,
            confidence=0.9,
            node_ids=node_ids,
            related_to=related_findings or [],
        )
        return f.record_finding(finding)

    # ------------------------------------------------------------------
    # Introspection
    # ------------------------------------------------------------------

    def get_hot_spots(self, top_k: int = 20) -> list[dict]:
        """Top historically buggy functions."""
        return self._memory.get_hot_spots(self._current_repo, top_k)

    def get_session_history(self) -> list[dict]:
        """All queries + actions in the current session."""
        return self._memory.get_session_history()

    def explain_selection(self, node_id: str) -> dict:
        """Explain why a node was selected — all signal values."""
        repo = self._current_repo
        mem_signals = self._memory.get_memory_signals([node_id])
        findings = self._findings.get_findings_for_node(node_id)

        algos = {
            "pagerank": (self._cached_pagerank.get(repo, {}) or {}).get(node_id, 0),
            "betweenness": (self._cached_betweenness.get(repo, {}) or {}).get(node_id, 0),
            "community": (self._cached_communities.get(repo, {}) or {}).get(node_id),
        }

        return {
            "node_id": node_id,
            "graph_signals": algos,
            "memory_signals": mem_signals.get(node_id, {}),
            "findings": findings,
        }

    def get_call_chain(self, source_id: str, target_id: str) -> list[str]:
        """Shortest call path between two functions."""
        return self._algos.shortest_call_path(source_id, target_id)

    def get_similar_functions(self, node_id: str, top_k: int = 10) -> list[tuple[str, float]]:
        """Functions with similar call neighborhoods."""
        return self._algos.similar_functions(node_id, top_k)
