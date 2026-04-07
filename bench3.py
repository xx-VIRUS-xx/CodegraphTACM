"""bench3.py — Experiment 03: TACM vs Naive RAG on sqlalchemy/sqlalchemy.

Third codebase validation: different domain (ORM/SQL toolkit), much larger graph
(15k+ nodes vs 315/801 for requests/flask), deep inheritance hierarchies.

Queries: natural language only — no function names, from issue descriptions.

Usage:
    python3 bench3.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from tacm.crg_adapter import open_store, query_to_scored_nodes
from tacm.resolver import resolve

REPO_ROOT = Path(__file__).parent / "sqlalchemy"
BUDGETS_TO_TEST = [800, 2000, 4000, 8000, 16000, 32000, 100000]

# ---------------------------------------------------------------------------
# Ground truth — 10 real sqlalchemy/sqlalchemy bugs, NL queries from issue text.
# Fix commits: d466d375, 6ee4d884, e4a802f9, 3cf6c111, 2ac8c1a7,
#              0f74af5c,  ca092e73, cdaf1824, d526cede, a55a8712
# ---------------------------------------------------------------------------

BUGS: list[dict] = [
    {
        "id": "sbug01",
        "desc": "Session.get() always hits DB when with_for_update=False",
        "query": "loading object from session always goes to database even when it is already in the identity map",
        "ground_truth": "lib/sqlalchemy/orm/session.py::Session.get",
        # fix: d466d375 — with_for_update=False was not treated same as None
    },
    {
        "id": "sbug02",
        "desc": "Parameters mutated in do_orm_execute event not used",
        "query": "changes made to query parameters inside an ORM execute event handler are ignored and not passed to the database",
        "ground_truth": "lib/sqlalchemy/orm/session.py::Session.execute",
        # fix: 6ee4d884 — ORMExecuteState.parameters mutation not propagated
    },
    {
        "id": "sbug03",
        "desc": "add_property raises AttributeError in mapper event hooks",
        "query": "calling add_property on a mapper inside a mapper event raises AttributeError because collections are not initialized yet",
        "ground_truth": "lib/sqlalchemy/orm/mapper.py::Mapper.add_property",
        # fix: e4a802f9 — early_setup check missing for property collection init
    },
    {
        "id": "sbug04",
        "desc": "joinedload + selectinload with of_type polymorphic not applied",
        "query": "chained eager loading options on a polymorphic relationship are not applied, related objects not loaded",
        "ground_truth": "lib/sqlalchemy/orm/path_registry.py::_AbstractEntityRegistry._getitem",
        # fix: 3cf6c111 — natural path not computed correctly for polymorphic
    },
    {
        "id": "sbug05",
        "desc": "selectinload after joinedload with of_type subclass not working",
        "query": "secondary eager load option after joinedload with subclass type filter silently does nothing",
        "ground_truth": "lib/sqlalchemy/orm/strategies.py::SelectInLoad.create_row_processor",
        # fix: 2ac8c1a7 — entity_isa check fails for subclass mapper
    },
    {
        "id": "sbug06",
        "desc": "WeakSequence.__getitem__ wrong exception type caught",
        "query": "accessing an index out of range on an internal sequence type raises wrong error message",
        "ground_truth": "lib/sqlalchemy/util/_collections.py::WeakSequence.__getitem__",
        # fix: 0f74af5c — catching KeyError instead of IndexError on a list
    },
    {
        "id": "sbug07",
        "desc": "AsyncResult.scalar() raises AttributeError",
        "query": "calling scalar on an async query result raises AttributeError about a missing attribute",
        "ground_truth": "lib/sqlalchemy/ext/asyncio/result.py::AsyncResult.__init__",
        # fix: ca092e73 — _source_supports_scalars not copied to AsyncResult
    },
    {
        "id": "sbug08",
        "desc": "SQLite reflection fails for constraint names with uppercase",
        "query": "reflecting a SQLite table fails when a constraint has an uppercase letter in its name",
        "ground_truth": "lib/sqlalchemy/dialects/sqlite/base.py::SQLiteDialect.get_pk_constraint",
        # fix: cdaf1824 — regex didn't handle quoted constraint names
    },
    {
        "id": "sbug09",
        "desc": "SQLite reflection fails for generated columns in WITHOUT ROWID tables",
        "query": "reflecting a SQLite table with generated columns raises an error when the table uses WITHOUT ROWID",
        "ground_truth": "lib/sqlalchemy/dialects/sqlite/base.py::SQLiteDialect.get_columns",
        # fix: d526cede — regex for generated column detection didn't allow table options
    },
    {
        "id": "sbug10",
        "desc": "use_existing_column with Annotated mapped_column in polymorphic fails",
        "query": "defining a column on a subclass mapper using use_existing_column with type annotations raises an error in polymorphic inheritance",
        "ground_truth": "lib/sqlalchemy/orm/properties.py::MappedColumn.declarative_scan",
        # fix: a55a8712 — use_existing_column path didn't handle Annotated type
    },
]


def _abs_gt(repo_root: Path, gt_relative: str) -> str:
    parts = gt_relative.split("::")
    abs_file = str(repo_root / parts[0])
    return abs_file + "::" + parts[1] if len(parts) > 1 else abs_file


def naive_rag_retrieve(store, repo_root: Path, query: str, gt_relative: str, budget: int):
    all_fns = store.get_nodes_by_kind(["Function"])
    query_words = set(query.lower().split())

    def match_score(n) -> int:
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


def mrr(ranks): return sum(1/r for r in ranks if r) / len(ranks) if ranks else 0.0
def gt_pct(ranks): return sum(1 for r in ranks if r) / len(ranks) * 100 if ranks else 0.0
def avg_tok(toks): return sum(toks) / len(toks) if toks else 0.0


def run_benchmark():
    store, root = open_store(REPO_ROOT)
    print(f"Repo: {root}")

    fns = store.get_nodes_by_kind(["Function"])
    prod = [n for n in fns if not n.is_test]
    print(f"Graph: {len(prod)} prod nodes")

    print("Pre-fetching candidates per budget...")
    candidates_cache: dict[int, dict[str, list]] = {}
    gt_absolutes = [_abs_gt(root, b["ground_truth"]) for b in BUGS]

    for budget in BUDGETS_TO_TEST:
        candidates_cache[budget] = {}
        for bug in BUGS:
            nodes = query_to_scored_nodes(store, bug["query"], root,
                                          max_candidates=80, token_budget=budget)
            candidates_cache[budget][bug["id"]] = nodes
    store.close()

    print(f"\n{'Budget':>7}  {'N-GT%':>6}  {'S-GT%':>6}  {'HG-GT%':>7}  {'HK-GT%':>7}  {'N-MRR':>7}  {'S-MRR':>7}  {'HG-MRR':>8}  {'HK-MRR':>8}")
    print("-" * 90)

    for budget in BUDGETS_TO_TEST:
        store2, _ = open_store(REPO_ROOT)
        n_ranks, n_toks = [], []
        s_ranks = []
        hg_ranks = []
        hk_ranks = []

        for i, bug in enumerate(BUGS):
            gt_abs = gt_absolutes[i]

            _, tok, rank = naive_rag_retrieve(store2, root, bug["query"], bug["ground_truth"], budget)
            n_ranks.append(rank); n_toks.append(tok)

            nodes = candidates_cache[budget][bug["id"]]

            sel = resolve(nodes, budget, strategy="structural", use_knapsack=True)
            s_ranks.append(next((j+1 for j,n in enumerate(sel) if n.node_id==gt_abs), None))

            sel = resolve(nodes, budget, strategy="hybrid_full", use_knapsack=False)
            hg_ranks.append(next((j+1 for j,n in enumerate(sel) if n.node_id==gt_abs), None))

            sel = resolve(nodes, budget, strategy="hybrid_full", use_knapsack=True)
            hk_ranks.append(next((j+1 for j,n in enumerate(sel) if n.node_id==gt_abs), None))

        store2.close()
        print(f"{budget:>7}  {gt_pct(n_ranks):>5.0f}%  {gt_pct(s_ranks):>5.0f}%  "
              f"{gt_pct(hg_ranks):>6.0f}%  {gt_pct(hk_ranks):>6.0f}%  "
              f"{mrr(n_ranks):>7.4f}  {mrr(s_ranks):>7.4f}  {mrr(hg_ranks):>8.4f}  {mrr(hk_ranks):>8.4f}")

    # Per-task at 4000
    print(f"\n--- Per-task @ budget=4000 ---")
    store3, _ = open_store(REPO_ROOT)
    print(f"{'ID':8s} {'Naive':8s} {'Struct':8s} {'HybGrdy':8s} {'HybKS':8s}  Description")
    print("-" * 74)
    for i, bug in enumerate(BUGS):
        gt_abs = gt_absolutes[i]
        _, _, nr = naive_rag_retrieve(store3, root, bug["query"], bug["ground_truth"], 4000)
        nodes = candidates_cache[4000][bug["id"]]

        sel_s  = resolve(nodes, 4000, strategy="structural",  use_knapsack=True)
        sel_hg = resolve(nodes, 4000, strategy="hybrid_full", use_knapsack=False)
        sel_hk = resolve(nodes, 4000, strategy="hybrid_full", use_knapsack=True)

        def rank_str(sel): r = next((j+1 for j,n in enumerate(sel) if n.node_id==gt_abs), None); return f"#{r}" if r else "MISS"
        print(f"{bug['id']:8s} {'#'+str(nr) if nr else 'MISS':8s} {rank_str(sel_s):8s} {rank_str(sel_hg):8s} {rank_str(sel_hk):8s}  {bug['desc'][:38]}")
    store3.close()


if __name__ == "__main__":
    run_benchmark()
