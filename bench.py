"""bench.py — Experiment 01: TACM Resolver strategies vs Naive RAG baseline.

Runs fully offline. No LLM call needed for retrieval metrics.
Ground truth = qualified_name of the function touched in each bug's fix commit.

Usage:
    python bench.py

Output:
    Per-task breakdown + aggregate table for all strategies.
"""

from __future__ import annotations

import sys
import time
from pathlib import Path
from typing import NamedTuple

sys.path.insert(0, str(Path(__file__).parent))

from tacm.crg_adapter import open_store, query_to_scored_nodes
from tacm.resolver import ScoredNode, resolve, Strategy

REPO_ROOT = Path(__file__).parent / "requests"
TOKEN_BUDGET = 4000   # realistic budget for actual LLM context usage
BUDGETS_TO_TEST = [800, 2000, 4000]


# ---------------------------------------------------------------------------
# Ground truth — 10 real psf/requests bugs with known fix locations
# These are derived from actual fix commits in psf/requests history.
# qualified_name format: file_path::ClassName.method_name
# ---------------------------------------------------------------------------

BUGS: list[dict] = [
    {
        "id": "bug01",
        "desc": "Unicode URL encoding — non-ASCII chars in URL path corrupt request",
        "query": "non-ASCII characters in URL path cause malformed request",
        "ground_truth": "src/requests/models.py::PreparedRequest.prepare_url",
    },
    {
        "id": "bug02",
        "desc": "Redirect loop — infinite redirect when Location header loops",
        "query": "HTTP client follows redirects infinitely without stopping",
        "ground_truth": "src/requests/sessions.py::SessionRedirectMixin.resolve_redirects",
    },
    {
        "id": "bug03",
        "desc": "Session cookies not sent after redirect to different host",
        "query": "cookies from session not included when redirecting to another host",
        "ground_truth": "src/requests/sessions.py::SessionRedirectMixin.rebuild_auth",
    },
    {
        "id": "bug04",
        "desc": "Proxy auth header stripped on redirect",
        "query": "proxy authentication credentials lost after redirect",
        "ground_truth": "src/requests/sessions.py::SessionRedirectMixin.rebuild_proxies",
    },
    {
        "id": "bug05",
        "desc": "Response encoding detection wrong for UTF-16 content",
        "query": "response text has wrong characters, encoding not detected from headers",
        "ground_truth": "src/requests/utils.py::get_encoding_from_headers",
    },
    {
        "id": "bug06",
        "desc": "Cookie jar not updated when merging session and request cookies",
        "query": "cookies set in session missing from merged request cookie jar",
        "ground_truth": "src/requests/cookies.py::merge_cookies",
    },
    {
        "id": "bug07",
        "desc": "SSL version compatibility check raises wrong error",
        "query": "SSL library version mismatch raises unexpected error on import",
        "ground_truth": "src/requests/__init__.py::check_compatibility",
    },
    {
        "id": "bug08",
        "desc": "Cookies from response not extracted to jar properly",
        "query": "set-cookie header from server not stored in cookie jar after response",
        "ground_truth": "src/requests/cookies.py::extract_cookies_to_jar",
    },
    {
        "id": "bug09",
        "desc": "Double percent-encoding of already-encoded URLs",
        "query": "URL with percent-encoded characters gets double-encoded on second call",
        "ground_truth": "src/requests/utils.py::requote_uri",
    },
    {
        "id": "bug10",
        "desc": "Auth credentials not parsed from URL with special chars",
        "query": "username and password in URL with special characters not parsed correctly",
        "ground_truth": "src/requests/utils.py::get_auth_from_url",
    },
]

def _abs_gt(repo_root: Path, gt_relative: str) -> str:
    """Convert relative GT path (src/requests/...) to absolute qualified_name."""
    # GT format: "src/requests/models.py::PreparedRequest.prepare_url"
    # QN format: "/abs/path/requests/src/requests/models.py::PreparedRequest.prepare_url"
    parts = gt_relative.split("::")
    abs_file = str(repo_root / parts[0])
    return abs_file + "::" + parts[1] if len(parts) > 1 else abs_file


# ---------------------------------------------------------------------------
# Naive RAG baseline — keyword BM25 over all function names + signatures
# (No graph structure — pure text retrieval within token budget)
# ---------------------------------------------------------------------------

class NaiveRAGResult(NamedTuple):
    selected_names: list[str]
    tokens_used: int
    rank: int | None   # 1-based rank of GT in selected list, None if absent


def naive_rag_retrieve(
    store,
    repo_root: Path,
    query: str,
    gt_relative: str,
    budget: int = TOKEN_BUDGET,
) -> NaiveRAGResult:
    """BM25 text search over all nodes, greedily fill to budget, no graph scoring."""
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

    return NaiveRAGResult(selected_names, tokens_used, rank)


# ---------------------------------------------------------------------------
# TACM retrieval — one run per strategy
# ---------------------------------------------------------------------------

class TACMResult(NamedTuple):
    selected_names: list[str]
    tokens_used: int
    rank: int | None
    strategy: Strategy


def tacm_retrieve(
    store,
    repo_root: Path,
    query: str,
    gt_relative: str,
    strategy: Strategy,
    budget: int = TOKEN_BUDGET,
) -> TACMResult:
    nodes = query_to_scored_nodes(store, query, repo_root)
    selected = resolve(nodes, budget, strategy=strategy)

    gt_abs = _abs_gt(repo_root, gt_relative)
    selected_names = [n.node_id for n in selected]
    tokens_used = sum(n.token_cost for n in selected)
    rank = None
    for i, n in enumerate(selected):
        if n.node_id == gt_abs:
            rank = i + 1
            break

    return TACMResult(selected_names, tokens_used, rank, strategy)


# ---------------------------------------------------------------------------
# Metrics helpers
# ---------------------------------------------------------------------------

def mrr(ranks: list[int | None]) -> float:
    rr = [1 / r for r in ranks if r is not None]
    return sum(rr) / len(ranks) if ranks else 0.0


def gt_present_pct(ranks: list[int | None]) -> float:
    hits = sum(1 for r in ranks if r is not None)
    return hits / len(ranks) * 100 if ranks else 0.0


def avg_tokens(token_counts: list[int]) -> float:
    return sum(token_counts) / len(token_counts) if token_counts else 0.0


def precision_at_k(selected_names_list: list[list[str]], gt_list: list[str], k: int = 5) -> float:
    scores = []
    for selected, gt_abs in zip(selected_names_list, gt_list):
        top_k = selected[:k]
        hit = 1 if gt_abs in top_k else 0
        scores.append(hit / k)
    return sum(scores) / len(scores) if scores else 0.0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_benchmark():
    store, root = open_store(REPO_ROOT)
    print(f"Repo: {root}")
    print(f"Token budget: {TOKEN_BUDGET}\n")
    print(f"{'ID':6s} {'GT present?':12s} {'Rank':6s}  Query")
    print("-" * 80)

    # (strategy_key, label, use_knapsack)
    strategy_configs: list[tuple[str, str, bool]] = [
        ("structural",  "Structural",  False),
        ("hybrid_full", "Hybrid-Grdy", False),
        ("hybrid_full", "Hybrid-KS",   True),
    ]
    config_keys = [label for _, label, _ in strategy_configs]

    def fmt(v: float, is_pct: bool = False) -> str:
        if is_pct:
            return f"{v:.1f}%"
        return f"{v:.4f}" if v < 10 else f"{v:.1f}"

    # Pre-fetch candidates once (hybrid_search is the expensive step)
    print("Pre-fetching candidates for all queries...")
    candidates_cache: dict[str, list] = {}
    gt_absolutes: list[str] = []
    for bug in BUGS:
        gt_absolutes.append(_abs_gt(root, bug["ground_truth"]))
        nodes = query_to_scored_nodes(store, bug["query"], root, max_candidates=80)
        candidates_cache[bug["id"]] = nodes
    store.close()

    for budget in BUDGETS_TO_TEST:
        print(f"\n{'='*74}")
        print(f"TOKEN BUDGET: {budget}")
        print(f"{'='*74}")

        naive_ranks: list[int | None] = []
        naive_tokens: list[int] = []
        naive_selected_all: list[list[str]] = []

        # keyed by label
        tacm_data: dict[str, dict] = {
            label: {"ranks": [], "tokens": [], "selected_all": []}
            for _, label, _ in strategy_configs
        }

        store2, _ = open_store(REPO_ROOT)
        for i, bug in enumerate(BUGS):
            gt_abs = gt_absolutes[i]
            nodes = candidates_cache[bug["id"]]

            naive = naive_rag_retrieve(store2, root, bug["query"], bug["ground_truth"], budget)
            naive_ranks.append(naive.rank)
            naive_tokens.append(naive.tokens_used)
            naive_selected_all.append(naive.selected_names)

            for strat_key, label, use_ks in strategy_configs:
                selected = resolve(nodes, budget, strategy=strat_key, use_knapsack=use_ks)
                sel_names = [n.node_id for n in selected]
                tok = sum(n.token_cost for n in selected)
                rank = next((j + 1 for j, n in enumerate(selected) if n.node_id == gt_abs), None)
                tacm_data[label]["ranks"].append(rank)
                tacm_data[label]["tokens"].append(tok)
                tacm_data[label]["selected_all"].append(sel_names)
        store2.close()

        # Per-task table
        CW = 12
        hdr = f"{'ID':6s} {'Naive':{CW}}" + "".join(f"{lbl:{CW}}" for lbl in config_keys) + "  Description"
        print("\n" + hdr)
        print("-" * len(hdr))
        for i, bug in enumerate(BUGS):
            nr = naive_ranks[i]
            row = f"{bug['id']:6s} {'#'+str(nr) if nr else 'MISS':{CW}}"
            for lbl in config_keys:
                r = tacm_data[lbl]["ranks"][i]
                row += f"{'#'+str(r) if r else 'MISS':{CW}}"
            print(row + "  " + bug["desc"][:40])

        # Aggregate metrics
        all_labels = ["Naive RAG"] + config_keys
        rows: dict[str, dict] = {}
        for lbl in all_labels:
            if lbl == "Naive RAG":
                ra, to, se = naive_ranks, naive_tokens, naive_selected_all
            else:
                ra = tacm_data[lbl]["ranks"]
                to = tacm_data[lbl]["tokens"]
                se = tacm_data[lbl]["selected_all"]
            rows[lbl] = {
                "gt_pct":  gt_present_pct(ra),
                "mrr":     mrr(ra),
                "p5":      precision_at_k(se, gt_absolutes, k=5),
                "avg_tok": avg_tokens(to),
            }

        COL = 13
        print()
        h2 = f"{'Metric':<22}" + "".join(f"{lbl:>{COL}}" for lbl in all_labels)
        print(h2)
        print("-" * len(h2))
        for mn, mk, pct in [("GT Present (%)", "gt_pct", True), ("MRR", "mrr", False),
                             ("Precision@5", "p5", False), ("Avg tokens", "avg_tok", True)]:
            print(f"{mn:<22}", end="")
            for lbl in all_labels:
                print(f"{fmt(rows[lbl][mk], pct):>{COL}}", end="")
            print()

        print(f"\n{'Delta vs Naive RAG':<22}", end="")
        for lbl in config_keys:
            print(f"{lbl:>{COL}}", end="")
        print()
        print("-" * (22 + COL * len(config_keys)))
        for mn, mk in [("GT present (pp)", "gt_pct"), ("MRR", "mrr"), ("P@5", "p5")]:
            base = rows["Naive RAG"][mk]
            print(f"{mn:<22}", end="")
            for lbl in config_keys:
                d = rows[lbl][mk] - base
                cell = f"{'+' if d >= 0 else ''}{d:.4f}"
                print(f"{cell:>{COL}}", end="")
            print()
        base_tok = rows["Naive RAG"]["avg_tok"]
        print(f"{'Tok reduction (avg)':<22}", end="")
        for lbl in config_keys:
            d = base_tok - rows[lbl]["avg_tok"]
            cell = f"{'+' if d >= 0 else ''}{d:.1f}"
            print(f"{cell:>{COL}}", end="")
        print()

        print(f"\nSuccess criteria @ budget={budget}:")
        for lbl in config_keys:
            mrr_ok = rows[lbl]["mrr"] >= rows["Naive RAG"]["mrr"] + 0.1
            tok_ok = rows[lbl]["avg_tok"] <= rows["Naive RAG"]["avg_tok"]
            gt_ok  = rows[lbl]["gt_pct"] >= rows["Naive RAG"]["gt_pct"]
            passed = sum([mrr_ok, tok_ok, gt_ok])
            print(f"  {lbl:13s}: MRR+0.1={'PASS' if mrr_ok else 'FAIL'}  "
                  f"tokens<={'PASS' if tok_ok else 'FAIL'}  "
                  f"GT>=   {'PASS' if gt_ok else 'FAIL'}  → {passed}/3")


if __name__ == "__main__":
    run_benchmark()
