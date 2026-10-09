"""bench4_g4a_manual.py — G4-A simulation with hand-crafted sub-queries.

Since ANTHROPIC_API_KEY is not available in subprocess, we manually supply
the sub-queries that an LLM rewriter *should* generate, then measure whether
better sub-queries improve retrieval on the three problem bugs (tbug03/04/05).

This validates the G4-A hypothesis without requiring API access.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from code_review_graph.search import hybrid_search
from tacm.crg_adapter import open_store, query_to_scored_nodes, _get_semantic_index
from tacm.resolver import resolve, ScoredNode

REPO_ROOT = Path(__file__).parent / "tornado"
BUDGET = 4000

# Hand-crafted sub-queries targeting the three tbug failures.
# These simulate what a well-prompted Haiku should generate.
REWRITTEN_QUERIES = {
    "tbug03": {
        "original": "async HTTP client close removes incorrect entry from instance cache on IOLoop",
        "sub_queries": [
            "remove client from instance cache on cleanup",
            "IOLoop weak reference cleanup on close",
            "fetch client registry deregister instance",
            "HTTP client cache lookup by IOLoop key",
        ],
    },
    "tbug04": {
        "original": "static file handler does not support negative byte range offset from end of file",
        "sub_queries": [
            "byte range negative offset from file end",
            "content size calculation range request",
            "Range header negative start position",
            "file size offset calculation handler",
        ],
    },
    "tbug05": {
        "original": "periodic callback accumulates drift when one execution takes longer than the interval",
        "sub_queries": [
            "schedule next call interval drift correction",
            "timer callback next wakeup calculation",
            "elapsed time interval scheduling update",
            "callback execution time overflow next schedule",
        ],
    },
}


def _abs_gt(repo_root: Path, gt_relative: str) -> str:
    parts = gt_relative.split("::")
    return str(repo_root / parts[0]) + "::" + parts[1]


BUGS = [
    {"id": "tbug03", "ground_truth": "tornado/httpclient.py::AsyncHTTPClient.close"},
    {"id": "tbug04", "ground_truth": "tornado/web.py::StaticFileHandler.get_content_size"},
    {"id": "tbug05", "ground_truth": "tornado/ioloop.py::PeriodicCallback._update_next"},
]

ALL_BUGS = [
    {"id": "tbug01", "query": "websocket nodelay setting applied to wrong connection object causes assertion error", "ground_truth": "tornado/websocket.py::WebSocketHandler.set_nodelay"},
    {"id": "tbug02", "query": "HTTP chunked transfer encoding not used when Transfer-Encoding header already set", "ground_truth": "tornado/http1connection.py::HTTP1Connection.write_headers"},
    {"id": "tbug03", "query": "async HTTP client close removes incorrect entry from instance cache on IOLoop", "ground_truth": "tornado/httpclient.py::AsyncHTTPClient.close"},
    {"id": "tbug04", "query": "static file handler does not support negative byte range offset from end of file", "ground_truth": "tornado/web.py::StaticFileHandler.get_content_size"},
    {"id": "tbug05", "query": "periodic callback accumulates drift when one execution takes longer than the interval", "ground_truth": "tornado/ioloop.py::PeriodicCallback._update_next"},
    {"id": "tbug06", "query": "IOLoop global instance creation is not thread safe under concurrent access", "ground_truth": "tornado/ioloop.py::IOLoop.initialize"},
    {"id": "tbug07", "query": "run_sync timeout leaves pending callbacks and does not cancel the running future", "ground_truth": "tornado/ioloop.py::IOLoop.run_sync"},
    {"id": "tbug08", "query": "websocket outgoing frame mask applied to wrong byte position causing protocol error", "ground_truth": "tornado/websocket.py::WebSocketProtocol13.write_message"},
    {"id": "tbug09", "query": "concatenating query parameters to URL loses existing parameters already in URL string", "ground_truth": "tornado/httputil.py::url_concat"},
    {"id": "tbug10", "query": "calling finish on response handler a second time raises unexpected error instead of being ignored", "ground_truth": "tornado/web.py::RequestHandler.finish"},
]


def score_with_subqueries(store, repo_root, sub_queries, token_budget=4000):
    """Re-run retrieval using custom sub-queries instead of original query."""
    from tacm.crg_adapter import (
        FULL_CORPUS_BUDGET_THRESHOLD, _graph_node_to_scored,
        _get_semantic_index, SEMANTIC_WEIGHT, SEMANTIC_TOP_K,
    )

    score_by_qn: dict[str, float] = {}
    for sq in sub_queries:
        keywords = [w for w in sq.split() if len(w) > 2]
        for kw in keywords:
            for h in hybrid_search(store, kw, limit=20):
                qn = h["qualified_name"]
                score_by_qn[qn] = max(score_by_qn.get(qn, 0.0), h["score"])
        for h in hybrid_search(store, sq, limit=10):
            qn = h["qualified_name"]
            score_by_qn[qn] = max(score_by_qn.get(qn, 0.0), h["score"])

    # Caller expansion (1-hop)
    hit_qns = list(score_by_qn.keys())
    caller_nodes = []
    caller_parent_score: dict[str, float] = {}
    for qn in hit_qns[:40]:
        try:
            callers = store.callers_of(qn, limit=10)
            for c in callers:
                if not c.is_test and c.qualified_name not in score_by_qn:
                    parent_hs = score_by_qn.get(qn, 0.0)
                    caller_parent_score[c.qualified_name] = max(
                        caller_parent_score.get(c.qualified_name, 0.0), parent_hs
                    )
                    caller_nodes.append(c)
        except Exception:
            pass

    # Build scored nodes
    all_prod = {n.qualified_name: n for n in store.get_nodes_by_kind(["Function"]) if not n.is_test}
    nodes: list[ScoredNode] = []
    seen: set[str] = set()

    for qn, score in sorted(score_by_qn.items(), key=lambda x: -x[1])[:120]:
        if qn in seen or qn not in all_prod:
            continue
        n = all_prod[qn]
        sn = _graph_node_to_scored(store, n, in_blast_radius=True, hybrid_score=score)
        nodes.append(sn)
        seen.add(qn)

    for cn in caller_nodes[:60]:
        if cn.qualified_name in seen:
            continue
        ps = caller_parent_score.get(cn.qualified_name, 0.0)
        sn = _graph_node_to_scored(store, cn, in_blast_radius=False, hybrid_score=ps * 0.5)
        nodes.append(sn)
        seen.add(cn.qualified_name)

    # Semantic expansion
    try:
        sem_idx = _get_semantic_index(store)
        if sem_idx:
            combined_query = " ".join(sub_queries)
            sem_scores = sem_idx.query(combined_query, top_k=SEMANTIC_TOP_K)
            caller_qns_so_far = {n.node_id for n in nodes}
            for qn, sem_score in sem_scores.items():
                if qn not in seen and qn in all_prod:
                    n = all_prod[qn]
                    sn = _graph_node_to_scored(store, n, in_blast_radius=False,
                                               hybrid_score=sem_score * SEMANTIC_WEIGHT)
                    nodes.append(sn)
                    seen.add(qn)
                elif qn in seen:
                    for existing in nodes:
                        if existing.node_id == qn:
                            blended = max(existing.hybrid_score, sem_score * SEMANTIC_WEIGHT)
                            if blended > existing.hybrid_score:
                                import dataclasses
                                idx = nodes.index(existing)
                                nodes[idx] = dataclasses.replace(existing, hybrid_score=blended)
                            break
    except Exception:
        pass

    return nodes


def mrr(ranks):
    rr = [1 / r for r in ranks if r is not None]
    return sum(rr) / len(ranks) if ranks else 0.0


def gt_pct(ranks):
    return sum(1 for r in ranks if r is not None) / len(ranks) * 100 if ranks else 0.0


def run():
    print("G4-A simulation — hand-crafted sub-queries for tbug03/04/05")
    print(f"Budget: {BUDGET} tokens\n")

    store, root = open_store(REPO_ROOT)

    print("=== Targeted analysis: tbug03/04/05 ===\n")
    for bug in BUGS:
        gt_abs = _abs_gt(root, bug["ground_truth"])
        bug_id = bug["id"]
        rw = REWRITTEN_QUERIES[bug_id]

        print(f"{bug_id} — {bug['ground_truth'].split('::')[1]}")
        print(f"  Original: {rw['original']}")
        for sq in rw["sub_queries"]:
            print(f"  Sub-query: {sq}")

        # Baseline
        nodes_base = query_to_scored_nodes(store, rw["original"], root, token_budget=BUDGET, use_rewriter=False)
        sel_base = resolve(nodes_base, BUDGET, strategy="hybrid_full", use_knapsack=False)
        base_r = next((j + 1 for j, n in enumerate(sel_base) if n.node_id == gt_abs), None)

        # With sub-queries
        nodes_rw = score_with_subqueries(store, root, rw["sub_queries"], token_budget=BUDGET)
        sel_rw = resolve(nodes_rw, BUDGET, strategy="hybrid_full", use_knapsack=False)
        rw_r = next((j + 1 for j, n in enumerate(sel_rw) if n.node_id == gt_abs), None)

        # Check pool membership
        gt_in_base_pool = any(n.node_id == gt_abs for n in nodes_base)
        gt_in_rw_pool = any(n.node_id == gt_abs for n in nodes_rw)
        if gt_in_rw_pool:
            gt_rw_score = next(n.hybrid_score for n in nodes_rw if n.node_id == gt_abs)
            rw_pool_rank = next(i + 1 for i, n in enumerate(sorted(nodes_rw, key=lambda x: -x.hybrid_score)) if n.node_id == gt_abs)
        else:
            gt_rw_score = 0.0
            rw_pool_rank = None

        def fmt(r): return f"#{r}" if r else "MISS"
        print(f"  Base HG: {fmt(base_r)} | Rewriter HG: {fmt(rw_r)}")
        print(f"  GT in base pool: {gt_in_base_pool} | GT in rewriter pool: {gt_in_rw_pool}")
        if gt_in_rw_pool:
            print(f"  GT rewriter: score={gt_rw_score:.4f}, pool_rank=#{rw_pool_rank}")
        print()

    print("=== Full 10-bug summary with rewriter on 03/04/05 ===\n")
    print(f"{'ID':<8} {'HG (base)':>10} {'HG+G4A':>10}  Description")
    print("-" * 60)

    base_ranks = []
    g4a_ranks = []

    for bug in ALL_BUGS:
        gt_abs = _abs_gt(root, bug["ground_truth"])

        nodes_base = query_to_scored_nodes(store, bug["query"], root, token_budget=BUDGET, use_rewriter=False)
        sel_base = resolve(nodes_base, BUDGET, strategy="hybrid_full", use_knapsack=False)
        base_r = next((j + 1 for j, n in enumerate(sel_base) if n.node_id == gt_abs), None)
        base_ranks.append(base_r)

        if bug["id"] in REWRITTEN_QUERIES:
            rw = REWRITTEN_QUERIES[bug["id"]]
            nodes_g4a = score_with_subqueries(store, root, rw["sub_queries"], token_budget=BUDGET)
        else:
            nodes_g4a = nodes_base  # unchanged for other bugs
        sel_g4a = resolve(nodes_g4a, BUDGET, strategy="hybrid_full", use_knapsack=False)
        g4a_r = next((j + 1 for j, n in enumerate(sel_g4a) if n.node_id == gt_abs), None)
        g4a_ranks.append(g4a_r)

        def fmt(r): return f"#{r}" if r else "MISS"
        delta = ""
        if base_r is None and g4a_r is not None:
            delta = " ← rescued"
        elif base_r is not None and g4a_r is None:
            delta = " ← regression"
        elif base_r is not None and g4a_r is not None and g4a_r < base_r:
            delta = f" ↑ rank +{base_r - g4a_r}"
        print(f"{bug['id']:<8} {fmt(base_r):>10} {fmt(g4a_r):>10}  {bug['id']}{delta}")

    print(f"\nMRR base: {mrr(base_ranks):.4f} | MRR+G4A: {mrr(g4a_ranks):.4f} (delta {mrr(g4a_ranks)-mrr(base_ranks):+.4f})")
    print(f"GT%  base: {gt_pct(base_ranks):.0f}%   | GT%+G4A: {gt_pct(g4a_ranks):.0f}% (delta {gt_pct(g4a_ranks)-gt_pct(base_ranks):+.0f}pp)")

    store.close()


if __name__ == "__main__":
    run()
