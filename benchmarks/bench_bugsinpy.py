"""bench_bugsinpy.py — BugsInPy benchmark runner with proper baselines.

Evaluates TACM vs three baselines:
  - Naive-Name: keyword match on function name only (original, weak)
  - BM25-Body:  BM25Okapi on full function source text (real BM25 baseline)
  - Semantic:   MiniLM top-K by cosine similarity only, no graph (isolates G3 vs graph)
  - TACM-HG:    G1+G2+G3 Hybrid-Greedy (full system)

Requirements:
- The project repo must be cloned and indexed with crg
- BugsInPy must be cloned at ./BugsInPy/
- rank_bm25 installed: pip install rank_bm25

Usage:
    python3 bench_bugsinpy.py --project thefuck --repo ./thefuck --max 30 --budget 4000
    python3 bench_bugsinpy.py --project scrapy  --repo ./scrapy  --max 30 --budget 800 4000
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from rank_bm25 import BM25Okapi

from tacm.bugsinpy import load_tasks, BUGSINPY_ROOT
from tacm.crg_adapter import open_store, query_to_scored_nodes
from tacm.resolver import ScoredNode, resolve


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def _commit_msg(repo_root: Path, commit: str) -> str:
    if not commit:
        return ""
    try:
        r = subprocess.run(
            ["git", "log", "--format=%s", "-1", commit],
            cwd=repo_root, capture_output=True, text=True, timeout=10,
        )
        return r.stdout.strip()
    except Exception:
        return ""


def _tokenize(text: str) -> list[str]:
    """Lowercase word-boundary tokenizer for BM25."""
    return re.findall(r"[a-z0-9]+", text.lower())


def _gt_match(gt_functions: list[str], candidates: list[ScoredNode]) -> int | None:
    """Return rank (1-based) of the first GT function found, or None."""
    for rank, node in enumerate(candidates, 1):
        qn = node.node_id
        suffix = qn.split("::")[-1] if "::" in qn else qn
        for gt in gt_functions:
            if suffix == gt or qn.endswith(f"::{gt}"):
                return rank
            if "." not in gt and suffix.split(".")[-1] == gt:
                return rank
    return None


def _gt_match_list(gt_functions: list[str], ranked: list) -> int | None:
    """Match against a plain list of ScoredNode (not necessarily ScoredNode type)."""
    return _gt_match(gt_functions, ranked)


def mrr(ranks: list[int | None]) -> float:
    return sum(1 / r for r in ranks if r is not None) / len(ranks) if ranks else 0.0


def gt_pct(ranks: list[int | None]) -> float:
    return 100 * sum(1 for r in ranks if r is not None) / len(ranks) if ranks else 0.0


# ---------------------------------------------------------------------------
# Baselines
# ---------------------------------------------------------------------------

def _naive_name_rank(nodes: list[ScoredNode], query: str) -> list[ScoredNode]:
    """Original weak baseline: keyword overlap on function name only."""
    qwords = set(query.lower().split())
    return sorted(
        [n for n in nodes if not n.is_test],
        key=lambda n: sum(1 for w in qwords if w in n.name.lower()),
        reverse=True,
    )


def _bm25_body_rank(nodes: list[ScoredNode], query: str) -> list[ScoredNode]:
    """BM25Okapi on full function source text — real BM25 baseline."""
    prod = [n for n in nodes if not n.is_test]
    if not prod:
        return []
    corpus = [_tokenize((n.source_text or n.name)) for n in prod]
    q_tokens = _tokenize(query)
    if not q_tokens:
        return prod
    bm25 = BM25Okapi(corpus)
    scores = bm25.get_scores(q_tokens)
    return [n for _, n in sorted(zip(scores, prod), key=lambda x: -x[0])]


def _semantic_only_rank(nodes: list[ScoredNode], query: str, sem_index) -> list[ScoredNode]:
    """MiniLM cosine similarity only — no graph signals (isolates G3 vs G1+G2).

    Ranks from the full candidate pool by semantic score alone.
    """
    if sem_index is None:
        return []
    prod = [n for n in nodes if not n.is_test]
    if not prod:
        return []
    # query() returns dict {qualified_name: score}
    scores_dict = sem_index.query(query, top_k=len(sem_index.qualified_names))
    # Map scores back to ScoredNode list
    scored = [(scores_dict.get(n.node_id, 0.0), n) for n in prod]
    return [n for _, n in sorted(scored, key=lambda x: -x[0])]


# ---------------------------------------------------------------------------
# Main benchmark
# ---------------------------------------------------------------------------

def run_benchmark(
    project: str,
    repo_root: Path,
    budgets: list[int],
    max_bugs: int = 30,
    two_hop: bool = True,
    show_pertask: bool = True,
) -> None:
    print(f"Project: {project}  Repo: {repo_root}")

    tasks = load_tasks(
        BUGSINPY_ROOT,
        projects=[project],
        max_per_project=max_bugs,
        require_gt=True,
        max_gt_functions=3,
    )
    if not tasks:
        print(f"No tasks loaded for {project}.")
        return

    for task in tasks:
        if not task.query:
            task.query = _commit_msg(repo_root, task.fixed_commit)

    no_query = sum(1 for t in tasks if not t.query)
    print(f"Tasks: {len(tasks)}  (no query: {no_query})")

    store, root = open_store(repo_root)
    all_prod = [n for n in store.get_nodes_by_kind(["Function"]) if not n.is_test]
    print(f"Graph: {len(all_prod)} prod nodes")

    # Load semantic index for semantic-only baseline
    try:
        from tacm.semantic import SemanticIndex
        db_path = repo_root / ".code-review-graph" / "graph.db"
        sem_index = SemanticIndex.build(db_path, all_prod)
        print(f"Semantic index: {'loaded' if sem_index else 'unavailable (build returned None)'}")
    except Exception as e:
        sem_index = None
        print(f"Semantic index: unavailable ({e})")

    # Pre-fetch TACM candidates (budget-dependent, includes graph traversal)
    print("Pre-fetching candidates...")
    candidates_cache: dict[int, dict[str, tuple]] = {}
    for budget in budgets:
        candidates_cache[budget] = {}
        for task in tasks:
            query = task.query or (task.gt_files[0].replace("/", " ").replace("_", " ").replace(".py", "") if task.gt_files else "bug")
            nodes = query_to_scored_nodes(
                store, query, root,
                token_budget=budget,
                use_rewriter=False,
                two_hop=two_hop,
                use_cochange=False,
            )
            candidates_cache[budget][task.bug_id] = (nodes, query)
    store.close()

    # Header
    print(f"\n{'Budget':>7}  {'NaiveName':>9}  {'BM25Body':>8}  {'Semantic':>8}  {'TACM-HG':>7}  "
          f"{'NN-MRR':>7}  {'BM25-MRR':>8}  {'Sem-MRR':>7}  {'HG-MRR':>7}")
    print("-" * 90)

    for budget in budgets:
        nn_ranks, bm25_ranks, sem_ranks, hg_ranks = [], [], [], []

        for task in tasks:
            nodes, query = candidates_cache[budget][task.bug_id]
            prod_nodes = [n for n in nodes if not n.is_test]

            nn_ranks.append(_gt_match(task.gt_functions, _naive_name_rank(nodes, query)))
            bm25_ranks.append(_gt_match(task.gt_functions, _bm25_body_rank(nodes, query)))

            if sem_index is not None:
                sem_sorted = _semantic_only_rank(nodes, query, sem_index)
                sem_ranks.append(_gt_match(task.gt_functions, sem_sorted))
            else:
                sem_ranks.append(None)

            hg_selected = resolve(nodes, token_budget=budget, strategy="hybrid_full", use_knapsack=False)
            hg_ranks.append(_gt_match(task.gt_functions, hg_selected))

        sem_str = f"{gt_pct(sem_ranks):>7.0f}%" if sem_index else "   N/A  "
        sem_mrr = f"{mrr(sem_ranks):>7.4f}" if sem_index else "   N/A "
        print(
            f"{budget:>7}  {gt_pct(nn_ranks):>8.0f}%  {gt_pct(bm25_ranks):>7.0f}%  "
            f"{sem_str}  {gt_pct(hg_ranks):>6.0f}%"
            f"  {mrr(nn_ranks):>7.4f}  {mrr(bm25_ranks):>8.4f}  {sem_mrr}  {mrr(hg_ranks):>7.4f}"
        )

    # Per-task at first budget
    if show_pertask:
        budget = budgets[0]
        print(f"\n--- Per-task @ budget={budget} ---")
        print(f"{'ID':<22} {'NN':>5} {'BM25':>5} {'Sem':>5} {'HG':>5}  GT")
        print("-" * 70)
        for task in tasks:
            nodes, query = candidates_cache[budget][task.bug_id]

            nn_r  = _gt_match(task.gt_functions, _naive_name_rank(nodes, query))
            bm25_r = _gt_match(task.gt_functions, _bm25_body_rank(nodes, query))
            sem_r  = _gt_match(task.gt_functions, _semantic_only_rank(nodes, query, sem_index)) if sem_index else None
            hg_sel = resolve(nodes, token_budget=budget, strategy="hybrid_full", use_knapsack=False)
            hg_r   = _gt_match(task.gt_functions, hg_sel)

            def fmt(r): return f"#{r}" if r else "MISS"
            gt_short = ", ".join(task.gt_functions[:2])
            print(f"{task.bug_id:<22} {fmt(nn_r):>5} {fmt(bm25_r):>5} {fmt(sem_r):>5} {fmt(hg_r):>5}  {gt_short}")


def main():
    parser = argparse.ArgumentParser(description="BugsInPy TACM benchmark with proper baselines")
    parser.add_argument("--project", required=True)
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--max", type=int, default=30)
    parser.add_argument("--budget", type=int, nargs="+", default=[800, 4000])
    parser.add_argument("--no-two-hop", action="store_true")
    parser.add_argument("--no-pertask", action="store_true")
    args = parser.parse_args()

    run_benchmark(
        project=args.project,
        repo_root=args.repo,
        budgets=args.budget,
        max_bugs=args.max,
        two_hop=not args.no_two_hop,
        show_pertask=not args.no_pertask,
    )


if __name__ == "__main__":
    main()
