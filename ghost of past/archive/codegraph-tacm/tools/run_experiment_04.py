"""Experiment 04: retrieval-context benchmark on code-grounded BugsInPy tasks.

This experiment removes the agent harness from the critical path. It evaluates
how well each context provider surfaces the ground-truth bug-fix code under a
fixed token budget.

Outputs:
  - per-run JSONL rows with ranks, hits, and context coverage
  - per-provider context dumps for each bug
  - aggregate JSON summary

Usage:
    python3 codegraph-tacm/tools/run_experiment_04.py
    python3 codegraph-tacm/tools/run_experiment_04.py --project thefuck scrapy
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import bench_v2  # noqa: E402
from code_review_graph.graph import GraphStore  # noqa: E402
from code_review_graph.incremental import get_db_path  # noqa: E402
from tacm_v2.graph.builder import GraphBuilder  # noqa: E402
from tacm_v2.graph.model import Layer  # noqa: E402
from tacm_v2.layers.serializers import serialize  # noqa: E402
from tacm_v2.selector.intent import classify_intent  # noqa: E402
from tacm_v2.selector.scoring import NodeScorer  # noqa: E402
from tacm_v2.selector.selector import select, select_dynamic  # noqa: E402
from context_providers import (  # noqa: E402
    _count_tokens,
    _read_source,
    tacm_l4_context,
    tacm_dyn_l4_context,
)


DEFAULT_DATASET = ROOT / "codegraph-tacm" / "datasets" / "bugsinpy_code_grounded_benchmark_ready.jsonl"
DEFAULT_OUT_DIR = ROOT / "codegraph-tacm" / "experiment_04_outputs"
DEFAULT_CONDITIONS = [
    "bm25",
    "minilm",
    "codesearch",
    "hybrid",
    "hybrid-cs",
    "tacm",
    "tacm-full",
    "tacm-dyn",
    "tacm-dyn-l4",
    "tacm-rerank",
]


@dataclass
class ContextRecord:
    node_id: str
    file_path: str
    layer: str
    rank: int
    token_cost: int
    score: float | None = None
    text: str = ""


@dataclass
class TaskResult:
    project: str
    bug_id: str
    condition: str
    query: str
    strict_rank: int | None
    lenient_rank: int | None
    file_rank: int | None
    class_rank: int | None
    hit_at_1: bool
    hit_at_5: bool
    hit_at_10: bool
    mrr: float
    selected_count: int
    function_count: int
    total_tokens: int
    context_has_gt_function: bool
    context_has_gt_file: bool
    context_has_gt_class: bool
    context_log_path: str


def _node_label(node) -> str:
    return getattr(node, "qualified_name", None) or getattr(node, "node_id", None) or node.name


def load_manifest(dataset_path: Path, labels: set[str]) -> dict[str, set[str]]:
    allowed: dict[str, set[str]] = {}
    with open(dataset_path) as f:
        for line in f:
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("label") not in labels:
                continue
            allowed.setdefault(row["project"], set()).add(row["bug_id"])
    return allowed


def _pack_function_nodes(
    ranked_nodes: list,
    budget: int,
    scores: dict[str, float] | None = None,
) -> tuple[list[ContextRecord], str]:
    records: list[ContextRecord] = []
    parts: list[str] = []
    remaining = budget

    for node in ranked_nodes:
        body = _read_source(node.file_path or "", node.line_start or 0, node.line_end or 0)
        if not body:
            continue
        node_label = _node_label(node)
        header = f"# {node_label} [{node.file_path or ''}]\n"
        block = header + body
        cost = _count_tokens(block)
        if cost > remaining:
            continue
        records.append(ContextRecord(
            node_id=node_label,
            file_path=node.file_path or "",
            layer="FUNCTION",
            rank=len(records) + 1,
            token_cost=cost,
            score=(scores or {}).get(node_label),
            text=block,
        ))
        parts.append(block)
        remaining -= cost
        if remaining <= 0:
            break

    return records, "\n\n".join(parts)


def _selection_to_records(selection) -> list[ContextRecord]:
    return [
        ContextRecord(
            node_id=sn.node.node_id,
            file_path=sn.node.file_path or "",
            layer=sn.layer.name,
            rank=i,
            token_cost=sn.token_cost,
            score=sn.score,
            text=sn.text,
        )
        for i, sn in enumerate(selection.nodes, 1)
    ]


def _filter_function_pairs(records: list[ContextRecord]) -> list[tuple[str, str]]:
    return [(r.node_id, r.file_path) for r in records if r.layer == "FUNCTION"]


def _match_records(task, records: list[ContextRecord]) -> tuple[int | None, int | None, int | None, int | None]:
    fn_pairs = _filter_function_pairs(records)
    strict_rank, lenient_rank, _, _ = bench_v2._match_ranked_nodes(
        task.gt_functions, task.gt_files, task.gt_classes, fn_pairs, top_k=max(len(fn_pairs), 1)
    )

    file_rank = None
    class_rank = None
    for r in records:
        if file_rank is None and bench_v2._file_matches_gt(r.file_path, task.gt_files):
            file_rank = r.rank
        if class_rank is None and task.gt_classes and bench_v2._class_matches_gt(r.node_id, task.gt_classes):
            class_rank = r.rank
        if file_rank and (class_rank or not task.gt_classes):
            break
    return strict_rank, lenient_rank, file_rank, class_rank


def _context_has_gt(task, records: list[ContextRecord]) -> tuple[bool, bool, bool]:
    strict_rank, _, file_rank, class_rank = _match_records(task, records)
    return strict_rank is not None, file_rank is not None, class_rank is not None


def _write_context_log(out_dir: Path, project: str, bug_id: str, condition: str, query: str, records: list[ContextRecord], context_text: str) -> Path:
    target = out_dir / "contexts" / project / bug_id / f"{condition}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {bug_id} :: {condition}",
        "",
        f"query: {query}",
        "",
        "## selected nodes",
        "",
    ]
    for r in records:
        lines.append(f"- rank={r.rank} layer={r.layer} tokens={r.token_cost} node={r.node_id} file={r.file_path}")
    lines.extend([
        "",
        "## context",
        "",
        "```text",
        context_text,
        "```",
        "",
    ])
    target.write_text("\n".join(lines))
    return target


def build_condition_output(condition: str, query: str, graph, flat_nodes, minilm_idx, codesearch_idx, budget: int) -> tuple[list[ContextRecord], str]:
    node_map = {_node_label(n): n for n in flat_nodes if not n.is_test}

    if condition == "bm25":
        ranked = bench_v2.bm25_rank_nodes(flat_nodes, query)
        ranked_nodes = [node_map[nid] for nid, _ in ranked if nid in node_map]
        return _pack_function_nodes(ranked_nodes, budget)

    if condition == "minilm":
        ranked = bench_v2._dense_rank_st(query, minilm_idx)
        ranked_nodes = [node_map[nid] for nid, _ in ranked if nid in node_map]
        return _pack_function_nodes(ranked_nodes, budget)

    if condition == "codesearch":
        ranked = bench_v2._dense_rank_st(query, codesearch_idx)
        ranked_nodes = [node_map[nid] for nid, _ in ranked if nid in node_map]
        return _pack_function_nodes(ranked_nodes, budget)

    if condition == "hybrid":
        bm25_ranked = bench_v2.bm25_rank_nodes(flat_nodes, query)
        dense_ranked = bench_v2._dense_rank_st(query, minilm_idx)
        ranked = bench_v2._hybrid_rrf_rank(bm25_ranked, dense_ranked)
        ranked_nodes = [node_map[nid] for nid, _ in ranked if nid in node_map]
        return _pack_function_nodes(ranked_nodes, budget)

    if condition == "hybrid-cs":
        bm25_ranked = bench_v2.bm25_rank_nodes(flat_nodes, query)
        dense_ranked = bench_v2._dense_rank_st(query, codesearch_idx)
        ranked = bench_v2._hybrid_rrf_rank(bm25_ranked, dense_ranked)
        ranked_nodes = [node_map[nid] for nid, _ in ranked if nid in node_map]
        return _pack_function_nodes(ranked_nodes, budget)

    if condition == "tacm":
        sel = select(graph, query, token_budget=budget)
        return _selection_to_records(sel), sel.context_text()

    if condition == "tacm-dyn":
        sel = select_dynamic(graph, query, token_budget=budget)
        return _selection_to_records(sel), sel.context_text()

    if condition == "tacm-dyn-l4":
        sel = select_dynamic(graph, query, token_budget=budget)
        return _selection_to_records(sel), tacm_dyn_l4_context(graph, query, budget)

    if condition == "tacm-full":
        intent = classify_intent(query)
        fn_nodes = [n for n in graph.nodes_at_layer(Layer.FUNCTION) if not n.is_test]
        all_nodes = [n for n in graph.nodes.values() if not n.is_test]
        texts = {n.node_id: serialize(n, graph) for n in all_nodes}
        scorer = NodeScorer(graph, query, intent, texts)
        scores = scorer.score_all(fn_nodes)
        ranked_nodes = sorted(fn_nodes, key=lambda n: -scores[n.node_id])
        score_map = {_node_label(n): scores[n.node_id] for n in ranked_nodes}
        return _pack_function_nodes(ranked_nodes, budget, scores=score_map)

    if condition == "tacm-rerank":
        # Stage 1: TACM scores all functions, take top-40 candidates
        intent = classify_intent(query)
        fn_nodes = [n for n in graph.nodes_at_layer(Layer.FUNCTION) if not n.is_test]
        all_nodes = [n for n in graph.nodes.values() if not n.is_test]
        texts = {n.node_id: serialize(n, graph) for n in all_nodes}
        scorer = NodeScorer(graph, query, intent, texts)
        scores = scorer.score_all(fn_nodes)
        ranked_nodes = sorted(fn_nodes, key=lambda n: -scores[n.node_id])
        top_candidates = ranked_nodes[:40]

        # Stage 2: LLM reranks top-20 by reading signatures + docstrings
        reranked = _llm_rerank(query, top_candidates, rate_limit_delay=2.5)
        return _pack_function_nodes(reranked, budget)

    raise ValueError(f"Unknown condition: {condition}")


def _llm_rerank(
    query: str,
    candidates: list,
    top_n: int = 20,
    rate_limit_delay: float = 2.5,
) -> list:
    """Rerank top TACM candidates using gpt-4o-mini (1 API call).

    Sends the top-N candidate function signatures + first docstring line to
    the model and asks it to return a ranked list of indices. Falls back to
    the original TACM order on any error (parse failure, API error, timeout).

    Rate limit: caller controls delay between calls via rate_limit_delay.
    """
    try:
        from openai import OpenAI
        client = OpenAI(api_key=_load_openai_key())
    except Exception:
        return candidates  # no key or no package — fall back silently

    pool = candidates[:top_n]
    if not pool:
        return candidates

    # Build numbered candidate list: name, file, first line of source
    lines = []
    for i, node in enumerate(pool, 1):
        src = _read_source(node.file_path or "", node.line_start or 0,
                          min((node.line_end or 0), (node.line_start or 0) + 4))
        first_line = src.strip().splitlines()[0][:120] if src.strip() else ""
        lines.append(
            f"{i}. {node.node_id}\n"
            f"   file: {node.file_path or ''}\n"
            f"   code: {first_line}"
        )

    prompt = (
        f"Bug report: {query}\n\n"
        f"Which of these {len(pool)} functions is most likely to contain the bug?\n"
        f"Return ONLY a comma-separated list of numbers, ranked from most to least likely.\n"
        f"Example: 3,1,7,2,...\n\n"
        + "\n".join(lines)
        + "\n\nRanking:"
    )

    try:
        time.sleep(rate_limit_delay)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=80,
            temperature=0.0,
        )
        raw = response.choices[0].message.content.strip()
        # Parse "3,1,7,2,..." → [2, 0, 6, 1, ...] (0-indexed)
        indices = []
        for tok in re.split(r"[,\s]+", raw):
            tok = tok.strip().rstrip(".")
            if tok.isdigit():
                idx = int(tok) - 1
                if 0 <= idx < len(pool) and idx not in indices:
                    indices.append(idx)

        if not indices:
            return candidates

        # Reranked pool first, then any tail candidates not in pool
        reranked = [pool[i] for i in indices]
        seen = set(indices)
        # Append pool members not mentioned by LLM (keep TACM order)
        for i, node in enumerate(pool):
            if i not in seen:
                reranked.append(node)
        # Append candidates beyond top_n (unchanged TACM order)
        reranked.extend(candidates[top_n:])
        return reranked

    except Exception:
        return candidates  # any error → fall back to TACM order


def _load_openai_key() -> str:
    """Load OpenAI key from .env or environment."""
    key = os.environ.get("OPENAI_API_KEY", "")
    if not key:
        env_path = ROOT / ".env"
        if env_path.exists():
            for line in env_path.read_text().splitlines():
                if line.startswith("OPENAI_API_KEY="):
                    key = line.split("=", 1)[1].strip()
                    break
    if not key:
        raise RuntimeError("OPENAI_API_KEY not found")
    return key


def aggregate_metrics(rows: list[TaskResult]) -> dict[str, dict]:
    by_condition: dict[str, list[TaskResult]] = {}
    for row in rows:
        by_condition.setdefault(row.condition, []).append(row)

    summary: dict[str, dict] = {}
    for condition, items in by_condition.items():
        total = len(items)
        summary[condition] = {
            "tasks": total,
            "hit_at_1": sum(1 for r in items if r.hit_at_1) / total if total else 0.0,
            "hit_at_5": sum(1 for r in items if r.hit_at_5) / total if total else 0.0,
            "hit_at_10": sum(1 for r in items if r.hit_at_10) / total if total else 0.0,
            "mrr": sum(r.mrr for r in items) / total if total else 0.0,
            "context_has_gt_function": sum(1 for r in items if r.context_has_gt_function) / total if total else 0.0,
            "context_has_gt_file": sum(1 for r in items if r.context_has_gt_file) / total if total else 0.0,
            "context_has_gt_class": sum(1 for r in items if r.context_has_gt_class) / total if total else 0.0,
            "avg_tokens": sum(r.total_tokens for r in items) / total if total else 0.0,
            "avg_selected_count": sum(r.selected_count for r in items) / total if total else 0.0,
            "avg_function_count": sum(r.function_count for r in items) / total if total else 0.0,
        }
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Experiment 04 retrieval-context benchmark")
    parser.add_argument("--project", nargs="+", dest="projects")
    parser.add_argument("--dataset", type=Path, default=DEFAULT_DATASET)
    parser.add_argument("--labels", nargs="+", default=["code_explicit", "semantic_code"])
    parser.add_argument("--conditions", nargs="+", default=DEFAULT_CONDITIONS)
    parser.add_argument("--budget", type=int, default=4000)
    parser.add_argument("--max-bugs", type=int, default=100)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    args = parser.parse_args()

    labels = set(args.labels)
    allowed = load_manifest(args.dataset, labels)
    projects = args.projects or sorted(allowed)

    out_dir = args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    results_path = out_dir / "experiment_04_results.jsonl"

    rows: list[TaskResult] = []

    for project in projects:
        repo_root = ROOT / project
        if not repo_root.exists():
            print(f"{project}: repo dir missing, skipping")
            continue

        tasks = bench_v2.load_tasks(project, repo_root, max_bugs=args.max_bugs, skip_no_query=True)
        tasks = [t for t in tasks if t.bug_id in allowed.get(project, set())]
        if not tasks:
            print(f"{project}: no filtered tasks")
            continue

        print(f"\n=== Experiment 04: {project} ===")
        print(f"  Tasks: {len(tasks)}  Budget: {args.budget}  Conditions: {args.conditions}")

        store = GraphStore(get_db_path(repo_root))
        try:
            graph = GraphBuilder(store).build()
        finally:
            store.close()

        store2 = GraphStore(get_db_path(repo_root))
        flat_nodes = [n for n in store2.get_nodes_by_kind(["Function"]) if not n.is_test]
        store2.close()

        needs_minilm = any(c in args.conditions for c in ("minilm", "hybrid"))
        needs_codesearch = any(c in args.conditions for c in ("codesearch", "hybrid-cs"))

        minilm_idx = bench_v2._build_minilm_index(flat_nodes, str(repo_root)) if needs_minilm else None
        codesearch_idx = bench_v2._build_codesearch_index(flat_nodes, str(repo_root)) if needs_codesearch else None

        for i, task in enumerate(tasks, 1):
            print(f"  [{i}/{len(tasks)}] {task.bug_id}")
            for condition in args.conditions:
                records, context_text = build_condition_output(
                    condition, task.query, graph, flat_nodes, minilm_idx, codesearch_idx, args.budget
                )
                strict_rank, lenient_rank, file_rank, class_rank = _match_records(task, records)
                has_fn, has_file, has_class = _context_has_gt(task, records)
                log_path = _write_context_log(out_dir, project, task.bug_id, condition, task.query, records, context_text)
                row = TaskResult(
                    project=project,
                    bug_id=task.bug_id,
                    condition=condition,
                    query=task.query,
                    strict_rank=strict_rank,
                    lenient_rank=lenient_rank,
                    file_rank=file_rank,
                    class_rank=class_rank,
                    hit_at_1=bool(strict_rank and strict_rank <= 1),
                    hit_at_5=bool(strict_rank and strict_rank <= 5),
                    hit_at_10=bool(strict_rank and strict_rank <= 10),
                    mrr=(1.0 / strict_rank) if strict_rank else 0.0,
                    selected_count=len(records),
                    function_count=sum(1 for r in records if r.layer == "FUNCTION"),
                    total_tokens=sum(r.token_cost for r in records),
                    context_has_gt_function=has_fn,
                    context_has_gt_file=has_file,
                    context_has_gt_class=has_class,
                    context_log_path=str(log_path),
                )
                rows.append(row)

    with open(results_path, "w") as f:
        for row in rows:
            f.write(json.dumps(asdict(row)) + "\n")

    summary = aggregate_metrics(rows)
    summary_path = out_dir / "experiment_04_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2))

    print("\n=== Experiment 04 Summary ===")
    print(f"{'Condition':<16} {'H@1':>6} {'H@5':>6} {'H@10':>6} {'MRR':>8} {'CtxFn':>8} {'AvgTok':>8}")
    for condition, stats in sorted(summary.items(), key=lambda kv: (-kv[1]["mrr"], kv[0])):
        print(
            f"{condition:<16} "
            f"{stats['hit_at_1']*100:>5.1f}% "
            f"{stats['hit_at_5']*100:>5.1f}% "
            f"{stats['hit_at_10']*100:>5.1f}% "
            f"{stats['mrr']:>8.4f} "
            f"{stats['context_has_gt_function']*100:>7.1f}% "
            f"{stats['avg_tokens']:>8.1f}"
        )
    print(f"\nSaved rows to {results_path}")
    print(f"Saved summary to {summary_path}")


if __name__ == "__main__":
    main()
