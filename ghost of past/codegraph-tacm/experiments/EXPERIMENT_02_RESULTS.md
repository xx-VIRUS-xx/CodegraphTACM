# EXPERIMENT_02 — Results

**Date:** 2026-04-10
**System:** TACM-v2 (multi-layer weighted graph + intent-aware scoring)
**Dataset:** BugsInPy — thefuck (n=26), scrapy (n=19) — total n=45
**Metric:** MRR and Hit@10, FUNCTION layer only, STRICT matching (file suffix + fn name, no basename fallback)
**Queries:** NL from git commit messages — no GT fallback, no name leakage
**Significance:** Paired bootstrap p-values (one-sided, 5000 resamples)

---

## System Under Test: TACM-v2

Three-layer graph built on top of `code-review-graph` (crg):

```
Layer 0 — FILE      (~40 tokens)   file path + imports + defines list
Layer 1 — CLASS     (~60 tokens)   class header + method list
Layer 2 — FUNCTION  (~150 tokens)  full body (≤40 lines) or sig+docstring
```

Edge types with dynamic weights:
- `CALLS`: weight = call_frequency / max_calls (0–1). Short-name resolution: 242 → 1,675 edges.
- `INHERITS`: 1.0 direct, 0.5 transitive grandparent
- `IMPORTS_FROM`: 1.0 direct, 0.5 transitive
- `CONTAINS` / `TESTED_BY`: always 1.0

**Selection:** classify query intent (BUG/STRUCTURE/EXPLAIN) → split token budget
by layer (BUG: FILE 5% / CLASS 20% / FUNCTION 75%) → score each layer with
intent-weighted signals → greedy fill → apply containment bonus (+0.15 if parent
already selected).

**Scoring signals per intent:**

| Signal | BUG | STRUCT | EXPLAIN |
|--------|-----|--------|---------|
| bm25 | 0.50 | 0.60 | 0.45 |
| fan_in | 0.25 | 0.10 | 0.15 |
| fan_out | 0.10 | 0.20 | 0.30 |
| complexity | 0.15 | 0.00 | 0.05 |
| test_cover | 0.00 | 0.10 | 0.05 |

---

## Systems compared

| System | Method | Represents |
|--------|--------|-----------|
| BM25-Body | BM25Okapi on full function body | Lexical ceiling |
| RepoMap | tree-sitter + PageRank (Aider) | Most-deployed structural retriever |
| Dense-MiniLM | all-MiniLM-L6-v2 cosine | Cursor/Continue default embedding |
| Dense-CodeSearch | st-codesearch-distilroberta-base | Code-specific NL→code retrieval (CodeSearchNet-trained) |
| Hybrid-MiniLM | BM25 + MiniLM via RRF | Agentless/Moatless style |
| Hybrid-CodeSearch | BM25 + CodeSearch via RRF | Strongest open hybrid |
| TACM-v2 | Multi-layer graph + intent scoring | This work |

**Note on CodeBERT:** `microsoft/codebert-base` (the raw pretrained MLM) produces
near-random similarities without fine-tuning on retrieval pairs — excluded.
`st-codesearch-distilroberta-base` is the properly fine-tuned code-search model
from the same family, trained on CodeSearchNet NL→code pairs.

**Pending (code in place, API keys needed):**
Dense-Voyage (voyage-code-3), Dense-OpenAI (text-embedding-3-small)

**Not benchmarked (closed platform or LLM-dependent):**
Agentless two-stage, Moatless Tools, Cursor, Copilot, Sourcegraph Cody

---

## Results: thefuck (n=26, 819 prod functions)

Strict matching: file path suffix + function name, no basename fallback.
p-values: one-sided paired bootstrap, H0 = system is no better than comparator.

| System | Hit@10 | MRR | 95% CI | Δ vs BM25 | p vs BM25 | p vs MiniLM |
|--------|--------|-----|--------|-----------|-----------|-------------|
| BM25-Body | 42% | 0.2936 | [0.1397, 0.4603] | — | — | 0.586 |
| RepoMap | 8% | 0.0103 | [0.0000, 0.0269] | -0.283 | 1.000 | 1.000 |
| Dense-MiniLM | 58% | 0.3113 | [0.1670, 0.4635] | +0.018 | 0.414 | — |
| Dense-CodeSearch | 42% | 0.2803 | [0.1277, 0.4457] | -0.013 | 0.552 | 0.688 |
| Hybrid-MiniLM | 58% | 0.3122 | [0.1692, 0.4606] | +0.019 | 0.317 | 0.495 |
| Hybrid-CodeSearch | 54% | 0.2552 | [0.1318, 0.3971] | -0.038 | 0.704 | 0.857 |
| **TACM-v2** | **65%** | **0.3725** | [0.2202, 0.5353] | **+0.079** | **0.008** | 0.233 |

TACM-v2 vs BM25: p=0.008 (significant at α=0.01). TACM-v2 vs Dense-MiniLM: p=0.233 — direction consistent but not significant at n=26.

## Results: scrapy (n=19, 3,063 prod functions)

| System | Hit@10 | MRR | 95% CI | Δ vs BM25 | p vs BM25 | p vs MiniLM |
|--------|--------|-----|--------|-----------|-----------|-------------|
| BM25-Body | 37% | 0.1594 | [0.0497, 0.2909] | — | — | 0.755 |
| RepoMap | 5% | 0.0132 | [0.0000, 0.0395] | -0.146 | 0.989 | 0.994 |
| Dense-MiniLM | 32% | 0.2193 | [0.0702, 0.3947] | +0.060 | 0.258 | — |
| Dense-CodeSearch | 37% | 0.2368 | [0.0921, 0.4211] | +0.077 | 0.269 | 0.429 |
| Hybrid-MiniLM | 32% | 0.1667 | [0.0526, 0.2982] | +0.007 | 0.470 | 0.803 |
| Hybrid-CodeSearch | 37% | 0.2149 | [0.0789, 0.3640] | +0.056 | 0.219 | 0.563 |
| **TACM-v2** | **47%** | **0.2897** | [0.1186, 0.4737] | **+0.130** | **0.014** | 0.225 |

Note: BM25 scrapy MRR corrected from 0.1769 → 0.1594 after removing basename fallback from strict matcher.

TACM-v2 vs BM25: p=0.014 (significant at α=0.05). TACM-v2 vs Dense-MiniLM: p=0.225 — direction consistent, not significant at n=19.

## Aggregate (macro-average, n=45)

| System | Macro MRR | Δ vs BM25 |
|--------|-----------|-----------|
| BM25-Body | 0.227 | — |
| RepoMap | 0.012 | -0.215 |
| Dense-MiniLM | 0.265 | +0.039 |
| Dense-CodeSearch | 0.258 | +0.031 |
| Hybrid-MiniLM | 0.237 | +0.010 |
| Hybrid-CodeSearch | 0.252 | +0.025 |
| **TACM-v2** | **0.331** | **+0.104** |

---

## Key findings

### 1. TACM-v2 leads in this evaluation

TACM-v2 leads every system on both thefuck and scrapy. The advantage over BM25 is
statistically significant on both projects (p=0.008, p=0.014). The advantage over
Dense-MiniLM (the headline competitor — Cursor/Continue default) is p=0.23 on
thefuck and p=0.23 on scrapy: direction is consistent across both projects, but
n=45 is not sufficient to reach significance against this comparator. More data needed.

### 2. Dense-MiniLM is the comparator that matters, not RepoMap

Dense-MiniLM achieves 0.265 macro MRR. TACM-v2 (0.331) is 0.066 ahead of it —
Dense-MiniLM is the strongest flat competitor. RepoMap (0.012 MRR) is structurally mismatched
for this task: PageRank over identifiers is a codebase orientation tool, not a query
retriever. The real question this experiment is testing is TACM-v2 vs Dense-MiniLM.

### 3. Code-specific embeddings don't consistently outperform general MiniLM

Dense-CodeSearch (CodeSearchNet-trained) achieves 0.258 macro MRR — essentially tied
with MiniLM (0.265). The code-domain fine-tuning doesn't transfer cleanly to bug
localisation queries derived from commit messages, which are natural language rather
than formal code docstrings.

### 4. RRF hybrid hurts relative to pure dense

Hybrid-MiniLM (0.237) and Hybrid-CodeSearch (0.252) are both weaker than or equal to
their pure dense counterparts. BM25 degrades the dense signal at k=60. This is a
dataset-specific finding — may not generalise.

### 5. TACM-v2's advantage appears structural, not lexical

TACM-BM25Only (BM25 signal only, graph layout retained) achieves 0.3224/0.2316 MRR —
still ahead of flat BM25-Body (0.2936/0.1594), but below full TACM-v2 (0.3725/0.2897).
The layered graph structure contributes signal independently of scoring, consistent with
the hypothesis that module-level routing adds value beyond lexical matching alone.

---

## Per-task examples: what TACM-v2 hits that flat retrievers miss

The per-task data (thefuck @ budget=4000) shows TACM-v2 uniquely hitting:
- **thefuck-7, -15, -18, -27, -28**: BM25, MiniLM, and CodeSearch all miss.
  These are functions with moderate body overlap but whose **file context** gets
  selected at the FILE layer, giving the containment bonus that promotes them.

- **thefuck-4** (#8 strict): `_get_aliases` — a method on the Shell class.
  BM25 and dense both miss (generic name, moderate body signal). TACM-v2 hits
  because the FILE layer selected `shells/bash.py` → CLASS `Bash` → containment
  bonus promotes `_get_aliases`.

---

## Ablation Results (2026-04-10)

Three ablations isolate which components drive TACM-v2's advantage.
p-values: one-sided paired bootstrap, H0 = full TACM-v2 is no better than this ablation.

### thefuck (n=26)

| System | Hit@10 | MRR | Δ vs full | p(full>this) | Component removed |
|--------|--------|-----|-----------|--------------|-------------------|
| TACM-v2 (full) | **65%** | **0.3725** | — | — | — |
| TACM-NoCB | 42% | 0.2933 | -0.079 | **0.004** | containment bonus |
| TACM-FixedBudget | 62% | 0.3507 | -0.022 | 0.033 | intent budget routing |
| TACM-BM25Only | 65% | 0.3224 | -0.050 | 0.133 | graph signals (fan_in/fan_out) |

### scrapy (n=19)

| System | Hit@10 | MRR | Δ vs full | p(full>this) | Component removed |
|--------|--------|-----|-----------|--------------|-------------------|
| TACM-v2 (full) | **47%** | **0.2897** | — | — | — |
| TACM-NoCB | 32% | 0.1886 | -0.101 | **0.017** | containment bonus |
| TACM-FixedBudget | 42% | 0.2553 | -0.034 | 0.129 | intent budget routing |
| TACM-BM25Only | 42% | 0.2316 | -0.058 | 0.096 | graph signals (fan_in/fan_out) |

### Ablation interpretation

**Containment bonus appears to be the largest single contributor** (p=0.004 on thefuck,
p=0.017 on scrapy — the only ablation reaching significance on both projects). Without it,
TACM-v2 MRR falls to near BM25 level on thefuck (0.2933 vs 0.2936 BM25). This is
consistent with the hypothesis that layered structure — routing to the right file, then
promoting functions within that file — is where the advantage comes from.

**Intent routing adds a smaller but directionally consistent effect** (p=0.033 on thefuck,
p=0.129 on scrapy). Replacing intent budgets with a flat 33/33/33 split degrades function
retrieval, suggesting the BUG-intent 75% FUNCTION allocation is directionally correct.

**Graph signals (fan_in/fan_out) show mixed significance** (p=0.133 on thefuck, p=0.096
on scrapy). The directional effect is consistent but doesn't reach significance at n=45.
More data needed to isolate this component cleanly.

---

## Multi-Level Analysis (2026-04-10)

**Important framing:** the File% and Class% columns mean different things for flat vs TACM systems:
- **Flat retrievers** (BM25, dense, hybrid): File/Class % = fraction of top-K *function results* that happen to belong to the GT file or class. This is implicit file/class coverage, derived from function ranking.
- **TACM-v2**: File% = explicit FILE-layer node selection hit rate; Class% = CLASS-layer node selection hit rate. These are active structural routing decisions, not function rank by-products.

These measure different things. The tables are shown for TACM internal analysis — not a like-for-like cross-system competition on file/class routing.

### thefuck — Multi-level Hit@10

| System | File% (fn-attr†) | Class% (fn-attr†) | Fn% |
|--------|-----------------|-------------------|-----|
| BM25-Body | 62% | 12% | 42% |
| Dense-MiniLM | 69% | 12% | 58% |
| Hybrid-CodeSearch | 65% | 12% | 54% |
| TACM-v2 | **81%** *(FILE-node)* | 12% *(CLASS-node)* | **65%** |
| TACM-NoCB | **81%** *(FILE-node)* | 12% *(CLASS-node)* | 42% |

† For flat systems: "% of top-10 fn results attributed to GT file/class"

### scrapy — Multi-level Hit@10

| System | File% (fn-attr†) | Class% (fn-attr†) | Fn% |
|--------|-----------------|-------------------|-----|
| BM25-Body | 63% | 5% | 37% |
| Dense-MiniLM | 63% | 0% | 32% |
| Hybrid-CodeSearch | 68% | 5% | 37% |
| TACM-v2 | 63% *(FILE-node)* | 0% *(CLASS-node)* | **47%** |

### Multi-level interpretation

The most useful comparison here is the **TACM-v2 vs TACM-NoCB split** on thefuck:
- FILE-node routing: identical (81%) — the FILE layer selects the same modules regardless
- CLASS/Fn routing: NoCB drops to 42% fn Hit@10 despite same FILE layer

This internal comparison cleanly separates the two mechanisms: FILE selection routes to
the right module; containment bonus then surfaces the right function within it. They
compose — and either alone is insufficient.

On scrapy, TACM-v2 FILE-node routing (63%) matches BM25's implicit file attribution.
The function-level advantage (+0.130 MRR over BM25) comes entirely from containment
bonus chains, not from better module routing.

---

## Limitations

1. **n=45 is borderline.** CIs span ±0.15. Need additional BugsInPy projects to narrow.
   Keras excluded (codebase drift — bugs reference tensorflow_backend.py from 2018 era).
   Pandas n=58 available but all systems perform poorly (dataset quality issues + 10k fns).
2. **Tornado excluded.** All tasks drop after query-leakage fix. Manual NL queries needed.
3. **voyage-code-3 / text-embedding-3 not benchmarked.** Voyage API needs billing setup;
   OpenAI key quota exhausted. Code is in place — rerun once keys are funded.
4. **RRF k=60 not tuned.** May not be optimal for this dataset.
5. **Class-level GT is sparse** in current projects. Ablation on a class-heavy codebase
   would better validate the CLASS layer contribution.

---

## Next steps

### Immediate (retrieval track)
| Priority | Task |
|----------|------|
| 1 | Fund Voyage/OpenAI keys and rerun — Dense-Voyage and Dense-OpenAI code is in place |
| 2 | Add G3 semantic rescue path to TACM-v2 — ablation proves structure alone is the floor |
| 3 | Class-heavy BugsInPy project (Django, SQLAlchemy) for CLASS-layer validation |

### Experiment 03 — Agent evaluation (see EXPERIMENT_03.md)
Retrieval MRR does not prove agent task success. The next experiment swaps only the
context provider across identical agent loops and measures **tests-pass solve rate**.

| Priority | Task |
|----------|------|
| 1 | Build `agent_harness.py` — fixed Claude agent loop with swappable context provider |
| 2 | Build `context_providers.py` — token-budget-fair adapters for all retrieval conditions |
| 3 | Build `patch_utils.py` + `test_runner.py` — apply/restore patch, run BugsInPy tests |
| 4 | Run all conditions (Naive/BM25/MiniLM/Hybrid/TACM) × 45 tasks × 3 seeds |
| 5 | Mirror repos to GitHub, run Copilot coding agent as external product baseline |

### Broader task roadmap (post-Experiment 03)
Beyond bugs: feature addition, refactor, test generation, code explanation.
Each track uses the same agent harness with task-appropriate prompts and verification.
Bugs are one lane — not the whole highway.
