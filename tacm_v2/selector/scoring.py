"""scoring.py — Intent-aware, per-signal scoring for node selection.

Each query intent activates a different weight vector over the available signals.
Signals are computed once per query, normalised to [0, 1], then combined.

Available signals:
    bm25        — BM25 relevance of node's serialized text to the query
    fan_in      — weighted call in-degree (how many things call this, weighted by frequency)
                  discounted by name-sharing ambiguity
    fan_out     — call out-degree (how many things this calls — orchestrators)
    complexity  — token_cost normalised (large functions are more complex)
    test_cover  — 1 if function has TESTED_BY edge, 0 otherwise

Weight vectors by intent:
    BUG:       bm25=0.50  fan_in=0.25  fan_out=0.10  complexity=0.15  test=0.00
    STRUCTURE: bm25=0.60  fan_in=0.10  fan_out=0.20  complexity=0.00  test=0.10
    EXPLAIN:   bm25=0.45  fan_in=0.15  fan_out=0.30  complexity=0.05  test=0.05

Rationale:
    BUG:       Relevance is primary. Fan-in identifies heavily-depended-on functions
               (bugs there have wide impact). Complexity adds weight to large functions
               where bugs tend to hide. Tests not useful here — we want to find the bug,
               not validate it.

    STRUCTURE: Relevance drives selection. Fan-out identifies orchestrators/entry points
               that reveal structure. Fan-in identifies shared utilities. Test coverage
               slightly useful for identifying "important" well-tested modules.

    EXPLAIN:   Fan-out is most important for explain queries — the function that calls
               many things IS the story of how something works. Relevance still primary.
               Complexity slightly useful — richer functions have more to explain.

Layer-specific scoring:
    FILE nodes:    use only bm25 + fan_out (files don't have fan_in in a useful sense)
    CLASS nodes:   use bm25 + fan_in + fan_out (class-level connectivity)
    FUNCTION nodes: full signal vector
"""

from __future__ import annotations

import math
import re
from collections import Counter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..graph.model import LayeredGraph, LNode, Layer
from ..graph.model import EdgeKind
from .intent import QueryIntent, INTENT_WEIGHTS as _WEIGHTS


# ---------------------------------------------------------------------------
# Signal computation
# ---------------------------------------------------------------------------

def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def compute_bm25(
    query: str,
    nodes: list["LNode"],
    texts: dict[str, str],      # node_id -> serialized text
    k1: float = 1.5,
    b: float = 0.75,
) -> dict[str, float]:
    """BM25 on pre-serialized node texts. Returns normalised {node_id: score}."""
    q_tokens = _tokenize(query)
    if not q_tokens or not nodes:
        return {n.node_id: 0.0 for n in nodes}

    corpus = [_tokenize(texts.get(n.node_id, "")) for n in nodes]
    N = len(corpus)

    df: dict[str, int] = {}
    for doc in corpus:
        for term in set(doc):
            df[term] = df.get(term, 0) + 1

    idf: dict[str, float] = {
        term: math.log((N - df.get(term, 0) + 0.5) / (df.get(term, 0) + 0.5) + 1)
        for term in q_tokens
    }

    avgdl = sum(len(d) for d in corpus) / N if N else 1.0

    raw: dict[str, float] = {}
    for node, doc in zip(nodes, corpus):
        dl = len(doc)
        tf_map: dict[str, int] = {}
        for term in doc:
            tf_map[term] = tf_map.get(term, 0) + 1
        score = 0.0
        for term in q_tokens:
            tf = tf_map.get(term, 0)
            denom = tf + k1 * (1 - b + b * dl / avgdl)
            score += idf.get(term, 0.0) * (tf * (k1 + 1) / denom if denom else 0)
        raw[node.node_id] = score

    max_score = max(raw.values()) if raw else 1.0
    if max_score > 0:
        return {k: v / max_score for k, v in raw.items()}
    return raw


def compute_fan_in(
    nodes: list["LNode"],
    graph: "LayeredGraph",
    name_counts: dict[str, int],
) -> dict[str, float]:
    """Weighted call in-degree, discounted by name-sharing ambiguity.

    When "send" is called and 4 nodes share the name, each gets 1/4 of the
    weight. This prevents common names from dominating the signal.

    Excludes test nodes as sources (test harness calls inflate fan_in).
    """
    raw: dict[str, float] = {}
    for node in nodes:
        in_edges = graph.in_adj.get(node.node_id, [])
        weighted = 0.0
        for e in in_edges:
            if e.kind != EdgeKind.CALLS:
                continue
            src = graph.nodes.get(e.source_id)
            if src is None or src.is_test:
                continue  # exclude test callers
            # Discount by how many nodes share this target's name
            sharing = max(1, name_counts.get(node.name, 1))
            weighted += e.weight / sharing
        raw[node.node_id] = weighted

    max_val = max(raw.values()) if raw else 1.0
    if max_val > 0:
        return {k: v / max_val for k, v in raw.items()}
    return {k: 0.0 for k in raw}


def compute_fan_out(
    nodes: list["LNode"],
    graph: "LayeredGraph",
) -> dict[str, float]:
    """Normalised call out-degree — how many distinct functions this node calls."""
    raw: dict[str, float] = {}
    for node in nodes:
        out_edges = graph.out_adj.get(node.node_id, [])
        raw[node.node_id] = float(sum(
            1 for e in out_edges if e.kind == EdgeKind.CALLS
        ))
    max_val = max(raw.values()) if raw else 1.0
    if max_val > 0:
        return {k: v / max_val for k, v in raw.items()}
    return {k: 0.0 for k in raw}


def compute_complexity(nodes: list["LNode"]) -> dict[str, float]:
    """token_cost as a proxy for function complexity, normalised."""
    raw = {n.node_id: float(n.token_cost) for n in nodes}
    max_val = max(raw.values()) if raw else 1.0
    if max_val > 0:
        return {k: v / max_val for k, v in raw.items()}
    return {k: 0.0 for k in raw}


def compute_test_cover(
    nodes: list["LNode"],
    graph: "LayeredGraph",
) -> dict[str, float]:
    """Binary: 1.0 if node has TESTED_BY edge, else 0.0."""
    return {
        n.node_id: 1.0 if any(
            e.kind == EdgeKind.TESTED_BY
            for e in graph.in_adj.get(n.node_id, [])
        ) else 0.0
        for n in nodes
    }


# ---------------------------------------------------------------------------
# Combined scorer
# ---------------------------------------------------------------------------

class NodeScorer:
    """Scores a set of nodes for a given query and intent.

    Usage:
        scorer = NodeScorer(graph, query, intent)
        scores = scorer.score_all(nodes)   # {node_id: float}
    """

    def __init__(
        self,
        graph: "LayeredGraph",
        query: str,
        intent: str,
        texts: dict[str, str],   # node_id -> serialized text (pre-computed)
        weight_override: dict[str, float] | None = None,
    ):
        self._graph  = graph
        self._query  = query
        self._intent = intent
        self._texts  = texts
        if weight_override is not None:
            base = _WEIGHTS.get(intent, _WEIGHTS[QueryIntent.BUG])
            keys = ("bm25", "fan_in", "fan_out", "complexity", "test_cover")
            self._weights = tuple(
                weight_override.get(k, base[i]) for i, k in enumerate(keys)
            )
        else:
            self._weights = _WEIGHTS.get(intent, _WEIGHTS[QueryIntent.BUG])

        # Pre-compute name sharing counts for fan_in discount
        self._name_counts: dict[str, int] = Counter(
            n.name for n in graph.nodes.values()
            if n.layer.name == "FUNCTION"
        )

    def score_all(self, nodes: list["LNode"]) -> dict[str, float]:
        """Compute combined intent-weighted score for each node."""
        if not nodes:
            return {}

        w_bm25, w_fan_in, w_fan_out, w_complex, w_test = self._weights

        # Compute each signal
        bm25     = compute_bm25(self._query, nodes, self._texts)
        fan_in   = compute_fan_in(nodes, self._graph, self._name_counts)  if w_fan_in   > 0 else {}
        fan_out  = compute_fan_out(nodes, self._graph)                    if w_fan_out  > 0 else {}
        complex_ = compute_complexity(nodes)                              if w_complex  > 0 else {}
        test     = compute_test_cover(nodes, self._graph)                 if w_test     > 0 else {}

        scores: dict[str, float] = {}
        for node in nodes:
            nid = node.node_id
            s = (
                w_bm25   * bm25.get(nid, 0.0)
              + w_fan_in  * fan_in.get(nid, 0.0)
              + w_fan_out * fan_out.get(nid, 0.0)
              + w_complex * complex_.get(nid, 0.0)
              + w_test    * test.get(nid, 0.0)
            )
            scores[nid] = s

        return scores

    def explain(self, node: "LNode") -> dict[str, float]:
        """Return per-signal breakdown for a single node (for debugging)."""
        w_bm25, w_fan_in, w_fan_out, w_complex, w_test = self._weights
        bm25    = compute_bm25(self._query, [node], self._texts)
        fan_in  = compute_fan_in([node], self._graph, self._name_counts)
        fan_out = compute_fan_out([node], self._graph)
        complex_= compute_complexity([node])
        test    = compute_test_cover([node], self._graph)
        nid = node.node_id
        return {
            "bm25":       round(bm25.get(nid, 0.0), 4),
            "fan_in":     round(fan_in.get(nid, 0.0), 4),
            "fan_out":    round(fan_out.get(nid, 0.0), 4),
            "complexity": round(complex_.get(nid, 0.0), 4),
            "test_cover": round(test.get(nid, 0.0), 4),
            "weights":    dict(zip(
                ("bm25", "fan_in", "fan_out", "complexity", "test_cover"),
                self._weights
            )),
        }
