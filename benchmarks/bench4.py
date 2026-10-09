"""bench4.py — Experiment 04: TACM vs Naive RAG on tornadoweb/tornado.

Fourth codebase validation: untouched codebase, no tuning, different domain (async HTTP).
Bugs sourced from BugsInPy tornado dataset. NL queries written from patch context only.

Usage:
    python3 bench4.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from tacm.crg_adapter import open_store, query_to_scored_nodes
from tacm.resolver import ScoredNode, resolve

REPO_ROOT = Path(__file__).parent / "tornado"
BUDGETS_TO_TEST = [800, 2000, 4000, 8000, 16000, 32000, 100000]

# ---------------------------------------------------------------------------
# Ground truth — 10 real tornadoweb/tornado bugs from BugsInPy.
# GT derived from bug_patch.txt hunk headers (class+method context lines).
# Queries written from patch diffs and commit context — no function names.
# BugsInPy bug IDs: 1-10
# ---------------------------------------------------------------------------

BUGS: list[dict] = [
    {
        "id": "tbug01",
        "desc": "WebSocket set_nodelay uses wrong attribute",
        "query": "websocket nodelay setting applied to wrong connection object causes assertion error",
        "ground_truth": "tornado/websocket.py::WebSocketHandler.set_nodelay",
    },
    {
        "id": "tbug02",
        "desc": "Chunked transfer encoding wrongly disabled when header present",
        "query": "HTTP chunked transfer encoding not used when Transfer-Encoding header already set",
        "ground_truth": "tornado/http1connection.py::HTTP1Connection.write_headers",
    },
    {
        "id": "tbug03",
        "desc": "AsyncHTTPClient close removes wrong instance from cache",
        "query": "async HTTP client close removes incorrect entry from instance cache on IOLoop",
        "ground_truth": "tornado/httpclient.py::AsyncHTTPClient.close",
    },
    {
        "id": "tbug04",
        "desc": "StaticFileHandler ignores negative byte-range start",
        "query": "static file handler does not support negative byte range offset from end of file",
        "ground_truth": "tornado/web.py::StaticFileHandler.get_content_size",
    },
    {
        "id": "tbug05",
        "desc": "PeriodicCallback drift when callback takes longer than interval",
        "query": "periodic callback accumulates drift when one execution takes longer than the interval",
        "ground_truth": "tornado/ioloop.py::PeriodicCallback._update_next",
    },
    {
        "id": "tbug06",
        "desc": "IOLoop.instance() not thread-safe during initialization",
        "query": "IOLoop global instance creation is not thread safe under concurrent access",
        "ground_truth": "tornado/ioloop.py::IOLoop.initialize",
    },
    {
        "id": "tbug07",
        "desc": "IOLoop.run_sync timeout does not clean up properly",
        "query": "run_sync timeout leaves pending callbacks and does not cancel the running future",
        "ground_truth": "tornado/ioloop.py::IOLoop.run_sync",
    },
    {
        "id": "tbug08",
        "desc": "WebSocket frame masking applied incorrectly on write",
        "query": "websocket outgoing frame mask applied to wrong byte position causing protocol error",
        "ground_truth": "tornado/websocket.py::WebSocketProtocol13.write_message",
    },
    {
        "id": "tbug09",
        "desc": "url_concat drops existing query parameters",
        "query": "concatenating query parameters to URL loses existing parameters already in URL string",
        "ground_truth": "tornado/httputil.py::url_concat",
    },
    {
        "id": "tbug10",
        "desc": "RequestHandler.finish called twice raises error",
        "query": "calling finish on response handler a second time raises unexpected error instead of being ignored",
        "ground_truth": "tornado/web.py::RequestHandler.finish",
    },
    {
        "id": "tbug11",
        "desc": "Chunked body not read when Transfer-Encoding header has mixed case",
        "query": "chunked body not parsed when Transfer-Encoding header value is not lowercase",
        "ground_truth": "tornado/http1connection.py::HTTP1Connection._read_body",
    },
    {
        "id": "tbug12",
        "desc": "FacebookGraphMixin.facebook_request fails when callback is a Future",
        "query": "oauth2 request callback is a future instead of callable causing authentication to fail",
        "ground_truth": "tornado/auth.py::FacebookGraphMixin.facebook_request",
    },
    {
        "id": "tbug13",
        "desc": "HTTP keep-alive detection raises AttributeError on response start lines",
        "query": "keep-alive detection crashes when start line has no method attribute on response",
        "ground_truth": "tornado/http1connection.py::HTTP1Connection._can_keep_alive",
    },
    {
        "id": "tbug14",
        "desc": "IOLoop.make_current raises when current IOLoop does not exist instead of when it does",
        "query": "make_current raises RuntimeError when no IOLoop exists instead of when one already exists",
        "ground_truth": "tornado/ioloop.py::IOLoop.make_current",
    },
    {
        "id": "tbug15",
        "desc": "StaticFileHandler allows path traversal outside root directory",
        "query": "static file handler serves files outside the root directory due to missing path separator check",
        "ground_truth": "tornado/web.py::StaticFileHandler.validate_absolute_path",
    },
    {
        "id": "tbug16",
        "desc": "WaitIterator holds reference cycle delaying garbage collection",
        "query": "wait iterator creates reference cycle preventing objects from being garbage collected",
        "ground_truth": "tornado/gen.py::WaitIterator.__init__",
    },
]


def _abs_gt(repo_root: Path, gt_relative: str) -> str:
    parts = gt_relative.split("::")
    abs_file = str(repo_root / parts[0])
    return abs_file + "::" + parts[1] if len(parts) > 1 else abs_file


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


def mrr(ranks):
    rr = [1 / r for r in ranks if r is not None]
    return sum(rr) / len(ranks) if ranks else 0.0

def gt_present_pct(ranks):
    return sum(1 for r in ranks if r is not None) / len(ranks) * 100 if ranks else 0.0


def run_benchmark():
    store, root = open_store(REPO_ROOT)
    print(f"Repo: {root}")

    all_prod = [n for n in store.get_nodes_by_kind(["Function"]) if not n.is_test]
    print(f"Graph: {len(all_prod)} prod nodes")

    gt_absolutes = [_abs_gt(root, b["ground_truth"]) for b in BUGS]

    print("Pre-fetching candidates per budget...")
    candidates_cache: dict[int, dict[str, list]] = {}
    for budget in BUDGETS_TO_TEST:
        candidates_cache[budget] = {}
        for bug in BUGS:
            nodes = query_to_scored_nodes(store, bug["query"], root, token_budget=budget)
            candidates_cache[budget][bug["id"]] = nodes
    store.close()

    print(f"\n{'Budget':>7}  {'N-GT%':>6}  {'S-GT%':>6}  {'HG-GT%':>7}  {'HK-GT%':>7}  {'N-MRR':>7}  {'S-MRR':>7}  {'HG-MRR':>8}  {'HK-MRR':>8}")
    print("-" * 90)

    for budget in BUDGETS_TO_TEST:
        store2, _ = open_store(REPO_ROOT)
        naive_ranks, s_ranks, hg_ranks, hk_ranks = [], [], [], []

        for i, bug in enumerate(BUGS):
            gt_abs = gt_absolutes[i]
            _, _, rank = naive_rag_retrieve(store2, root, bug["query"], bug["ground_truth"], budget)
            naive_ranks.append(rank)

            nodes = candidates_cache[budget][bug["id"]]

            sel = resolve(nodes, budget, strategy="structural", use_knapsack=True)
            s_ranks.append(next((j+1 for j,n in enumerate(sel) if n.node_id==gt_abs), None))

            sel = resolve(nodes, budget, strategy="hybrid_full", use_knapsack=False)
            hg_ranks.append(next((j+1 for j,n in enumerate(sel) if n.node_id==gt_abs), None))

            sel = resolve(nodes, budget, strategy="hybrid_full", use_knapsack=True)
            hk_ranks.append(next((j+1 for j,n in enumerate(sel) if n.node_id==gt_abs), None))

        store2.close()
        print(f"{budget:>7}  {gt_present_pct(naive_ranks):>5.0f}%  {gt_present_pct(s_ranks):>5.0f}%  "
              f"{gt_present_pct(hg_ranks):>6.0f}%  {gt_present_pct(hk_ranks):>6.0f}%  "
              f"{mrr(naive_ranks):>7.4f}  {mrr(s_ranks):>7.4f}  {mrr(hg_ranks):>8.4f}  {mrr(hk_ranks):>8.4f}")

    print(f"\n--- Per-task @ budget=4000 ---")
    store3, _ = open_store(REPO_ROOT)
    print(f"{'ID':<8} {'Naive':>6} {'Struct':>6} {'HybGrdy':>8} {'HybKS':>6}  Description")
    print("-" * 72)
    for i, bug in enumerate(BUGS):
        gt_abs = gt_absolutes[i]
        _, _, nr = naive_rag_retrieve(store3, root, bug["query"], bug["ground_truth"], 4000)
        nodes = candidates_cache[4000][bug["id"]]

        sel = resolve(nodes, 4000, strategy="structural", use_knapsack=True)
        sr = next((j+1 for j,n in enumerate(sel) if n.node_id==gt_abs), None)

        sel = resolve(nodes, 4000, strategy="hybrid_full", use_knapsack=False)
        hgr = next((j+1 for j,n in enumerate(sel) if n.node_id==gt_abs), None)

        sel = resolve(nodes, 4000, strategy="hybrid_full", use_knapsack=True)
        hkr = next((j+1 for j,n in enumerate(sel) if n.node_id==gt_abs), None)

        def fmt(r): return f"#{r}" if r else "MISS"
        print(f"{bug['id']:<8} {fmt(nr):>6} {fmt(sr):>6} {fmt(hgr):>8} {fmt(hkr):>6}  {bug['desc'][:40]}")

    store3.close()


if __name__ == "__main__":
    run_benchmark()
