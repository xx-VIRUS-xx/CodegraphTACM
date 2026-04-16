"""bench4_g4a.py — G4-A experiment: query rewriter on tornado.

Compares Hybrid-Greedy with and without the LLM query rewriter (G4-A).
Prints rewrites for each bug so we can inspect what sub-queries Haiku generates.

Usage:
    python3 bench4_g4a.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from tacm.crg_adapter import open_store, query_to_scored_nodes
from tacm.resolver import resolve
from tacm.query_rewriter import rewrite_query

REPO_ROOT = Path(__file__).parent / "tornado"
BUDGET = 4000

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
]


def _abs_gt(repo_root: Path, gt_relative: str) -> str:
    parts = gt_relative.split("::")
    abs_file = str(repo_root / parts[0])
    return abs_file + "::" + parts[1] if len(parts) > 1 else abs_file


def mrr(ranks):
    rr = [1 / r for r in ranks if r is not None]
    return sum(rr) / len(ranks) if ranks else 0.0


def gt_pct(ranks):
    return sum(1 for r in ranks if r is not None) / len(ranks) * 100 if ranks else 0.0


def run():
    print(f"G4-A query rewriter experiment — tornadoweb/tornado @ budget={BUDGET}")
    print(f"Model: claude-haiku-4-5-20251001\n")

    # Print sub-queries before loading store (API calls are cheap, do upfront)
    print("=== Query rewrites (Haiku) ===")
    rewrites: dict[str, list[str]] = {}
    for bug in BUGS:
        subs = rewrite_query(bug["query"])
        rewrites[bug["id"]] = subs
        print(f"\n{bug['id']}: {bug['desc']}")
        print(f"  Original: {bug['query']}")
        for i, sq in enumerate(subs, 1):
            print(f"  Sub-{i}: {sq}")

    print("\n\n=== Per-task comparison @ budget=4000 ===")
    print(f"{'ID':<8} {'HG (base)':>10} {'HG+G4A':>8}  Description")
    print("-" * 60)

    store, root = open_store(REPO_ROOT)
    gt_absolutes = [_abs_gt(root, b["ground_truth"]) for b in BUGS]

    base_ranks = []
    g4a_ranks = []

    for i, bug in enumerate(BUGS):
        gt_abs = gt_absolutes[i]

        # Baseline: no rewriter
        nodes_base = query_to_scored_nodes(store, bug["query"], root, token_budget=BUDGET, use_rewriter=False)
        sel_base = resolve(nodes_base, BUDGET, strategy="hybrid_full", use_knapsack=False)
        base_r = next((j + 1 for j, n in enumerate(sel_base) if n.node_id == gt_abs), None)
        base_ranks.append(base_r)

        # G4-A: with rewriter
        nodes_g4a = query_to_scored_nodes(store, bug["query"], root, token_budget=BUDGET, use_rewriter=True)
        sel_g4a = resolve(nodes_g4a, BUDGET, strategy="hybrid_full", use_knapsack=False)
        g4a_r = next((j + 1 for j, n in enumerate(sel_g4a) if n.node_id == gt_abs), None)
        g4a_ranks.append(g4a_r)

        def fmt(r):
            return f"#{r}" if r else "MISS"

        delta = ""
        if base_r is None and g4a_r is not None:
            delta = " ← rescued"
        elif base_r is not None and g4a_r is None:
            delta = " ← regression"
        elif base_r is not None and g4a_r is not None and g4a_r < base_r:
            delta = f" ↑ +{base_r - g4a_r}"
        elif base_r is not None and g4a_r is not None and g4a_r > base_r:
            delta = f" ↓ -{g4a_r - base_r}"

        print(f"{bug['id']:<8} {fmt(base_r):>10} {fmt(g4a_r):>8}  {bug['desc'][:35]}{delta}")

    store.close()

    print(f"\n{'Metric':<20} {'HG (base)':>12} {'HG+G4A':>10}")
    print("-" * 45)
    print(f"{'GT%':<20} {gt_pct(base_ranks):>11.0f}% {gt_pct(g4a_ranks):>9.0f}%")
    print(f"{'MRR':<20} {mrr(base_ranks):>12.4f} {mrr(g4a_ranks):>10.4f}")
    delta_mrr = mrr(g4a_ranks) - mrr(base_ranks)
    delta_gt = gt_pct(g4a_ranks) - gt_pct(base_ranks)
    print(f"\nDelta: MRR {delta_mrr:+.4f}, GT% {delta_gt:+.0f}pp")


if __name__ == "__main__":
    run()
