"""test_regression.py — Regression guards for all prior TACM claims.

Runs before any benchmark rerun or selector change. If any assertion fails,
the change broke a prior claim and must be fixed or explicitly overridden.

Claims guarded:
  [L1] thefuck MRR >= 0.35  (Exp02: 0.3725, guard at -6%)
  [L2] thefuck Hit@10 >= 60% (Exp02: 65%)
  [L3] scrapy  MRR >= 0.26  (Exp02: 0.2897, guard at -10%)
  [L4] scrapy  Hit@10 >= 42% (Exp02: 47%)
  [L6] Containment bonus contributes: TACM_full MRR > TACM_NoCB MRR on thefuck
  [A1] thefuck-14 GT function in TACM context (tacm unique agent win)
  [A2] thefuck-15 GT function in TACM context
  [A3] thefuck-25 GT function in TACM context
  [A4] thefuck-28 GT function in TACM context

Usage:
    python3 tacm_v2/tests/test_regression.py
    python3 -m pytest tacm_v2/tests/test_regression.py -v
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "archive" / "pre-research"))

THEFUCK_REPO = ROOT / "thefuck"
SCRAPY_REPO  = ROOT / "scrapy"

# Exp02 baselines — guards set at ~90% of reported value
GUARDS = {
    "thefuck_mrr":   0.35,   # Exp02: 0.3725
    "thefuck_hit10": 0.60,   # Exp02: 0.65
    "scrapy_mrr":    0.26,   # Exp02: 0.2897
    "scrapy_hit10":  0.42,   # Exp02: 0.47
}

# TACM-only agent wins: bug_id -> (gt_fn_short, gt_file_suffix)
TACM_UNIQUE_WINS = {
    "thefuck-14": ("_get_overridden_aliases", "shells/fish.py"),
    "thefuck-15": ("get_new_command",         "rules/git_add.py"),
    "thefuck-25": ("get_new_command",         "rules/mkdir_p.py"),
    "thefuck-28": ("get_new_command",         None),  # any file
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _load_graph(repo_root: Path):
    from code_review_graph.graph import GraphStore
    from code_review_graph.incremental import get_db_path
    from tacm_v2.graph.builder import GraphBuilder
    store = GraphStore(get_db_path(repo_root))
    try:
        graph = GraphBuilder(store).build()
    finally:
        store.close()
    return graph


def _load_tasks(project: str, repo_root: Path):
    from bench_v2 import load_tasks
    return load_tasks(project, repo_root, max_bugs=100, skip_no_query=True)


def _run_tacm(graph, query: str, budget: int = 4000, nocb: bool = False):
    """Return list of (node_id, file_path, fn_name) selected by TACM."""
    from tacm_v2.selector.selector import (
        SelectionResult, SelectedNode, _count_tokens,
        classify_intent, _LAYER_BUDGETS,
    )
    from tacm_v2.graph.model import Layer
    from tacm_v2.layers.serializers import serialize
    from tacm_v2.selector.scoring import NodeScorer

    if not nocb:
        from tacm_v2.selector.selector import select
        result = select(graph, query, budget)
    else:
        # Re-implement select with containment bonus disabled
        intent = classify_intent(query)
        file_frac, class_frac, _ = _LAYER_BUDGETS[intent]
        file_budget  = int(budget * file_frac)
        class_budget = int(budget * class_frac)
        fn_budget    = budget - file_budget - class_budget
        all_nodes = [n for n in graph.nodes.values() if not n.is_test]
        texts = {n.node_id: serialize(n, graph) for n in all_nodes}
        scorer = NodeScorer(graph, query, intent, texts)
        selected = []
        layer_counts = {}
        for layer, lbudget in [(Layer.FILE, file_budget), (Layer.CLASS, class_budget), (Layer.FUNCTION, fn_budget)]:
            if lbudget <= 0:
                continue
            nodes = [n for n in graph.nodes_at_layer(layer) if not n.is_test]
            if not nodes:
                continue
            scores = scorer.score_all(nodes)
            node_scores = sorted([(scores[n.node_id], n) for n in nodes], key=lambda x: -x[0])
            remaining = lbudget
            count = 0
            for score, node in node_scores:
                text = texts[node.node_id]
                cost = _count_tokens(text)
                if cost <= remaining:
                    selected.append(SelectedNode(node=node, layer=layer, text=text,
                                                 token_cost=cost, score=score, intent=intent))
                    remaining -= cost
                    count += 1
            layer_counts[layer.name] = count
        result = SelectionResult(nodes=selected, total_tokens=sum(n.token_cost for n in selected),
                                 budget=budget, intent=intent, layer_counts=layer_counts)

    return [(n.node.node_id, n.node.file_path or "", n.node.name, n.layer.name) for n in result.nodes]


def _rank_in_selected(selected, gt_functions, gt_files):
    """Return rank (1-based) within FUNCTION-layer nodes only, or None if not found."""
    from bench_v2 import _node_matches_gt_strict
    fn_rank = 0
    for nid, fpath, name, layer_name in selected:
        if layer_name != "FUNCTION":
            continue
        fn_rank += 1
        for gt_fn in gt_functions:
            if _node_matches_gt_strict(nid, fpath, gt_fn, gt_files):
                return fn_rank
    return None


def _mrr_hit(graph, tasks, nocb: bool = False, top_k: int = 10) -> tuple[float, float]:
    from bench_v2 import mrr as _mrr
    ranks = []
    for task in tasks:
        if not task.gt_functions:
            ranks.append(None)
            continue
        selected = _run_tacm(graph, task.query, nocb=nocb)
        rank = _rank_in_selected(selected, task.gt_functions, task.gt_files)
        ranks.append(rank)
    hit_ranks = [r for r in ranks if r is not None and r <= top_k]
    n = len(ranks)
    hit10 = len(hit_ranks) / n if n else 0.0
    return _mrr(ranks), hit10


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_thefuck_localisation():
    """[L1,L2] TACM MRR >= 0.35 and Hit@10 >= 60% on thefuck."""
    if not THEFUCK_REPO.exists():
        print("  SKIP: thefuck repo not found")
        return True
    graph = _load_graph(THEFUCK_REPO)
    tasks = _load_tasks("thefuck", THEFUCK_REPO)
    mrr, hit10 = _mrr_hit(graph, tasks)
    print(f"  thefuck  MRR={mrr:.4f} (guard>={GUARDS['thefuck_mrr']})  "
          f"Hit@10={hit10:.2%} (guard>={GUARDS['thefuck_hit10']:.0%})")
    assert mrr   >= GUARDS["thefuck_mrr"],   f"[L1] MRR {mrr:.4f} < {GUARDS['thefuck_mrr']} — localisation regressed!"
    assert hit10 >= GUARDS["thefuck_hit10"], f"[L2] Hit@10 {hit10:.2%} < {GUARDS['thefuck_hit10']:.0%} — localisation regressed!"
    return True


def test_scrapy_localisation():
    """[L3,L4] TACM MRR >= 0.26 and Hit@10 >= 42% on scrapy."""
    if not SCRAPY_REPO.exists():
        print("  SKIP: scrapy repo not found")
        return True
    graph = _load_graph(SCRAPY_REPO)
    tasks = _load_tasks("scrapy", SCRAPY_REPO)
    mrr, hit10 = _mrr_hit(graph, tasks)
    print(f"  scrapy   MRR={mrr:.4f} (guard>={GUARDS['scrapy_mrr']})  "
          f"Hit@10={hit10:.2%} (guard>={GUARDS['scrapy_hit10']:.0%})")
    assert mrr   >= GUARDS["scrapy_mrr"],   f"[L3] MRR {mrr:.4f} < {GUARDS['scrapy_mrr']} — scrapy localisation regressed!"
    assert hit10 >= GUARDS["scrapy_hit10"], f"[L4] Hit@10 {hit10:.2%} < {GUARDS['scrapy_hit10']:.0%} — scrapy localisation regressed!"
    return True


def test_containment_bonus_contributes():
    """[L6] TACM_full MRR > TACM_NoCB MRR (containment bonus must still help)."""
    if not THEFUCK_REPO.exists():
        print("  SKIP: thefuck repo not found")
        return True
    graph = _load_graph(THEFUCK_REPO)
    tasks = _load_tasks("thefuck", THEFUCK_REPO)
    mrr_full, _ = _mrr_hit(graph, tasks, nocb=False)
    mrr_nocb, _ = _mrr_hit(graph, tasks, nocb=True)
    print(f"  TACM_full MRR={mrr_full:.4f}  TACM_NoCB MRR={mrr_nocb:.4f}  delta={mrr_full-mrr_nocb:+.4f}")
    assert mrr_full > mrr_nocb, \
        f"[L6] Containment bonus no longer helps! full={mrr_full:.4f} <= nocb={mrr_nocb:.4f}"
    return True


def test_tacm_unique_agent_wins():
    """[A1-A4] GT function must appear in TACM context for all 4 unique agent wins."""
    if not THEFUCK_REPO.exists():
        print("  SKIP: thefuck repo not found")
        return True
    from bench_v2 import load_tasks
    graph = _load_graph(THEFUCK_REPO)
    tasks = {t.bug_id: t for t in load_tasks("thefuck", THEFUCK_REPO, max_bugs=100, skip_no_query=True)}

    all_passed = True
    for bug_id, (fn_short, file_suffix) in TACM_UNIQUE_WINS.items():
        task = tasks.get(bug_id)
        if not task:
            print(f"  SKIP {bug_id}: not in task list")
            continue
        selected = _run_tacm(graph, task.query, budget=4000)
        found = any(
            name == fn_short and (file_suffix is None or fpath.endswith(file_suffix))
            for _, fpath, name, _layer in selected
        )
        status = "OK  " if found else "FAIL"
        print(f"  [{status}] {bug_id}: '{fn_short}' in context={found}")
        if not found:
            all_passed = False

    assert all_passed, "[A1-A4] One or more TACM unique agent wins lost from context — selector regressed!"
    return True


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def run_all() -> bool:
    tests = [
        test_thefuck_localisation,
        test_scrapy_localisation,
        test_containment_bonus_contributes,
        test_tacm_unique_agent_wins,
    ]
    passed = failed = 0
    for test in tests:
        print(f"\n{'='*60}")
        print(f"TEST: {test.__name__}")
        print(f"  {test.__doc__.strip()}")
        try:
            test()
            print(f"  → PASSED")
            passed += 1
        except AssertionError as e:
            print(f"  → FAILED: {e}")
            failed += 1
        except Exception as e:
            import traceback
            print(f"  → ERROR: {e}")
            traceback.print_exc()
            failed += 1

    print(f"\n{'='*60}")
    print(f"RESULT: {passed} passed, {failed} failed out of {passed+failed} tests")
    if failed:
        print("⚠  Regression detected — do NOT run benchmark until fixed.")
    else:
        print("✓  All claims hold — safe to proceed.")
    return failed == 0


if __name__ == "__main__":
    ok = run_all()
    sys.exit(0 if ok else 1)
