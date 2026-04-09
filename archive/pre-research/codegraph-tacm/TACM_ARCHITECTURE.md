# TACM Architecture

## Full Pipeline

```
NL Bug Query
"cookies not sent after redirect to another host"
        │
        ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        PHASE 0: FILE ROUTING                        │
│                   (only when corpus ≥ 3000 nodes)                   │
│                                                                     │
│  MiniLM embeds query → cosine sim against file-level embeddings     │
│  → restricts FTS5 + semantic search to top-K relevant files         │
│  Prevents: sqlalchemy-scale noise (15k nodes, 400+ files)           │
└──────────────────────────────┬──────────────────────────────────────┘
                               │ file filter (set of paths)
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    PHASE 1: CANDIDATE RETRIEVAL (G1)                │
│                                                                     │
│  Input query split into keywords: ["cookies","redirect","host",..] │
│                                                                     │
│  Per keyword → crg hybrid_search(kw, limit=20)                      │
│    └─ crg FTS5 BM25 on: name │ qualified_name │ file_path │ sig     │
│    └─ crg RRF merge with vector embeddings (if built)              │
│    └─ kind boost (snake_case → Function 1.5×)                       │
│                                                                     │
│  Also: hybrid_search(full_query, limit=10)  ← phrase fallback       │
│                                                                     │
│  Score aggregation: score[node] = max(score across all kw hits)     │
│                                                                     │
│  Output: ~40-80 direct FTS5 hit nodes + scores                      │
│                                                                     │
│  ⚠ GAP: crg has body text in source but FTS5 only indexes          │
│     name/signature — body vocabulary completely unused here          │
└──────────────────────────────┬──────────────────────────────────────┘
                               │ direct_nodes + score_by_qn
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                  PHASE 2a: GRAPH TRAVERSAL (G2)                     │
│                                                                     │
│  For each direct FTS5 hit node:                                     │
│    get_edges_by_target(qn)  → hop-1 callers (inherit score × 0.5)  │
│    search_edges_by_target_name(name) → name-match callers           │
│                                                                     │
│  Hop-1 callers → hop-2 callers (inherit score × 0.25)              │
│  Cap: hop-1 ≤ 40 nodes, hop-2 ≤ 20 nodes                           │
│                                                                     │
│  Purpose: find functions that CALL a matching function              │
│  Example: AppContext.pop calls teardown() → caught even though      │
│           "pop" doesn't appear in the bug description               │
│                                                                     │
│  ⚠ GAP: only traverses CALLS edges. crg also has:                  │
│     IMPORTS, INHERITS, TESTED_BY edges — all unused for traversal  │
└──────────────────────────────┬──────────────────────────────────────┘
                               │ caller_nodes
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                  PHASE 2b: SEMANTIC EXPANSION (G3)                  │
│                                                                     │
│  MiniLM (all-MiniLM-L6-v2, 384-dim, CPU)                           │
│  Corpus embeddings: pre-computed, cached to .npy per model slug     │
│                                                                     │
│  query → embed → cosine sim vs all prod nodes → top-40 hits        │
│                                                                     │
│  New nodes from semantic (not in FTS5 hits) → added to pool        │
│  Score blend: final_hs = max(fts_score, sem_score × 0.8)           │
│                                                                     │
│  Purpose: Mode B rescue — finds functions with zero FTS5 overlap    │
│  Example: rebuild_auth ← "cookies redirect host" has no tokens     │
│           in common with function name, but MiniLM body sim works  │
│                                                                     │
│  ⚠ GAP: embeds function SOURCE TEXT but crg's FTS5 only uses       │
│     name+signature. These are two separate indices — no unified     │
│     score. The max() blend is a heuristic, not a principled fusion  │
└──────────────────────────────┬──────────────────────────────────────┘
                               │ scored candidate pool (~120 nodes)
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                   PHASE 3: SCORING (hybrid_full)                    │
│                                                                     │
│  Per node:                                                          │
│    h      = ramp(hybrid_score, lo=min_score, hi=max_score) → [0,1] │
│    degree = min(edge_count / 15, 1.0)   ← prod edges only          │
│    blast  = 1 if FTS5 hit AND score ≥ top 30% threshold            │
│    test   = 1 if has TESTED_BY edge                                │
│                                                                     │
│    score = 0.55×h + 0.25×degree + 0.10×test + 0.10×blast          │
│                                                                     │
│  Ramp computed per-call from actual score distribution:             │
│    lo = min nonzero score (noise floor)                             │
│    hi = max score (full credit)                                     │
│  Prevents saturation when FTS5 returns [0.5, 3.0] range scores     │
│                                                                     │
│  ⚠ GAP: degree = ALL edges (calls + imports + inherits + tests)    │
│     Test functions inflate degree. Proxy fix: cap at 15.            │
│     Real fix: count only production CALLS edges separately          │
└──────────────────────────────┬──────────────────────────────────────┘
                               │ nodes with .score assigned
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│              PHASE 4: BUDGET-AWARE SELECTION (Resolver)             │
│                                                                     │
│  Strategy: Hybrid-Greedy (use_knapsack=False)                       │
│    Sort by score descending                                         │
│    Greedily take nodes until token_budget exhausted                 │
│    token_cost = len(source_text) / 4                               │
│                                                                     │
│  Strategy: Knapsack (use_knapsack=True)                            │
│    0/1 DP: maximise sum(score) subject to sum(cost) ≤ budget       │
│    Full 2D table — correct backtracking                             │
│    O(n × budget) — fast at n≤200, budget≤32k                       │
│                                                                     │
│  Output: ordered list of ScoredNode within token budget            │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
                    Ranked context for LLM
              [AppContext.push, rebuild_proxies, ...]
                     within token budget
```

---

## What crg Provides vs What TACM Adds

```
crg (code-review-graph)                    TACM adds on top
────────────────────────                   ─────────────────
Tree-sitter AST parsing               →   per-keyword FTS5 decomposition (G1)
SQLite graph (nodes + edges)          →   caller traversal with score decay (G2)
FTS5 index (name/sig/path)            →   separate MiniLM semantic index (G3)
hybrid_search(full_query)             →   per-keyword max aggregation
  └─ FTS5 BM25                            adaptive ramp normalisation
  └─ RRF with optional embeddings         degree scoring (capped, prod-only)
  └─ kind/context boosting                blast-radius refinement
CALLS / IMPORTS / INHERITS edges      →   token budget-aware selection (Greedy/KS)
TESTED_BY edges                            0/1 knapsack DP
get_impact_radius() (blast radius)         function truncation at >40 lines
22 MCP tools for LLM interaction      →   (not used — TACM bypasses MCP layer)
```

---

## The Three Gaps I Can See

### Gap 1 — FTS5 only indexes name+signature, not body

crg's FTS5 virtual table:
```sql
CREATE VIRTUAL TABLE nodes_fts USING fts5(
    name, qualified_name, file_path, signature,
    tokenize='porter unicode61'
)
```

Function **body text is not indexed**. When you search "cookies redirect host", FTS5 can only match those words against `name`, `qualified_name`, `file_path`, `signature`. A function called `rebuild_auth` with a body full of cookie/redirect logic — FTS5 never sees the body.

TACM's G3 semantic search embeds the full body (via `_read_source`), but this is a separate index that doesn't feed back into FTS5. The fix: add body text to FTS5 index, or use BM25-Body (which `bench_bugsinpy.py` now measures as a separate baseline and consistently outperforms TACM-HG on MRR).

### Gap 2 — Graph traversal only uses CALLS edges

TACM's Phase 2a only expands via `CALLS` edges (callers of FTS5 hits). crg also builds:
- `IMPORTS` edges — if file A imports from file B, changes in B affect A
- `INHERITS` edges — subclass methods inherit parent context
- `TESTED_BY` edges — used only as a boolean signal, not for traversal

A function like `SessionRedirectMixin.rebuild_auth` might be reached via `INHERITS` from `Session` which IS an FTS5 hit. That path is never explored.

### Gap 3 — Two separate embedding systems, no unified score

TACM's `SemanticIndex` (G3) and crg's optional `EmbeddingStore` are completely independent:
- crg's embeddings: built with `code-review-graph embed`, stored in a separate SQLite table, merged with FTS5 via RRF inside `hybrid_search`
- TACM's embeddings: built lazily, stored in `.npy`, scores injected after FTS5 with a `max()` heuristic

The `max(fts_score, sem_score × 0.8)` blend means FTS5 and semantic are never jointly ranked — whichever is higher wins, with a fixed 0.8 discount on semantic. Principled fusion (learned weights, or RRF like crg does internally) would likely improve both precision and Mode B recall.

---

## Score Flow for One Node

```
"cookies not sent after redirect"
        │
        ├─ FTS5: "cookies" hits → rebuild_auth? NO (name mismatch)
        ├─ FTS5: "redirect" hits → resolve_redirects ✓, rebuild_proxies ✓
        ├─ FTS5: "session" hits → SessionRedirectMixin ✓
        │
        │   rebuild_auth:  fts_score = 0.0   (never hit by any keyword)
        │   MiniLM body:   sem_score = 0.73  (body has "cookies", "redirect", "auth")
        │   blended_hs   = max(0.0, 0.73×0.8) = 0.584
        │
        ▼
   _score_hybrid_full(rebuild_auth):
        h     = ramp(0.584, lo=0.01, hi=2.1) = 0.277   ← semantic floor only
        d     = min(8/15, 1.0)               = 0.533   ← 8 edges
        test  = 1.0                                     ← has tests
        blast = 0.0                                     ← fts_score=0, below threshold

        score = 0.55×0.277 + 0.25×0.533 + 0.10×1.0 + 0.10×0.0
              = 0.152 + 0.133 + 0.100 + 0.000
              = 0.385

   At budget=4000 → selected at rank ~#19   ← Mode B rescued but ranked low
```

---

## What's Missing That Would Actually Move the Number

| Missing piece | Impact | Effort |
|---|---|---|
| Add body text to FTS5 index | BM25-Body already shows 0.46 MRR vs 0.21 TACM on thefuck | Medium — requires crg fork or separate SQLite FTS table |
| Use INHERITS + IMPORTS edges in traversal | Finds subclass/import-connected bugs | Low — crg already has the edges |
| Principled FTS+semantic fusion (RRF or learned weights) | Replaces brittle `max(fts, sem×0.8)` heuristic | Medium |
| Production-only degree signal | Removes test inflation without the /15 cap hack | Low — filter edges by target.is_test |
| crg's own embeddings via `hybrid_search(model=...)` | Unifies two embedding systems | Low — one parameter change, if embeddings are pre-built |
