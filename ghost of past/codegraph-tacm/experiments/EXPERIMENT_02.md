# EXPERIMENT_02 — TACM-v2 Multi-Layer Graph vs BM25 vs Aider RepoMap

**Date:** 2026-04-09
**Status:** Complete — see EXPERIMENT_02_RESULTS.md

> **Note on baseline choice:** RepoMap was chosen as the most widely deployed
> open-source structural code retriever (used in Aider, Continue.dev). It is
> NOT claimed to be the strongest possible retrieval system. The strongest
> retrieval systems for bug localisation are dense embedding retrievers
> (e.g. Agentless localization, Moatless BM25+embedding, GraphCodeBERT on
> CodeSearchNet). RepoMap was chosen because it uses the same input modality
> (no LLM calls, no embeddings) and represents the structural graph retrieval
> family fairly. A future experiment should add a dense embedding baseline.

---

## Motivation

Experiment 01 established that the pre-research TACM system (flat BM25+semantic
retrieval on top of crg) beats naive RAG on bug localisation. But that system
was architecturally a flat retriever — it happened to use a graph store as a
node database, not as a structured graph.

Experiment 02 validates the real intended architecture: a **multi-layer weighted
graph** (FILE → CLASS → FUNCTION) with intent-aware, multi-signal scoring. The
hypothesis is that the layered structure — especially the containment bonus that
surfaces methods of already-selected classes — produces coherent, high-rank
context that beats both lexical and structural baselines.

---

## System Under Test: TACM-v2

### Architecture

Three-layer graph built on top of `code-review-graph` (crg):

```
Layer 0 — FILE      (~40 tokens)   file path + imports + defines list
Layer 1 — CLASS     (~60 tokens)   class header + method list
Layer 2 — FUNCTION  (~150 tokens)  full body (≤40 lines) or sig+docstring
```

Edge types with dynamic weights:
- `CALLS`:       weight = call_frequency / max_calls (0–1)
- `INHERITS`:    1.0 direct, 0.5 transitive grandparent
- `IMPORTS_FROM`:1.0 direct, 0.5 transitive
- `CONTAINS`:    1.0 always
- `TESTED_BY`:   1.0 always

Short-name CALLS resolution: crg stores 88% of call targets as unqualified
names (e.g. "send"). Builder uses a name-index to resolve "send" → all nodes
named "send" with "::" in their qualified_name. Result: 242 → 1,675 CALLS edges
after resolution for requests-sized repos.

### Selection Algorithm

1. Classify query intent: BUG / STRUCTURE / EXPLAIN (keyword + phrase matching)
2. Split token budget by intent:
   - BUG:       FILE 5% / CLASS 20% / FUNCTION 75%
   - STRUCTURE: FILE 30% / CLASS 50% / FUNCTION 20%
   - EXPLAIN:   FILE 10% / CLASS 35% / FUNCTION 55%
3. For each layer (FILE → CLASS → FUNCTION):
   - Score all nodes with intent-weighted signal vector
   - Apply containment bonus (+0.15, capped at 1.0) if parent already selected
   - Greedy fill within layer budget
4. Return SelectionResult with per-layer counts and total token cost

### Scoring Signals

| Signal     | BUG  | STRUCT | EXPLAIN | Description |
|------------|------|--------|---------|-------------|
| bm25       | 0.50 | 0.60   | 0.45    | BM25 on serialized node text |
| fan_in     | 0.25 | 0.10   | 0.15    | weighted in-degree (excl. test callers) |
| fan_out    | 0.10 | 0.20   | 0.30    | call out-degree (orchestrators) |
| complexity | 0.15 | 0.00   | 0.05    | token_cost as proxy |
| test_cover | 0.00 | 0.10   | 0.05    | binary: has TESTED_BY edge |

### Containment Bonus

After each layer's greedy fill, selected node IDs enter a shared `selected_ids`
set. For the next layer down, any node whose `parent_id` is in `selected_ids`
receives a +0.15 score boost (capped at 1.0).

Effect: if `HTTPDigestAuth` is selected at CLASS layer, its methods
(`handle_401`, `build_digest_header`, `__call__`) score 0.15 higher at FUNCTION
layer, creating coherent context clusters.

---

## Baselines

### BM25-Body (lexical ceiling)
BM25Okapi on full function source text. No structure awareness, no budget
splitting, no graph signals. This is the strongest lexical baseline — it has
access to the full body text of every function.

### Aider RepoMap (structural graph baseline)
Aider's tree-sitter + NetworkX PageRank graph ranker. Used in production by
Aider and adopted by Continue.dev.

**What it is:** A structural orientation tool, not a query retriever. RepoMap
ranks all function definitions by:
1. Global PageRank of each identifier across the whole codebase
2. Boost for files/identifiers whose names match query word tokens

RepoMap is NOT a semantic retriever — queries are used to boost identifier
centrality, not to do BM25 or embedding search. It is the right comparison for
"structural graph ranking" but is not the ceiling of retrieval quality.

**All benchmarked systems (see EXPERIMENT_02_RESULTS.md):**
- Dense-MiniLM: all-MiniLM-L6-v2 (Cursor/Continue default) — macro MRR 0.265
- Dense-CodeSearch: st-codesearch-distilroberta-base (CodeSearchNet-trained) — macro MRR 0.261
- Hybrid-MiniLM: BM25 + MiniLM RRF (Agentless/Moatless style) — macro MRR 0.245
- Hybrid-CodeSearch: BM25 + CodeSearch RRF — macro MRR 0.237

**Benchmarked but API unavailable (code in place, rerun once keys are funded):**
- Dense-Voyage: voyage-code-3 (Continue.dev recommended) — Voyage AI billing required
- Dense-OpenAI: text-embedding-3-small — OpenAI quota exhausted

**Not benchmarked (closed platform / LLM-dependent):**
- Cursor, Windsurf, Claude Code, Copilot, Sourcegraph Cody, Gemini Code Assist — IDE
  agents, not isolatable retrievers. They wrap the same embedding primitives above.
- Agentless two-stage, Moatless Tools — require LLM call for localisation step.

**TACM-v2 ablations (see EXPERIMENT_02_RESULTS.md):**
- TACM-NoCB: TACM-v2 without containment bonus — drops to BM25 level on thefuck
- TACM-FixedBudget: equal 33/33/33 layer split, no intent routing
- TACM-BM25Only: BM25 signal only, no graph signals (fan_in/fan_out/complexity)

---

## Dataset

**BugsInPy** — real bug benchmarks with ground-truth fix functions extracted
from unified diffs. GT extracted by heuristic parser (walks diff context lines
for enclosing `def`/`class`), reliable for >85% of single-function fixes.

Tasks are loaded from `bug.info` (`fixed_commit_id="abc"` format). Queries come
from `git log --format=%B` on the fixed commit. Tasks where commit message
lookup fails are **dropped** — no GT-name fallback to prevent query leakage.

| Project | Tasks (after filter) | Functions | Domain |
|---------|---------------------|-----------|--------|
| thefuck | 26 / 30             | 819       | shell rule matching |
| scrapy  | 19 / 30             | 3,063     | web scraping framework |
| tornado | 0 / 4               | 2,017     | excluded — no valid commit queries |

GT matching uses **strict mode**: the node's file path must end with the GT
relative path (full suffix match, no basename fallback) AND the function short name
must match. This is intentionally conservative — duplicated basenames across
subdirectories (e.g. `http/response.py` vs `tests/http/response.py`) do not match.
Lenient (name-only) is tracked separately for diagnosis but not reported as headline.

---

## Metric

**MRR** (Mean Reciprocal Rank) at top-K=10, computed over FUNCTION-layer nodes
only (GT is always a function). Hit% = fraction of tasks where GT appears in
top-10.

For TACM-v2: top-K applies to the FUNCTION layer slice of the selection result,
ranked by descending score. FILE and CLASS nodes are excluded from rank counting.

For BM25/RepoMap: top-K over the full ranked function list.

---

## Hypothesis

1. TACM-v2 MRR > BM25-Body MRR on both projects (p < 0.05, paired bootstrap)
2. TACM-v2 MRR > Dense-MiniLM MRR — the real comparator, not RepoMap
3. The containment bonus is a net positive, isolatable by ablation

Note: RepoMap was the initial structural baseline but is not the headline comparison.
Dense-MiniLM (Cursor/Continue default) is the strongest open competitor.

---

## Success Criteria

| Criterion | Target | Outcome |
|-----------|--------|---------|
| Beat BM25 MRR on both projects (p < 0.05) | primary | ✓ p=0.008, p=0.014 |
| Beat Dense-MiniLM MRR on both projects | primary | direction ✓, not yet significant |
| Containment bonus isolated as net positive (p < 0.05) | ablation | ✓ p=0.004, p=0.017 |
| Token efficiency: structured context, not raw bodies | inherent | ✓ |

---

## Files

| File | Description |
|------|-------------|
| `bench_v2.py` | Benchmark runner (tacm_v2 + BM25 + RepoMap) |
| `tacm_v2/graph/model.py` | LayeredGraph data model |
| `tacm_v2/graph/builder.py` | crg → LayeredGraph builder |
| `tacm_v2/layers/serializers.py` | Per-layer text serializers |
| `tacm_v2/selector/intent.py` | Intent classification + weight vectors |
| `tacm_v2/selector/scoring.py` | 5-signal NodeScorer |
| `tacm_v2/selector/selector.py` | Main select() with containment bonus |
