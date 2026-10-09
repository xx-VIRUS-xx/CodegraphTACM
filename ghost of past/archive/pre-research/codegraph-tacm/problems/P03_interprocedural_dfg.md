# P03 — Inter-procedural Data Flow at Scale
**Severity:** 🟠 HIGH | **Status:** ❓ OPEN | **Blocks:** G2 (Causal Graph)

## Problem
Control Flow Graph (CFG) and Data Flow Graph (DFG) are well-understood within a single function. At repository scale — tracking a value across multiple function calls across multiple files — it becomes unsolved even in production compilers.

**We must define exactly what G2 claims to provide.**

## Levels of DFG (choose one)

### Level 1 — Intra-function only
Track variable assignments and reads within a single function body.
```python
def process(text):
    cleaned = normalize(text)    # DFG: text → normalize → cleaned
    tokens = tokenize(cleaned)   # DFG: cleaned → tokenize → tokens
    return tokens
```
- ✅ 100% accurate with ast analysis
- ✅ Implementable in 2 days
- ❌ Misses cross-function data flow (the most interesting cases for bugs)

### Level 2 — Module-cluster (RECOMMENDED for v1)
Track data flow within a file and across its direct imports.
- Function A passes return value to Function B (same file)
- Function A calls Function B from imported module, tracks argument flow
- ✅ Covers ~80% of real bug scenarios
- ✅ Tractable without a full compiler
- ❌ Misses transitive flows (A→B→C where B is in a third file)

### Level 3 — Full inter-procedural
Track values across arbitrary call chains across all files.
- ✅ Maximum accuracy
- ❌ Requires full type inference (pyright/mypy level)
- ❌ Potentially O(n²) in codebase size
- ❌ Overclaiming risk in paper

## What the Paper Must Say
Explicitly state the scope: "G2 provides module-cluster-level data flow analysis. Full inter-procedural DFG is left for future work."

Reviewers respect honest scoping. They penalise overclaiming.

## Agent Task
1. Implement Level 2 DFG extraction using Python ast
2. Test on ast_parser.py itself — extract all data flow edges
3. Measure: how many cross-function flows are captured vs missed
4. Produce a sample DFG for a real bug in the BugsInPy dataset
5. Show: does the DFG surface the buggy data flow path?

## Acceptance Criteria
- G2 extracts at minimum: ASSIGNS, PASSES_TO, RETURNS_TO edge types
- G2 edges are a strict superset of what G1 provides for the same codebase
- At least one real bug in BugsInPy is reachable via G2 traversal but not G1 traversal

## Key Files to Read First
- `architecture/DATA_MODELS.md` — G2 edge type definitions
- `problems/P02_cross_file_symbols.md` — G2 depends on P02 being solved first
