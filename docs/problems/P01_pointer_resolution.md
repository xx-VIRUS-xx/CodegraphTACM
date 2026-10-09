# P01 — Pointer Resolution
**Severity:** 🔴 CRITICAL | **Status:** ✅ RESOLVED | **Blocks:** All components

## Problem
How does the LLM consume TACM output? The "pointer" concept must be precisely defined or the architecture is incoherent.

## Resolution
**Server-side resolution only.** The LLM never sees raw pointers or node IDs.

Pointers exist internally between the graph layer and the resolver only:
- Phase 1 (Skeleton): node IDs used as internal keys to fetch scores — never sent to LLM
- Phase 2 (Payload): resolver expands selected node IDs to full text before LLM call
- LLM always receives resolved natural text (structured XML or pseudo-code)

The innovation is the resolver's selection intelligence, not a novel prompt encoding.

## What "Pointer" Actually Means in TACM
A stable internal address (`fn:parser.py::Parser.parse`) used by:
1. The graph database to locate a node
2. The Elasticsearch store to fetch its payload
3. The resolver's budget manager to track what's been selected

The LLM call happens after all resolution is complete.

## Implications
- No fine-tuning required to make this work
- Works with any LLM today (Claude, GPT-4o, Llama, etc.)
- The compression claim comes from resolver selectivity, not from compact prompt encoding
- "Pointer" is an internal architectural concept, not a user-facing feature

## Closed. No further action needed.
