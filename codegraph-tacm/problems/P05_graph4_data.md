# P05 — Graph 4 Data Availability
**Severity:** 🟠 HIGH | **Status:** ❓ OPEN | **Blocks:** G4 (Historical Graph)

## Problem
G4 requires historical signals per code node: bug frequency, change frequency (churn), co-change patterns, fix history. These signals only exist in Git history and issue trackers.

**Availability by repo type:**
| Repo type | Git history | GitHub Issues | CI logs |
|---|---|---|---|
| Public open-source | ✅ Always | ✅ Usually | ✅ Sometimes |
| Private company | ✅ Always | ❓ Maybe | ❓ Maybe |
| SWE-bench tasks | ✅ Always | ✅ Always | ❌ No |

## Signals to Extract

### From Git history only (v1 scope)
```python
per_function_signals = {
    "commit_frequency":   # how many commits touched this function
    "churn_rate":         # lines added+deleted per month (rolling 6mo)
    "last_modified":      # days since last change
    "author_count":       # number of distinct authors
    "co_change_partners": # which other functions change in same commits
}
```

### From GitHub Issues API (v2)
```python
per_function_signals["bug_report_count"]  # issues mentioning this function
per_function_signals["issue_resolution_time"]  # avg days to fix
```

### Composite risk score (what TACM actually uses)
```python
risk_score(node) = (
    normalise(commit_frequency) * 0.3 +
    normalise(churn_rate)       * 0.4 +
    normalise(bug_count)        * 0.3   # 0 if no issue data
)
```

## Agent Task
1. Use GitPython to extract per-function change frequency from the `requests` library repo
2. Map git blame output to CGI node IDs (function names)
3. Compute risk scores for all functions
4. Identify top 10 highest-risk functions — do they match known bug-prone areas?
5. Measure: how long does G4 indexing take for a 5k-line repo? 50k-line repo?

## Key Challenge — Mapping Git Diffs to Functions
Git diffs are line-based. CGI nodes are function-based. You need to:
1. For each commit, get changed line ranges
2. Map line ranges to function node IDs using G1 (line_start, line_end per node)
3. Increment that function's commit count

```python
# Pseudocode
for commit in repo.iter_commits():
    diff = commit.diff(commit.parents[0])
    for file_diff in diff:
        changed_lines = get_changed_lines(file_diff)
        for node in g1_nodes_in_file(file_diff.b_path):
            if overlaps(changed_lines, (node.line_start, node.line_end)):
                g4_signals[node.id]["commit_frequency"] += 1
```

## Acceptance Criteria
- G4 signals extracted for 100% of G1 nodes that exist in Git history
- Risk score correctly identifies functions with known bugs in BugsInPy
- G4 indexing time ≤ 2 minutes for a 10k-line repo with 1000 commits
- Works with GitPython only (no shell subprocess dependency)
