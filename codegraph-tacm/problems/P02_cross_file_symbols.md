# P02 — Cross-file Symbol Resolution
**Severity:** 🔴 CRITICAL | **Status:** ❓ OPEN | **Blocks:** G1, G2, G3

## Problem
Python's `ast` module alone cannot resolve `from utils import parse` to the actual `def parse()` in `utils.py`. Without this, Graph 1 has broken edges at every file boundary.

**Concrete example:**
```python
# file_a.py
from utils import parse
result = parse(text)   # ast sees a Call to 'parse' but doesn't know where parse lives
```
The CALLS edge from `file_a.process()` → `parse` is broken — it points to a name, not a node.

## Why It Matters
- G1 broken edges → G2 broken data flow paths → G3 incorrect semantic clusters
- Cross-file calls are the majority of interesting relationships in real codebases
- SWE-bench tasks almost always involve cross-file interactions

## Known Approaches

### Option A — jedi library
```python
import jedi
script = jedi.Script(source, path=filepath)
completions = script.infer(line, col)  # returns actual definition location
```
- ✅ High accuracy, handles dynamic imports, well-maintained
- ✅ Used by VS Code Python extension — battle-tested
- ❌ Slow for large repos (full type inference)
- ❌ Requires jedi as runtime dependency

### Option B — rope library
```python
import rope.base.project as project
proj = project.Project('/path/to/repo')
# use rope's find_definition
```
- ✅ Designed for refactoring — excellent cross-file resolution
- ❌ Less maintained than jedi
- ❌ Heavier API

### Option C — Two-pass import map
```python
# Pass 1: build {module_name: file_path} map for entire repo
# Pass 2: resolve import names to node IDs using the map
```
- ✅ No extra dependencies
- ✅ Fast — O(files) not O(symbols)
- ❌ Misses `from x import *`, dynamic imports, conditional imports
- ❌ Only resolves to file level, not function level

### Option D — Scope to same-package only
- Only resolve imports within the indexed repo
- Mark stdlib/third-party imports as external leaf nodes
- ✅ Simple, fast, no false edges
- ❌ Misses inter-package relationships

## Agent Task
1. Benchmark jedi resolution accuracy on 3 mid-size Python repos (requests, flask, django/core)
2. Measure: resolution rate (% of imports successfully resolved), time per repo, memory usage
3. Compare Option A vs Option C resolution rate on same repos
4. Recommend: which approach for v1 prototype? which for production?

## Acceptance Criteria
- Resolution rate ≥ 80% of import statements in a typical Python repo
- Resolution time ≤ 30 seconds for a 10k-line codebase
- No false-positive edges (A calls B when it doesn't)

## Current Best Thinking
Option C (two-pass import map) for v1 — fast, no deps, covers 70%+ of cases.
Option A (jedi) for v2 — higher accuracy when performance is optimised.
