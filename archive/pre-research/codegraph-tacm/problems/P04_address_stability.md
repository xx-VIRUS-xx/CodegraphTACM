# P04 — Address Stability Under Code Change
**Severity:** 🟠 HIGH | **Status:** ❓ OPEN | **Blocks:** TACM Layer

## Problem
TACM addresses must be stable enough to be useful but invalidate correctly when meaning changes.

| Change type | Should address survive? |
|---|---|
| Whitespace / formatting | ✅ Yes |
| Adding a comment | ✅ Yes |
| Moving function to another file | ❌ No — new location |
| Renaming function | ❌ No — new identity |
| Changing function signature | ❌ No — new contract |
| Changing function body only | ✅ Yes (address stable, payload updates) |

## Candidate Schemes

### Scheme A — Qualified name + file path hash
```
fn:module.ClassName.method_name:a3f9b2[:8]
```
- Stable across: line changes, body changes, formatting
- Breaks on: rename, move to different file
- ✅ Simple to implement
- ✅ Human-readable
- ✅ Breaks intentionally on meaningful changes

### Scheme B — Semantic fingerprint (signature-based)
```
fn:sha256(normalised_signature)[:12]
```
Where normalised signature = `parse(str) -> List[Token]` (no whitespace, no defaults)
- Stable across: renames that preserve signature, moves, formatting
- Breaks on: signature changes
- ✅ Location-independent
- ❌ Two different functions with same signature collide

### Scheme C — UUID assigned at index time
```
fn:550e8400-e29b-41d4-a716
```
- Stable across: everything until re-index
- Requires: mapping table between UUID and current code location
- ✅ Maximally stable
- ❌ Opaque — no human readability
- ❌ Stale after re-index if not carefully managed

### Scheme D — Git object hash
```
fn:blob:3a9f2c (git hash of function source)
```
- Stable across: anything in committed history
- Breaks on: any content change
- ✅ Perfectly stable for historical analysis (G4)
- ❌ Useless for uncommitted work
- ❌ Changes on every commit touching the function

## Agent Task
1. Implement Scheme A in Python — generate addresses for all nodes from ast_parser.py output
2. Simulate 5 types of code changes on a test file (rename, move, reformat, body change, signature change)
3. For each change: does the address survive correctly? Does it invalidate when it should?
4. Measure: what % of addresses survive a typical refactoring commit in a real repo?
5. Recommendation: which scheme for v1?

## Acceptance Criteria
- Address survives whitespace/formatting changes: 100%
- Address correctly invalidates on rename/signature change: 100%
- Address is human-readable enough to debug without a lookup table
- No two distinct semantic units share the same address

## Current Best Thinking
Scheme A for v1. Simple, human-readable, breaks on the right events.
Consider Scheme B for G3 (semantic similarity) since location-independence matters there.
