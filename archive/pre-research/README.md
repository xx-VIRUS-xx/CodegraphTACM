# Pre-Research Archive

Archived on 2026-04-09. This is the complete state of the system before the architectural pivot.

## What this was

A flat function-level retrieval pipeline built on top of crg (code-review-graph).
Not the intended architecture. Kept as baseline reference and for benchmark numbers.

## What it proved

- BM25-Body on function source text: 0.425 MRR on thefuck (BugsInPy, n=27)
- Semantic-only MiniLM: 0.602 MRR — graph signals were adding noise, not signal
- Knapsack budget selection works correctly
- crg provides File/Class/Function/Test nodes and CALLS/CONTAINS/IMPORTS_FROM/INHERITS/TESTED_BY edges
- crg edges have NO weights — all traversal was unweighted

## What it did not build

- Multi-layer graph (module → class → function → variable)
- Weighted edges
- Layer selector / context pool
- Variable layer (crg does not emit variable nodes)

## Contents

- `benchmarks/` — bench.py through bench_bugsinpy.py, all BugsInPy runs
- `tacm/` — the flat retrieval module (crg_adapter, resolver, semantic, etc.)
- `docs/` — codegraph-tacm design docs (architecture, experiments, research, problems)

## Key benchmark results at archive time

| Repo | Naive MRR | TACM-HG MRR | BM25-Body | Semantic-only |
|------|-----------|-------------|-----------|---------------|
| thefuck (n=27) | 0.087 | 0.425 | 0.438 | 0.602 |
| scrapy (n=19) | 0.047 | 0.251 | 0.268 | 0.318 |
| tornado (n=16) | 0.130 | 0.282 | — | — |
