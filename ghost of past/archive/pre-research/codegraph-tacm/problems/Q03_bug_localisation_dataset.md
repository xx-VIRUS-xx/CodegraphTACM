# Q03 — Primary Benchmark Dataset for Bug Localisation
**Status:** ❓ OPEN | **Blocks:** Evaluation / Paper

## Problem
Bug localisation is our primary novel task. We need a dataset where:
- Ground truth = the specific buggy function (not just file)
- Bugs are real (not synthetic)
- Codebase is Python
- We have access to the full codebase at the time of the bug

## Dataset Options

### Option A — BugsInPy
- 493 bugs from 17 real Python projects (matplotlib, pandas, scrapy, etc.)
- Ground truth: buggy files + line ranges
- Codebase: full Git snapshot available
- ✅ Best fit — Python, real bugs, function-level ground truth derivable
- ✅ Used by several code intelligence papers
- Access: github.com/soarsmu/BugsInPy

### Option B — SWE-bench Lite (adapted)
- 300 real GitHub issues with confirmed fixes
- Ground truth: changed files (not functions — must derive functions from diffs)
- ✅ Gold standard, every system reports on it
- ❌ Designed for fix generation, not localisation
- ❌ Ground truth is at file level, not function level

### Option C — Custom dataset from GitHub
- Scrape Flask, Requests, Django issues with "bug" label + linked PR
- Extract: issue text, buggy commit, fixed commit, changed functions
- ✅ Maximum control
- ❌ Significant manual labelling effort (30–50 hrs)
- ❌ Delays benchmark

### Option D — PyBugs / ManyBugs
- Older datasets, fewer Python bugs, less maintained
- ❌ Not recommended

## Agent Task
1. Download BugsInPy repo and sample 20 bugs
2. For each bug: can you identify the specific buggy function(s) from the diff?
3. Can the full codebase at bug-time be reconstructed from the Git snapshot?
4. Measure: what % of bugs have function-level ground truth (not just file-level)?
5. Confirm BugsInPy is usable, or propose adaptation of SWE-bench Lite

## Acceptance Criteria
- ≥50 bugs with function-level ground truth
- Full codebase available at bug-time for each
- At least 3 different Python projects represented
- Ground truth derivable programmatically (not requiring manual inspection)
