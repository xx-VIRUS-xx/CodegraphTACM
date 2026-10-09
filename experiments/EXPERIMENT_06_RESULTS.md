# EXPERIMENT_06 RESULTS — Query-side identifier expansion: no Pareto win across a full scale sweep

**Date:** 2026-04-22 (initial) / 2026-04-23 (scale sweep added)
**Status:** Complete (n=47 paired Python instances; default-scale 0.25 run + full sweep over `identifier_exact_scale` ∈ {0.05, 0.10, 0.15, 0.20, 0.25} at `--top-k 5`; `bm25`/`hybrid` re-benchmarked as reference and match Exp 05 exactly)
**Dataset:** SWE-bench Lite + Multilingual Python-only (same 47 instances as Exp 05)
**Raw results (k=5, paired with Exp 05):** [`agent_results/zero_cost_executable_benchmark_20260422_210007.json`](../agent_results/zero_cost_executable_benchmark_20260422_210007.json)
**Baseline (Exp 05, k=5):** [`agent_results/zero_cost_executable_benchmark_20260422_103746.json`](../agent_results/zero_cost_executable_benchmark_20260422_103746.json)

> **Note on an earlier k=20 run.** An earlier version of this doc reported MRR 0.215 for TACM-PPR based on a run at `--top-k 20` ([`zero_cost_executable_benchmark_20260422_143421.json`](../agent_results/zero_cost_executable_benchmark_20260422_143421.json)). That run packed a deeper candidate tail and inflated Hit@10/File%/Tok numbers that were not apples-to-apples with Exp 05's k=5 budget. The table below is the corrected paired comparison; the k=20 file is preserved for reference only.

---

## Primary results — SWE-bench Lite + Multilingual (n=47, Python, k=5 paired)

**Table 1: Retrieval metrics with 95% CIs on MRR (percentile bootstrap, 5000 resamples, seed=7)**

```
Condition            MRR    95% CI            Hit@1  Hit@5  File%   Tok   p50ms
-------------------------------------------------------------------------------
tacm-ppr (Exp 05)   0.198  [0.110, 0.297]     10.6%  36.2%  59.6%  5032   2844
tacm-ppr (Exp 06)   0.189  [0.094, 0.293]     12.8%  29.8%  59.6%  4805   3049
hybrid   (Exp 05)   0.192  [0.096, 0.298]     14.9%  27.7%  59.6%  2673  25085
tacm     (Exp 06)   0.172  [0.082, 0.271]     10.6%  27.7%  59.6%  4782   2946
tacm     (Exp 05)   0.165  [0.089, 0.253]      6.4%  34.0%  53.2%  5118   3036
bm25     (Exp 05)   0.148  [0.070, 0.239]      8.5%  27.7%  59.6%  3271    694
```

**Statistical significance (paired bootstrap, one-sided, 5000 resamples, seed=42):**

| Comparison | Δ MRR | p-value |
|---|---|---|
| tacm (Exp 06) > tacm (Exp 05) | **+0.006** | 0.419 |
| tacm-ppr (Exp 06) > tacm-ppr (Exp 05) | **−0.009** | 0.656 |
| tacm-ppr (Exp 06) > hybrid (Exp 05) | −0.003 | 0.510 |
| tacm-ppr (Exp 06) > bm25 (Exp 05) | +0.041 | 0.103 |
| tacm (Exp 06) > bm25 (Exp 05) | +0.024 | 0.212 |
| tacm-ppr (Exp 06) > tacm (Exp 06) | +0.018 | 0.092 |

**Headline:** At the correctly-paired `k=5` budget, identifier expansion **does not produce a statistically significant MRR lift**. TACM moves +0.006 (p=0.42, within noise). TACM-PPR moves **−0.009** (worse). The intervention is **not the pure-algo win** the earlier k=20 draft suggested.

Hit@1 rises for both conditions (TACM 6.4→10.6%, TACM-PPR 10.6→12.8%) but Hit@5 **falls** (TACM 34.0→27.7%, TACM-PPR 36.2→29.8%). The identifier-exact bonus promotes correctly-named siblings into rank 1–2 on some queries but also demotes correct mid-range hits out of top-5 on others. The redistribution is roughly zero-sum at Hit@5 and slightly negative overall.

---

## Head-to-head — tacm-ppr Exp 05 → Exp 06 (paired, k=5)

```
helped: 1    hurt: 6    tied: 40
```

**Win:**

| Instance | Rank Exp 05 → Exp 06 |
|---|---|
| pydata__xarray-4094 | 3 → **1** (Hybrid parity achieved) |

**Losses:**

| Instance | Rank Exp 05 → Exp 06 |
|---|---|
| pydata__xarray-3364 | 3 → **MISS** |
| pallets__flask-4045 | 4 → **MISS** |
| django__django-11019 | 5 → **MISS** |
| mwaskom__seaborn-3407 | 3 → 4 |
| mwaskom__seaborn-3190 | 4 → 5 |
| pytest-dev__pytest-11148 | 2 → 4 |

Three of the six losses are **pool dropouts** (the GT fell outside top-5 entirely). These are the instances where the k=20 run's better-looking numbers came from: at k=20 the GT was still within the expanded candidate pool, just demoted into rank 8–17. The identifier bonus is firing on sibling nodes and pushing the GT past rank 5.

---

## Seam tracking — Exp 05 Hybrid-wins-TACM-loses

| Instance | Hybrid | TACM-PPR Exp 05 | TACM-PPR Exp 06 (k=5) | Status |
|---|---|---|---|---|
| pydata__xarray-4094 | 1 | 3 | **1** | ✅ closed |
| scikit-learn__scikit-learn-10297 | 2 | MISS (7 @k=20) | MISS | ➖ unchanged at k=5 |
| django__django-11001 | 3 | MISS | MISS | ➖ unchanged |

Only the xarray seam actually closes at k=5. The sklearn case was never in top-5 under Exp 05 either — the "rank 7" figure in the Exp 05 doc was from its top-K=20 diagnostic. At the benchmark budget of k=5, it remained a miss across all TACM variants.

---

## Per-repo breakdown (k=5 paired)

Columns: `t5/p5 = Exp 05 tacm / tacm-ppr MRR`, `t6/p6 = Exp 06`, `Δppr = p6 − p5`.

```
repo                      N   bm25    hyb     t5     p5     t6     p6     Δppr
--------------------------------------------------------------------------------
pydata/xarray             4  0.250  0.250  0.167  0.146  0.250  0.250   +0.104
astropy/astropy           4  0.333  0.333  0.250  0.375  0.250  0.375    0.000
matplotlib/matplotlib     4  0.146  0.333  0.250  0.375  0.375  0.375    0.000
psf/requests              4  0.125  0.250  0.133  0.175  0.125  0.175    0.000
pylint-dev/pylint         4  0.125  0.050  0.333  0.375  0.333  0.375    0.000
scikit-learn/scikit-learn 4  0.250  0.375  0.250  0.250  0.250  0.250    0.000
sphinx-doc/sphinx         4  0.000  0.000  0.000  0.000  0.000  0.000    0.000
sympy/sympy               4  0.000  0.000  0.000  0.000  0.000  0.000    0.000
mwaskom/seaborn           4  0.083  0.000  0.100  0.146  0.100  0.113   −0.033
django/django             4  0.000  0.083  0.000  0.050  0.000  0.000   −0.050
pytest-dev/pytest         4  0.050  0.083  0.125  0.125  0.083  0.062   −0.062
pallets/flask             3  0.500  0.667  0.444  0.417  0.333  0.333   −0.083
```

One repo (xarray) accounts for all the aggregate TACM-PPR gain and is fully cancelled by four regressing repos (seaborn, django, pytest, flask). Nine of twelve repos are flat or negative. The xarray lift alone isn't enough to move the aggregate MRR meaningfully.

---

## Miss taxonomy

```
Condition     hit    right_file_wrong_fn    ranked_outside_k    gt_not_in_pool
------------------------------------------------------------------------------
tacm          28%                      0%                 68%                4%
tacm-ppr      30%                      0%                 66%                4%
```

`gt_not_in_pool` unchanged (4% = 2/47 — upstream candidate pool). `ranked_outside_k` rose from Exp 05's 49% to 66-68% — consistent with the "pool dropouts" pattern above.

---

## Key findings

### Finding 1: The headline MRR lift from the earlier k=20 run does not reproduce at k=5

At `--top-k 20` the TACM-PPR MRR was 0.215 with Hit@10 42.6% and File% 77%. At the correctly-paired `--top-k 5`, it is 0.189 / Hit@5 29.8% / File% 59.6%. **The earlier numbers measured a different experiment** (richer candidate tail, different packer behaviour) and were not apples-to-apples with Exp 05. This corrected run shows no pure-algo win over Exp 05 at the Hybrid-paired budget.

### Finding 2: Identifier expansion trades Hit@5 for Hit@1 — net negative on MRR for TACM-PPR

| | TACM Exp 05 | TACM Exp 06 | TACM-PPR Exp 05 | TACM-PPR Exp 06 |
|---|---|---|---|---|
| Hit@1 | 6.4% | **10.6%** | 10.6% | **12.8%** |
| Hit@5 | **34.0%** | 27.7% | **36.2%** | 29.8% |
| MRR | 0.165 | 0.172 | **0.198** | 0.189 |

For TACM (no PPR), Hit@1 gain outweighs Hit@5 loss and MRR climbs slightly. For TACM-PPR (which already had a strong Hit@5 signal from the structural channel), the identifier-exact bonus competes with PPR's rank-2/3/4 placements and demotes them, costing more than it gains. The intervention interacts badly with the Exp 05 gate.

### Finding 3: Three Exp 05 hits became pool dropouts

`pallets__flask-4045` (4→MISS), `pydata__xarray-3364` (3→MISS), `django__django-11019` (5→MISS). All three were cleanly in top-5 under Exp 05 and are now outside the top-5 pool. This is the core mechanism behind the Hit@5 regression: a bonus of 0.25 magnitude is large enough to reshuffle near-tied siblings past rank 5.

### Finding 4: The one durable win is pydata__xarray-4094

Rank 3 → 1 for both TACM and TACM-PPR. The query extracts unambiguous identifiers (`to_xarray`, `MultiIndex`, `Dataset`) and the target function is the only one matching all three. This is the cleanest case the expansion was designed for, and it works as intended.

### Finding 5: The identifier_exact_scale = 0.25 default is too aggressive

Three pool dropouts and four net-negative repos out of twelve suggest the bonus is dominating the combined score in ways that aren't gated by query structure. Leading candidates for a better default:

- **Scale sweep.** 0.25 was chosen by intuition, not tuning. A sweep over {0.05, 0.10, 0.15, 0.20} would likely find a setting that keeps the Hit@1 gains without the Hit@5 losses.
- **Multi-identifier gate.** Require `len(q_idents) >= 2` before activating the bonus. Single-identifier queries are where sibling-class ambiguity hurts most.
- **Dampen under high-density PPR.** The bonus competes most with PPR on call-graph-rich repos. Scaling the identifier bonus down when PPR density is already saturated would let PPR's stronger signal keep its top-5 placements.

### Finding 6: Expansion is still useful as a Hit@1 lever

Both conditions gained +2–4pp at Hit@1. For downstream use cases that read only the top-1 candidate (not top-5 context for an agent), expansion is a net win. For the top-K retrieval use case that feeds an agent or reranker, it is not.

### Finding 7: Latency and tokens genuinely unchanged at matched k

| | Exp 05 tacm-ppr | Exp 06 tacm-ppr |
|---|---|---|
| Tok | 5032 | 4805 |
| p50 ms | 2844 | 3049 |

The +200 ms latency comes from the extra BM25 variants and the identifier-exact pass; the token delta is noise. Claims of latency/token parity from the earlier draft hold.

---

## Scale sweep — `identifier_exact_scale` ∈ {0.05, 0.10, 0.15, 0.20, 0.25}

Run 2026-04-23. Each scale is a full 47-instance rerun of `tacm` and `tacm-ppr` at `--top-k 5`; `bm25`/`hybrid` re-benchmarked once as a reference (results match Exp 05 exactly, confirming the feature is gated).

**Table 2: Retrieval metrics across the full scale sweep (n=47, k=5)**

```
condition       scale    MRR     Hit@1   Hit@5
------------------------------------------------
bm25            —       0.148   0.085   0.277
hybrid          —       0.192   0.149   0.277

tacm            0.00 *  0.165   0.064   0.340    ← Exp 05 baseline
tacm            0.05    0.159   0.064   0.319
tacm            0.10    0.160   0.085   0.298
tacm            0.15    0.170   0.085   0.319
tacm            0.20    0.161   0.085   0.298
tacm            0.25    0.175   0.106   0.298

tacm-ppr        0.00 *  0.198   0.106   0.362    ← Exp 05 baseline
tacm-ppr        0.05    0.172   0.085   0.319
tacm-ppr        0.10    0.177   0.106   0.298
tacm-ppr        0.15    0.187   0.106   0.340
tacm-ppr        0.20    0.186   0.128   0.298
tacm-ppr        0.25    0.198   0.128   0.319
```

`* scale 0.00` = `identifier_expansion_enabled=False` (Exp 05 numbers, no rerun).

Raw JSONs: [0.05](../agent_results/zero_cost_executable_benchmark_20260422_220903.json) · [0.10](../agent_results/zero_cost_executable_benchmark_20260422_224402.json) · [0.15](../agent_results/zero_cost_executable_benchmark_20260422_231748.json) · [0.20](../agent_results/zero_cost_executable_benchmark_20260422_235107.json) · [0.25](../agent_results/zero_cost_executable_benchmark_20260423_002416.json) · [bm25/hybrid reference](../agent_results/zero_cost_executable_benchmark_20260423_011707.json).

### What the sweep shows

1. **No scale recovers the Exp 05 TACM-PPR MRR of 0.198.** Best is scale 0.25 at **0.1975** — statistically indistinguishable but not an improvement. Every other scale is strictly worse on MRR.
2. **Hit@1 climbs monotonically-ish with scale.** TACM-PPR goes 10.6% → 12.8% at scale ≥ 0.20. TACM reaches 10.6% at scale 0.25.
3. **Hit@5 never recovers the 36.2% baseline.** Best expansion setting is scale 0.15 at **34.0%**. Scales ≥ 0.20 drop Hit@5 to 29.8%.
4. **No Pareto-optimal scale exists.** The entire Pareto frontier is: baseline dominates on Hit@5/MRR, scale 0.25 dominates on Hit@1. Every non-baseline scale is worse on ≥1 metric vs. baseline.
5. **The TACM-PPR per-instance trace confirms the mechanism.** At scale 0.15: 0 wins, 3 losses (all top-5 demotions). At scale 0.25: 2 wins (`xarray-4094` 3→1, `flask-4045` 4→3), 4 losses (3 pool dropouts + 1 demotion). The bonus is zero-sum-to-negative across the instance set — it moves ranks around but doesn't create new hits.

### Best scale by criterion

| Criterion | Winner | Condition | Value |
|---|---|---|---|
| MRR | **baseline (scale 0.00)** | tacm-ppr | 0.198 |
| Hit@1 | scale 0.20 or 0.25 | tacm-ppr | 12.8% |
| Hit@5 | **baseline (scale 0.00)** | tacm-ppr | 36.2% |
| Hybrid parity on Hit@1 | — | — | unreached (Hybrid 14.9%) |

---

## What this experiment does NOT cover

1. ~~**Scale sweep on `identifier_exact_scale`.**~~ Covered above — no scale is a net win on MRR.
2. **Multi-identifier gate** (`len(q_idents) >= 2` before firing the bonus). Untested. The three pool dropouts (`flask-4045`, `xarray-3364`, `django-11019`) should be inspected to see if their queries have ≥2 extracted identifiers; if they do, a count gate won't save them.
3. **PPR-density-aware damping.** The Exp 05 adaptive-PPR gate scales PPR by seed density. A symmetric move would scale the identifier bonus *down* when PPR density is high, letting PPR keep its top-5 placements on call-graph-rich repos. Untested.
4. **Per-repo scale selection.** Repos with prose-heavy queries (sphinx, sympy) get no signal from expansion; repos with identifier-rich queries (xarray, requests) benefit. A repo-adaptive scale might beat the global sweep winner.
5. **Hybrid rerun with expansion.** Hybrid was not modified; its numbers are unchanged by construction. Porting the expansion signal into Hybrid is a separate experiment.

---

## Verdict

**Identifier expansion does not produce a Pareto improvement at any tested scale.** The scale sweep over {0.05, 0.10, 0.15, 0.20, 0.25} confirms: baseline (expansion off) beats or ties every scale on MRR and Hit@5; the only thing expansion buys is +2pp Hit@1 at high scales (0.20–0.25), paid for with −3 to −7pp Hit@5. For an agent-feeding retrieval use case, expansion is a **net regression** and should stay off by default.

The one durable mechanism the experiment uncovered — query-side identifier extraction via [`_extract_query_identifiers`](../tacm_v2/selector/scoring.py) — is worth keeping in the codebase as a building block. It just doesn't earn its keep as an additive top-5 bonus at any tested scale.

**Recommended default:** `identifier_expansion_enabled = False`. Leave the knob in place for Hit@1-specialised use cases (scale 0.25 is the sweet spot there: +2pp Hit@1 vs. baseline, matching Hybrid Hit@5 within noise) and as scaffolding for a future density-damped or repo-adaptive variant.

**What to try next (not in this experiment):**
- Density-damped expansion (expand *less* when PPR density is high).
- Qname-prefix trie signal for dotted-path queries (new signal, not a stronger version of the existing one).
- Hit@1-tuned reranker that consumes top-5 as a candidate pool and uses the expansion signal only at the final tie-break stage.

---

## Reproducibility

```bash
# run from the repository root

# Paired k=5 rerun at default scale 0.25 (this experiment's canonical numbers)
TOKENIZERS_PARALLELISM=false python3 zero_cost_runner.py \
    --retriever tacm,tacm-ppr \
    --dataset executable_benchmark.json \
    --python-only \
    --no-exec \
    --top-k 5

# Scale sweep (added 2026-04-23)
for s in 0.05 0.10 0.15 0.20 0.25; do
  TACM_IDENT_SCALE=$s TOKENIZERS_PARALLELISM=false python3 zero_cost_runner.py \
      --retriever tacm,tacm-ppr \
      --dataset executable_benchmark.json \
      --python-only --no-exec --top-k 5
done

# bm25+hybrid reference (confirms feature is gated — results match Exp 05)
TOKENIZERS_PARALLELISM=false python3 zero_cost_runner.py \
    --retriever bm25,hybrid \
    --dataset executable_benchmark.json \
    --python-only --no-exec --top-k 5
```

Raw JSON (default-scale run): [`zero_cost_executable_benchmark_20260422_210007.json`](../agent_results/zero_cost_executable_benchmark_20260422_210007.json). Sweep JSONs linked inline in Table 2.

Config knobs in [`tacm_v2/selector/config.py`](../tacm_v2/selector/config.py):

- `identifier_expansion_enabled: bool = False` (default; set True for this experiment)
- `identifier_exact_scale: float = 0.25` (default for this experiment; **swept {0.05–0.25}**; no scale was Pareto-optimal — keeping default False)

The `TACM_IDENT_SCALE` env var in [`zero_cost_runner.py`](../zero_cost_runner.py) overrides the scale for sweep reproducibility (scale 0 → expansion disabled).

Implementation in [`tacm_v2/selector/scoring.py`](../tacm_v2/selector/scoring.py): `_extract_query_identifiers`, `compute_identifier_exact`, `_cascading_bm25` identifier-blob variants.

To disable and reproduce Exp 05 numbers, revert the `zero_cost_runner.py` config block to `SelectorConfig(ppr_enabled=True) if condition == "tacm-ppr" else DEFAULT_CONFIG`.
