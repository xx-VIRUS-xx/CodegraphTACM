"""Report agent benchmark results joined with the code-grounded dataset.

This script reads:
  - raw agent results from `agent_results/*.jsonl`
  - dataset labels from a JSONL manifest

It reports:
  - solve rate by project and condition
  - solve rate by dataset label and condition
  - overall any-pass rates on the filtered benchmark slice

Usage:
    python3 tools/report_dataset_results.py
    python3 tools/report_dataset_results.py --project thefuck
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from agent_harness import load_all_results  # noqa: E402


DEFAULT_DATASET = ROOT / "datasets" / "bugsinpy_code_grounded_benchmark_ready.jsonl"
DEFAULT_LABELS = {"code_explicit", "semantic_code"}


def load_manifest(dataset_path: Path, labels: set[str]) -> tuple[dict[str, dict], dict[str, set[str]]]:
    by_bug: dict[str, dict] = {}
    by_project: dict[str, set[str]] = defaultdict(set)
    with open(dataset_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if row.get("label") not in labels:
                continue
            bug_id = row["bug_id"]
            by_bug[bug_id] = row
            by_project[row["project"]].add(bug_id)
    return by_bug, by_project


def any_pass_rate(results, allowed_bug_ids: set[str]) -> dict[str, tuple[int, int, int, float, float]]:
    by_condition: dict[str, dict[str, bool]] = defaultdict(dict)
    for r in results:
        if r.bug_id not in allowed_bug_ids:
            continue
        by_condition[r.condition][r.bug_id] = by_condition[r.condition].get(r.bug_id, False) or r.success

    out = {}
    total = len(allowed_bug_ids)
    for condition, per_bug in by_condition.items():
        covered = len(per_bug)
        solved = sum(1 for bug_id in allowed_bug_ids if per_bug.get(bug_id, False))
        out[condition] = (
            solved,
            covered,
            total,
            (solved / total if total else 0.0),
            (covered / total if total else 0.0),
        )
    return out


def print_table(title: str, rows: list[tuple[str, int, int, int, float, float]]) -> None:
    print(f"\n{title}")
    print("-" * len(title))
    print(f"{'Condition':<16} {'Solved':>6} {'Seen':>6} {'Total':>6} {'Solve%':>8} {'Cover%':>8}")
    for condition, solved, covered, total, rate, coverage in sorted(rows, key=lambda x: (-x[4], x[0])):
        print(f"{condition:<16} {solved:>6} {covered:>6} {total:>6} {rate*100:>7.1f}% {coverage*100:>7.1f}%")


def main() -> None:
    parser = argparse.ArgumentParser(description="Report agent results on code-grounded dataset")
    parser.add_argument("--dataset", type=Path, default=DEFAULT_DATASET)
    parser.add_argument("--labels", nargs="+", default=sorted(DEFAULT_LABELS))
    parser.add_argument("--project", help="Optional single project to report")
    args = parser.parse_args()

    labels = set(args.labels)
    by_bug, by_project = load_manifest(args.dataset, labels)

    projects = [args.project] if args.project else sorted(by_project)
    for project in projects:
        allowed = by_project.get(project, set())
        if not allowed:
            print(f"\n{project}: no bugs matched dataset filter")
            continue

        results = load_all_results(project)
        project_rates = any_pass_rate(results, allowed)
        rows = [
            (cond, solved, covered, total, rate, coverage)
            for cond, (solved, covered, total, rate, coverage) in project_rates.items()
        ]
        print_table(f"Project: {project}  (labels={sorted(labels)}, bugs={len(allowed)})", rows)

        # Label-specific breakdown inside the project
        label_groups: dict[str, set[str]] = defaultdict(set)
        for bug_id in allowed:
            label_groups[by_bug[bug_id]["label"]].add(bug_id)
        for label, bug_ids in sorted(label_groups.items()):
            rates = any_pass_rate(results, bug_ids)
            rows = [
                (cond, solved, covered, total, rate, coverage)
                for cond, (solved, covered, total, rate, coverage) in rates.items()
            ]
            print_table(f"  Label: {label}  (bugs={len(bug_ids)})", rows)

    # Global aggregate over selected projects
    global_allowed = set().union(*(by_project.get(p, set()) for p in projects))
    global_results = []
    for project in projects:
        global_results.extend(load_all_results(project))
    global_rates = any_pass_rate(global_results, global_allowed)
    rows = [
        (cond, solved, covered, total, rate, coverage)
        for cond, (solved, covered, total, rate, coverage) in global_rates.items()
    ]
    print_table(f"Global aggregate  (projects={projects}, bugs={len(global_allowed)})", rows)


if __name__ == "__main__":
    main()
