"""Build a code-grounded BugsInPy subset for TACM benchmarking.

This script labels each task as one of:

  - code_explicit: issue text directly names code-facing concepts
  - semantic_code: issue text is still about code behavior, but less lexical
  - non_code: query is mostly workflow / PR metadata / vague text

The goal is not to mutate TACM around noisy issue text, but to produce a local
benchmark slice aligned with what TACM is actually built to do: code retrieval.

Usage:
    python3 tools/build_code_grounded_dataset.py
    python3 tools/build_code_grounded_dataset.py --projects thefuck scrapy
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import bench_v2  # noqa: E402


OUT_DIR = ROOT / "datasets"

STOPWORDS = {
    "the", "a", "an", "and", "or", "to", "of", "in", "on", "for", "by",
    "with", "from", "into", "out", "up", "down", "is", "are", "was", "were",
    "be", "been", "being", "do", "does", "did", "done", "fix", "fixed",
    "bug", "issue", "handle", "support", "using", "use", "also", "some",
    "more", "less", "minor", "properly", "wrong", "fail", "fails", "failing",
    "not", "no", "all", "when", "where", "how", "why", "this", "that",
    "these", "those", "merge", "pull", "request", "tests", "test",
}

NON_CODE_PATTERNS = [
    re.compile(r"^merge pull request\b", re.I),
    re.compile(r"^tests?[!:. ]", re.I),
    re.compile(r"\bminor issues\b", re.I),
    re.compile(r"\bre-enable tests\b", re.I),
]

CODE_FORMAT_PATTERNS = [
    re.compile(r"`[^`]+`"),
    re.compile(r"\b[a-zA-Z_][a-zA-Z0-9_]*\(\)"),
    re.compile(r"\b[a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*"),
    re.compile(r"\b__\w+__\b"),
]


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def split_identifier(text: str) -> list[str]:
    parts = re.split(r"[_./:()-]+", text)
    out: list[str] = []
    for part in parts:
        if not part:
            continue
        camel = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", part).split()
        out.extend(t.lower() for t in camel if t)
    return [t for t in out if t]


def source_vocab(repo_root: Path, rel_files: list[str], limit: int = 80) -> set[str]:
    vocab: Counter[str] = Counter()
    for rel in rel_files[:2]:
        path = repo_root / rel
        if not path.exists():
            continue
        try:
            text = path.read_text(errors="replace")
        except OSError:
            continue
        for tok in tokenize(text):
            if len(tok) >= 4 and tok not in STOPWORDS:
                vocab[tok] += 1
    return {tok for tok, _ in vocab.most_common(limit)}


def classify_task(task, repo_root: Path | None) -> dict:
    query = (task.query or "").strip()
    if not query:
        return {
            "bug_id": task.bug_id,
            "project": task.project,
            "query": "",
            "label": "query_unavailable",
            "explicit_score": 0,
            "semantic_score": 0,
            "penalty": 0,
            "reasons": ["query_unavailable"],
            "gt_functions": task.gt_functions,
            "gt_files": task.gt_files,
            "repo_available": bool(repo_root and repo_root.exists() and (repo_root / ".git").exists()),
        }

    q_tokens = set(tokenize(query))

    fn_tokens = set()
    cls_tokens = set()
    file_tokens = set()

    for gt in task.gt_functions:
        fn_tokens.update(t for t in split_identifier(gt.split(".")[-1]) if len(t) >= 3)
        if "." in gt:
            cls_tokens.update(t for t in split_identifier(gt.split(".")[0]) if len(t) >= 3)

    for rel in task.gt_files:
        path = Path(rel)
        file_tokens.update(t for t in split_identifier(path.stem) if len(t) >= 3)
        file_tokens.update(t for t in split_identifier("/".join(path.parts[-3:])) if len(t) >= 3)

    vocab_tokens = source_vocab(repo_root, task.gt_files) if repo_root and repo_root.exists() else set()

    fn_overlap = sorted(q_tokens & fn_tokens)
    cls_overlap = sorted(q_tokens & cls_tokens)
    file_overlap = sorted(q_tokens & file_tokens)
    vocab_overlap = sorted(t for t in (q_tokens & vocab_tokens) if t not in STOPWORDS)

    explicit_score = 0
    semantic_score = 0
    penalty = 0
    reasons: list[str] = []

    if fn_overlap:
        explicit_score += 3
        reasons.append(f"fn_overlap={fn_overlap[:4]}")
    if cls_overlap:
        explicit_score += 2
        reasons.append(f"class_overlap={cls_overlap[:4]}")
    if file_overlap:
        explicit_score += 2
        reasons.append(f"file_overlap={file_overlap[:4]}")
    if vocab_overlap:
        semantic_score += 1 if len(vocab_overlap) <= 2 else 2
        reasons.append(f"source_vocab_overlap={vocab_overlap[:5]}")

    if any(p.search(query) for p in CODE_FORMAT_PATTERNS):
        explicit_score += 1
        reasons.append("code_formatted_query")

    for pat in NON_CODE_PATTERNS:
        if pat.search(query):
            penalty += 2
            reasons.append(f"non_code_pattern={pat.pattern}")

    # Technical-ish terms still count as semantic code, even when they do not
    # directly name the GT function/file.
    technical = {
        "regex", "alias", "branch", "url", "request", "response", "redirect",
        "shell", "middleware", "contract", "cache", "formrequest", "classcell",
        "canonicalize", "parse", "headers", "proxy", "cookies",
    }
    tech_overlap = sorted(q_tokens & technical)
    if tech_overlap:
        semantic_score += 1
        reasons.append(f"technical_terms={tech_overlap[:4]}")

    total = explicit_score + semantic_score - penalty

    if explicit_score >= 2 and penalty == 0:
        label = "code_explicit"
    elif total >= 1 and penalty <= 1:
        label = "semantic_code"
    else:
        label = "non_code"

    return {
        "bug_id": task.bug_id,
        "project": task.project,
        "query": task.query,
        "label": label,
        "explicit_score": explicit_score,
        "semantic_score": semantic_score,
        "penalty": penalty,
        "reasons": reasons,
        "gt_functions": task.gt_functions,
        "gt_files": task.gt_files,
        "repo_available": bool(repo_root and repo_root.exists() and (repo_root / ".git").exists()),
    }


def build_dataset(projects: list[str]) -> list[dict]:
    rows: list[dict] = []
    for project in projects:
        repo_root = ROOT / project
        tasks = bench_v2.load_tasks(project, repo_root, max_bugs=100, skip_no_query=False)
        for task in tasks:
            rows.append(classify_task(task, repo_root if repo_root.exists() else None))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Build code-grounded BugsInPy subset")
    parser.add_argument("--projects", nargs="+")
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if args.projects:
        projects = args.projects
    else:
        projects = sorted([p.name for p in (ROOT / "BugsInPy" / "projects").iterdir() if p.is_dir()])

    rows = build_dataset(projects)

    jsonl_path = OUT_DIR / "bugsinpy_code_grounded_tasks.jsonl"
    csv_path = OUT_DIR / "bugsinpy_code_grounded_tasks.csv"
    benchmark_jsonl = OUT_DIR / "bugsinpy_code_grounded_benchmark_ready.jsonl"
    benchmark_csv = OUT_DIR / "bugsinpy_code_grounded_benchmark_ready.csv"

    with open(jsonl_path, "w") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=True) + "\n")

    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "bug_id", "project", "label", "query",
                "explicit_score", "semantic_score", "penalty",
                "gt_functions", "gt_files", "reasons", "repo_available",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow({
                **row,
                "gt_functions": "; ".join(row["gt_functions"]),
                "gt_files": "; ".join(row["gt_files"]),
                "reasons": "; ".join(row["reasons"]),
            })

    benchmark_rows = [
        row for row in rows
        if row["label"] in {"code_explicit", "semantic_code"} and row["query"]
    ]

    with open(benchmark_jsonl, "w") as f:
        for row in benchmark_rows:
            f.write(json.dumps(row, ensure_ascii=True) + "\n")

    with open(benchmark_csv, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "bug_id", "project", "label", "query",
                "explicit_score", "semantic_score", "penalty",
                "gt_functions", "gt_files", "reasons", "repo_available",
            ],
        )
        writer.writeheader()
        for row in benchmark_rows:
            writer.writerow({
                **row,
                "gt_functions": "; ".join(row["gt_functions"]),
                "gt_files": "; ".join(row["gt_files"]),
                "reasons": "; ".join(row["reasons"]),
            })

    counts = Counter(row["label"] for row in rows)
    print(f"Wrote {jsonl_path}")
    print(f"Wrote {csv_path}")
    print(f"Wrote {benchmark_jsonl}")
    print(f"Wrote {benchmark_csv}")
    print("Counts:", dict(counts))
    print("Benchmark-ready:", len(benchmark_rows))
    print("\nSample rows:")
    for row in rows[:10]:
        print(f"{row['bug_id']}: {row['label']} | {row['query']} | {', '.join(row['reasons'][:3])}")


if __name__ == "__main__":
    main()
