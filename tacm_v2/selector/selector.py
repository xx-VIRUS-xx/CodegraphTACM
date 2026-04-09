"""selector.py — Context pool selector for the layered graph.

Given a query and a token budget, the selector:

1. Scores every node across all three layers using graph signals + query relevance
2. Decides the layer mix — how much budget to spend at each abstraction level
3. Picks the specific nodes within each layer to fill the budget

The layer mix is driven by query intent:
    "structure / overview / architecture"  → more FILE + CLASS, less FUNCTION
    "bug / why / failing / error"          → more FUNCTION, some CLASS for context
    "what does X do / explain"             → CLASS + FUNCTION mix

Within each layer, nodes are scored by:
    - Query relevance: BM25 on the serialized text of that node at its layer
    - Graph centrality: weighted in-degree (how many things point to this node)
    - Containment bonus: if a selected parent is already in context, its children
      score higher (they explain something the selector already showed the LLM)

Selection uses a greedy fill per layer: sort by score, take until layer budget exhausted.
The selector is intentionally simple — correctness before cleverness.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from ..graph.model import Layer, LayeredGraph, LNode, EdgeKind
from ..layers.serializers import serialize, serialized_token_cost
from .intent import QueryIntent, classify_intent, LAYER_BUDGETS as _LAYER_BUDGETS
from .scoring import NodeScorer


# ---------------------------------------------------------------------------
# Selected node result
# ---------------------------------------------------------------------------

@dataclass
class SelectedNode:
    node:        LNode
    layer:       Layer
    text:        str          # serialized text at this layer
    token_cost:  int
    score:       float
    intent:      str          # which intent signal drove selection


# ---------------------------------------------------------------------------
# Selector
# ---------------------------------------------------------------------------

@dataclass
class SelectionResult:
    nodes:        list[SelectedNode]
    total_tokens: int
    budget:       int
    intent:       str
    layer_counts: dict[str, int] = field(default_factory=dict)

    def context_text(self, separator: str = "\n\n") -> str:
        """Concatenate all selected nodes into a single context string."""
        return separator.join(n.text for n in self.nodes)


def select(
    graph: LayeredGraph,
    query: str,
    token_budget: int,
    intent: Optional[str] = None,
    exclude_tests: bool = True,
) -> SelectionResult:
    """Main entry point. Returns selected nodes within token_budget.

    Args:
        graph:        The LayeredGraph for the repo.
        query:        Natural language query.
        token_budget: Maximum tokens to spend on context.
        intent:       Override intent classification (for testing/ablation).
        exclude_tests: Skip test nodes (default True).
    """
    if intent is None:
        intent = classify_intent(query)

    file_frac, class_frac, fn_frac = _LAYER_BUDGETS[intent]
    file_budget  = int(token_budget * file_frac)
    class_budget = int(token_budget * class_frac)
    fn_budget    = token_budget - file_budget - class_budget

    selected: list[SelectedNode] = []
    layer_counts: dict[str, int] = {}

    # Pre-serialize all nodes once — scorer and greedy fill both need the text
    all_nodes = [
        n for n in graph.nodes.values()
        if not (exclude_tests and n.is_test)
    ]
    texts: dict[str, str] = {n.node_id: serialize(n, graph) for n in all_nodes}

    # Build one scorer for the whole query — shared across all layers
    scorer = NodeScorer(graph, query, intent, texts)

    # Tracks node_ids selected so far — used for containment bonus.
    # Populated after each layer, read by the next layer down.
    selected_ids: set[str] = set()

    for layer, budget in [
        (Layer.FILE,     file_budget),
        (Layer.CLASS,    class_budget),
        (Layer.FUNCTION, fn_budget),
    ]:
        if budget <= 0:
            continue

        nodes = [
            n for n in graph.nodes_at_layer(layer)
            if not (exclude_tests and n.is_test)
        ]
        if not nodes:
            continue

        # Intent-aware scoring via NodeScorer
        scores = scorer.score_all(nodes)

        # Containment bonus — applied after base scoring.
        #
        # If a node's direct parent was selected in a higher layer,
        # add CONTAINMENT_BONUS to its score.
        #
        # Rationale: the LLM has already seen the class skeleton (methods list).
        # A function body from that class completes what the LLM was shown —
        # it's more coherent context than an unrelated function at the same score.
        #
        # The bonus (0.15) is intentionally modest:
        # - Strong enough to surface a method over a same-scored stranger
        # - Weak enough that an irrelevant method can't beat a clearly relevant
        #   function from elsewhere (base scores range [0, 1], so 0.15 is ~15%)
        CONTAINMENT_BONUS = 0.15
        for node in nodes:
            if node.parent_id and node.parent_id in selected_ids:
                scores[node.node_id] = min(1.0, scores[node.node_id] + CONTAINMENT_BONUS)

        node_scores = sorted(
            [(scores[n.node_id], n) for n in nodes],
            key=lambda x: -x[0],
        )

        # Greedy fill within this layer's budget
        remaining = budget
        count = 0
        for score, node in node_scores:
            text = texts[node.node_id]
            cost = _count_tokens(text)
            if cost <= remaining:
                selected.append(SelectedNode(
                    node=node,
                    layer=layer,
                    text=text,
                    token_cost=cost,
                    score=score,
                    intent=intent,
                ))
                selected_ids.add(node.node_id)
                remaining -= cost
                count += 1

        layer_counts[layer.name] = count

    total = sum(n.token_cost for n in selected)
    return SelectionResult(
        nodes=selected,
        total_tokens=total,
        budget=token_budget,
        intent=intent,
        layer_counts=layer_counts,
    )


def _count_tokens(text: str) -> int:
    return max(1, len(text) // 4)
