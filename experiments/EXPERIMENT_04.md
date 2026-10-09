# EXPERIMENT_04 — Retrieval-Context Benchmark on Code-Grounded BugsInPy

## Goal

Experiment 04 evaluates `retrieval/context quality`, not end-to-end patching.

The agent harness introduced a large amount of noise from:
- malformed unified diffs
- wrong patch file paths
- patch application failures
- model-side formatting variance

This experiment removes the LLM patch-writing step and asks a cleaner question:

**Given a solved, code-grounded bug report, which context provider surfaces the correct fix context best under a fixed token budget?**

## Dataset

Input tasks come from:
- [bugsinpy_code_grounded_benchmark_ready.jsonl](../datasets/bugsinpy_code_grounded_benchmark_ready.jsonl)

Only these labels are included:
- `code_explicit`
- `semantic_code`

Excluded:
- `non_code`
- `query_unavailable`

Current benchmark-ready total:
- `thefuck`: 23
- `scrapy`: 18
- `pandas`: 36
- `keras`: 11
- total: 88

## Systems

Experiment 04 compares final context providers, not agent loops:

- `bm25`
- `minilm`
- `codesearch`
- `hybrid`
- `hybrid-cs`
- `tacm`
- `tacm-full`
- `tacm-dyn`
- `tacm-dyn-l4`

## Metrics

### Function-ranking metrics

These use `strict` GT matching:
- function short name must match
- file path suffix must match

Definitions:

- `Hit@1`: percentage of tasks where the first GT-matching function appears at rank `1`
- `Hit@5`: percentage of tasks where the first GT-matching function appears within ranks `1..5`
- `Hit@10`: percentage of tasks where the first GT-matching function appears within ranks `1..10`
- `MRR`: mean reciprocal rank of the first strict GT hit

Examples:
- rank `1` -> reciprocal rank `1.0`
- rank `2` -> reciprocal rank `0.5`
- rank `5` -> reciprocal rank `0.2`
- miss -> reciprocal rank `0.0`

Why these matter:
- `Hit@1` tells us how often the method gets the fix function immediately right
- `Hit@5` and `Hit@10` tell us how often it is near the top
- `MRR` rewards earlier hits more strongly than later hits

### Context-presence metrics

These score the final packed context under the token budget:

- `context_has_gt_function`
- `context_has_gt_file`
- `context_has_gt_class`

These answer:
- did the final context contain the actual fix function?
- did it at least route to the correct file?
- did it preserve the right class/module neighborhood?

### Budget/accounting metrics

- `avg_tokens`
- `selected_count`
- `function_count`

These show how expensive the retrieved context is and how much of it is actual function content versus higher-level structure.

## Context Logging

Experiment 04 keeps a readable log of each provider's output for each bug.

Output layout:
- `results/experiment_04/experiment_04_results.jsonl`
- `results/experiment_04/experiment_04_summary.json`
- `results/experiment_04/contexts/<project>/<bug_id>/<condition>.md`

Each context log contains:
- the query
- ordered selected nodes
- the exact final context text shown by that provider

This makes debugging much easier:
- if a provider misses, we can inspect what it actually returned
- if TACM loses, we can see whether it was ranking, packing, or just different context composition

## Run

```bash
python3 tools/run_experiment_04.py
```

Project-specific:

```bash
python3 tools/run_experiment_04.py --project thefuck scrapy
```
