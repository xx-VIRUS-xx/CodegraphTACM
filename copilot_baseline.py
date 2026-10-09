"""copilot_baseline.py — Set up and score the Copilot coding agent baseline.

Phase 1 — setup:
  Creates GitHub repos (forks of thefuck/scrapy) and posts one issue per
  BugsInPy task. Copilot coding agent is then manually enabled on each repo
  and assigned to each issue via GitHub UI or gh cli.

Phase 2 — score:
  Polls PRs opened against each issue. For each PR, checks out the branch,
  runs the BugsInPy test file, records pass/fail.

Phase 3 — report:
  Prints solve rate table comparable to agent_harness.py output.

Usage:
    # Phase 1: create repos and issues
    python3 copilot_baseline.py setup --project thefuck --repo ./thefuck
    python3 copilot_baseline.py setup --project scrapy  --repo ./scrapy

    # After assigning Copilot to issues, poll for PRs
    python3 copilot_baseline.py score --project thefuck --repo ./thefuck

    # Print combined report
    python3 copilot_baseline.py report
"""

from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).parent
BUGSINPY_ROOT = ROOT / "BugsInPy"
RESULTS_DIR   = ROOT / "agent_results"
COPILOT_STATE = ROOT / "copilot_state.json"

GH_USER = "xx-VIRUS-xx"

# Maps project → GitHub repo name we'll create under GH_USER
BENCH_REPOS = {
    "thefuck": f"{GH_USER}/tacm-bench-thefuck",
    "scrapy":  f"{GH_USER}/tacm-bench-scrapy",
}

# Maps project → upstream fork source
UPSTREAM = {
    "thefuck": "nvbn/thefuck",
    "scrapy":  "scrapy/scrapy",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def gh(*args, check=True) -> str:
    """Run a gh CLI command and return stdout."""
    result = subprocess.run(
        ["gh"] + list(args),
        capture_output=True, text=True,
    )
    if check and result.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args)} failed:\n{result.stderr}")
    return result.stdout.strip()


def load_state() -> dict:
    if COPILOT_STATE.exists():
        return json.loads(COPILOT_STATE.read_text())
    return {}


def save_state(state: dict) -> None:
    COPILOT_STATE.write_text(json.dumps(state, indent=2))


# ---------------------------------------------------------------------------
# Phase 1: Setup — fork repo + create issues
# ---------------------------------------------------------------------------

def setup(project: str, repo_root: Path, dry_run: bool = False) -> None:
    """Fork the project repo and create one GitHub issue per BugsInPy task."""
    from bench_v2 import load_tasks
    from test_runner import get_test_file

    bench_repo = BENCH_REPOS[project]
    repo_name  = bench_repo.split("/")[1]

    print(f"\n=== Setup: {project} → {bench_repo} ===")

    # --- Create fork / repo ---
    # Check if it already exists
    existing = gh("repo", "view", bench_repo, "--json", "name", check=False)
    if '"name"' in existing:
        print(f"  Repo {bench_repo} already exists — skipping fork")
    else:
        print(f"  Forking {UPSTREAM[project]} → {bench_repo} ...")
        if not dry_run:
            gh("repo", "fork", UPSTREAM[project],
               "--clone=false", "--fork-name", repo_name)
            # Wait for fork to propagate
            time.sleep(5)
            print(f"  Forked ok")
        else:
            print("  [DRY RUN] would fork")

    # --- Load tasks ---
    tasks = load_tasks(project, repo_root, max_bugs=50, skip_no_query=True)
    print(f"  Tasks to create issues for: {len(tasks)}")

    state = load_state()
    project_state = state.setdefault(project, {})

    for task in tasks:
        if task.bug_id in project_state:
            print(f"  {task.bug_id}: already has issue #{project_state[task.bug_id]['issue_number']}")
            continue

        bug_dir = BUGSINPY_ROOT / "projects" / project / "bugs" / task.bug_id.split("-")[1]
        test_file = get_test_file(bug_dir)
        patch_text = task.patch_path.read_text(errors="replace")[:3000]

        # Read the bug description from bug.info
        bug_info = (bug_dir / "bug.info").read_text()

        issue_title = f"[TACM-BENCH] {task.bug_id}: {task.query[:80]}"
        issue_body = _issue_body(task, test_file, patch_text, bug_info)

        print(f"  Creating issue: {issue_title[:70]} ...", end=" ", flush=True)
        if not dry_run:
            out = gh(
                "issue", "create",
                "--repo", bench_repo,
                "--title", issue_title,
                "--body", issue_body,
                "--label", "bug",
            )
            # gh returns the issue URL, extract number
            issue_url = out.strip()
            issue_number = int(issue_url.rstrip("/").split("/")[-1])
            project_state[task.bug_id] = {
                "issue_number": issue_number,
                "issue_url": issue_url,
                "gt_functions": task.gt_functions,
                "gt_files": task.gt_files,
                "test_file": test_file,
                "query": task.query,
                "pr_number": None,
                "pr_url": None,
                "solved": None,
            }
            save_state(state)
            print(f"#{issue_number}")
            time.sleep(1)   # rate limit headroom
        else:
            print("[DRY RUN]")

    print(f"\n  Issues created. Next steps:")
    print(f"  1. Go to https://github.com/{bench_repo}/settings/copilot")
    print(f"     Enable 'Copilot coding agent' on the repo")
    print(f"  2. Run: python3 copilot_baseline.py assign --project {project}")
    print(f"     (assigns @copilot to all open issues)")
    print(f"  3. Wait for Copilot to open PRs (usually 5-30 min per issue)")
    print(f"  4. Run: python3 copilot_baseline.py score --project {project} --repo ./{project}")


def _issue_body(task, test_file: str, patch_preview: str, bug_info: str) -> str:
    """Format the GitHub issue body for a BugsInPy bug task."""
    gt_fns = ", ".join(f"`{f}`" for f in task.gt_functions[:3])
    gt_files = ", ".join(f"`{f}`" for f in task.gt_files[:3])

    return f"""## Bug description

{task.query}

## Context

This is a BugsInPy benchmark task (`{task.bug_id}`). The fix involves changes to:
- **Functions**: {gt_fns}
- **Files**: {gt_files}

## Failing test

```
{test_file}
```

Run the test with:
```bash
python -m pytest {test_file} -x -q
```

The test should **fail** on the current code and **pass** after the correct fix is applied.

## What to do

1. Identify the bug in the relevant functions/files listed above
2. Apply a minimal fix that makes the failing test pass
3. Open a PR with the fix

## Patch preview (for reference)

<details>
<summary>Patch from fixed commit (do not copy directly — find the bug independently)</summary>

```diff
{patch_preview}
```
</details>

---
*TACM-v2 Experiment 03 — Copilot agent baseline. Bug ID: `{task.bug_id}`*
"""


# ---------------------------------------------------------------------------
# Phase 1b: Assign — bulk-assign @copilot to all open issues
# ---------------------------------------------------------------------------

def assign(project: str) -> None:
    """Assign @copilot to every open issue for this project.

    Run AFTER enabling Copilot coding agent in repo Settings.
    """
    bench_repo = BENCH_REPOS[project]
    state = load_state()
    project_state = state.get(project, {})

    if not project_state:
        print(f"No state for {project}. Run setup first.")
        return

    print(f"\n=== Assigning @copilot to issues: {bench_repo} ===")

    for bug_id, info in project_state.items():
        issue_num = info.get("issue_number")
        if not issue_num:
            continue
        print(f"  {bug_id}: assigning issue #{issue_num} ...", end=" ", flush=True)
        try:
            out = gh(
                "api",
                f"repos/{bench_repo}/issues/{issue_num}/assignees",
                "--method", "POST",
                "--field", "assignees[]=copilot",
            )
            print("ok")
        except RuntimeError as e:
            err = str(e)
            if "not a collaborator" in err.lower() or "copilot" in err.lower():
                print(f"FAILED — Copilot not enabled yet on {bench_repo}")
                print(f"  Enable it at: https://github.com/{bench_repo}/settings/copilot")
                return
            print(f"error: {err[:120]}")
        time.sleep(0.5)

    print(f"\n  Done. Copilot will now begin working on each issue.")
    print(f"  Monitor PRs at: https://github.com/{bench_repo}/pulls")


# ---------------------------------------------------------------------------
# Phase 2 helpers
# ---------------------------------------------------------------------------

def _build_issue_pr_map(owner: str, repo_name: str) -> dict[int, dict]:
    """Build a map from issue_number → best PR via GraphQL.

    Strategy (in priority order):
    1. closingIssuesReferences — Copilot used 'Closes #N' in body
    2. PR body contains '#N' — Copilot mentioned the issue
    3. PR branch name contains the issue number as part of a dash-separated token
    """
    import re as _re

    # Fetch all PRs with closing refs + body
    result = gh(
        "api", "graphql",
        "-f", f"""query={{
          repository(owner: "{owner}", name: "{repo_name}") {{
            pullRequests(first: 100, states: [OPEN, MERGED, CLOSED]) {{
              nodes {{
                number
                url
                headRefName
                state
                body
                closingIssuesReferences(first: 5) {{
                  nodes {{ number }}
                }}
              }}
            }}
          }}
        }}""",
        check=False,
    )
    try:
        data = json.loads(result)
        prs = data["data"]["repository"]["pullRequests"]["nodes"]
    except Exception:
        return {}

    issue_to_pr: dict[int, dict] = {}

    # Pass 1: closing refs (highest confidence)
    for pr in prs:
        for ref in pr["closingIssuesReferences"]["nodes"]:
            inum = ref["number"]
            if inum not in issue_to_pr:
                issue_to_pr[inum] = pr

    # Pass 2: body mentions '#N'
    for pr in prs:
        body = pr.get("body") or ""
        for m in _re.finditer(r"#(\d+)", body):
            inum = int(m.group(1))
            if inum not in issue_to_pr:
                issue_to_pr[inum] = pr

    # Pass 3: branch name contains issue number as a dash token
    # e.g. 'copilot/thefuck-25-fix-hdfs' → issue numbers after 'thefuck-' prefix
    for pr in prs:
        branch = pr.get("headRefName", "")
        parts = branch.replace("/", "-").split("-")
        for i, part in enumerate(parts):
            if part.isdigit():
                inum = int(part)
                if inum not in issue_to_pr:
                    issue_to_pr[inum] = pr

    return issue_to_pr


# ---------------------------------------------------------------------------
# Phase 2: Score — check PRs, run tests
# ---------------------------------------------------------------------------

def score(project: str, repo_root: Path) -> None:
    """Poll PRs for each issue, run tests, record pass/fail."""
    from test_runner import run_tests
    from patch_utils import restore_repo

    bench_repo = BENCH_REPOS[project]
    state = load_state()
    project_state = state.get(project, {})

    if not project_state:
        print(f"No state for {project}. Run setup first.")
        return

    print(f"\n=== Scoring: {project} @ {bench_repo} ===")

    # Build issue→PR map via GraphQL (closing refs + body mentions)
    owner, repo_name = bench_repo.split("/")
    issue_to_pr = _build_issue_pr_map(owner, repo_name)
    print(f"  PR map built: {len(issue_to_pr)} issues have a matched PR")

    for bug_id, info in project_state.items():
        if info.get("solved") is not None:
            status = "PASS" if info["solved"] else "fail"
            print(f"  {bug_id}: already scored → {status}")
            continue

        issue_num = info["issue_number"]
        matched_pr = issue_to_pr.get(issue_num)

        if not matched_pr:
            # Fall back to pr_number already recorded in state (e.g. manually set)
            if info.get("pr_number"):
                pr_num = info["pr_number"]
                pr_url = info.get("pr_url", f"https://github.com/{bench_repo}/pull/{pr_num}")
            else:
                print(f"  {bug_id}: no PR yet (issue #{issue_num})")
                continue
        else:
            pr_num = matched_pr["number"]
            pr_url = matched_pr["url"]
        print(f"  {bug_id}: PR #{pr_num} found — checking out and testing ...",
              end=" ", flush=True)

        info["pr_number"] = pr_num
        info["pr_url"] = pr_url

        # Checkout the PR branch into the local repo.
        # Use `git -C repo_root fetch` + `git checkout` directly to avoid gh
        # picking up the outer repo's .git when repo_root is a subdirectory.
        try:
            # Fetch the PR ref directly into the inner repo
            subprocess.run(
                ["git", "fetch", f"https://github.com/{bench_repo}.git",
                 f"refs/pull/{pr_num}/head:pr/{pr_num}"],
                cwd=repo_root, capture_output=True, check=True, timeout=120,
            )
            subprocess.run(
                ["git", "checkout", f"pr/{pr_num}"],
                cwd=repo_root, capture_output=True, check=True, timeout=30,
            )
            test_result = run_tests(repo_root, info["test_file"], timeout=90)
            info["solved"] = test_result.passed
            info["test_output"] = test_result.stdout[-1000:]
            status = "PASS" if test_result.passed else "fail"
            print(status)
        except Exception as e:
            info["solved"] = False
            info["test_output"] = str(e)
            print(f"error: {e}")
        finally:
            restore_repo(repo_root)
            # Return to default branch and delete the temp pr branch
            subprocess.run(["git", "checkout", "master"], cwd=repo_root,
                           capture_output=True)
            subprocess.run(["git", "branch", "-D", f"pr/{pr_num}"],
                           cwd=repo_root, capture_output=True)

        save_state(state)
        time.sleep(2)

    # Summary
    solved = sum(1 for v in project_state.values() if v.get("solved") is True)
    total  = sum(1 for v in project_state.values() if v.get("solved") is not None)
    print(f"\n  {project}: {solved}/{total} solved ({100*solved/total:.0f}%)" if total else "  No PRs scored yet.")


# ---------------------------------------------------------------------------
# Phase 3: Report
# ---------------------------------------------------------------------------

def report() -> None:
    """Print Copilot solve rates alongside agent_harness results."""
    state = load_state()
    if not state:
        print("No copilot_state.json found. Run setup + score first.")
        return

    print("\n" + "="*60)
    print("COPILOT AGENT BASELINE RESULTS")
    print("="*60)

    for project, project_state in state.items():
        scored  = {k: v for k, v in project_state.items() if v.get("solved") is not None}
        pending = {k: v for k, v in project_state.items() if v.get("solved") is None}
        solved  = sum(1 for v in scored.values() if v["solved"])

        print(f"\n  {project}:")
        print(f"    Total issues: {len(project_state)}")
        print(f"    PRs scored:   {len(scored)}")
        print(f"    Pending PRs:  {len(pending)}")
        if scored:
            pct = 100 * solved / len(scored)
            print(f"    Solve rate:   {solved}/{len(scored)} = {pct:.0f}%")

        print(f"\n    Per-bug breakdown:")
        for bug_id, info in sorted(project_state.items()):
            solved_s = "PASS" if info.get("solved") else ("fail" if info.get("solved") is False else "pending")
            pr = f"PR #{info['pr_number']}" if info.get("pr_number") else "no PR"
            print(f"      {bug_id:<20} {solved_s:<8} {pr}")

    # Also load agent_harness results for comparison
    results_dir = ROOT / "agent_results"
    if results_dir.exists():
        import glob
        all_files = sorted(glob.glob(str(results_dir / "*.jsonl")))
        if all_files:
            from collections import defaultdict
            tacm_results: dict[str, list] = defaultdict(list)
            for f in all_files:
                with open(f) as fh:
                    for line in fh:
                        d = json.loads(line)
                        if d["condition"] == "tacm":
                            tacm_results[d["bug_id"]].append(d["success"])

            if tacm_results:
                print(f"\n  TACM-v2 agent results (from agent_harness):")
                tacm_solved = sum(1 for runs in tacm_results.values() if any(runs))
                print(f"    Solve rate: {tacm_solved}/{len(tacm_results)} = "
                      f"{100*tacm_solved/len(tacm_results):.0f}%")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Copilot coding agent baseline")
    sub = parser.add_subparsers(dest="cmd")

    setup_p = sub.add_parser("setup", help="Create repos and issues")
    setup_p.add_argument("--project", required=True)
    setup_p.add_argument("--repo", type=Path, required=True)
    setup_p.add_argument("--dry-run", action="store_true")

    assign_p = sub.add_parser("assign", help="Bulk-assign @copilot to all open issues")
    assign_p.add_argument("--project", required=True)

    score_p = sub.add_parser("score", help="Score Copilot PRs by running tests")
    score_p.add_argument("--project", required=True)
    score_p.add_argument("--repo", type=Path, required=True)

    sub.add_parser("report", help="Print comparison report")

    args = parser.parse_args()

    if args.cmd == "setup":
        setup(args.project, args.repo.resolve(), dry_run=args.dry_run)
    elif args.cmd == "assign":
        assign(args.project)
    elif args.cmd == "score":
        score(args.project, args.repo.resolve())
    elif args.cmd == "report":
        report()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
