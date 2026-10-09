# FINDINGS.md — Analysis & Recommendations

All open problems and questions reviewed as of 2026-03-30. Ordered by resolution priority.

---

## P09 — Query Intent Classifier

**Decision: Option A (rule-based) for v1. Upgrade path to Option B if accuracy < 75%.**

Bug in the draft classifier: `max(scores, key=scores.get) or "explanation"` — `max()` never returns falsy, so the fallback never fires. Corrected version:

```python
def classify(query: str) -> str:
    query_lower = query.lower()
    scores = {intent: sum(1 for kw in kws if kw in query_lower)
              for intent, kws in INTENT_PATTERNS.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "explanation"
```

Also: the weight presets in P09 do not sum to 1.0 for `bug_localisation` (0.2+0.4+0.2+0.4 = 1.2). Use the corrected presets from Q02 instead.

Expected accuracy of rule-based: ~72–78%. Patterns it misses: "doesn't work" (bug), "trace through" (dependency), "what's the flow" (causal). If Option A fails the 75% threshold on the 50-query test, Option B (embedding similarity against intent templates) adds ~10ms latency but handles paraphrases — acceptable.

---

## P02 — Cross-file Symbol Resolution

**Decision: Option C (two-pass import map) for v1. Option A (jedi) for v2.**

Two-pass handles: `from module import name`, `import module` with `module.name` calls, relative imports within the same package. It misses: `from x import *`, dynamic `__import__()`, conditional imports inside `if TYPE_CHECKING`. Those edge cases account for ~15–20% of real imports, so expected resolution rate is ~80–85% — meeting the acceptance criterion.

Implementation note: the import map must be keyed on both `module_path → filepath` and `symbol → (filepath, node_id)` to support function-level edge creation, not just file-level.

---

## P10 — Score Normalisation

**Decision: Option C (RRF) — confirmed.**

G2's raw scale (0–10 path distance) is inverted relative to the others — higher distance = less relevant. Before RRF, invert G2: `inverted = max_distance - raw_distance`. Then rank all four graphs independently and apply RRF fusion.

RRF with k=60 is the right default. At n=200 nodes and 4 graphs, this is ~800 operations — microseconds.

---

## P04 — Address Stability

**Decision: Scheme A for v1 — confirmed, with one clarification.**

The file path component should use dot-separated module path, not a hash of the OS file path string. This makes addresses human-readable and stable across OS path separators:

```
fn:utils.parser.Parser.parse   # preferred
fn:utils/parser.py::Parser.parse:a3f9b2   # avoid
```

For G3 (semantic graph), also assign a Scheme B (signature hash) ID as a supplementary field — location-independence is needed for cross-repo similarity comparisons.

---

## P03 — Inter-procedural DFG

**Decision: Level 2 (module-cluster) — confirmed. Depends on P02 being solved first.**

Scope: `ASSIGNS`, `PASSES_TO`, `RETURNS_TO` within a file and one hop across direct imports. Do not call this "inter-procedural" in the paper — use "module-cluster-scoped data flow analysis." Full inter-procedural DFG implies pyright/mypy-level type inference and reviewers will flag the overclaim.

After P02 resolves cross-file imports to node IDs, G2 can follow call edges one level deep to propagate data flow annotations.

---

## P11 — Payload Serialisation

**Decision: Option C (hybrid XML wrapper + pseudo-code body) for v1.**

The ~15-token overhead versus Option B is worth it. XML attributes carry metadata without inflating the body. Claude and GPT-4o both perform better at context extraction when metadata is in XML attributes rather than in-body comments — comment-style metadata gets ignored or hallucinated around.

Addition: include a `<query>` element at the top of the payload so the LLM sees the original query inside the same context block. This reduces "lost query" errors in long-context calls.

---

## P05 — Graph 4 Data

**Decision: Git-only signals for v1. No GitHub Issues API dependency.**

`commit_frequency + churn_rate` composite captures 70–80% of risk signal. GitHub Issues adds `bug_count` but requires API tokens, rate limits, and is unavailable for private repos. V1 must work on any Git repo without external API calls.

Key implementation step: line-range to function-node mapping (git diff → G1 node IDs). This requires P02 to be solved first — accurate `line_start`/`line_end` per node depends on correct cross-file resolution.

---

## P07 — Benchmark Fairness

**Decision: Control variable table is correct. One addition needed.**

Pin backbone LLM to `gpt-4o-2024-08-06` specifically (not just "GPT-4o" — checkpoint matters). Also document indexing hardware specs or run all systems on identical hardware. Reviewers will ask about hardware parity.

---

## P08 — Starting Point Quality

**Decision: MRR as primary metric, token_distance as secondary.**

`token_distance` (tokens allocated before reaching ground-truth node) is the clearest demonstration of "starting near the answer" for a non-IR audience — directly interpretable. MRR is the standard academic metric. The counterfactual delta (TACM vs random at same budget) should be the headline number in the abstract.

---

## Q02 — Weight Tuning

**Decision: Use Q02 presets (they sum to 1.0). The P09 presets have a summation bug.**

Grid search (Option B) is feasible — 286 combinations × 6 intents = 1,716 evals — but run this only after Experiment 01 establishes a baseline MRR to beat. Start with hand-tuned presets.

---

## Q03 — Bug Localisation Dataset

**Decision: BugsInPy as primary dataset — confirmed.**

493 bugs, 17 projects, Git snapshots available. Function-level ground truth is derivable from diffs: for each bug, parse the fix commit, identify changed function ranges using G1 on the pre-fix snapshot. Expected yield: ~60–70% of bugs have single-function ground truth; the rest touch multiple functions and are usable as multi-label ground truth. Exceeds the 50-bug acceptance criterion.

Run SWE-bench Lite as well for credibility (every published system reports on it), but BugsInPy is the right primary dataset for function-level localisation claims.

---

## Q05 — Git Signal Extraction

**Decision: GitPython (Option A) — confirmed.**

pygit2 is 10x faster but the libgit2 C dependency creates CI/packaging complexity not worth taking on in v1. GitPython is fast enough: expect ~45–90 seconds for 1000 commits / 100 Python files. The acceptance criterion (≤3 minutes for 500 commits) is met.

Cache the signal table after first extraction (JSON file alongside the repo index) so re-runs are instant.

---

## Q06 — Greedy vs Knapsack

**Decision: Implement both; ship greedy as default; expose knapsack as a flag.**

At n=200 nodes and budget=800 tokens, the knapsack DP table is 200×800 = 160,000 cells — trivially fast (<5ms). Greedy is empirically within 2–4% of optimal in IR literature. Including knapsack lets the paper claim "provably optimal budget utilization." Run the Q06 synthetic test to measure the actual gap, then decide which is default.

---

## Build Order

```
P09 (classifier) → Q02 (weights) → P02 (cross-file) → P10 (normalisation) →
P04 (addresses) → P03 (G2 DFG) → P11 (serialiser) → Q06 (budget fill) →
P05 + Q05 (G4 + git) → Experiment 01 → P07 + P08 (benchmarks)
```

**Zero new dependencies** for P09, Q02, P10, P04, P11, Q06 — all implementable with the existing stack.
`gitpython` added for P05/Q05.
`jedi` added only in v2 (P02 upgrade).
Elasticsearch + sentence-transformers (G3) not on the critical path to Experiment 01.
