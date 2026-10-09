# CodeGraph-TACM

Research on TACM (Topology-Aware Context Manager): query-adaptive, multi-layer code graphs for building small, high-value context for an LLM answering questions about a codebase. A resolver scores code units (files, classes, functions) using several signals (text match, call and inheritance structure, semantic similarity, history) and packs the best ones into a fixed token budget. The experiments here measure whether that beats flat retrieval (BM25, dense embeddings, hybrids) at localising bugs.

## Research question

> What is the minimal structured representation of a codebase that enables correct LLM reasoning, and which graph signal layers are necessary to achieve it?

The original claim, and the success criteria it was held to, are in [docs/research/THESIS.md](docs/research/THESIS.md). Related work and novelty analysis: [docs/research/](docs/research/).

## Experiments

Each experiment has a design doc and a results doc in [experiments/](experiments/). Numbers below are copied from those results docs; read them for datasets, caveats and statistics.

| # | Question | Setup | Reported outcome |
|---|---|---|---|
| 01 | Does graph-aware hybrid retrieval beat naive RAG on bug localisation? | Six codebases (requests, flask, sqlalchemy, tornado, thefuck, scrapy), natural-language queries, ground truth = fixed function | Higher MRR than naive RAG in the pre-semantic runs (e.g. flask at 4000 tokens: 0.208 vs 0.064); later adds semantic embeddings as a fifth signal ([results](experiments/EXPERIMENT_01_RESULTS.md)) |
| 02 | TACM-v2 (layered graph, intent-aware scoring) versus flat retrievers | BugsInPy thefuck + scrapy, n=45, strict function-level matching, paired bootstrap | Macro MRR 0.331 versus BM25 0.227 (significant, p=0.008 / 0.014) and Dense-MiniLM 0.265 (not significant, p=0.23); n is small ([results](experiments/EXPERIMENT_02_RESULTS.md)) |
| 03 | Does better context solve more bugs in an agent loop? | gpt-4o-mini agent, 4000-token budget, 3 seeds, thefuck + scrapy | Mixed: unbudgeted `tacm-full` leads on scrapy (42% vs 37% bm25/minilm), while BM25 leads on thefuck (77%, 3-seed) ([results](experiments/EXPERIMENT_03_RESULTS.md)) |
| 04 | Pure retrieval quality without agent noise | 88-bug code-grounded BugsInPy dataset, 10 conditions | On the clean n=41 subset TACM reaches 31.7% H@1 / MRR 0.409 versus 22.0% / 0.330 for the best text baseline; an LLM reranker adds more (41.5% / 0.478). pandas results carry a dataset-quality caveat ([results](experiments/EXPERIMENT_04_RESULTS.md)) |
| 05 | Does density-gated personalised PageRank close gaps to the hybrid baseline? | SWE-bench Lite + Multilingual, Python only, n=47 | `tacm-ppr` MRR 0.198 [0.110, 0.297] versus hybrid 0.192 [0.096, 0.298] and BM25 0.148: within each other's confidence intervals ([results](experiments/EXPERIMENT_05_RESULTS.md)) |
| 06 | Does query-side identifier expansion help? | Same 47 instances, scale sweep 0.05 to 0.25 | Negative result: no Pareto improvement at any scale; recommended default is off ([results](experiments/EXPERIMENT_06_RESULTS.md)) |

Design notes for follow-on work: [experiments/DESIGN_07_SESSION_SUBGRAPHS.md](experiments/DESIGN_07_SESSION_SUBGRAPHS.md). Plans: [experiments/BENCHMARK_PLANv2.md](experiments/BENCHMARK_PLANv2.md), [experiments/ABLATION_PLAN.md](experiments/ABLATION_PLAN.md).

## Repository layout

```
docs/
  research/        thesis, related work, novelty, working notes
  architecture/    TACM architecture, data models, decisions, stack, MCP interface spec
  problems/        numbered design problems and open questions (P01-P11, Q01-Q06)
  FINDINGS.md      decisions taken on each problem; GAP_TRACKER.md, USAGE.md, plan.md
  history/         READMEs from earlier phases of the project
experiments/       design and results docs for experiments 01-06, plans
datasets/          code-grounded BugsInPy tasks (jsonl, csv)
results/experiment_04/   per-query context dumps, results.jsonl, summary.json
tools/             dataset builder, experiment 04 runner, results reporter
tacm/              v1 package (resolver, reranker, semantic embeddings, BugsInPy loader)
tacm_v2/           v2 engine: graph model, layered selector and scoring, neo4j memory, tests/
benchmarks/        v1 benchmark scripts
agent_harness.py, bench_v2.py, zero_cost_runner.py, copilot_baseline.py, ...
                   harnesses that run the experiments; they resolve paths relative to the repo root
agent_results*/, logs/, tacm_traces/   raw outputs referenced by the results docs
dashboard/         small Flask app for browsing runs
```

## Tests

```bash
pip install pytest numpy
python3 -m pytest tacm_v2/tests -q
```

24 tests pass: 20 unit tests for the selector scoring, intent, cache and graph model (`test_scoring.py`), and 4 regression guards for the Experiment 02 claims (`test_regression.py`). The regression guards need local clones of `thefuck` and `scrapy` in the repository root; without them they print `SKIP` and pass, so a green run does not by itself confirm those claims. They also return a boolean instead of asserting, which newer pytest versions warn about.

## Reproducing the experiments

There is no requirements file. From the imports, the code uses `numpy`, `torch`, `transformers`, `sentence-transformers`, `rank_bm25`, `neo4j`, `flask`, `openai` and `anthropic`, plus the external `code_review_graph` package (not vendored here; install it separately). LLM-based conditions need API keys in a local `.env`, which is git-ignored.

The benchmark target repositories (BugsInPy clones, thefuck, scrapy, pandas, keras, and the SWE-bench Lite instances) are third-party data and are not included. Clone them into the repository root (they are git-ignored) and see [docs/USAGE.md](docs/USAGE.md) and the "Reproducibility" sections of the Experiment 03 to 06 results docs for the commands. Example:

```bash
python3 tools/run_experiment_04.py --project thefuck scrapy
python3 tools/report_dataset_results.py
```

## Third-party material

- Benchmarks and data: BugsInPy and SWE-bench; code under test comes from third-party projects such as `nvbn/thefuck`, `scrapy/scrapy`, `pandas-dev/pandas`, `keras-team/keras`. These are not part of this project's license or authorship. Some repository branches (`copilot/*`) contain upstream `thefuck` history.
- Models and libraries: all-MiniLM-L6-v2 (Hugging Face), codesearch-distilroberta-base (the `codesearch` condition), gpt-4o-mini for the agent and reranker conditions.
- The `code_review_graph` package is an external dependency; confirm its license before redistributing anything derived from it.

## Limitations and next steps

- Sample sizes are small (n between 18 and 47 per condition); several differences, including `tacm-ppr` versus hybrid in Experiment 05, are inside the confidence intervals.
- Experiment 04's pandas results are flagged in the results doc as low quality, and keras was excluded for the wrong repository version.
- The engine and harness scripts sit at the repository root and are not packaged; there is no `pyproject.toml` or pinned requirements.
- `results/experiment_04` contains absolute paths from the original machine inside the dumped contexts and results.
- Some docs under `docs/` still use the older nested paths when describing where files live.
- `agent_harness.py`, `bench_v2.py`, the dashboard and the regression tests still add `archive/pre-research` to `sys.path`; the entry is harmless now that `tacm/` is at the root.
- The v1 benchmark scripts in `benchmarks/` expect target repos next to them and were already out of step with their original layout.
- No LICENSE has been chosen for the project.
