# P07 — Benchmark Fairness
**Severity:** 🟡 MEDIUM | **Status:** ❓ OPEN | **Blocks:** Paper / Evaluation

## Problem
CodexGraph, CGM, and GraphCoder have been optimised for SWE-bench. A comparison must control for: backbone LLM, retrieval token budget, evaluation criteria, and scaffolding complexity.

## Control Variables (must be fixed across all systems)

| Variable | Value to fix | Reason |
|---|---|---|
| Backbone LLM | GPT-4o (gpt-4o-2024-08-06) | Most papers use this |
| Context token budget | 4,096 tokens | Typical retrieval budget |
| Evaluation metric | % Resolved (Pass@1) | SWE-bench standard |
| Temperature | 0.0 | Deterministic |
| Max generation tokens | 2,048 | Standard |

## Baselines to Include

| System | Why include | Source |
|---|---|---|
| No retrieval (LLM only) | Floor — shows what LLM knows without context | Implement |
| Naive RAG (LlamaIndex chunking) | Primary baseline — what we beat | Implement |
| BM25 only | Tests lexical retrieval alone | Implement |
| CodexGraph | Best published graph-based system | Their paper |
| Our G1 only | Tests whether graph helps vs chunking | Implement |
| Our full system | Primary result | Implement |

## What to Report Per System
- % Resolved on SWE-bench Lite (primary credibility metric)
- % Resolved on BugsInPy (primary novel metric)
- Average tokens used per query
- Average retrieval latency (ms)
- Index build time (minutes)

## Agent Task
1. Set up LlamaIndex naive RAG baseline on SWE-bench Lite (10-task subset first)
2. Set up BM25-only baseline on same subset
3. Run both with GPT-4o at 4096-token context budget
4. Record: % Resolved, tokens used, latency
5. These numbers become the baseline columns in the results table

## Acceptance Criteria
- At least 3 baselines implemented before claiming any result
- All baselines use identical LLM, temperature, budget
- Results reproducible with a single script run
