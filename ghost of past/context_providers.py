"""context_providers.py — Token-budget-fair context providers for the agent harness.

Each provider takes (query, graph, flat_nodes, repo_root, budget) and returns a
context string ready to inject into the agent prompt.

All providers respect the same token budget. Flat retrievers fill greedily from
their ranked function list using source bodies. TACM-v2 uses its layered selection.

Layer 04 — Variable Layer:
  TACM-v2 includes an optional Layer 04 (DYNAMIC) that adapts its granularity
  based on query intent and the agent's current context gap:
    - BUG + high complexity score → include call-chain snippets (callers of GT fn)
    - EXPLAIN → include cross-file dependency summaries
    - STRUCTURE → include module-level docstrings and __all__ exports
  Layer 04 nodes are generated on-the-fly from graph edges, not pre-serialized.
  They sit between CLASS and FUNCTION in token budget allocation for BUG intent,
  and consume up to 10% of budget.

  This layer is not part of the base TACM-v2 used in Experiment 02. It is
  proposed here and will be ablated in Experiment 03 (TACM-v2 vs TACM-v2+L4).
"""

from __future__ import annotations

import math
import re
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Token counting (shared, consistent with bench_v2.py)
# ---------------------------------------------------------------------------

def _count_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def _read_source(file_path: str, line_start: int, line_end: int) -> str:
    try:
        lines = Path(file_path).read_text(errors="replace").splitlines()
        return "\n".join(lines[max(0, line_start - 1): line_end])
    except OSError:
        return ""


def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


# ---------------------------------------------------------------------------
# Naive provider — repo file tree only
# ---------------------------------------------------------------------------

def naive_context(repo_root: Path, budget: int) -> str:
    """No retrieval. Agent gets a directory listing only."""
    try:
        r = __import__("subprocess").run(
            ["find", ".", "-name", "*.py", "-not", "-path", "./.git/*",
             "-not", "-path", "*/node_modules/*"],
            cwd=repo_root, capture_output=True, text=True, timeout=10,
        )
        listing = r.stdout.strip()
    except Exception:
        listing = "(could not list files)"
    header = f"Repository: {repo_root.name}\nPython files:\n"
    full = header + listing
    return full[:budget * 4]   # rough char limit


# ---------------------------------------------------------------------------
# BM25 provider
# ---------------------------------------------------------------------------

def bm25_context(query: str, flat_nodes, budget: int) -> str:
    """BM25-ranked function bodies, greedy fill to budget."""
    prod = [n for n in flat_nodes if not n.is_test]
    if not prod:
        return ""

    q_tokens = _tokenize(query)
    corpus_texts = [
        _read_source(n.file_path, n.line_start or 0, n.line_end or 0) or n.name
        for n in prod
    ]
    corpus = [_tokenize(t) for t in corpus_texts]
    N = len(corpus)
    k1, b = 1.5, 0.75

    df: dict[str, int] = {}
    for doc in corpus:
        for term in set(doc):
            df[term] = df.get(term, 0) + 1

    if not q_tokens:
        return _pack_bodies(list(zip([0.0] * N, prod, corpus_texts)), budget)

    idf = {
        t: math.log((N - df.get(t, 0) + 0.5) / (df.get(t, 0) + 0.5) + 1)
        for t in q_tokens
    }
    avgdl = sum(len(d) for d in corpus) / N if N else 1.0

    scored = []
    for node, doc, raw in zip(prod, corpus, corpus_texts):
        dl = len(doc)
        tf_map: dict[str, int] = {}
        for term in doc:
            tf_map[term] = tf_map.get(term, 0) + 1
        s = sum(
            idf.get(t, 0.0) * (
                tf_map.get(t, 0) * (k1 + 1) /
                (tf_map.get(t, 0) + k1 * (1 - b + b * dl / avgdl))
            )
            for t in q_tokens
        )
        scored.append((s, node, raw))

    scored.sort(key=lambda x: -x[0])
    return _pack_bodies(scored, budget)


def _pack_bodies(scored: list[tuple], budget: int) -> str:
    """Greedily pack function bodies until budget exhausted."""
    parts = []
    remaining = budget
    for _, node, body in scored:
        if not body:
            continue
        header = f"\n# {getattr(node, 'qualified_name', node.name)} [{getattr(node, 'file_path', '')}]\n"
        block = header + body
        cost = _count_tokens(block)
        if cost <= remaining:
            parts.append(block)
            remaining -= cost
        if remaining <= 0:
            break
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Dense embedding provider (MiniLM / CodeSearch)
# ---------------------------------------------------------------------------

def dense_context(query: str, index_tuple: tuple, budget: int, model_type: str = "st") -> str:
    """Dense cosine-ranked function bodies, greedy fill to budget."""
    if index_tuple is None:
        return ""
    import numpy as np

    ids, mat, model = index_tuple
    if model_type == "voyage":
        resp = model.embed([query], model="voyage-code-3", input_type="query")
        q_vec = np.array(resp.embeddings[0], dtype="float32")
    elif model_type == "openai":
        resp = model.embeddings.create(input=[query[:32000]], model="text-embedding-3-small")
        q_vec = np.array(resp.data[0].embedding, dtype="float32")
    else:
        q_vec = model.encode([query], normalize_embeddings=True)[0]

    q_vec = q_vec / max(np.linalg.norm(q_vec), 1e-9)
    sims = mat @ q_vec
    order = np.argsort(-sims)

    parts = []
    remaining = budget
    for i in order:
        nid, fpath = ids[i]
        # Read source from file path embedded in node_id
        try:
            body = Path(fpath).read_text(errors="replace") if fpath and Path(fpath).exists() else ""
        except Exception:
            body = ""
        if not body:
            body = nid.split("::")[-1]
        header = f"\n# {nid} [{fpath}]\n"
        block = header + body[:4000]
        cost = _count_tokens(block)
        if cost <= remaining:
            parts.append(block)
            remaining -= cost
        if remaining <= 0:
            break
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Hybrid RRF provider
# ---------------------------------------------------------------------------

def hybrid_context(query: str, flat_nodes, dense_index: tuple, budget: int) -> str:
    """BM25 + dense RRF, greedy fill to budget."""
    import numpy as np
    from collections import defaultdict

    prod = [n for n in flat_nodes if not n.is_test]
    if not prod:
        return ""

    # BM25 ranks
    bm25_ranked = _bm25_rank(query, prod)
    bm25_pos = {nid: i for i, (nid, _) in enumerate(bm25_ranked)}

    # Dense ranks
    if dense_index is not None:
        ids, mat, model = dense_index
        q_vec = model.encode([query], normalize_embeddings=True)[0]
        sims = mat @ q_vec
        order = np.argsort(-sims)
        dense_pos = {ids[i][0]: rank for rank, i in enumerate(order)}
    else:
        dense_pos = {}

    # RRF fusion
    k = 60
    scores: dict[str, float] = defaultdict(float)
    for nid, rank in bm25_pos.items():
        scores[nid] += 1.0 / (k + rank)
    for nid, rank in dense_pos.items():
        scores[nid] += 1.0 / (k + rank)

    node_map = {n.qualified_name: n for n in prod}
    ranked = sorted(scores.items(), key=lambda x: -x[1])

    parts = []
    remaining = budget
    for nid, _ in ranked:
        node = node_map.get(nid)
        if node is None:
            continue
        body = _read_source(node.file_path, node.line_start or 0, node.line_end or 0)
        if not body:
            continue
        header = f"\n# {nid} [{node.file_path}]\n"
        block = header + body
        cost = _count_tokens(block)
        if cost <= remaining:
            parts.append(block)
            remaining -= cost
        if remaining <= 0:
            break
    return "\n".join(parts)


def _bm25_rank(query: str, nodes) -> list[tuple[str, str]]:
    q_tokens = _tokenize(query)
    corpus_texts = [
        _read_source(n.file_path, n.line_start or 0, n.line_end or 0) or n.name
        for n in nodes
    ]
    corpus = [_tokenize(t) for t in corpus_texts]
    N = len(corpus)
    if not q_tokens or N == 0:
        return [(n.qualified_name, n.file_path or "") for n in nodes]

    k1, b = 1.5, 0.75
    df: dict[str, int] = {}
    for doc in corpus:
        for term in set(doc):
            df[term] = df.get(term, 0) + 1
    idf = {t: math.log((N - df.get(t, 0) + 0.5) / (df.get(t, 0) + 0.5) + 1) for t in q_tokens}
    avgdl = sum(len(d) for d in corpus) / N

    scored = []
    for node, doc in zip(nodes, corpus):
        dl = len(doc)
        tf_map: dict[str, int] = {}
        for term in doc:
            tf_map[term] = tf_map.get(term, 0) + 1
        s = sum(idf.get(t, 0.0) * (tf_map.get(t, 0) * (k1 + 1) /
                (tf_map.get(t, 0) + k1 * (1 - b + b * dl / avgdl)))
                for t in q_tokens)
        scored.append((s, node))
    scored.sort(key=lambda x: -x[0])
    return [(n.qualified_name, n.file_path or "") for _, n in scored]


# ---------------------------------------------------------------------------
# TACM-v2 provider (standard)
# ---------------------------------------------------------------------------

def tacm_context(graph, query: str, budget: int) -> str:
    """TACM-v2 layered selection, serialized as agent-readable context."""
    from tacm_v2.selector.selector import select
    sel = select(graph, query, token_budget=budget)
    return sel.context_text()


def tacm_dynamic_context(graph, query: str, budget: int) -> str:
    """TACM-v2 with dynamic cross-layer budget allocation."""
    from tacm_v2.selector.selector import select_dynamic
    sel = select_dynamic(graph, query, token_budget=budget)
    return sel.context_text()


# ---------------------------------------------------------------------------
# TACM-v2 + Layer 04 (Variable Layer) — proposed for Experiment 03 ablation
# ---------------------------------------------------------------------------

def _append_l4_context(graph, query: str, budget: int, dynamic_base: bool) -> str:
    """Shared Layer 04 appender for TACM selectors.

    Layer 04 is a dynamic context layer generated on-the-fly from graph edges.
    It adapts its content based on query intent:

    BUG intent:
        For each selected FUNCTION node, include its top-2 callers (fan-in)
        as short snippets: "called by: FileLoader.load() [loader.py:42]"
        Rationale: knowing what calls the buggy function helps the agent
        understand the impact radius and the fix's downstream consequences.

    EXPLAIN intent:
        Include cross-file import chains: which modules import this function,
        and what they use it for (the call sites).

    STRUCTURE intent:
        Include module-level docstrings and __all__ exports for selected FILES.

    Budget: Layer 04 consumes up to L4_BUDGET_FRAC of total budget,
    taken from whatever remains after FUNCTION layer fill.
    """
    from tacm_v2.selector.selector import select, select_dynamic
    from tacm_v2.selector.intent import classify_intent
    from tacm_v2.graph.model import EdgeKind

    L4_BUDGET_FRAC = 0.10   # Layer 04 gets up to 10% of total budget
    l4_budget = int(budget * L4_BUDGET_FRAC)
    base_budget = budget - l4_budget

    intent = classify_intent(query)
    selector = select_dynamic if dynamic_base else select
    sel = selector(graph, query, token_budget=base_budget)
    base_text = sel.context_text()

    l4_parts = []
    remaining = l4_budget

    if intent.lower() == "bug":
        # For each selected function, add its top callers as short context snippets
        fn_nodes = [sn for sn in sel.nodes if sn.layer.name == "FUNCTION"]
        caller_lines: dict[str, list[str]] = {}

        for sn in fn_nodes:
            node = sn.node
            in_edges = graph.in_adj.get(node.node_id, [])
            callers = []
            for e in in_edges:
                if e.kind != EdgeKind.CALLS:
                    continue
                src = graph.nodes.get(e.source_id)
                if src is None or src.is_test:
                    continue
                # Short caller snippet: qualified name + file + line
                fpath = src.file_path or ""
                rel = Path(fpath).name if fpath else "?"
                callers.append(f"  called by: {src.name} [{rel}]")
            if callers:
                caller_lines[node.node_id] = callers[:2]   # top 2 callers only

        for node_id, lines in caller_lines.items():
            snippet = "# call-chain context\n" + "\n".join(lines) + "\n"
            cost = _count_tokens(snippet)
            if cost <= remaining:
                l4_parts.append(snippet)
                remaining -= cost

    elif intent.lower() == "explain":
        # Cross-file import context: who imports each selected file?
        file_nodes = [sn for sn in sel.nodes if sn.layer.name == "FILE"]
        for sn in file_nodes:
            node = sn.node
            in_edges = graph.in_adj.get(node.node_id, [])
            importers = []
            for e in in_edges:
                if e.kind not in (EdgeKind.IMPORTS_FROM,):
                    continue
                src = graph.nodes.get(e.source_id)
                if src is None:
                    continue
                rel = Path(src.file_path or "").name
                importers.append(f"  imported by: {rel}")
            if importers:
                snippet = f"# import context for {Path(node.file_path or '').name}\n"
                snippet += "\n".join(importers[:3]) + "\n"
                cost = _count_tokens(snippet)
                if cost <= remaining:
                    l4_parts.append(snippet)
                    remaining -= cost

    elif intent.lower() == "structure":
        # Module docstrings for selected files
        file_nodes = [sn for sn in sel.nodes if sn.layer.name == "FILE"]
        for sn in file_nodes:
            node = sn.node
            if not node.file_path:
                continue
            try:
                source = Path(node.file_path).read_text(errors="replace")
                # Extract module docstring (first triple-quoted string)
                import ast
                tree = ast.parse(source)
                docstring = ast.get_docstring(tree)
                if docstring:
                    snippet = f"# module docstring: {Path(node.file_path).name}\n"
                    snippet += f'"""{docstring[:300]}"""\n'
                    cost = _count_tokens(snippet)
                    if cost <= remaining:
                        l4_parts.append(snippet)
                        remaining -= cost
            except Exception:
                pass

    l4_text = "\n".join(l4_parts)
    if l4_text:
        return base_text + "\n\n# --- Layer 04: Variable context ---\n" + l4_text
    return base_text


def tacm_l4_context(graph, query: str, budget: int) -> str:
    """TACM-v2 + Layer 04 (Variable Layer) on top of standard selector."""
    return _append_l4_context(graph, query, budget, dynamic_base=False)


def tacm_dyn_l4_context(graph, query: str, budget: int) -> str:
    """TACM-v2 dynamic selector + Layer 04 caller/import/doc context."""
    return _append_l4_context(graph, query, budget, dynamic_base=True)


# ---------------------------------------------------------------------------
# TACM-full provider — no budget cutoff (pure retrieval quality measurement)
#
# Ranks all non-test FUNCTION nodes by TACM's hybrid score (BM25 50% + fan_in
# 25% + fan_out 10% + complexity 15% for BUG intent), then greedily packs
# function bodies in rank order until the token budget is exhausted.
#
# The key difference from `tacm`:
#   - `tacm`      splits budget across FILE/CLASS/FUNCTION layers (~164 fn slots)
#   - `tacm-full` gives all budget to FUNCTION layer — same coverage as BM25
#                 but ranked by TACM's graph-aware hybrid score instead of BM25
#
# Use this condition to compare TACM scoring quality vs BM25 scoring quality
# without the token-budget exclusion artifact contaminating the result.
# ---------------------------------------------------------------------------

def tacm_full_context(graph, query: str, budget: int) -> str:
    """TACM hybrid scoring over all functions, no layer budget split."""
    from tacm_v2.selector.scoring import NodeScorer
    from tacm_v2.layers.serializers import serialize
    from tacm_v2.selector.intent import classify_intent
    from tacm_v2.graph.model import Layer

    intent = classify_intent(query)

    fn_nodes = [n for n in graph.nodes_at_layer(Layer.FUNCTION) if not n.is_test]
    if not fn_nodes:
        return ""

    all_nodes = [n for n in graph.nodes.values() if not n.is_test]
    texts = {n.node_id: serialize(n, graph) for n in all_nodes}

    scorer = NodeScorer(graph, query, intent, texts)
    scores = scorer.score_all(fn_nodes)

    ranked = sorted(fn_nodes, key=lambda n: -scores[n.node_id])

    parts = []
    remaining = budget
    for node in ranked:
        # Use actual source body for the agent (same as bm25_context does)
        body = _read_source(node.file_path or "", node.line_start or 0, node.line_end or 0)
        if not body:
            body = texts.get(node.node_id, node.name)
        header = f"\n# {getattr(node, 'qualified_name', node.name)} [{node.file_path or ''}]\n"
        block = header + body
        cost = _count_tokens(block)
        if cost <= remaining:
            parts.append(block)
            remaining -= cost
        if remaining <= 0:
            break

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Provider registry — used by agent_harness.py
# ---------------------------------------------------------------------------

PROVIDERS = {
    "naive":      "naive",
    "bm25":       "bm25",
    "minilm":     "minilm",        # Dense MiniLM (Cursor default)
    "codesearch": "codesearch",    # Dense CodeSearch (code-specific embedding)
    "hybrid":     "hybrid",        # BM25 + MiniLM RRF
    "hybrid-cs":  "hybrid-cs",     # BM25 + CodeSearch RRF
    "tacm":       "tacm",
    "tacm-dyn":   "tacm-dyn",      # TACM-v2 with dynamic cross-layer budget
    "tacm-l4":    "tacm-l4",       # TACM-v2 + Layer 04
    "tacm-dyn-l4":"tacm-dyn-l4",   # TACM-v2 dynamic selector + Layer 04
    "tacm-full":  "tacm-full",     # TACM scoring, no layer budget split (benchmarking only)
}
