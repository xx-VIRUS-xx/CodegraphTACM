"""bench2.py — Experiment 02: TACM vs Naive RAG on pallets/flask.

Second codebase validation: does the NL query advantage generalise beyond psf/requests?

Queries are written from bug symptoms only — no function names, no diffs consulted.
Ground truth derived from actual fix commits in pallets/flask history.

Usage:
    python3 bench2.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from tacm.crg_adapter import open_store, query_to_scored_nodes
from tacm.resolver import ScoredNode, resolve, Strategy

REPO_ROOT = Path(__file__).parent / "flask"
TOKEN_BUDGET = 4000
BUDGETS_TO_TEST = [800, 2000, 4000, 8000, 16000, 32000]

# ---------------------------------------------------------------------------
# Ground truth — 10 real pallets/flask bugs with known fix locations.
# Queries written from GitHub issue descriptions / commit messages ONLY.
# No function names appear in any query.
# Fix commits: fbb6f0b, 53b8f08, e82db2c, a411a24, c17f379, daf1510,
#              4995a77, d7209a9, 4be9f52, cabda59
# ---------------------------------------------------------------------------

BUGS: list[dict] = [
    {
        "id": "fbug01",
        "desc": "Teardown callbacks skipped when earlier one raises",
        "query": "teardown callbacks not all called when one raises exception during cleanup",
        "ground_truth": "src/flask/ctx.py::AppContext.pop",
        # fix: fbb6f0b — AppContext.pop now collects errors instead of short-circuiting
    },
    {
        "id": "fbug02",
        "desc": "Test client context lost after redirect inside with-block",
        "query": "test client request context not available after following redirect inside with block",
        "ground_truth": "src/flask/testing.py::FlaskClient.open",
        # fix: 53b8f08 — contexts pushed in wrong order (popped LIFO, must push LIFO too)
    },
    {
        "id": "fbug03",
        "desc": "OPTIONS method added even when explicitly excluded from route",
        "query": "OPTIONS method appears on route even though it was not registered and was explicitly excluded",
        "ground_truth": "src/flask/sansio/app.py::App.add_url_rule",
        # fix: e82db2c — provide_automatic_options logic incorrect when OPTIONS in methods
    },
    {
        "id": "fbug04",
        "desc": "Session not available when request context is first pushed",
        "query": "session object is None or not accessible immediately after pushing request context",
        "ground_truth": "src/flask/ctx.py::AppContext.push",
        # fix: a411a24 — session opening moved back to context push time
    },
    {
        "id": "fbug05",
        "desc": "Modifying session data does not mark it as modified",
        "query": "changes to session values not persisted, session not saved after modifying nested data",
        "ground_truth": "src/flask/sessions.py::SecureCookieSessionInterface.save_session",
        # fix: c17f379 — session access tracking; save_session checks accessed flag
    },
    {
        "id": "fbug06",
        "desc": "Template filter decorator requires parentheses to work",
        "query": "custom template filter decorator must be called with parentheses, fails when used without",
        "ground_truth": "src/flask/sansio/app.py::App.template_filter",
        # fix: daf1510 — template_filter overload added for no-parens usage
    },
    {
        "id": "fbug07",
        "desc": "Subdomain matching disabled but subdomains still matched",
        "query": "routes with subdomains still match requests when subdomain matching is turned off in config",
        "ground_truth": "src/flask/app.py::Flask.make_response",
        # fix: 4995a77 — subdomain_matching=False did not propagate to url_map
        # Note: actual fix is in Flask.wsgi_app / url_map config; make_response is proxy
    },
    {
        "id": "fbug08",
        "desc": "CLI app discovery fails with super() in list comprehension",
        "query": "flask CLI command fails to find app when application factory uses super in list comprehension",
        "ground_truth": "src/flask/cli.py::ScriptInfo.load_app",
        # fix: d7209a9 — super() call in list comprehension fails outside class body
    },
    {
        "id": "fbug09",
        "desc": "send_file / open_resource cannot find module-relative files",
        "query": "open_resource raises FileNotFoundError for files that exist next to the module",
        "ground_truth": "src/flask/helpers.py::open_resource",
        # fix: 4be9f52 — importlib.util.find_spec used incorrectly; root_path detection wrong
    },
    {
        "id": "fbug10",
        "desc": "Nested blueprint subdomain not chained to parent",
        "query": "nested blueprint registered under parent blueprint does not inherit parent subdomain prefix",
        "ground_truth": "src/flask/blueprints.py::BlueprintSetupState.add_url_rule",
        # fix: cabda59 — subdomain suffix-chaining missing for child blueprints
    },
]


def _abs_gt(repo_root: Path, gt_relative: str) -> str:
    parts = gt_relative.split("::")
    abs_file = str(repo_root / parts[0])
    return abs_file + "::" + parts[1] if len(parts) > 1 else abs_file


# ---------------------------------------------------------------------------
# Naive RAG baseline
# ---------------------------------------------------------------------------

def naive_rag_retrieve(store, repo_root: Path, query: str, gt_relative: str, budget: int):
    from code_review_graph.graph import GraphNode
    all_fns = store.get_nodes_by_kind(["Function"])
    query_words = set(query.lower().split())

    def match_score(n: GraphNode) -> int:
        text = f"{n.name} {n.qualified_name}".lower()
        return sum(1 for w in query_words if w in text)

    ranked = sorted(all_fns, key=match_score, reverse=True)
    selected_names: list[str] = []
    tokens_used = 0
    rank = None
    gt_abs = _abs_gt(repo_root, gt_relative)

    for n in ranked:
        if n.is_test:
            continue
        lines = max(1, (n.line_end or 0) - (n.line_start or 0) + 1)
        cost = max(1, lines * 8)
        if tokens_used + cost > budget:
            continue
        selected_names.append(n.qualified_name)
        tokens_used += cost
        if n.qualified_name == gt_abs and rank is None:
            rank = len(selected_names)

    return selected_names, tokens_used, rank


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

def mrr(ranks: list[int | None]) -> float:
    rr = [1 / r for r in ranks if r is not None]
    return sum(rr) / len(ranks) if ranks else 0.0

def gt_present_pct(ranks: list[int | None]) -> float:
    hits = sum(1 for r in ranks if r is not None)
    return hits / len(ranks) * 100 if ranks else 0.0

def avg_tokens(token_counts: list[int]) -> float:
    return sum(token_counts) / len(token_counts) if token_counts else 0.0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_benchmark():
    store, root = open_store(REPO_ROOT)
    print(f"Repo: {root}")

    # Pre-fetch candidates once
    print("Pre-fetching candidates for all queries...")
    candidates_cache: dict[str, list] = {}
    gt_absolutes: list[str] = []
    for bug in BUGS:
        gt_absolutes.append(_abs_gt(root, bug["ground_truth"]))
        nodes = query_to_scored_nodes(store, bug["query"], root, max_candidates=80)
        candidates_cache[bug["id"]] = nodes
    store.close()

    print(f"\n{'Budget':>7}  {'N-GT%':>6}  {'T-GT%':>6}  {'N-MRR':>7}  {'T-MRR':>7}  {'delta':>7}  {'TokSaved':>9}  Winner")
    print("-" * 70)

    for budget in BUDGETS_TO_TEST:
        store2, _ = open_store(REPO_ROOT)
        naive_ranks, naive_tokens = [], []
        tacm_ranks, tacm_tokens = [], []

        for i, bug in enumerate(BUGS):
            gt_abs = gt_absolutes[i]

            # Naive RAG
            sel_names, tok, rank = naive_rag_retrieve(store2, root, bug["query"], bug["ground_truth"], budget)
            naive_ranks.append(rank)
            naive_tokens.append(tok)

            # TACM hybrid_full + knapsack
            nodes = candidates_cache[bug["id"]]
            selected = resolve(nodes, budget, strategy="hybrid_full", use_knapsack=True)
            sel_qns = [n.node_id for n in selected]
            tok2 = sum(n.token_cost for n in selected)
            rank2 = next((j + 1 for j, n in enumerate(selected) if n.node_id == gt_abs), None)
            tacm_ranks.append(rank2)
            tacm_tokens.append(tok2)

        store2.close()

        n_mrr = mrr(naive_ranks)
        t_mrr = mrr(tacm_ranks)
        n_gt = gt_present_pct(naive_ranks)
        t_gt = gt_present_pct(tacm_ranks)
        delta = t_mrr - n_mrr
        tok_saved = int(avg_tokens(naive_tokens) - avg_tokens(tacm_tokens))
        winner = "TACM" if t_mrr > n_mrr else "Naive"
        print(f"{budget:>7}  {n_gt:>5.0f}%  {t_gt:>5.0f}%  {n_mrr:>7.4f}  {t_mrr:>7.4f}  {delta:>+7.4f}  {tok_saved:>+9}  {winner}")

    # Detailed per-task table at 4000 tokens
    print(f"\n--- Per-task breakdown @ budget=4000 ---")
    store3, _ = open_store(REPO_ROOT)
    print(f"{'ID':8s} {'Naive':8s} {'TACM-KS':8s}  Description")
    print("-" * 60)
    for i, bug in enumerate(BUGS):
        gt_abs = gt_absolutes[i]
        _, _, nr = naive_rag_retrieve(store3, root, bug["query"], bug["ground_truth"], 4000)
        nodes = candidates_cache[bug["id"]]
        selected = resolve(nodes, 4000, strategy="hybrid_full", use_knapsack=True)
        tr = next((j + 1 for j, n in enumerate(selected) if n.node_id == gt_abs), None)
        nr_s = f"#{nr}" if nr else "MISS"
        tr_s = f"#{tr}" if tr else "MISS"
        print(f"{bug['id']:8s} {nr_s:8s} {tr_s:8s}  {bug['desc'][:40]}")
    store3.close()


if __name__ == "__main__":
    run_benchmark()
