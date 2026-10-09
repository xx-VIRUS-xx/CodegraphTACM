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
    nbr_bonus   — adaptive neighborhood support from query-relevant callers/callees

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
from .config import DEFAULT_CONFIG, SelectorConfig
from .cache import get_scorer_cache, personalized_pagerank


# ---------------------------------------------------------------------------
# Signal computation
# ---------------------------------------------------------------------------

def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def _expand_query(
    query: str,
    graph: "LayeredGraph",
    expansion_cap: int = 12,
) -> str:
    """Structurally expand a query using graph neighbor names.

    When a query mentions a class or function name, add the names of its
    direct callers and callees to the query before BM25 scoring. This
    recovers cases where the bug is in a member function not named in the
    query (e.g. "WrappedRequest" → adds get_headers, authenticate, etc.).

    Only adds names longer than 3 chars to avoid noise from short tokens.
    ``expansion_cap`` bounds the number of extra terms to avoid diluting
    IDF weights on large graphs.
    """
    query_lower = query.lower()
    expansions: set[str] = set()

    for node in graph.nodes.values():
        if not node.name or len(node.name) < 4:
            continue
        parts = re.split(r"[_\s]", node.name.lower())
        if not any(p and p in query_lower for p in parts if len(p) > 3):
            continue
        for e in graph.out_adj.get(node.node_id, []):
            nb = graph.nodes.get(e.target_id)
            if nb and nb.name and len(nb.name) > 3 and not nb.is_test:
                expansions.add(nb.name.lower())
        for e in graph.in_adj.get(node.node_id, []):
            nb = graph.nodes.get(e.source_id)
            if nb and nb.name and len(nb.name) > 3 and not nb.is_test:
                expansions.add(nb.name.lower())

    if not expansions:
        return query
    extra = " ".join(list(expansions)[:expansion_cap])
    return query + " " + extra


_IDENT_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]{2,}")
_QUOTED_RE = re.compile(r"`([^`]+)`|\"([^\"]+)\"|'([^']+)'")


def _extract_query_identifiers(query: str) -> set[str]:
    """Extract code-like identifier tokens from a natural-language query.

    Pulls (a) backtick/quoted tokens verbatim, (b) any token that is
    CamelCase, snake_case, or dotted.foo.bar, and (c) their piece-wise
    identifier splits. Everything is lowercased. Used to seed aggressive
    BM25 variants and the identifier-exact-match side signal.
    """
    out: set[str] = set()
    for m in _QUOTED_RE.finditer(query):
        for g in m.groups():
            if g:
                out.add(g.lower())
                for part in re.split(r"[.\s]+", g):
                    if part:
                        out.add(part.lower())
                        out.update(_split_identifier(part))
    for tok in _IDENT_RE.findall(query):
        has_upper = any(c.isupper() for c in tok[1:])
        has_under = "_" in tok
        if not (has_upper or has_under):
            continue
        out.add(tok.lower())
        out.update(_split_identifier(tok))
    # Also pick up dotted paths like requests.auth.get_headers
    for tok in re.findall(r"[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]+)+", query):
        for part in tok.split("."):
            if part:
                out.add(part.lower())
                out.update(_split_identifier(part))
    return {t for t in out if len(t) >= 3}


def _cascading_bm25(
    query: str,
    nodes: list["LNode"],
    texts: dict[str, str],
    graph: "LayeredGraph",
    k1: float = 1.5,
    b: float = 0.75,
    expansion_cap: int = 12,
    identifier_expansion_enabled: bool = False,
) -> dict[str, float]:
    """Run BM25 over three query variants and return per-node maximum.

    Variants:
      1. Raw query
      2. camelCase/snake_case split (GetNewCommand → get new command)
      3. Structurally expanded query (class name → member function names)
      4. (Experiment 06) Aggressive identifier-token concatenation, when
         ``identifier_expansion_enabled`` is set.

    Taking the max rather than averaging ensures a strong hit on any variant
    is not diluted by weak hits on others.

    Opt-in via :data:`SelectorConfig.use_cascading_bm25` to preserve
    previous benchmark numbers by default.
    """
    split = re.sub(r"([A-Z])", r" \1", re.sub(r"_", " ", query)).lower()
    expanded = _expand_query(query, graph, expansion_cap=expansion_cap)

    variants = [query, split, expanded]
    if identifier_expansion_enabled:
        idents = _extract_query_identifiers(query)
        if idents:
            # Feed the raw identifiers (CamelCase intact) and their splits.
            # Keeping both forms means BM25 hits both `WrappedRequest` in
            # corpus text and `wrapped request` in split corpora.
            ident_blob = " ".join(idents)
            variants.append(ident_blob)
            variants.append(query + " " + ident_blob)

    variants = list(dict.fromkeys(variants))  # stable-dedup
    all_scores = [compute_bm25(q, nodes, texts, k1, b) for q in variants]

    return {
        n.node_id: max(s.get(n.node_id, 0.0) for s in all_scores)
        for n in nodes
    }


def compute_pagerank(
    nodes: list["LNode"],
    graph: "LayeredGraph",
    alpha: float = 0.85,
    max_iter: int = 50,
) -> dict[str, float]:
    """Simplified PageRank over the CALLS subgraph.

    PageRank weights a node's importance by the importance of its callers,
    not just their count. A function called by three critical orchestrators
    scores higher than one called by ten test helpers. This is a strictly
    better signal than raw fan_in for identifying architecturally central
    functions.

    Uses a sparse power-iteration implementation to avoid NetworkX dependency.
    Restricted to FUNCTION nodes; normalised to [0, 1].
    """
    # Build index over the scored node set only
    node_ids = {n.node_id for n in nodes}

    # Outgoing edges (for computing dangling nodes)
    out_links: dict[str, list[str]] = {}
    in_links: dict[str, list[tuple[str, float]]] = {n.node_id: [] for n in nodes}

    for node in nodes:
        targets = [
            (e.target_id, e.weight)
            for e in graph.out_adj.get(node.node_id, [])
            if e.kind == EdgeKind.CALLS and e.target_id in node_ids
        ]
        out_links[node.node_id] = [t for t, _ in targets]
        for t, w in targets:
            in_links[t].append((node.node_id, w))

    N = len(nodes)
    if N == 0:
        return {}

    rank = {n.node_id: 1.0 / N for n in nodes}

    for _ in range(max_iter):
        new_rank: dict[str, float] = {}
        dangling_sum = sum(
            rank[nid] for nid in node_ids if not out_links.get(nid)
        )
        for node in nodes:
            nid = node.node_id
            incoming = sum(
                rank[src] * w / max(1, len(out_links.get(src, [])))
                for src, w in in_links.get(nid, [])
            )
            new_rank[nid] = (
                (1 - alpha) / N
                + alpha * (incoming + dangling_sum / N)
            )
        rank = new_rank

    max_val = max(rank.values()) if rank else 1.0
    if max_val > 0:
        return {k: v / max_val for k, v in rank.items()}
    return rank


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
    # Guard against all-empty corpora (e.g. serializers returned empty strings
    # because source files weren't on disk). Without this the inner denom
    # computation divides by zero.
    if avgdl == 0:
        return {n.node_id: 0.0 for n in nodes}

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

    Discount is scoped to same-file sharing: `DataFrame.__init__` and
    `Series.__init__` in different files each get a discount of 1 (no
    sharing within their file), not 100 (all __init__ across the project).
    This preserves the disambiguation intent while not collapsing fan_in
    for genuinely important functions in large API-surface codebases.

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
            # Discount by how many nodes share this name *within the same file*.
            # Global name counts collapse fan_in to near-zero for common names
            # like __init__, get, apply when shared across 100+ classes.
            sharing = max(1, name_counts.get((node.name, node.file_path), 1))
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


def compute_neighborhood_bonus(
    nodes: list["LNode"],
    graph: "LayeredGraph",
    base_scores: dict[str, float],
) -> dict[str, float]:
    """Adaptive support from nearby query-relevant functions.

    Motivation:
      Bug-fixing often needs a small neighborhood rather than a single function.
      A target function becomes more patchable when one of its callers is also
      highly relevant. We therefore add a bounded bonus from neighboring CALLS
      edges, with callers weighted more strongly than callees.

    The bonus is intentionally local and bounded:
      - only FUNCTION nodes receive it
      - only CALLS neighbors contribute
      - callers matter more than callees
      - the final value is normalised to [0, 1] before scaling in score_all()
    """
    raw: dict[str, float] = {}
    for node in nodes:
        if node.layer.name != "FUNCTION":
            raw[node.node_id] = 0.0
            continue

        caller_support = 0.0
        callee_support = 0.0

        for e in graph.in_adj.get(node.node_id, []):
            if e.kind != EdgeKind.CALLS:
                continue
            src = graph.nodes.get(e.source_id)
            if src is None or src.is_test:
                continue
            caller_support += e.weight * base_scores.get(src.node_id, 0.0)

        for e in graph.out_adj.get(node.node_id, []):
            if e.kind != EdgeKind.CALLS:
                continue
            tgt = graph.nodes.get(e.target_id)
            if tgt is None or tgt.is_test:
                continue
            callee_support += e.weight * base_scores.get(tgt.node_id, 0.0)

        # Callers constrain bug fixes more often than callees, so they get a
        # larger contribution. Callees still help for orchestration functions.
        raw[node.node_id] = caller_support + 0.5 * callee_support

    max_val = max(raw.values()) if raw else 1.0
    if max_val > 0:
        return {k: v / max_val for k, v in raw.items()}
    return {k: 0.0 for k in raw}


# ---------------------------------------------------------------------------
# Identifier-match signals (FUNCTION disambiguation)
# ---------------------------------------------------------------------------

def _split_identifier(name: str) -> list[str]:
    """Split an identifier on _ and CamelCase into lowercase token list."""
    if not name:
        return []
    # Split snake_case, then CamelCase.
    pieces: list[str] = []
    for chunk in name.split("_"):
        pieces.extend(re.findall(r"[A-Z]+(?=[A-Z][a-z])|[A-Z]?[a-z0-9]+|[A-Z]+", chunk))
    return [p.lower() for p in pieces if p]


def compute_name_match(
    query: str,
    nodes: list["LNode"],
    graph: "LayeredGraph",
    min_len: int = 3,
) -> dict[str, float]:
    """Fraction of (informative) query tokens that appear in the function's
    bare name or its qualified name (ClassName.method).

    BM25 on 150-token bodies drowns out name hits. This signal isolates the
    name channel so that ``build_digest_header`` wins on a query like
    "digest header" even when sibling methods share the rest of the corpus.
    Computed only for FUNCTION nodes; other layers get 0.
    """
    q_tokens = {t for t in _tokenize(query) if len(t) >= min_len}
    if not q_tokens:
        return {n.node_id: 0.0 for n in nodes}

    raw: dict[str, float] = {}
    for node in nodes:
        if node.layer.name != "FUNCTION":
            raw[node.node_id] = 0.0
            continue

        # Build identifier token set from bare + qualified name.
        tokens: set[str] = set(_split_identifier(node.name))
        parent = graph.nodes.get(node.parent_id) if node.parent_id else None
        if parent is not None and parent.name:
            tokens.update(_split_identifier(parent.name))
        qname = getattr(node, "qualified_name", None)
        if qname:
            tokens.update(_split_identifier(qname))

        tokens = {t for t in tokens if len(t) >= min_len}
        if not tokens:
            raw[node.node_id] = 0.0
            continue

        hits = sum(1 for q in q_tokens if q in tokens)
        raw[node.node_id] = hits / len(q_tokens)

    # Already in [0, 1] by construction — no further normalisation.
    return raw


def compute_identifier_exact(
    query: str,
    nodes: list["LNode"],
    graph: "LayeredGraph",
) -> dict[str, float]:
    """Fraction of *query-extracted identifier tokens* that appear in the
    FUNCTION node's name/qualified-name/parent-class token set.

    Unlike :func:`compute_name_match`, which tokenises the whole query
    (including natural-language words), this signal only ever considers
    code-like tokens pulled from the query by :func:`_extract_query_identifiers`.
    That kills the "digest" false-positive on a noun-heavy query while
    strongly rewarding true references like ``WrappedRequest`` or
    ``get_headers``.

    Returns values in ``[0, 1]``; non-FUNCTION nodes get 0.
    """
    q_idents = _extract_query_identifiers(query)
    if not q_idents:
        return {n.node_id: 0.0 for n in nodes}

    raw: dict[str, float] = {}
    for node in nodes:
        if node.layer.name != "FUNCTION":
            raw[node.node_id] = 0.0
            continue
        tokens: set[str] = set(_split_identifier(node.name or ""))
        # Also match against intact identifier form (e.g. "WrappedRequest").
        if node.name:
            tokens.add(node.name.lower())
        parent = graph.nodes.get(node.parent_id) if node.parent_id else None
        if parent is not None and parent.name:
            tokens.add(parent.name.lower())
            tokens.update(_split_identifier(parent.name))
        qname = getattr(node, "qualified_name", None)
        if qname:
            tokens.add(qname.lower())
            tokens.update(_split_identifier(qname))
        hits = sum(1 for q in q_idents if q in tokens)
        raw[node.node_id] = hits / len(q_idents)
    return raw


def compute_path_match(
    query: str,
    nodes: list["LNode"],
    min_len: int = 4,
) -> dict[str, float]:
    """Fraction of (informative) query tokens that appear in the file path.

    Bug reports frequently say "in requests/auth.py" or mention a module
    name. BM25 on the function body never sees the path. This signal closes
    that gap. Applied to any layer (file/class/function) — paths are always
    present.
    """
    q_tokens = {t for t in _tokenize(query) if len(t) >= min_len}
    if not q_tokens:
        return {n.node_id: 0.0 for n in nodes}

    raw: dict[str, float] = {}
    for node in nodes:
        if not node.file_path:
            raw[node.node_id] = 0.0
            continue
        path_tokens = set(_tokenize(node.file_path))
        hits = sum(1 for q in q_tokens if q in path_tokens)
        raw[node.node_id] = hits / len(q_tokens)
    return raw


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
        config: SelectorConfig = DEFAULT_CONFIG,
    ):
        self._graph  = graph
        self._query  = query
        self._intent = intent
        self._texts  = texts
        self._config = config
        if weight_override is not None:
            base = _WEIGHTS.get(intent, _WEIGHTS[QueryIntent.BUG])
            keys = ("bm25", "fan_in", "fan_out", "complexity", "test_cover")
            self._weights = tuple(
                weight_override.get(k, base[i]) for i, k in enumerate(keys)
            )
        else:
            self._weights = _WEIGHTS.get(intent, _WEIGHTS[QueryIntent.BUG])

        # Query-independent signals (PageRank, name-counts) are cached per
        # graph. This turns a per-query O(N * iters) PageRank recomputation
        # into a one-shot cost amortised across the whole benchmark.
        cache = get_scorer_cache(graph, config)
        self._name_counts = cache.name_counts
        self._pagerank_full = cache.pagerank
        self._ppr_index = cache.ppr_index

    def score_all(self, nodes: list["LNode"]) -> dict[str, float]:
        """Compute combined intent-weighted score for each node.

        Uses adaptive BM25 weighting: when the query produces weak BM25 signal
        across all nodes (mean normalised score < ``config.bm25_weak_threshold``),
        a fraction of the BM25 weight (``config.bm25_shed_fraction``) is
        redistributed to graph signals (fan_in, fan_out, complexity, test).
        When BM25 is strong, the original weights are used unchanged.

        When ``config.use_cascading_bm25`` is true, BM25 is run over three
        query variants (raw / split / structurally-expanded) and the per-node
        maximum is taken — helps on CamelCase and class-name queries.
        """
        if not nodes:
            return {}

        cfg = self._config
        w_bm25, w_fan_in, w_fan_out, w_complex, w_test = self._weights

        # Always compute BM25 first — needed for adaptive weight decision
        if cfg.use_cascading_bm25:
            bm25 = _cascading_bm25(
                self._query, nodes, self._texts, self._graph,
                expansion_cap=cfg.cascading_expansion_cap,
                identifier_expansion_enabled=cfg.identifier_expansion_enabled,
            )
        else:
            bm25 = compute_bm25(self._query, nodes, self._texts)

        # Adaptive weight: if average BM25 score is very weak, shift weight
        # from BM25 toward graph signals proportionally.
        bm25_values = list(bm25.values())
        mean_bm25 = sum(bm25_values) / len(bm25_values) if bm25_values else 0.0

        if mean_bm25 < cfg.bm25_weak_threshold and w_bm25 > 0:
            bm25_shed = w_bm25 * cfg.bm25_shed_fraction
            graph_total = w_fan_in + w_fan_out + w_complex + w_test
            if graph_total > 0:
                w_fan_in  = w_fan_in  + bm25_shed * (w_fan_in  / graph_total)
                w_fan_out = w_fan_out + bm25_shed * (w_fan_out / graph_total)
                w_complex = w_complex + bm25_shed * (w_complex / graph_total)
                w_test    = w_test    + bm25_shed * (w_test    / graph_total)
            w_bm25 = w_bm25 - bm25_shed

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

        # Neighborhood support is applied as a bounded post-score bonus.
        neighborhood = compute_neighborhood_bonus(nodes, self._graph, scores)
        nbr_scale = (
            cfg.neighborhood_scale_strong
            if mean_bm25 >= cfg.bm25_weak_threshold
            else cfg.neighborhood_scale_weak
        )
        for node in nodes:
            if node.layer.name != "FUNCTION":
                continue
            nid = node.node_id
            scores[nid] = min(1.0, scores[nid] + nbr_scale * neighborhood.get(nid, 0.0))

        # Structural PageRank bonus — PPR when enabled (query-aware),
        # otherwise the cached vanilla PageRank (query-independent).
        if cfg.ppr_enabled:
            pr_vec, density_factor = self._compute_ppr(nodes, bm25)
            pr_scale = (
                cfg.ppr_scale_strong
                if mean_bm25 >= cfg.bm25_weak_threshold
                else cfg.ppr_scale_weak
            )
            pr_scale *= density_factor
        else:
            pr_vec = self._pagerank_full
            pr_scale = (
                cfg.pagerank_scale_strong
                if mean_bm25 >= cfg.bm25_weak_threshold
                else cfg.pagerank_scale_weak
            )
        for node in nodes:
            if node.layer.name != "FUNCTION":
                continue
            nid = node.node_id
            scores[nid] = min(
                1.0,
                scores[nid] + pr_scale * pr_vec.get(nid, 0.0),
            )

        # --- Identifier-match bonuses ----------------------------------
        # These are the main levers for within-file function disambiguation.
        # Applied as bounded additive bonuses so the [0, 1] range is preserved.
        if cfg.name_match_scale > 0:
            nm = compute_name_match(
                self._query, nodes, self._graph,
                min_len=cfg.identifier_min_length,
            )
            for node in nodes:
                if node.layer.name != "FUNCTION":
                    continue
                nid = node.node_id
                scores[nid] = min(
                    1.0,
                    scores[nid] + cfg.name_match_scale * nm.get(nid, 0.0),
                )

        if cfg.path_match_scale > 0:
            pm = compute_path_match(
                self._query, nodes, min_len=cfg.identifier_min_length + 1,
            )
            for node in nodes:
                nid = node.node_id
                scores[nid] = min(
                    1.0,
                    scores[nid] + cfg.path_match_scale * pm.get(nid, 0.0),
                )

        # --- Identifier-exact-match bonus (Experiment 06) ---------------
        # Operates only on code-like tokens extracted from the query,
        # rewarding FUNCTION nodes that actually carry that identifier.
        if cfg.identifier_expansion_enabled and cfg.identifier_exact_scale > 0:
            ie = compute_identifier_exact(self._query, nodes, self._graph)
            for node in nodes:
                if node.layer.name != "FUNCTION":
                    continue
                nid = node.node_id
                scores[nid] = min(
                    1.0,
                    scores[nid] + cfg.identifier_exact_scale * ie.get(nid, 0.0),
                )

        return scores

    def _compute_ppr(
        self,
        nodes: list["LNode"],
        bm25: dict[str, float],
    ) -> tuple[dict[str, float], float]:
        """Run Personalized PageRank seeded by the current query's BM25 hits.

        Seeds are the top-K FUNCTION nodes by BM25 score, weighted by that
        score (higher BM25 → more teleport mass). Non-function nodes can't
        seed — PPR runs on the function-layer CALLS graph.

        Returns ``(pr_vec, density_factor)``. ``density_factor ∈ [min, 1.0]``
        is a multiplier the caller applies on top of the configured PPR scale,
        computed from the average CALLS out-degree of the seed set. When
        seeds have no neighborhood to propagate through (shallow-library
        queries), PPR reduces to a noisier BM25 — so we damp its contribution.
        """
        cfg = self._config
        # Rank FUNCTION nodes by BM25 and keep the top-K as seeds.
        fn_bm25 = [
            (nid, bm25.get(nid, 0.0))
            for nid in (n.node_id for n in nodes if n.layer.name == "FUNCTION")
        ]
        fn_bm25.sort(key=lambda kv: -kv[1])
        seeds = {nid: s for nid, s in fn_bm25[: cfg.ppr_seed_k] if s > 0}

        pr_vec = personalized_pagerank(
            self._ppr_index,
            seed_weights=seeds,
            alpha=cfg.ppr_alpha,
            max_iter=cfg.ppr_max_iter,
            tol=cfg.ppr_tol,
        )

        density_factor = 1.0
        if cfg.ppr_density_enabled and seeds:
            idx_of = self._ppr_index.index_of
            out_links = self._ppr_index.out_links
            degrees = [
                len(out_links[idx_of[nid]])
                for nid in seeds
                if nid in idx_of
            ]
            if degrees:
                avg_deg = sum(degrees) / len(degrees)
                # Linear ramp from min_scale at deg=0 → 1.0 at saturation.
                sat = max(1e-9, cfg.ppr_density_saturation)
                ratio = min(1.0, avg_deg / sat)
                density_factor = (
                    cfg.ppr_density_min_scale
                    + (1.0 - cfg.ppr_density_min_scale) * ratio
                )

        return pr_vec, density_factor

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
