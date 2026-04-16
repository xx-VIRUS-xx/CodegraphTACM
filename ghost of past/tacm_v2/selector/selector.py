"""selector.py — Context pool selectors for the layered graph.

Two selectors are provided:

1. `select()`:
   Original TACM-v2 behavior. Scores nodes by layer, allocates a fixed per-layer
   budget from query intent, then greedily fills each layer in order.

2. `select_dynamic()`:
   Cross-layer budget allocation. It seeds a small amount of structure, then
   lets all remaining nodes compete for budget globally. This targets the main
   weakness seen in Experiment 03: hard function exclusion caused by rigid layer
   quotas, even when highly relevant functions remain.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from ..graph.model import Layer, LayeredGraph, LNode
from ..layers.serializers import serialize, serialize_function_for_scoring
from .intent import classify_intent, LAYER_BUDGETS as _LAYER_BUDGETS
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


def _prepare_serialized_texts(
    graph: LayeredGraph,
    exclude_tests: bool,
) -> tuple[list[LNode], dict[str, str], dict[str, str]]:
    """Return all selectable nodes plus agent/scoring text views."""
    all_nodes = [
        n for n in graph.nodes.values()
        if not (exclude_tests and n.is_test)
    ]
    agent_texts: dict[str, str] = {n.node_id: serialize(n, graph) for n in all_nodes}
    score_texts: dict[str, str] = {
        n.node_id: (
            serialize_function_for_scoring(n, graph)
            if n.layer == Layer.FUNCTION
            else agent_texts[n.node_id]
        )
        for n in all_nodes
    }
    return all_nodes, agent_texts, score_texts


# ---------------------------------------------------------------------------
# Adaptive overflow constants (used by both selectors)
# ---------------------------------------------------------------------------

DEFAULT_MAX_OVERFLOW_RATIO = 0.5     # up to 50% extra tokens beyond base budget
DEFAULT_OVERFLOW_SCORE_FLOOR = 0.25  # minimum score to enter overflow at all


def _count_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def _overflow_quality_gate(
    overflow_used: int,
    max_overflow: int,
    score_floor: float,
) -> float:
    """Rising quality gate: easier at start of overflow, harder near the cap.

    Returns the minimum score a node must have to be accepted into overflow.

    At 0% overflow consumed → gate = score_floor          (permissive)
    At 100% overflow consumed → gate = 1.0                (impossible)
    Linear ramp in between.
    """
    if max_overflow <= 0:
        return 1.0  # no overflow allowed
    progress = min(1.0, overflow_used / max_overflow)
    return score_floor + progress * (1.0 - score_floor)


def select(
    graph: LayeredGraph,
    query: str,
    token_budget: int,
    intent: Optional[str] = None,
    exclude_tests: bool = True,
    max_overflow_ratio: float = DEFAULT_MAX_OVERFLOW_RATIO,
    overflow_score_floor: float = DEFAULT_OVERFLOW_SCORE_FLOOR,
) -> SelectionResult:
    """Main entry point. Returns selected nodes, with adaptive overflow.

    The base budget is allocated per-layer as before. After the FUNCTION layer
    fills its base quota, an **overflow zone** allows additional high-scoring
    functions to be included. The overflow zone is bounded by
    ``token_budget * max_overflow_ratio`` extra tokens, and each candidate must
    clear a rising quality gate to be admitted.

    Args:
        graph:                The LayeredGraph for the repo.
        query:                Natural language query.
        token_budget:         Base token budget (hard floor for the base phase).
        intent:               Override intent classification (for testing/ablation).
        exclude_tests:        Skip test nodes (default True).
        max_overflow_ratio:   Fraction of token_budget available as overflow (default 0.5).
        overflow_score_floor: Minimum score to enter overflow at all (default 0.25).
    """
    if intent is None:
        intent = classify_intent(query)

    file_frac, class_frac, _ = _LAYER_BUDGETS[intent]
    file_budget  = int(token_budget * file_frac)
    class_budget = int(token_budget * class_frac)
    fn_budget    = token_budget - file_budget - class_budget

    selected: list[SelectedNode] = []
    layer_counts: dict[str, int] = {}

    all_nodes, agent_texts, score_texts = _prepare_serialized_texts(graph, exclude_tests)

    # Build one scorer for the whole query — shared across all layers
    scorer = NodeScorer(graph, query, intent, score_texts)

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
            text = agent_texts[node.node_id]
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
            elif (
                layer == Layer.FUNCTION
                and max_overflow_ratio > 0
                and remaining <= 0
            ):
                # --- Adaptive overflow for FUNCTION layer ---
                # Once the base fn budget is consumed, allow high-scoring
                # functions into an overflow zone with a rising quality gate.
                max_overflow = int(token_budget * max_overflow_ratio)
                overflow_used = -remaining  # how far past zero we've gone
                if overflow_used + cost > max_overflow:
                    continue  # would exceed hard cap
                gate = _overflow_quality_gate(
                    overflow_used, max_overflow, overflow_score_floor,
                )
                if score >= gate:
                    selected.append(SelectedNode(
                        node=node,
                        layer=layer,
                        text=text,
                        token_cost=cost,
                        score=score,
                        intent=intent,
                    ))
                    selected_ids.add(node.node_id)
                    remaining -= cost  # goes further negative
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


def _diversity_penalty(
    node: LNode,
    parent_counts: dict[str, int],
    file_counts: dict[str, int],
) -> float:
    """Return a bounded redundancy penalty for over-clustered selections.

    Intuition:
      A coherent local neighborhood is useful, but after selecting several
      nodes from the same parent/file, additional siblings often become less
      valuable than the best function from a nearby but distinct area.

    Policy:
      - first 2 children from a parent are free
      - first 3 nodes from a file are free
      - penalty grows gently after that, capped so relevance still dominates
    """
    penalty = 0.0
    if node.parent_id:
        extra_siblings = max(0, parent_counts.get(node.parent_id, 0) - 1)
        penalty += min(0.12, 0.04 * extra_siblings)

    if node.file_path:
        extra_file_nodes = max(0, file_counts.get(node.file_path, 0) - 2)
        penalty += min(0.12, 0.03 * extra_file_nodes)

    return min(0.18, penalty)


def select_dynamic(
    graph: LayeredGraph,
    query: str,
    token_budget: int,
    intent: Optional[str] = None,
    exclude_tests: bool = True,
    max_overflow_ratio: float = DEFAULT_MAX_OVERFLOW_RATIO,
    overflow_score_floor: float = DEFAULT_OVERFLOW_SCORE_FLOOR,
) -> SelectionResult:
    """Cross-layer TACM selector with dynamic budget allocation + overflow.

    Strategy:
    1. Score each layer independently with the same NodeScorer.
    2. Seed a minimal structural skeleton (top FILE and top CLASS when useful).
    3. Let all remaining nodes compete for the rest of the budget globally.
    4. Apply the same containment bonus during global selection.
    5. **Overflow**: after the base budget is consumed, continue selecting nodes
       that clear a rising quality gate, up to ``token_budget * max_overflow_ratio``
       additional tokens.

    This keeps TACM's structural priors while avoiding the rigid layer split
    that excluded too many functions in the budgeted Experiment 03 setting.
    """
    if intent is None:
        intent = classify_intent(query)

    selected: list[SelectedNode] = []
    selected_ids: set[str] = set()
    layer_counts: dict[str, int] = {}
    parent_counts: dict[str, int] = {}
    file_counts: dict[str, int] = {}

    all_nodes, agent_texts, score_texts = _prepare_serialized_texts(graph, exclude_tests)
    scorer = NodeScorer(graph, query, intent, score_texts)

    by_layer: dict[Layer, list[LNode]] = {
        layer: [
            n for n in graph.nodes_at_layer(layer)
            if not (exclude_tests and n.is_test)
        ]
        for layer in (Layer.FILE, Layer.CLASS, Layer.FUNCTION)
    }
    base_scores: dict[str, float] = {}
    for layer, nodes in by_layer.items():
        if nodes:
            base_scores.update(scorer.score_all(nodes))

    remaining = token_budget
    containment_bonus = 0.15

    # Seed a tiny amount of structure so the global pass has something to
    # attach to, but do not pre-commit large quotas by layer.
    seed_targets = {
        "bug": (1, 1),
        "explain": (1, 1),
        "structure": (2, 2),
    }
    seed_files, seed_classes = seed_targets.get(intent, (1, 1))

    def _pick_top_seed(layer: Layer, count: int) -> None:
        nonlocal remaining
        if count <= 0:
            return
        ranked = sorted(
            by_layer.get(layer, []),
            key=lambda n: -base_scores.get(n.node_id, 0.0),
        )
        picked = 0
        for node in ranked:
            if node.node_id in selected_ids:
                continue
            text = agent_texts[node.node_id]
            cost = _count_tokens(text)
            if cost > remaining:
                continue
            selected.append(SelectedNode(
                node=node,
                layer=layer,
                text=text,
                token_cost=cost,
                score=base_scores.get(node.node_id, 0.0),
                intent=intent,
            ))
            selected_ids.add(node.node_id)
            layer_counts[layer.name] = layer_counts.get(layer.name, 0) + 1
            if node.parent_id:
                parent_counts[node.parent_id] = parent_counts.get(node.parent_id, 0) + 1
            if node.file_path:
                file_counts[node.file_path] = file_counts.get(node.file_path, 0) + 1
            remaining -= cost
            picked += 1
            if picked >= count:
                break

    _pick_top_seed(Layer.FILE, seed_files)
    _pick_top_seed(Layer.CLASS, seed_classes)

    # Global competition for the remaining budget, then overflow.
    max_overflow = int(token_budget * max_overflow_ratio)
    remaining_nodes = [n for n in all_nodes if n.node_id not in selected_ids]
    in_overflow = False

    while remaining_nodes:
        best_node: LNode | None = None
        best_score = -1.0
        best_cost = 0

        for node in remaining_nodes:
            text = agent_texts[node.node_id]
            cost = _count_tokens(text)

            # Budget check: base phase vs overflow phase
            if remaining > 0:
                if cost > remaining:
                    continue
            else:
                # In overflow phase — check hard cap
                overflow_used = -remaining
                if overflow_used + cost > max_overflow:
                    continue

            adjusted = base_scores.get(node.node_id, 0.0)
            if node.parent_id and node.parent_id in selected_ids:
                adjusted = min(1.0, adjusted + containment_bonus)
            adjusted = max(0.0, adjusted - _diversity_penalty(node, parent_counts, file_counts))

            if adjusted > best_score:
                best_node = node
                best_score = adjusted
                best_cost = cost

        if best_node is None:
            break

        # In overflow phase, apply the quality gate
        if remaining <= 0:
            overflow_used = -remaining
            gate = _overflow_quality_gate(
                overflow_used, max_overflow, overflow_score_floor,
            )
            if best_score < gate:
                break  # best candidate can't clear the gate — stop
            if not in_overflow:
                in_overflow = True

        selected.append(SelectedNode(
            node=best_node,
            layer=best_node.layer,
            text=agent_texts[best_node.node_id],
            token_cost=best_cost,
            score=best_score,
            intent=intent,
        ))
        selected_ids.add(best_node.node_id)
        layer_counts[best_node.layer.name] = layer_counts.get(best_node.layer.name, 0) + 1
        if best_node.parent_id:
            parent_counts[best_node.parent_id] = parent_counts.get(best_node.parent_id, 0) + 1
        if best_node.file_path:
            file_counts[best_node.file_path] = file_counts.get(best_node.file_path, 0) + 1
        remaining -= best_cost
        remaining_nodes = [n for n in remaining_nodes if n.node_id != best_node.node_id]

    total = sum(n.token_cost for n in selected)
    return SelectionResult(
        nodes=selected,
        total_tokens=total,
        budget=token_budget,
        intent=intent,
        layer_counts=layer_counts,
    )
