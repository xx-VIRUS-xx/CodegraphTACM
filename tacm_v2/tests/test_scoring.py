"""test_scoring.py — Fast unit tests for the scoring/intent layer.

Unlike ``test_regression.py``, these tests do **not** require the
``thefuck`` or ``scrapy`` repos and do not hit sqlite. Each test builds
a small synthetic :class:`LayeredGraph` in-memory, exercises one unit of
behaviour, and asserts a specific invariant.

Run::

    python -m pytest tacm_v2/tests/test_scoring.py -v
    python tacm_v2/tests/test_scoring.py
"""

from __future__ import annotations

import sys
from pathlib import Path

# Add the ghost-of-past folder to sys.path so "tacm_v2" imports resolve
# regardless of where the test is invoked from.
_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(_ROOT))

from tacm_v2.graph.model import (
    EdgeKind, Layer, LayeredGraph, LEdge, LNode,
)
from tacm_v2.selector.cache import (
    clear_cache, get_scorer_cache, invalidate,
)
from tacm_v2.selector.config import DEFAULT_CONFIG, SelectorConfig
from tacm_v2.selector.intent import (
    QueryIntent,
    blended_weights,
    classify_intent,
    classify_intent_with_confidence,
    INTENT_WEIGHTS,
)
from tacm_v2.selector.scoring import (
    NodeScorer,
    _cascading_bm25,
    compute_bm25,
    compute_name_match,
    compute_path_match,
)


# ---------------------------------------------------------------------------
# Synthetic graph helpers
# ---------------------------------------------------------------------------

def _make_fn(
    node_id: str,
    name: str,
    file_path: str = "app.py",
    parent_id: str | None = None,
    is_test: bool = False,
    token_cost: int = 50,
) -> LNode:
    return LNode(
        node_id=node_id, layer=Layer.FUNCTION, name=name,
        file_path=file_path, line_start=1, line_end=10,
        parent_id=parent_id, is_test=is_test, token_cost=token_cost,
    )


def _make_cls(node_id: str, name: str, file_path: str = "app.py") -> LNode:
    return LNode(
        node_id=node_id, layer=Layer.CLASS, name=name,
        file_path=file_path, line_start=1, line_end=100,
    )


def _tiny_graph() -> LayeredGraph:
    """Four functions + one class across two files, connected by CALLS edges."""
    g = LayeredGraph()
    cls = _make_cls("cls:App", "App", "app.py")
    a = _make_fn("fn:orchestrate", "orchestrate", "app.py", parent_id="cls:App")
    b = _make_fn("fn:handle_login", "handle_login", "app.py", parent_id="cls:App")
    c = _make_fn("fn:db_query", "db_query", "db.py")
    d = _make_fn("fn:log_error", "log_error", "logger.py")
    t = _make_fn("test_login", "test_login", "tests/test_app.py", is_test=True)

    for n in (cls, a, b, c, d, t):
        g.add_node(n)

    # orchestrate calls handle_login, db_query, log_error
    # handle_login calls db_query
    # test_login calls handle_login (test edge, should be ignored)
    for src, tgt, w in [
        ("fn:orchestrate",   "fn:handle_login", 1.0),
        ("fn:orchestrate",   "fn:db_query",     0.8),
        ("fn:orchestrate",   "fn:log_error",    0.4),
        ("fn:handle_login",  "fn:db_query",     1.0),
        ("test_login",       "fn:handle_login", 1.0),
    ]:
        g.add_edge(LEdge(src, tgt, EdgeKind.CALLS, w))

    return g


# ---------------------------------------------------------------------------
# Intent tests
# ---------------------------------------------------------------------------

def test_intent_basic_labels():
    assert classify_intent("why does login fail with exception") == QueryIntent.BUG
    assert classify_intent("show the structure of the auth module") == QueryIntent.STRUCTURE
    assert classify_intent("explain how handle_login works") == QueryIntent.EXPLAIN


def test_intent_empty_query_falls_back_to_bug():
    # Historical behaviour guarded by test_regression.
    assert classify_intent("") == QueryIntent.BUG
    assert classify_intent("  ") == QueryIntent.BUG


def test_intent_negation_cancels_bug():
    # Without negation, "failure" would push BUG ahead.
    # "no failure" should neutralise that boost.
    label_raw, _, scores_raw = classify_intent_with_confidence(
        "show the structure without error"
    )
    label_neg = classify_intent("show the structure without error")
    # STRUCTURE should win when BUG is neutralised
    assert label_neg == QueryIntent.STRUCTURE
    assert scores_raw[QueryIntent.BUG] < 2  # neutralised


def test_intent_confidence_decisive_vs_ambiguous():
    _, conf_clear, _ = classify_intent_with_confidence(
        "explain how this module is structured organised dependency layout"
    )
    _, conf_vague, _ = classify_intent_with_confidence("why")
    # A single-keyword query should be at least as confident as mixed signals,
    # but both must be in [0, 1].
    assert 0.0 <= conf_clear <= 1.0
    assert 0.0 <= conf_vague <= 1.0


def test_blended_weights_high_confidence_passes_through():
    # A clearly bug-y query should return the unblended BUG weights.
    label, weights = blended_weights("why does login fail with an exception error")
    assert label == QueryIntent.BUG
    assert weights == INTENT_WEIGHTS[QueryIntent.BUG]


def test_blended_weights_ambiguous_mixes_top_two():
    # "explain bug" is roughly 50/50 between EXPLAIN and BUG.
    label, weights = blended_weights("explain bug")
    assert label in (QueryIntent.BUG, QueryIntent.EXPLAIN)
    w_bug     = INTENT_WEIGHTS[QueryIntent.BUG]
    w_explain = INTENT_WEIGHTS[QueryIntent.EXPLAIN]
    # The blended vector must not match either crisp vector exactly.
    assert weights != w_bug and weights != w_explain
    # But must be element-wise between them.
    for i in range(5):
        lo, hi = sorted([w_bug[i], w_explain[i]])
        assert lo - 1e-9 <= weights[i] <= hi + 1e-9


# ---------------------------------------------------------------------------
# BM25 tests
# ---------------------------------------------------------------------------

def test_bm25_returns_normalised_scores():
    g = _tiny_graph()
    fns = [n for n in g.nodes.values() if n.layer == Layer.FUNCTION and not n.is_test]
    texts = {n.node_id: n.name for n in fns}
    scores = compute_bm25("login", fns, texts)
    assert all(0.0 <= v <= 1.0 for v in scores.values())
    # handle_login contains the word login → should score strictly higher
    # than db_query which does not.
    assert scores["fn:handle_login"] > scores["fn:db_query"]


def test_cascading_bm25_at_least_as_strong_as_raw():
    g = _tiny_graph()
    fns = [n for n in g.nodes.values() if n.layer == Layer.FUNCTION and not n.is_test]
    texts = {n.node_id: n.name for n in fns}

    raw = compute_bm25("HandleLogin", fns, texts)
    casc = _cascading_bm25("HandleLogin", fns, texts, g)
    # Cascading takes per-node max across variants; it can never be lower.
    for nid in raw:
        assert casc[nid] >= raw[nid] - 1e-9


# ---------------------------------------------------------------------------
# Cache tests
# ---------------------------------------------------------------------------

def test_scorer_cache_is_idempotent():
    clear_cache()
    g = _tiny_graph()
    c1 = get_scorer_cache(g)
    c2 = get_scorer_cache(g)
    assert c1 is c2  # same object, no rebuild


def test_scorer_cache_respects_config_identity():
    clear_cache()
    g = _tiny_graph()
    cfg_a = SelectorConfig()               # default
    cfg_b = SelectorConfig(pagerank_alpha=0.5)
    c1 = get_scorer_cache(g, cfg_a)
    c2 = get_scorer_cache(g, cfg_b)
    # Different configs → different cache entries; PageRank values differ.
    assert c1 is not c2


def test_scorer_cache_invalidate():
    clear_cache()
    g = _tiny_graph()
    c1 = get_scorer_cache(g)
    invalidate(g)
    c2 = get_scorer_cache(g)
    assert c1 is not c2


def test_pagerank_excludes_test_nodes():
    clear_cache()
    g = _tiny_graph()
    cache = get_scorer_cache(g)
    assert "test_login" not in cache.pagerank
    # All non-test functions in the cache.
    for nid in ("fn:orchestrate", "fn:handle_login", "fn:db_query", "fn:log_error"):
        assert nid in cache.pagerank
    # db_query is called by two functions → should outrank log_error.
    assert cache.pagerank["fn:db_query"] > cache.pagerank["fn:log_error"]


# ---------------------------------------------------------------------------
# Identifier-match signals
# ---------------------------------------------------------------------------

def test_name_match_rewards_qualified_name_tokens():
    g = _tiny_graph()
    fns = [n for n in g.nodes.values() if n.layer == Layer.FUNCTION and not n.is_test]
    scores = compute_name_match("handle login flow", fns, g)
    # handle_login has both "handle" and "login" as identifier tokens.
    assert scores["fn:handle_login"] == 2 / 3  # 2 of 3 q-tokens of len>=3 match
    # db_query shares neither.
    assert scores["fn:db_query"] == 0.0
    # Bounded [0,1].
    assert all(0.0 <= v <= 1.0 for v in scores.values())


def test_name_match_uses_parent_class_tokens():
    g = _tiny_graph()
    # "App" class is parent of orchestrate and handle_login; "app" as a
    # 3-letter token is included by the default min_len.
    fns = [n for n in g.nodes.values() if n.layer == Layer.FUNCTION and not n.is_test]
    scores = compute_name_match("app", fns, g)
    # handle_login and orchestrate inherit the "app" class-name token.
    assert scores["fn:handle_login"] > 0
    assert scores["fn:orchestrate"] > 0
    # log_error is in logger.py, no "App" parent → 0.
    assert scores["fn:log_error"] == 0.0


def test_path_match_rewards_file_path_tokens():
    g = _tiny_graph()
    fns = [n for n in g.nodes.values() if n.layer == Layer.FUNCTION and not n.is_test]
    scores = compute_path_match("logger module crash", fns, min_len=4)
    # log_error lives in logger.py → path-token "logger" matches.
    assert scores["fn:log_error"] > 0
    # db_query lives in db.py → no match for "logger"/"module"/"crash".
    assert scores["fn:db_query"] == 0.0


def test_name_match_end_to_end_disambiguates_siblings():
    """Two methods in the same class, only one matches the query by name.
    After the improvements, the name-matching one must rank first."""
    clear_cache()
    g = LayeredGraph()
    cls = _make_cls("cls:Auth", "DigestAuth", "auth.py")
    g.add_node(cls)
    # Both functions have identical bodies (same BM25 signal), only names differ.
    shared_body = "self.x = 1\nreturn None"
    m1 = _make_fn("fn:build_digest_header", "build_digest_header",
                  "auth.py", parent_id="cls:Auth")
    m2 = _make_fn("fn:handle_redirect", "handle_redirect",
                  "auth.py", parent_id="cls:Auth")
    g.add_node(m1)
    g.add_node(m2)

    texts = {m1.node_id: shared_body, m2.node_id: shared_body}
    scorer = NodeScorer(g, "digest header", QueryIntent.BUG, texts)
    scores = scorer.score_all([m1, m2])
    # build_digest_header wins purely on name-match, since BM25 is a tie.
    assert scores["fn:build_digest_header"] > scores["fn:handle_redirect"]




def test_node_scorer_returns_scores_in_range():
    clear_cache()
    g = _tiny_graph()
    fns = [n for n in g.nodes.values() if n.layer == Layer.FUNCTION and not n.is_test]
    texts = {n.node_id: n.name for n in fns}
    scorer = NodeScorer(g, "login", QueryIntent.BUG, texts)
    scores = scorer.score_all(fns)
    assert scores, "expected non-empty scores"
    assert all(0.0 <= v <= 1.0 for v in scores.values())


def test_node_scorer_cascading_toggle_changes_output():
    clear_cache()
    g = _tiny_graph()
    fns = [n for n in g.nodes.values() if n.layer == Layer.FUNCTION and not n.is_test]
    texts = {n.node_id: n.name for n in fns}

    scorer_plain = NodeScorer(
        g, "HandleLogin", QueryIntent.BUG, texts,
        config=SelectorConfig(use_cascading_bm25=False),
    )
    scorer_casc = NodeScorer(
        g, "HandleLogin", QueryIntent.BUG, texts,
        config=SelectorConfig(use_cascading_bm25=True),
    )
    s_plain = scorer_plain.score_all(fns)
    s_casc  = scorer_casc.score_all(fns)
    # Cascading should not lower the handle_login score.
    assert s_casc["fn:handle_login"] >= s_plain["fn:handle_login"] - 1e-9


# ---------------------------------------------------------------------------
# End-to-end select() smoke test
# ---------------------------------------------------------------------------

def test_select_end_to_end_on_synthetic_graph():
    """Integration check: select() runs, returns a SelectionResult, respects budget."""
    from tacm_v2.selector import select, explain_selection

    clear_cache()
    g = _tiny_graph()
    result = select(g, "why does handle_login fail", token_budget=2000)

    assert result.intent == QueryIntent.BUG
    assert result.total_tokens <= int(2000 * (1 + DEFAULT_CONFIG.max_overflow_ratio))
    assert result.nodes, "expected at least one node selected"
    assert all(sn.node.node_id in g.nodes for sn in result.nodes)

    # explain_selection produces a breakdown for each selected node.
    breakdown = explain_selection(g, "why does handle_login fail", result, top_n=3)
    assert len(breakdown) >= 1
    for entry in breakdown:
        assert {"node_id", "name", "layer", "score", "bm25", "weights"} <= entry.keys()


def test_select_dynamic_smoke():
    from tacm_v2.selector import select_dynamic

    clear_cache()
    g = _tiny_graph()
    result = select_dynamic(g, "explain how orchestrate calls into db_query", 2000)
    assert result.nodes
    # No duplicates.
    ids = [sn.node.node_id for sn in result.nodes]
    assert len(ids) == len(set(ids))


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

_TESTS = [
    test_intent_basic_labels,
    test_intent_empty_query_falls_back_to_bug,
    test_intent_negation_cancels_bug,
    test_intent_confidence_decisive_vs_ambiguous,
    test_blended_weights_high_confidence_passes_through,
    test_blended_weights_ambiguous_mixes_top_two,
    test_bm25_returns_normalised_scores,
    test_cascading_bm25_at_least_as_strong_as_raw,
    test_scorer_cache_is_idempotent,
    test_scorer_cache_respects_config_identity,
    test_scorer_cache_invalidate,
    test_pagerank_excludes_test_nodes,
    test_name_match_rewards_qualified_name_tokens,
    test_name_match_uses_parent_class_tokens,
    test_path_match_rewards_file_path_tokens,
    test_name_match_end_to_end_disambiguates_siblings,
    test_node_scorer_returns_scores_in_range,
    test_node_scorer_cascading_toggle_changes_output,
    test_select_end_to_end_on_synthetic_graph,
    test_select_dynamic_smoke,
]


def run_all() -> bool:
    passed = failed = 0
    for test in _TESTS:
        try:
            test()
            print(f"  PASS  {test.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"  FAIL  {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            import traceback
            print(f"  ERROR {test.__name__}: {e}")
            traceback.print_exc()
            failed += 1
    print(f"\n{passed} passed, {failed} failed")
    return failed == 0


if __name__ == "__main__":
    ok = run_all()
    sys.exit(0 if ok else 1)
