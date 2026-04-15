# Current Limitations And Likely Fixes

## Purpose

This document explains the current performance bottlenecks in TACM and the agent harness, along with the most practical next improvements.

The main theme is simple:

- retrieval is now reasonably strong
- end-to-end bug solving is still limited by context packing, agent loop constraints, and patch generation quality

## 1. Solve Rate Ceiling (~21-38%)

### Problem

Even the stronger setups currently solve only about 1 in 3 to 1 in 5 bugs.

The core failure mode is often **not** that the agent cannot find the right file. The agent usually gets close, but then fails to produce a correct patch within the allowed loop.

### Root Causes

- `Context incompleteness`
  The fix may require understanding 2-3 related functions together, but the current token budget often fits only one function body plus limited surrounding structure.

- `Iteration cap is too tight`
  On more complex repos, especially `scrapy`, the agent spends early steps reading supporting files before it is ready to patch. A 5-step cap leaves little room for recovery.

- `Patch quality under pressure`
  Smaller models such as `gpt-4o-mini` are more likely to emit malformed or low-quality patches when context is dense and time is short.

### Likely Fixes

- `Layer 4: call-chain snippets`
  Add short caller snippets for selected functions. These are relatively cheap in tokens and can show the constraints around a function without including full extra bodies.

- `Increase iteration cap from 5 to 8`
  This directly tests whether some current failures are "almost solved" but run out of room before applying a valid patch.

- `Hybrid model strategy`
  Use a smaller model for reading and navigation, then switch to a stronger model for final patch writing only.

### What This Would Test

These changes test whether the real blocker is:

- missing local context
- insufficient planning room
- weak patch generation

rather than poor retrieval.

## 2. Token Budget Excludes Too Many Functions

### Problem

The fixed budget split across `FILE`, `CLASS`, and `FUNCTION` layers means many relevant functions never get a chance to appear in context at all.

This is one of the clearest reasons `tacm` underperforms `tacm-full`.

### Root Cause

Budget is allocated to layers in advance:

- some tokens always go to files
- some always go to classes
- the remainder goes to functions

That means a highly relevant function can lose to a low-value file or class node simply because the function layer ran out of budget.

### Likely Fixes

- `Dynamic budget allocation`
  Score all layers together and fill by value, not by pre-committed layer share.

- `Two-pass selection`
  First choose a very small amount of structural guidance, then spend almost all remaining budget on functions.

- `Soft cutoff`
  Allow lower-ranked functions to occasionally enter the context with score-weighted sampling instead of a hard exclusion boundary.

### What This Would Test

These changes test whether TACM is currently losing because the ranking is wrong, or because good candidates are being cut off after ranking.

## 3. Speed: Graph Build Is Slow On First Run

### Problem

Initial graph construction can take 10-30 seconds on larger repositories.

That hurts usability in real agent workflows, especially if the graph is rebuilt too often.

### Root Cause

The builder currently:

- loads all CRG nodes and edges
- resolves many short-name calls
- computes transitive edges such as `INHERITS` and `IMPORTS_FROM`

This is valuable work, but expensive if repeated from scratch.

### Likely Fixes

- `Persist the LayeredGraph`
  Save the built graph and reload it unless the CRG database has changed.

- `Lazy transitive closure`
  Compute only the transitive relationships needed around the selected subgraph instead of materializing everything up front.

- `Incremental build`
  Rebuild only the nodes and edges affected by changed files.

### What This Would Test

These changes test whether TACM can become practical for repeated interactive use, not just offline benchmarking.

## 4. BM25 Statistics Are Global, Not Query-Adaptive

### Problem

BM25 currently treats document frequency globally across the whole repository.

That can under-value terms that are common across many rule files but still highly informative for the specific bug being queried.

### Root Cause

A term can look "common" globally even when it is highly discriminative within the local neighborhood that matters for the query.

### Likely Fixes

- `Scoped BM25`
  Pre-filter to a smaller relevant region, then compute BM25 over that subset.

- `Query expansion / local boosting`
  If the query implies a module, rule, or file name, add a targeted boost to nodes inside that area.

- `BM25F`
  Treat function name, class name, and body as different fields rather than one flat bag of text.

### What This Would Test

These changes test whether TACM loses some easy keyword-aligned bugs because lexical relevance is being normalized at the wrong scale.

## 5. Fan-In Signal Is Too Weak For Common Names

### Problem

Functions such as `get_new_command` appear in many places. The current ambiguity discount can suppress fan-in so aggressively that the signal becomes almost useless.

### Root Cause

The current logic discounts by how many nodes share the same short name. That protects against false confidence, but can erase meaningful signal for locally important functions with globally common names.

### Likely Fixes

- `Qualified fan-in`
  Prefer callers in the same file or nearby subtree rather than global callers everywhere.

- `Softer ambiguity discount`
  Use a gentler penalty such as `sqrt(sharing_count)` instead of a full division by the raw count.

- `Personalized PageRank`
  Seed graph propagation from query-relevant nodes so importance spreads through the local graph neighborhood rather than relying on raw in-degree.

### What This Would Test

These changes test whether TACM can preserve structural signal without washing it out for common utility-style names.

## Recommended Priority Order

If the goal is to improve end-to-end agent performance soon, the best order is:

1. `Fix context incompleteness`
   Add Layer 4 call-chain snippets and test a larger iteration cap.

2. `Fix the hard function cutoff`
   Move from rigid layer budgets to dynamic or two-pass allocation.

3. `Improve patch generation quality`
   Use a stronger model only for patch writing.

4. `Speed up graph reuse`
   Persist the built graph and rebuild incrementally.

5. `Refine lexical and graph signals`
   Improve BM25 scope and fan-in calibration after the larger agent bottlenecks are addressed.

## Overall Interpretation

The current evidence suggests TACM is no longer blocked by the basic idea. The architecture is good enough to retrieve distinctive structural context.

The main bottlenecks now are:

- how that context is packed
- how much room the agent gets to act
- how reliably the patch is written and applied

That means the next phase is less about inventing a new retrieval system and more about turning a strong retriever into a stronger end-to-end coding workflow.
