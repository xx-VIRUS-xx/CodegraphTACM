# Q05 — Git Signal Extraction Without Shell Dependencies
**Status:** ❓ OPEN | **Blocks:** G4 Implementation

## Problem
G4 requires parsing Git history for per-function risk signals. Must work cross-platform without requiring git CLI.

## Options

### Option A — GitPython (RECOMMENDED)
```python
from git import Repo
repo = Repo('/path/to/repo')
for commit in repo.iter_commits('main', max_count=500):
    for diff in commit.diff(commit.parents[0] if commit.parents else None):
        # get changed lines per file
        pass
```
- ✅ Pure Python, no shell subprocess
- ✅ Well-maintained (used by many tools)
- ✅ Full access to commits, diffs, blame
- ❌ Slower than libgit2 for large repos (10k+ commits)

### Option B — pygit2 (libgit2 bindings)
```python
import pygit2
repo = pygit2.Repository('/path/to/repo')
```
- ✅ 10x faster than GitPython for large repos
- ❌ Requires C library (libgit2) — installation complexity
- ❌ Less Pythonic API

### Option C — Dulwich
- Pure Python, no C dependencies
- Slowest option, but truly zero external deps
- ✅ Good for environments where even GitPython is unavailable

## Agent Task
1. Implement G4 signal extraction using GitPython
2. Test on requests library repo (medium size: ~1000 commits, ~50 Python files)
3. Extract: commit_frequency, churn_rate, last_modified for each function node
4. Measure: extraction time, memory usage
5. Identify: top 10 highest-risk functions by composite score
6. Validate: do high-risk functions correspond to known issue areas?

## Key Algorithm
```python
def extract_g4_signals(repo_path: str, g1_result: ParseResult) -> dict:
    repo = Repo(repo_path)
    signals = {node.id: {"commits": 0, "churn": 0} for node in g1_result.nodes}
    
    for commit in repo.iter_commits(max_count=1000):
        if not commit.parents: continue
        for diff in commit.diff(commit.parents[0]):
            if not diff.b_path.endswith('.py'): continue
            changed_lines = parse_diff_lines(diff)
            for node in g1_result.nodes_in_file(diff.b_path):
                if lines_overlap(changed_lines, node.line_start, node.line_end):
                    signals[node.id]["commits"] += 1
                    signals[node.id]["churn"] += len(changed_lines)
    return signals
```

## Acceptance Criteria
- Extraction completes in ≤ 3 minutes for a repo with 500 commits and 100 Python files
- No shell subprocess calls
- Works on Linux, macOS, Windows
