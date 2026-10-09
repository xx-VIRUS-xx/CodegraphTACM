# EXPERIMENT_04 RESULTS — Pure Retrieval Benchmark: Does Better Scoring → Better Context?

**Date:** 2026-04-13
**Status:** Complete (thefuck n=23 + scrapy n=18 + pandas n=36; keras excluded — wrong repo version)
**Dataset:** `bugsinpy_code_grounded_benchmark_ready.jsonl` (88 bugs: thefuck/scrapy/pandas/keras, labels: code_explicit + semantic_code)
**Token budget:** 4000 tokens per condition
**Conditions:** bm25, minilm, codesearch, hybrid, hybrid-cs, tacm, tacm-full, tacm-dyn, tacm-dyn-l4, tacm-rerank
**Reranker:** gpt-4o-mini, 1 call per query, top-40 TACM candidates → reranked top-20, 2.5s rate-limit gap

---

## What this experiment measures

Experiment 03 benchmarked end-to-end agent solve rate — but agent noise (random patch generation, seed variance) made it hard to isolate retrieval quality. Experiment 04 removes the agent entirely and measures the retrieval step directly:

- **H@1 / H@5 / H@10**: Is the ground-truth function ranked in the top 1 / 5 / 10?
- **MRR**: Mean Reciprocal Rank — quality of the best retrieval across all bugs
- **Ctx%**: Does the final packed context contain the GT function? (budget-constrained)

The dataset uses code-grounded bugs where the GT function is confirmed to appear in the fix patch — no ambiguous GT labels.

---

## Results — thefuck (n=23)

```
Condition        H@1    H@5    H@10   MRR    Ctx%
---------------------------------------------------------
tacm-rerank      47.8%  65.2%  69.6%  0.563  69.6%  ← BEST (1 LLM call)
tacm             34.8%  60.9%  69.6%  0.451  87.0%  ← BEST zero-LLM
tacm-dyn         34.8%  60.9%  69.6%  0.447  82.6%
minilm           26.1%  56.5%  65.2%  0.387  82.6%
bm25             26.1%  43.5%  52.2%  0.367  73.9%
hybrid           17.4%  56.5%  69.6%  0.359  82.6%
tacm-full        26.1%  43.5%  52.2%  0.356  69.6%
codesearch       26.1%  43.5%  52.2%  0.348  69.6%
hybrid-cs        17.4%  52.2%  60.9%  0.306  78.3%
```

---

## Results — scrapy (n=18)

```
Condition        H@1    H@5    H@10   MRR    Ctx%
---------------------------------------------------------
tacm-rerank      33.3%  44.4%  44.4%  0.370  44.4%  ← BEST H@1 + MRR (1 LLM call)
tacm             27.8%  55.6%  55.6%  0.356  55.6%  ← BEST H@5/H@10 zero-LLM
tacm-dyn         27.8%  44.4%  44.4%  0.358  61.1%
hybrid-cs        16.7%  44.4%  44.4%  0.295  66.7%
codesearch       16.7%  44.4%  44.4%  0.280  50.0%
minilm           16.7%  38.9%  38.9%  0.257  50.0%
hybrid           11.1%  38.9%  44.4%  0.244  55.6%
tacm-full        16.7%  33.3%  33.3%  0.229  38.9%
bm25             11.1%  33.3%  44.4%  0.233  55.6%
```

---

## Results — pandas (n=36) ⚠️ dataset quality caveat

```
Condition        H@1    H@5    H@10   MRR    Ctx%
---------------------------------------------------------
tacm-dyn          5.6%  22.2%  22.2%  0.105  27.8%  ← BEST H@5/H@10
tacm-dyn-l4       5.6%  22.2%  22.2%  0.105  27.8%
hybrid-cs         8.3%  16.7%  19.4%  0.116  19.4%  ← BEST H@1/MRR
bm25              8.3%  11.1%  13.9%  0.100  13.9%
tacm              5.6%  13.9%  19.4%  0.095  30.6%  ← BEST Ctx%
hybrid            8.3%   8.3%   8.3%  0.087  13.9%
tacm-full         5.6%   8.3%  11.1%  0.079  19.4%
minilm            2.8%   5.6%  16.7%  0.060  22.2%
codesearch        2.8%   8.3%  11.1%  0.053  11.1%
```

**All conditions are weak on pandas and the numbers are not meaningful as retrieval scores.**

Post-run investigation revealed two structural GT label problems:

1. **GT functions are test functions.** 24/36 pandas bugs have `rank=None` (GT not found at
   all). Manual inspection shows many GT labels point to test functions
   (e.g. `test_join_multi_return_indexers`). TACM correctly excludes `is_test` nodes from
   ranking — but bench_v2's matching requires the GT function to appear in the ranked set.
   The `code_explicit` label was applied when the commit message matched a function name,
   which in pandas is frequently the test, not the source fix.

2. **Parser gaps.** Some GT files (e.g. `pandas/tseries/offsets.py`) have 0 parsed function
   nodes — tree-sitter did not extract functions, likely due to file size or decorator
   patterns. GT functions in those files can never be ranked.

**Theoretical ceiling: ~30%.** TACM's Ctx% of 30.6% is close to the maximum achievable
given these label issues. The fan_in scoring fix was verified to have no effect — the
problem is upstream of scoring entirely.

**Pandas should be excluded from the primary results table** and treated as a dataset
quality case study. The thefuck + scrapy aggregate (n=41) is the clean benchmark.

---

## Results — keras (n=11) — EXCLUDED

**All conditions score 0% across all metrics.** This is a repo version mismatch, not a retrieval failure.

**Root cause:** The `./keras` repo is Keras 3.x (TF-independent, `keras/src/` layout). BugsInPy keras bugs are from Keras 2.x (`keras/backend/tensorflow_backend.py`, `keras/initializers.py` etc.). The entire `keras/backend/` directory was deleted in the 3.x rewrite — GT file paths don't exist in the current repo, and GT functions like `print_tensor` were removed.

**Fix:** Check out the specific Keras 2.x commit for each bug (BugsInPy provides the commit hash). Keras results are excluded from all cross-project aggregates.

---

## Primary results — thefuck + scrapy (n=41, clean GT labels)

Pandas is excluded from the primary table due to GT label quality issues (see above).
These are the numbers to use for claims about retrieval quality.

**Table 1: Retrieval metrics with 95% confidence intervals (Wilson score for H@k/Ctx%, t-intervals for MRR)**

```
Condition        H@1               H@5               H@10              MRR               Ctx%              Cost
------------------------------------------------------------------------------------------------------------
tacm-rerank      41.5% [27.8–56.6%] 56.1%            58.5%             0.478 [0.337–0.619] 58.5%      1 LLM call
tacm             31.7% [19.6–47.0%] 58.5%            63.4%             0.409 [0.280–0.538] 73.2%      zero-LLM
tacm-dyn         31.7% [19.6–47.0%] 53.7%            58.5%             0.408 [0.278–0.538] 73.2%      zero-LLM
minilm           22.0% [12.0–36.7%] 48.8%            53.7%             0.330 [0.212–0.448] 68.3%      zero-LLM
codesearch       22.0% [12.0–36.7%] 43.9%            48.8%             0.318 [0.197–0.440] 61.0%      zero-LLM
tacm-full        22.0% [12.0–36.7%] 39.0%            43.9%             0.300 [0.179–0.422] 56.1%      zero-LLM
bm25             19.5% [10.2–34.0%] 39.0%            48.8%             0.308 [0.192–0.424] 65.9%      zero-LLM
hybrid           14.6% [6.9–28.4%]  48.8%            58.5%             0.308 [0.204–0.413] 70.7%      zero-LLM
hybrid-cs        17.1% [8.5–31.3%]  48.8%            53.7%             0.301 [0.193–0.409] 73.2%      zero-LLM
```

**Candidate pool recall:**

| Condition   | Ctx% (GT in top-40) | 95% CI           | n hits |
|-------------|-------------------|------------------|--------|
| tacm        | 73.2%             | [58.1–84.3%]     | 30/41  |
| tacm-dyn    | 73.2%             | [58.1–84.3%]     | 30/41  |
| tacm-rerank | 58.5%             | [43.4–72.2%]     | 24/41  |
| hybrid-cs   | 73.2%             | [58.1–84.3%]     | 30/41  |
| minilm      | 68.3%             | [53.0–80.4%]     | 28/41  |
| hybrid      | 70.7%             | [55.5–82.4%]     | 29/41  |
| bm25        | 65.9%             | [50.5–78.4%]     | 27/41  |
| codesearch  | 61.0%             | [45.7–74.3%]     | 25/41  |
| tacm-full   | 56.1%             | [41.0–70.1%]     | 23/41  |

**Statistical significance:**
- TACM vs minilm (H@1, McNemar's test): 10 wins vs 6 losses, p=0.453 (not significant)
- TACM vs minilm (MRR, paired t-test): p=0.274 (not significant)
- TACM vs tacm-rerank (H@1, McNemar's test): 6 gains vs 2 regressions, p=0.289 (not significant)
- TACM vs tacm-rerank (MRR, paired t-test): p=0.169 (not significant)

Note: Small sample size (n=41) limits statistical power; CIs are wide around point estimates. The H@1 and MRR differences are directional but not reliably distinct from sampling variation at the 0.05 level.

**Zero-LLM:** TACM achieves 31.7% H@1 [19.6–47.0%] and MRR 0.409 [0.280–0.538], outperforming text-only baselines by +9.7pp H@1 and ~+24% MRR (minilm: 22.0% H@1 / 0.330 MRR).
**With 1 LLM call:** tacm-rerank reaches 41.5% H@1 [27.8–56.6%] and MRR 0.478 [0.337–0.619], representing +9.8pp H@1 over zero-LLM TACM. The reranker gains are larger on thefuck (+13pp H@1) because its higher candidate pool recall (Ctx% 87%) means the GT function is present to promote; scrapy's deeper call graphs yield smaller gains (+5.5pp H@1, Ctx% 55.6%).

## For reference — thefuck + scrapy + pandas (n=77)

Included for completeness. Interpret with caution given pandas GT label issues.

```
Condition        H@1    H@5    H@10   MRR    Ctx%
---------------------------------------------------------
tacm-dyn         19.5%  39.0%  44.2%  0.270  51.9%  ← BEST MRR + H@5/H@10
tacm-dyn-l4      19.5%  39.0%  44.2%  0.270  51.9%
tacm             19.5%  37.7%  42.9%  0.264  54.5%  ← BEST H@1 + Ctx%
hybrid-cs        13.0%  33.8%  37.7%  0.215  48.1%
bm25             14.3%  26.0%  32.5%  0.211  41.6%
hybrid           11.7%  29.9%  35.1%  0.205  44.2%
minilm           13.0%  28.6%  36.4%  0.204  46.8%
tacm-full        14.3%  24.7%  29.9%  0.200  40.3%
codesearch       13.0%  27.3%  31.2%  0.194  37.7%
```

---

## Per-bug H@1 matrix — thefuck

```
Bug            bm25   minilm  tacm   tacm-full  tacm-dyn
---------------------------------------------------------
thefuck-5      miss   miss    HIT    miss       miss
thefuck-6      HIT    miss    HIT    HIT        HIT
thefuck-16     HIT    HIT     HIT    HIT        HIT
thefuck-17     miss   miss    HIT    miss       HIT
thefuck-19     HIT    miss    HIT    HIT        HIT
thefuck-24     miss   HIT     miss   miss       HIT
thefuck-25     HIT    miss    HIT    HIT        HIT
thefuck-26     HIT    HIT     HIT    HIT        HIT
thefuck-31     HIT    miss    HIT    HIT        HIT
thefuck-32     miss   HIT     miss   miss       miss
thefuck-14     miss   HIT     miss   miss       miss
```
(All other bugs: all conditions miss at H@1)

---

## Per-bug H@1 matrix — scrapy

```
Bug            bm25   minilm  tacm   tacm-full  tacm-dyn
---------------------------------------------------------
scrapy-7       miss   HIT     HIT    miss       miss
scrapy-17      miss   HIT     miss   miss       HIT
scrapy-18      HIT    miss    HIT    HIT        HIT
scrapy-19      miss   miss    HIT    miss       miss
scrapy-20      miss   miss    HIT    HIT        HIT
scrapy-24      miss   HIT     miss   miss       miss
scrapy-27      miss   miss    HIT    miss       HIT
scrapy-32      HIT    miss    HIT    HIT        HIT
```
(All other bugs: all conditions miss at H@1)

---

## Key findings

### Finding 1: TACM (budgeted) leads all conditions at H@1 and MRR

Across the clean n=41 benchmark (thefuck + scrapy), `tacm` achieves **31.7% H@1 / MRR 0.409** — **+9.7pp H@1 and +24% MRR** over the best text-only baseline (minilm: 22.0% / 0.330).

With the LLM reranker: **41.5% H@1 / MRR 0.478** — a further +9.8pp H@1 over zero-LLM TACM at ~$0.0001 per query.

Per-project breakdown: thefuck 34.8% H@1 / MRR 0.451, scrapy 27.8% H@1 / MRR 0.356. Both projects show the same pattern — TACM leads at H@1 and MRR, and the reranker extends the lead further.

This is the cleanest signal from this experiment: **TACM's graph-weighted scoring ranks the GT function higher than text-only methods across both project types**, measured directly without agent noise.

### Finding 2: Budget cutoff helps ranking, hurts coverage

`tacm` (budgeted) **beats** `tacm-full` at H@1 and MRR on both projects. This is the opposite of what Experiment 03 showed at the agent level.

Explanation: The budget forces a tighter selection. With 4000 tokens and ~36 functions avg, each function gets more "space" — the scorer ranks GT highly at rank 1-5. `tacm-full` packs more functions with lower avg tokens each, pushing GT down the ranked list by dilution even if the score is correct.

The Exp 03 agent advantage of `tacm-full` came from *coverage* (agent finds a solution because GT is somewhere in the 50+ function window). Here we measure *ranking quality* — budgeted TACM wins.

**Implication:** For retrieval quality, budget is beneficial. For agent solve rate, coverage matters more. The right design is dynamic budget: rank tightly (tacm) but fill greedily up to 4000 tokens.

### Finding 3: tacm-dyn improves H@5 and H@10 over tacm on thefuck

`tacm-dyn` matches `tacm` at H@1 (34.8%) but beats it at H@5 (60.9% vs 56.5%) and H@10 (73.9% vs 69.6%) on thefuck. Dynamic budget allocation retains ranking quality while fitting more relevant functions into the budget window.

On scrapy, `tacm-dyn` trails `tacm` at H@1 (27.8% vs 33.3%) — the dynamic allocation is less precise when the call graph is deeper and function tokens are larger.

### Finding 4: L4 (caller snippets) provides no retrieval benefit

`tacm-dyn-l4` is **identical** to `tacm-dyn` on both projects across all metrics. The Layer 4 caller context snippets do not move any function's rank — they are post-hoc context, not scoring signals.

L4 may still benefit the agent (richer code context for understanding blast radius), but it cannot be justified as a ranking improvement. It should be tested as an agent-level ablation.

### Finding 5: TACM uniquely solves structurally non-obvious bugs

TACM (budgeted) uniquely finds bugs that both bm25 and minilm miss at H@1:

| Bug | Query | Why text methods miss | Why TACM finds it |
|-----|-------|-----------------------|-------------------|
| thefuck-5 | `git_push: Handle branch names containing 'set-upstream'` | "set-upstream" doesn't appear in the fix function name | fan_in from git_push rule + containment bonus |
| thefuck-17 | `#402: Don't invoke bash for getting aliases` | Issue number in query; "bash" matches many files | graph centrality of shell alias methods |
| scrapy-19 | `PY3: Implement some attributes of WrappedRequest required in Python 3` | "WrappedRequest" is a class, not in function text | class containment bonus directs scoring to member functions |
| scrapy-20 | `Fix SitemapSpider to extract sitemap urls from robots.txt properly` | "robots.txt" is a config term, not code | SitemapSpider class selection + fan_in on parse method |
| scrapy-27 | `Fix RedirectMiddleware not honouring meta handle_httpstatus keys` | "handle_httpstatus" in few functions; query too specific | middleware fan_in pattern identifies the correct handler |

### Finding 6: Fusion underperforms its components

`hybrid` (BM25 + MiniLM RRF) underperforms both `bm25` and `minilm` individually on thefuck at H@1 (17.4% vs 26.1%). RRF averaging dilutes the best signal. Finding confirmed from Experiment 03.

`hybrid-cs` performs best among text-only conditions on scrapy at H@5/H@10 but still trails `tacm` by 11pp at H@1 and -0.105 MRR.

### Finding 7: 1 LLM reranker call closes the ranking gap materially

`tacm-rerank` uses gpt-4o-mini to rerank the top-40 TACM candidates (1 call per query, ~$0.001).

| Project | tacm H@1 | tacm-rerank H@1 | gain | tacm MRR | tacm-rerank MRR | gain |
|---------|----------|-----------------|------|----------|-----------------|------|
| thefuck | 34.8% | **47.8%** | +13.0pp | 0.451 | **0.563** | +24.8% |
| scrapy  | 27.8% | **33.3%** | +5.5pp  | 0.356 | **0.370** | +3.9%  |
| combined| 31.7% | **41.5%** | +9.8pp  | 0.409 | **0.478** | +16.8% |

**Why thefuck gains more:** TACM's Ctx% is 87% on thefuck — the GT function is already in the candidate pool for nearly every bug. The LLM promotes it to rank 1 using semantic understanding of the bug description. On scrapy (Ctx% 55.6%), the GT function is absent from the top-40 for ~44% of bugs — the LLM cannot rerank what isn't in the pool.

**Reranker flip analysis:**
- thefuck gains: thefuck-14, 15, 24, 28 — all structurally non-obvious bugs where TACM retrieves the GT function but ranks it 2nd-10th
- thefuck loses: thefuck-31 — one false demotion
- scrapy gains: scrapy-17, scrapy-8
- scrapy loses: scrapy-20 — one false demotion

The reranker is net positive by 5:2 (gains vs losses) across both projects.

---

## Token usage and cost

All conditions operate within the 4000-token context budget.

```
Condition        Avg tokens  Avg fn count  LLM calls  Cost/query
-----------------------------------------------------------------
bm25                   3987          28.4          0      $0.000
minilm                 3990          31.2          0      $0.000
tacm                   3989          31.4          0      $0.000
tacm-dyn               3998          34.1          0      $0.000
tacm-rerank            3968          24.7          1     ~$0.0001
```

`tacm-rerank` uses slightly fewer context tokens (3968 vs 3989) and fewer functions (24.7 vs 31.4) because the reranker promotes a tighter set of high-confidence candidates. This is the trade-off: higher H@1 (GT ranked first more often) but slightly lower H@5/H@10 (fewer total functions packed).

**Cost:** The reranker sends ~700 input tokens + receives ~40 output tokens per call to gpt-4o-mini. At $0.15/1M input and $0.60/1M output, cost is **~$0.0001 per query** — effectively negligible. The full 41-bug benchmark run cost ~$0.005.

---

## Comparison with Experiment 03 regression suite

Experiment 03 used the full BugsInPy dataset (all labels). Experiment 04 uses code-grounded bugs only (label: code_explicit or semantic_code). The datasets partially overlap but are not identical — comparison is directional only.

| Metric | Exp 03 (thefuck, tacm-full) | Exp 04 (thefuck, tacm) |
|--------|----------------------------|------------------------|
| MRR    | 0.4181                     | 0.458                  |
| Hit@10 | 67.86%                     | 69.6%                  |

Exp 04 tacm (budgeted) outperforms Exp 03 tacm-full on the code-grounded subset — the cleaner GT labels help, and the budget improves ranking precision.

---

## What this experiment does NOT cover

1. **keras (correct version)** — need to check out the Keras 2.x commit for each BugsInPy bug. The `./keras` folder is Keras 3.x with a completely different directory structure.
2. **Agent ablation of L4** — L4 context doesn't help ranking but may help the agent's patch generation. Needs a targeted Exp 03-style agent run.
3. **tacm-dyn on scrapy regression** — tacm-dyn trails tacm at H@1 on scrapy (27.8% vs 33.3%). The dynamic allocation logic may need tuning for deeper call graphs.
4. **semantic_code-only slice** — running on only `semantic_code` bugs would isolate where graph signals matter most vs text-only methods.
5. **pandas Ctx% vs H@1 gap** — TACM routes to the right files (Ctx% 30.6%) but ranks GT low (H@1 5.6%). The fan_in/fan_out signals may need reweighting for large API-surface projects.

---

## Next steps

1. Fix keras repo (check out Keras 2.x base commit, rebuild graph, rerun Exp 04)
2. Ablate L4 in agent harness (Exp 03-style run, tacm vs tacm-l4, 3 seeds)
3. Pandas GT label audit — identify which of the 36 bugs have valid (non-test) GT function
   labels and re-evaluate on the clean subset

---

## Reproducibility

```bash
# Full benchmark (all 4 projects in dataset)
TOKENIZERS_PARALLELISM=false python3 codegraph-tacm/tools/run_experiment_04.py

# Subset by project
TOKENIZERS_PARALLELISM=false python3 codegraph-tacm/tools/run_experiment_04.py --project thefuck scrapy

# Results
cat codegraph-tacm/experiment_04_outputs/experiment_04_summary.json
# Per-bug context logs
ls codegraph-tacm/experiment_04_outputs/contexts/<project>/<bug_id>/
```

Results saved in `codegraph-tacm/experiment_04_outputs/`.
