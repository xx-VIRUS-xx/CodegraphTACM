# EXPERIMENT_05 — Adaptive PPR: Density-Gated Structural Signal

## Goal

Experiment 05 asks a narrower question than prior runs:

**When does the Personalized PageRank (PPR) channel help, and when does it hurt — and can we gate it adaptively without any ML layer?**

Experiment 04 established that budgeted TACM beats text-only baselines on retrieval quality. The follow-on SWE-bench run on 2026-04-22 (`zero_cost_executable_benchmark_20260422_012137.json`) then showed that flat PPR lifts TACM (MRR 0.170 → 0.189, Hit@5 28% → 32%), but **Hybrid (RRF of BM25 + MiniLM) still won outright at MRR 0.222** — the gap concentrated on shallow-library repos (flask, xarray, sklearn).

The analyzer (`analyze_zcr.py`) isolated the mechanism:

- On **call-graph-rich** repos (pylint, seaborn, sphinx) the BM25 seed set has non-trivial CALLS fan-out, so PPR's random walk finds structurally central neighbors and promotes the true target.
- On **shallow-library** repos (flask, xarray, sklearn) the seeds have near-zero out-degree. PPR mass gets stuck on the teleport vector, which is effectively BM25 — but rank normalisation adds noise that demotes the correct hit.

Experiment 05 introduces an **adaptive density gate**: scale the PPR contribution continuously with the average out-degree of the BM25 seed set, so the structural signal is used only where the graph actually supports it. No learning, no dense encoder, no extra latency budget.

## Hypothesis

If we multiply the per-query PPR bonus by a density factor in `[ppr_density_min_scale, 1.0]` — linearly ramping from 0 at avg seed out-degree = 0 to full weight at saturation (default 6.0) — then:

1. The **TACM-PPR → Hybrid gap** on shallow-library repos should close, because PPR no longer injects ranking noise when seeds have no neighborhood to explore.
2. The **PPR lift on call-graph-rich repos** should be preserved, because saturation is reached quickly for seeds with real fan-out.
3. Aggregate MRR should move up (or at worst stay flat) with no regression vs flat PPR, and paired-bootstrap p-values vs vanilla TACM should remain significant.

## Design principle

Zero ML. Zero extra latency beyond looking up `len(out_links[idx])` for a handful of seed nodes. The gate is a single multiplicative scalar on the PPR channel; all other scoring stays identical to Experiment 04's TACM.

## Dataset

Same as the 2026-04-22 baseline run so results are paired and directly comparable:

- SWE-bench Lite + Multilingual, Python instances only: **n = 47**
- 12 repositories, covering shallow-library (flask, xarray, sklearn, requests) and call-graph-rich (pylint, seaborn, sphinx, django, pytest) code
- Seeds and instance ordering pinned; paired bootstrap over the same 47 instances

Raw results (Exp 05): [`agent_results/zero_cost_executable_benchmark_20260422_103746.json`](../agent_results/zero_cost_executable_benchmark_20260422_103746.json)
Raw baseline (flat PPR): [`agent_results/zero_cost_executable_benchmark_20260422_012137.json`](../agent_results/zero_cost_executable_benchmark_20260422_012137.json)

## Systems

Four conditions, one budget (4000 tokens), paired on instance id:

- `bm25` — lexical baseline (Okapi BM25 over function bodies, identifier-tokenised)
- `hybrid` — RRF of BM25 + MiniLM (this is the bar to beat; uses a dense encoder)
- `tacm` — vanilla TACM (3-layer weighted graph scorer, no PPR)
- `tacm-ppr` — TACM + **adaptive density-gated PPR** (Experiment 05's new condition)

`tacm-ppr` is the new default behind `ppr_enabled=True`. Flat (un-gated) PPR is recovered by setting `ppr_density_enabled=False`.

## Metrics

Function-ranking (strict GT match = name + file-suffix match):

- `Hit@1` / `Hit@5` / `Hit@10` — percentage of instances with GT in top-k
- `MRR` — mean reciprocal rank (miss → 0)
- `File%` — fraction of instances where GT file appears at any rank

Operational:

- `p50ms` — median retrieval latency (wall-clock, single-threaded)
- `Avg tokens` — average packed context size under the 4000-token budget

Statistical:

- **95% CI** on MRR via percentile bootstrap (5000 resamples, seed=7)
- **Paired bootstrap p-value** (one-sided, 5000 resamples, seed=42) for MRR deltas
- **Miss taxonomy** per instance: `hit` / `ranked_outside_k` / `gt_not_in_pool` / `no_gt_fn`

## Adaptive gate — mechanism

Computed once per query inside `_compute_ppr` in [`selector/scoring.py`](../tacm_v2/selector/scoring.py):

```
seeds        = BM25 top-K function node_ids (K = ppr_seed_k, default 20)
degrees      = [len(out_links[i]) for i in seed indices present in PPR index]
avg_deg      = mean(degrees)
sat          = max(1e-9, ppr_density_saturation)      # default 6.0
ratio        = min(1.0, avg_deg / sat)
density_factor = ppr_density_min_scale                 # default 0.0
               + (1.0 - ppr_density_min_scale) * ratio
```

The PPR scale applied to a node's score is then `pr_scale * density_factor`, where `pr_scale` is the configured strong/weak PPR weight from Exp 04.

Three new knobs in [`selector/config.py`](../tacm_v2/selector/config.py):

```python
ppr_density_enabled:     bool  = True
ppr_density_min_scale:   float = 0.0   # shed full PPR weight on zero-fanout seeds
ppr_density_saturation:  float = 6.0   # full weight at avg seed out-degree ≥ 6
```

Saturation = 6 was chosen from the analyzer's per-repo breakdown: repos where PPR helped had mean seed out-degree ≥ 6 (pylint, seaborn, sphinx), repos where it hurt had mean seed out-degree < 1.5 (flask, xarray, sklearn).

## Run

```bash
# Adaptive PPR (this experiment)
cd ghost\ of\ past
python3 zero_cost_runner.py \
    --dataset swebench_lite_multilingual \
    --python-only \
    --conditions bm25 hybrid tacm tacm-ppr \
    --top-k-tokens 4000 \
    --seed 42 \
    --out agent_results/zero_cost_executable_benchmark_20260422_103746.json

# Analyzer slice
python3 analyze_zcr.py agent_results/zero_cost_executable_benchmark_20260422_103746.json
```

To reproduce the flat-PPR baseline, toggle the new config:

```python
SelectorConfig(ppr_enabled=True, ppr_density_enabled=False)
```
