# EXPERIMENT_06 — Aggressive Query-Side Identifier Expansion

## Goal

Experiment 05's adaptive PPR brought TACM-PPR into MRR parity with Hybrid, but Hybrid still led at **Hit@1** (14.9% vs 10.6%). The analyzer showed the MiniLM signal dominates rank 1 on queries where a code identifier is paraphrased in natural language — e.g. *"PY3: Implement some attributes of WrappedRequest"* or *"RedirectMiddleware not honouring meta handle_httpstatus keys"*. TACM's BM25 splits document-side identifiers (via `serialize_function_for_scoring`) but the **query-side** split is shallow (a single camelCase/underscore pass), and the identifier signal only lives inside BM25 body scoring where 150-token bodies dilute it.

**Question this experiment asks:**

> If we aggressively extract code-like tokens from the query and promote them both into BM25 variants AND into a dedicated identifier-exact-match side signal, can we close the Hit@1 gap to Hybrid without any ML?

No dense encoder, no LLM reranker, no candidate-pool changes. Pure query-side surgery.

## Hypothesis

If we (a) detect every CamelCase / snake_case / dotted / backtick-quoted token in the raw query, (b) feed their full + split forms as extra BM25 variants (taken via per-node max with existing cascading BM25), and (c) add a bounded additive bonus for FUNCTION nodes whose name or qualified-name token set contains any extracted identifier verbatim — then:

1. **Hit@1** should rise for both `tacm` and `tacm-ppr` on instances where the query explicitly names a class/function/module.
2. **Hit@5 / MRR** should move up monotonically (the signal is additive and bounded to `[0, identifier_exact_scale]`, so it cannot push a correct rank-1 out of top-5).
3. Instances with **no code-like tokens** in the query should be unchanged — the extractor returns an empty set and all new code paths no-op.
4. Latency should be unchanged within measurement noise; the extractor is a handful of regex scans on the query string.

## Design principle

**Query-side only.** No graph rebuild, no corpus change, no encoder, no LLM. The extractor runs once per query (`O(len(query))`), the exact-match signal is `O(|nodes| × |q_idents|)`. Everything is gated by a single config flag (`identifier_expansion_enabled`, default False).

## Mechanism

Three additions, all in `tacm_v2/selector/`:

### 1. `_extract_query_identifiers(query)` — scoring.py

Pulls code-like tokens from a natural-language query:
- **Quoted/backtick spans** (`` `foo.bar.baz` ``, `"WrappedRequest"`) — kept whole + split.
- **CamelCase / snake_case** words (any token with internal uppercase transition or underscore) — kept whole + `_split_identifier()`'d.
- **Dotted paths** (`requests.auth.get_headers`) — each dotted part kept + split.

Smoke-test results:

| Query | Extracted tokens |
|---|---|
| "PY3: Implement some attributes of WrappedRequest required in Python 3" | `py3, request, wrapped, wrappedrequest` |
| "Fix RedirectMiddleware not honouring meta handle_httpstatus keys" | `handle, handle_httpstatus, httpstatus, middleware, redirect, redirectmiddleware` |
| "AttributeError when calling to_xarray on a Dataset with MultiIndex" | `attribute, attributeerror, error, index, multi, multiindex, to_xarray, xarray` |
| "issue with \`requests.auth.get_headers\` returning None" | `auth, get, get_headers, headers, requests, requests.auth.get_headers` |
| "just plain words no code" | `∅` (no-op) |

### 2. Identifier-expanded BM25 variants — `_cascading_bm25`

When `identifier_expansion_enabled=True`, the cascading BM25 adds two more variants alongside raw / split / expanded:

- `"<ident1> <ident2> ..."` — pure identifier blob
- `"<raw query> <ident1> <ident2> ..."` — query with identifiers appended (doubles their IDF weight)

Per-node maximum across all variants is preserved, so a strong hit on any single variant wins — no averaging dilution.

### 3. `compute_identifier_exact(query, nodes, graph)` — new side signal

Unlike `compute_name_match`, which tokenises the *entire* query (including natural-language noise like "digest" in "digest header authentication"), this signal only considers tokens from `_extract_query_identifiers`. For each FUNCTION node, it computes:

```
hits = |{q in q_idents : q in name_tokens ∪ parent_name_tokens ∪ qname_tokens}|
score = hits / len(q_idents)
```

Name tokens include both the intact identifier (`wrappedrequest`) and its split pieces (`wrapped`, `request`). Added as a bounded bonus:

```python
scores[nid] += cfg.identifier_exact_scale * compute_identifier_exact(...)
```

`identifier_exact_scale` defaults to `0.25` — strong enough to promote a rank-3 exact hit to rank 1, bounded enough that an unrelated function with no other signal can't break into top-5.

## Dataset

Same paired 47 SWE-bench Lite+Multilingual Python instances as Experiments 04/05 — results are directly comparable and paired-bootstrap p-values can be computed on the same instance axis.

Raw baseline (Exp 05, adaptive PPR, **no** identifier expansion): [`agent_results/zero_cost_executable_benchmark_20260422_103746.json`](../agent_results/zero_cost_executable_benchmark_20260422_103746.json)

## Systems

Per the user directive, **only the two conditions that changed are rerun**:

- `tacm` — TACM baseline **+ identifier expansion**
- `tacm-ppr` — adaptive-PPR TACM **+ identifier expansion**

The `bm25` and `hybrid` numbers are inherited from the Exp 05 run (unchanged — no code touched their paths).

## Metrics

Unchanged from Exp 05:

- Hit@1 / Hit@5 / Hit@10, MRR, File%
- 95% CI on MRR via percentile bootstrap (5000 resamples, seed=7)
- Paired bootstrap p-value for MRR deltas (5000 resamples, seed=42)
- p50 retrieval latency, avg packed tokens
- Miss taxonomy (`hit`, `ranked_outside_k`, `gt_not_in_pool`, `no_gt_fn`)

## Ablation axes (for the results doc)

The benchmark itself is one-shot; the ablation view comes from per-instance deltas against Exp 05:

- **Code-heavy vs prose-heavy queries** — partition the 47 instances by `len(_extract_query_identifiers(query)) >= 3`. Expansion should help on the code-heavy side and no-op on the prose-heavy side.
- **Seam tracking** — Exp 05 left 2 Hybrid-wins-TACM-PPR-loses seams (sklearn-10297, django-11001). Do they close?
- **Regression check** — any instance where Exp 05 had a rank and Exp 06 demoted it? Expansion bonus is additive so this should be rare; if it happens, the scale knob (`identifier_exact_scale`) needs damping.

## Run

```bash
cd ghost\ of\ past

# Benchmark only the two conditions that changed
TOKENIZERS_PARALLELISM=false python3 zero_cost_runner.py \
    --retriever tacm,tacm-ppr \
    --dataset executable_benchmark.json \
    --python-only \
    --no-exec \
    --top-k 20

# Analyzer slice (per-repo, seams, miss depth)
python3 analyze_zcr.py agent_results/<latest>.json
```

To disable identifier expansion (reproduce Exp 05 numbers for `tacm`/`tacm-ppr`), revert the two-line change in `zero_cost_runner.py`:

```python
cfg = (
    SelectorConfig(ppr_enabled=True) if condition == "tacm-ppr"
    else DEFAULT_CONFIG
)
```
