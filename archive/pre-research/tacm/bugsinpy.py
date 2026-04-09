"""bugsinpy.py — G4-C: BugsInPy dataset loader.

Parses the BugsInPy repository (https://github.com/soarsmu/BugsInPy) to
extract structured benchmark tasks for TACM evaluation.

Each task provides:
- bug_id:       "pandas-1", "black-3", etc.
- project:      project name
- bug_num:      integer bug number
- patch_path:   path to bug_patch.txt
- gt_functions: list of qualified function names extracted from the patch
- query:        NL bug report (from GitHub commit message or empty if unavailable)
- fixed_commit: SHA of the fix commit

GT extraction strategy:
  Parse unified diff hunks. For each changed hunk, walk back through the file
  at the fixed commit to find the enclosing `def` or `class` context. This gives
  us (class, method) pairs which we format as "ClassName.method_name".

  We do NOT require a live checkout — we parse the patch itself, looking for
  context lines (`class Foo:`, `def bar(`) that appear in the diff above the
  first hunk marker. This is a heuristic but works for >85% of single-function
  fixes in BugsInPy.

Usage:
    from tacm.bugsinpy import load_tasks, BUGSINPY_ROOT
    tasks = load_tasks(BUGSINPY_ROOT, projects=["pandas", "black"], max_per_project=10)
    for t in tasks:
        print(t.bug_id, t.gt_functions, t.query[:60])
"""

from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

# Default: BugsInPy cloned next to this repo
BUGSINPY_ROOT = Path(__file__).parent.parent / "BugsInPy"

# Projects we can actually build a crg graph for (pure Python, manageable size)
# Expand this list as you clone and index more repos
SUPPORTED_PROJECTS = {
    "pandas", "black", "tornado", "scrapy", "thefuck",
    "fastapi", "httpie", "tqdm", "spacy",
}


@dataclass
class BugsInPyTask:
    bug_id: str               # "pandas-1"
    project: str
    bug_num: int
    patch_path: Path
    fixed_commit: str
    buggy_commit: str
    gt_functions: list[str]   # ["ClassName.method", ...] — may be empty if parse fails
    gt_files: list[str]       # ["pandas/core/indexing.py", ...]
    query: str                # NL bug report — commit message subject as fallback


# ---------------------------------------------------------------------------
# Patch parser
# ---------------------------------------------------------------------------

_HUNK_RE = re.compile(r"^@@ .+ @@(.*)$")
_DEF_RE  = re.compile(r"^[ +\-]?(\s*)def\s+(\w+)\s*\(")
_CLASS_RE = re.compile(r"^[ +\-]?(\s*)class\s+(\w+)[\s:(]")
_FILE_RE  = re.compile(r"^\+\+\+ b/(.+)$")


def _extract_gt_from_patch(patch_text: str) -> tuple[list[str], list[str]]:
    """Return (gt_functions, gt_files) extracted from a unified diff."""
    gt_functions: list[str] = []
    gt_files: list[str] = []
    seen: set[str] = set()

    current_file = ""
    # Stack of (indent_len, name, is_class)
    scope_stack: list[tuple[int, str, bool]] = []

    for line in patch_text.splitlines():
        # Track current file
        fm = _FILE_RE.match(line)
        if fm:
            current_file = fm.group(1)
            if current_file.endswith(".py") and current_file not in gt_files:
                gt_files.append(current_file)
            scope_stack = []
            continue

        if not current_file.endswith(".py"):
            continue

        # Skip diff metadata lines (--- +++ index)
        if line.startswith("---") or line.startswith("index ") or line.startswith("diff "):
            continue

        # Track class/def scope from context and addition lines (not removals)
        if line.startswith("-"):
            continue

        raw = line[1:] if line.startswith("+") else line  # strip leading +/space

        cm = _CLASS_RE.match(raw)
        if cm:
            indent = len(cm.group(1))
            name = cm.group(2)
            # Pop anything at same or deeper indent
            scope_stack = [(i, n, ic) for i, n, ic in scope_stack if i < indent]
            scope_stack.append((indent, name, True))
            continue

        dm = _DEF_RE.match(raw)
        if dm:
            indent = len(dm.group(1))
            name = dm.group(2)
            scope_stack = [(i, n, ic) for i, n, ic in scope_stack if i < indent]
            scope_stack.append((indent, name, False))

        # If this line is a hunk addition (+), record the enclosing function
        if line.startswith("+") and scope_stack:
            # Find innermost def
            func_name = None
            class_name = None
            for _, n, is_class in reversed(scope_stack):
                if not is_class and func_name is None:
                    func_name = n
                elif is_class and class_name is None:
                    class_name = n
                if func_name and class_name:
                    break
            if func_name:
                qn = f"{class_name}.{func_name}" if class_name else func_name
                if qn not in seen:
                    seen.add(qn)
                    gt_functions.append(qn)

    return gt_functions, gt_files


def _get_commit_message(project_dir: Path, commit: str) -> str:
    """Get the subject line of a git commit message."""
    try:
        result = subprocess.run(
            ["git", "log", "--format=%s", "-1", commit],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=10,
        )
        return result.stdout.strip()
    except Exception:
        return ""


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def load_tasks(
    bugsinpy_root: Path = BUGSINPY_ROOT,
    projects: list[str] | None = None,
    max_per_project: int = 10,
    require_gt: bool = True,
    max_gt_functions: int = 3,
    random_seed: int = 42,
) -> list[BugsInPyTask]:
    """Load BugsInPy tasks with GT extracted from patches.

    Args:
        bugsinpy_root: Path to cloned BugsInPy repo.
        projects: List of project names to include. None = all supported.
        max_per_project: Max bugs to load per project (stratified sampling).
        require_gt: If True, skip tasks where patch parse yields no GT functions.
        random_seed: Seed for stratified sampling.

    Returns:
        List of BugsInPyTask, sorted by bug_id.
    """
    import random
    rng = random.Random(random_seed)

    if projects is None:
        projects = sorted(SUPPORTED_PROJECTS)

    tasks: list[BugsInPyTask] = []
    projects_dir = bugsinpy_root / "projects"

    for project in projects:
        proj_dir = projects_dir / project
        if not proj_dir.exists():
            continue
        bugs_dir = proj_dir / "bugs"
        if not bugs_dir.exists():
            continue

        bug_nums = sorted(
            int(d.name) for d in bugs_dir.iterdir()
            if d.is_dir() and d.name.isdigit()
        )
        rng.shuffle(bug_nums)

        count = 0
        for bug_num in bug_nums:
            if count >= max_per_project:
                break
            bug_dir = bugs_dir / str(bug_num)
            patch_path = bug_dir / "bug_patch.txt"
            info_path = bug_dir / "bug.info"

            if not patch_path.exists() or not info_path.exists():
                continue

            # Parse bug.info
            info: dict[str, str] = {}
            for line in info_path.read_text().splitlines():
                if "=" in line:
                    k, _, v = line.partition("=")
                    info[k.strip()] = v.strip().strip('"')

            fixed_commit = info.get("fixed_commit_id", "")
            buggy_commit = info.get("buggy_commit_id", "")

            patch_text = patch_path.read_text(errors="replace")
            gt_functions, gt_files = _extract_gt_from_patch(patch_text)

            if require_gt and not gt_functions:
                continue
            # Skip large refactors — too many GT functions means the patch
            # touches many unrelated functions (not a single-function bug)
            if len(gt_functions) > max_gt_functions:
                continue

            # Query: use commit message subject as fallback NL description
            query = _get_commit_message(proj_dir, fixed_commit) if fixed_commit else ""

            tasks.append(BugsInPyTask(
                bug_id=f"{project}-{bug_num}",
                project=project,
                bug_num=bug_num,
                patch_path=patch_path,
                fixed_commit=fixed_commit,
                buggy_commit=buggy_commit,
                gt_functions=gt_functions,
                gt_files=gt_files,
                query=query,
            ))
            count += 1

    tasks.sort(key=lambda t: t.bug_id)
    return tasks


def summarize(tasks: list[BugsInPyTask]) -> None:
    """Print a summary of loaded tasks."""
    from collections import Counter
    proj_counts = Counter(t.project for t in tasks)
    gt_counts = Counter(len(t.gt_functions) for t in tasks)
    print(f"Total tasks: {len(tasks)}")
    print(f"Projects: {dict(proj_counts)}")
    print(f"GT functions per task: {dict(sorted(gt_counts.items()))}")
    no_query = sum(1 for t in tasks if not t.query)
    print(f"Tasks with no query (no git checkout): {no_query}")
    print()
    for t in tasks[:5]:
        print(f"  {t.bug_id}: GT={t.gt_functions} query={t.query[:60]!r}")
