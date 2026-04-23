# DESIGN 07 — Session-scoped subgraph retrieval for coding agents

**Status:** Design review, pre-implementation. No code written.
**Date:** 2026-04-23
**Author note:** This is a consolidation of a design discussion. Everything here is up for revision. Each open question has a ✅/❌/❓ marker for you to fill in after your own research.

---

## 1. One-line pitch

Wrap TACM in a session layer so that retrieval gets progressively cheaper and more accurate across an agent's multi-turn session, by scoping candidates to the subgraphs the session has already touched — with BM25 routing, node/subgraph decay, and full-graph fallback when a query doesn't fit.

---

## 2. Why this instead of "more experiments on TACM"

- Exp 06 confirmed the pure-algorithm Hit@1 ceiling — no scale of identifier-expansion beat the Exp 05 baseline on MRR.
- Current TACM-PPR Hit@5 = 36.2% (best in the benchmark) is competitive; Hit@1 = 10.6% is the weak point.
- Reframing the contribution from "better retrieval metric" to "stateful retrieval that saves agent tokens per session" converts a month of research into a measurable engineering claim.
- No single competitor (Cursor, Claude Code, Copilot, SWE-agent, Aider, Cline) has published a session-scoped graph-retrieval architecture for code agents. The combination of (a) structural code graph, (b) session-mutated subgraphs, and (c) TACM as precision retriever inside each subgraph is novel.

**Core claim to prove:** *on multi-turn agent sessions, scoping TACM to session-touched subgraphs improves Hit@5 and reduces tokens with no loss in solve rate.*

---

## 3. Architecture at a glance

### 3.1 Lifecycle

1. **Session start.**
   TACM builds the full repo graph (current TACM layers: FILE → CLASS → FUNCTION). Persists it in a graph DB.
2. **First query of a thread.**
   TACM retrieves against the full graph. Agent traverses its top-K, does its work, and the set of *actually-used* nodes becomes a **first-query subgraph** tagged with that query's BM25 signature.
3. **Follow-up queries.**
   Router scores the new query against each existing subgraph's BM25 signature.
   - **High-similarity match** → retrieve inside that subgraph only (small candidate pool, higher precision).
   - **No match above threshold** → treat as a new thread, create a new first-query subgraph against the full graph.
4. **Decay.**
   Nodes and whole subgraphs decay with a combination of time-since-touch and query-similarity drift. Dead subgraphs are archived, not deleted (can be revived if a later query matches them).
5. **Miss fallback.**
   If TACM-inside-subgraph returns a weak top-5, fall back to full-graph retrieval; optionally promote the newly-retrieved nodes into the active subgraph.

### 3.2 Data model

```
Session
├── full_repo_graph (immutable reference)
├── subgraphs: list[FirstQuerySubgraph]
└── dispatch_log: list[(turn, query, routed_to)]

FirstQuerySubgraph
├── spawn_query: str
├── spawn_bm25_signature: Counter[str]  # token → tf
├── nodes: set[node_id]
├── last_touched_turn: int
├── queries_served: int
└── per_node_activity: dict[node_id, float]  # decayed score
```

### 3.3 Router

```
def route(query, subgraphs) -> RouteDecision:
    scores = [(sg, bm25(query, sg.spawn_bm25_signature)) for sg in subgraphs]
    best_sg, best_score = max(scores)
    if best_score >= ROUTE_THRESHOLD:
        return RouteDecision(attach_to=best_sg)
    else:
        return RouteDecision(spawn_new=True)
```

---

## 4. Design decisions already made (from the discussion)

| # | Decision | Rationale |
|---|---|---|
| 1 | Graph DB: **Kuzu** (embedded, Cypher-like, Python-native) | Avoid Neo4j's server overhead; NetworkX doesn't scale |
| 2 | Router signal: **BM25 query-vs-subgraph-signature** | Cheap, interpretable, no ML dependency |
| 3 | Multiple first-query subgraphs coexist | Real sessions are threaded (auth bug AND cache bug), don't force a linear topic model |
| 4 | Node decay: **time + query-BM25 similarity** | Two signals, both cheap; drift-aware eviction |
| 5 | Subgraph decay: **aggregate of node activity** | A subgraph is dead when its nodes are — no separate policy needed |
| 6 | Miss fallback: retrieve from full graph, promote found nodes into subgraph | Option 2 from the discussion — handles "right area, too-tight pool" cleanly |
| 7 | TACM stays unchanged at the retrieval core | All the architecture is a wrapper; `_extract_query_identifiers`, PPR, cascading BM25 all keep working |

---

## 5. Design decisions still OPEN — please answer after research

For each, mark ✅ (agree with proposal), ❌ (need different approach), or ❓ (need more data to decide). Add rationale.

### 5.1 How many concurrent subgraphs?

**Proposal:** hard cap of 5 most-recently-active subgraphs + subgraph-level time decay (archive, don't delete, if not queried in N=10 turns).

**Alternatives:**
- Merge-on-similarity (if two subgraphs' signatures converge, union them).
- Unbounded with aggressive per-node decay only.
- Hierarchical (primary thread + secondary threads).

**Your answer:** ❓
**Rationale:** 

---

### 5.2 BM25 routing threshold

**Proposal:** tune on real multi-turn session data. Don't guess. Start at the median similarity score observed in Week 1 validation.

**Risk:** if real follow-ups are terse ("try again", "fix it"), BM25 similarity will be uniformly weak and routing won't activate.

**Your answer:** ❓
**Rationale:** 

---

### 5.3 Dispatch on routing ties

**Proposal:** route to top-1 subgraph if margin ≥ 0.1; otherwise union-retrieve from top-2.

**Alternatives:**
- Always top-1 (cleaner, loses signal on ambiguous queries).
- Always union top-2 (safer, dilutes precision).
- Ask the agent to disambiguate.

**Your answer:** ❓
**Rationale:** 

---

### 5.4 What counts as a "touched" node in a subgraph?

**Three possibilities:**
- (A) Any node TACM returned in its top-K for this query.
- (B) Any node the agent actually *read* (opened the file).
- (C) Any node the agent *acted on* (edited, cited in its output, ran test against).

**Proposal:** (B) with a fallback to (A) if the agent doesn't emit "read" signals. (C) is ideal but requires deep agent integration.

**Your answer:** ❓
**Rationale:** 

---

### 5.5 Decay curve shape

**Proposal:** exponential decay per turn-since-touch, activity score `= exp(-k × turns_since_touched)`. `k` tunable. Below threshold 0.1 → node evicted.

**Alternatives:**
- Linear decay (simpler, cliff at eviction).
- LRU only (no continuous score, just recency).
- Query-weighted: decay faster if recent queries are dissimilar to the node's BM25 context.

**Your answer:** ❓
**Rationale:** 

---

### 5.6 Full graph persistence

**Open question:** does the full repo graph persist across sessions, or is it rebuilt each session?

**Tradeoffs:**
- Persist: fast session startup, stale if repo changes.
- Rebuild: always fresh, slow startup (tens of seconds for large repos).
- Persist + invalidate on git HEAD change: best of both, moderate complexity.

**Your answer:** ❓
**Rationale:** 

---

### 5.7 Which agent to integrate with first

**Options:**
- **SWE-agent** (open source, clean harness, published benchmark numbers)
- **Aider** (active OSS, has retrieval layer, friendly to contributions)
- **Cline / Continue.dev** (IDE-integrated, more users, less benchmarkable)
- **Custom minimal agent** (full control, no ecosystem)

**Proposal:** SWE-agent first for benchmarkability, Aider second for community.

**Your answer:** ❓
**Rationale:** 

---

### 5.8 Multi-turn benchmark dataset

**The hard one.** SWE-bench is single-query; there is no standard multi-turn code-agent benchmark.

**Options:**
- Synthesize multi-turn sessions by chaining related SWE-bench instances from the same repo.
- Mine real agent trajectories (SWE-agent public logs, Aider session dumps).
- Hand-craft 50 multi-turn sessions ourselves.
- Adopt an existing benchmark (LiveCodeBench, RepoEval, CoderEval) even if imperfect.

**Proposal:** hand-craft 50 sessions from SWE-bench-Multilingual for prototype; mine real trajectories for a larger evaluation later.

**Your answer:** ❓
**Rationale:** 

---

## 6. Assumptions that MUST be empirically validated before building

These kill the whole architecture if false. Do them before committing to 6+ weeks of implementation.

### Assumption A: Structural locality in agent trajectories
**Claim:** consecutive node-touches by a coding agent within a session are structurally nearby in the code graph (same file, sibling functions, call-adjacent) more often than chance.

**Test:** take 20+ SWE-agent trajectories. For each consecutive pair of touched nodes (n_i, n_{i+1}), measure graph distance. Compare to random pairs.

**Kill condition:** if agent touches scatter randomly across the graph, subgraphs don't help.

**Your answer:** ❓

---

### Assumption B: BM25 signal in follow-up queries
**Claim:** follow-up queries have enough lexical content to be routed by BM25 against subgraph signatures.

**Test:** on the same trajectories, measure BM25 similarity between consecutive agent queries and the accumulated subgraph signature.

**Kill condition:** if follow-ups are overwhelmingly terse ("fix it", "try again", "why") with no content, BM25 router will always fail → you'd need a different router (heuristic: attach to most-recent subgraph by default).

**Your answer:** ❓

---

### Assumption C: Precision-on-subgraph actually beats precision-on-full-graph
**Claim:** TACM retrieval restricted to a 100–500 node subgraph gives higher Hit@1/Hit@5 than TACM on the full repo graph.

**Test:** on existing SWE-bench results, artificially restrict TACM to the ground-truth-containing file's call-neighborhood (oracle subgraph). Measure Hit@1/Hit@5 on that slice vs. full-graph.

**Kill condition:** if Hit@5 doesn't rise substantially even with an *oracle* subgraph, shrinking the candidate pool doesn't help → reconsider.

**Your answer:** ❓

---

### Assumption D: Modern agents don't already do this effectively
**Claim:** Claude Code / Cursor / Copilot do NOT already maintain session-scoped retrieval state that makes this redundant.

**Test:** read the Claude Code MCP docs, Cursor's docs on indexing, any available Copilot documentation. Check if session-scoped retrieval is already in-house.

**Kill condition:** if all major agents already do something functionally equivalent, this is reinvention without differentiation.

**Your answer:** ❓

---

### Assumption E: Token savings are measurable at session scale
**Claim:** on a realistic 5–10 turn session, the subgraph architecture saves ≥20% of retrieval-related tokens vs. full-graph-every-turn.

**Test:** back-of-envelope first — model a typical session, estimate token counts with/without subgraph scoping.

**Kill condition:** if the math shows <10% savings even in the ideal case, the engineering complexity isn't worth it.

**Your answer:** ❓

---

## 7. Failure modes and how the design mitigates them

| Failure mode | Mitigation built in |
|---|---|
| Topic shift mid-session | BM25 router spawns new subgraph |
| Subgraph pool hollowing out | Node decay + miss-fallback to full graph + promote found nodes back into subgraph |
| Terse follow-up queries | **Not yet mitigated** — if Assumption B fails, need a different router (see 5.2) |
| Subgraph proliferation | Hard cap + subgraph-level decay |
| Stale subgraph across sessions | Subgraphs are per-session by default; cross-session persistence is out of scope for v1 |
| Full repo graph stale after git pull | Invalidate on HEAD change (see 5.6) |
| Agent doesn't signal which nodes it used | Fall back to "TACM top-K returned" = touched (see 5.4) |

---

## 8. Proposed build plan (if all assumptions hold)

| Week | Milestone | Output |
|---|---|---|
| 1 | Assumption validation (A, B, C) on existing trajectories | Go/no-go memo |
| 2 | In-memory prototype: subgraphs, router, decay — no DB | Runs on hand-crafted sessions |
| 3 | Swap storage to Kuzu; persist full graph across turns | End-to-end single-agent prototype |
| 4 | Build multi-turn benchmark harness | 50 hand-crafted sessions runnable |
| 5 | Integrate with SWE-agent | First real multi-turn numbers |
| 6 | Tune routing threshold, decay constants on real data | Stable config |
| 7 | Full evaluation run (tokens, solve rate, Hit@k, latency) | Results dataset |
| 8 | Write up (blog + workshop paper draft) | Shareable artifact |

**Total:** ~2 months. Week 1 is the kill-switch — if assumptions fail, stop.

---

## 9. What a successful outcome looks like

A blog post / short paper titled something like **"Session-scoped graph retrieval for code agents: stateful precision without dense encoders."**

Headline numbers it would contain:
- Token reduction % across 5-turn sessions vs. stateless retrieval.
- Solve-rate preservation vs. baseline.
- Hit@1 / Hit@5 within subgraph vs. on full graph.
- Latency (p50, p95) of routing + retrieval per turn.
- Ablation: router off (always full graph) vs. router on.
- Ablation: decay off (unbounded pool) vs. decay on.

This is a fundable-conversation artifact, not a product. The audience is:
- Open-source agent maintainers (SWE-agent, Aider, Cline).
- Workshop reviewers at NeurIPS / ICLR code-LLM tracks.
- PhD admissions committees / research lab interviewers.
- Not VCs. Not Anthropic/OpenAI/GitHub as customers.

---

## 10. What this explicitly does NOT commit to

- Cross-session memory. Each session is its own slate in v1.
- A UI or product wrapper. This is research infrastructure.
- Beating Hybrid on single-query Hit@1. That ship sailed with Exp 06.
- Supporting every language. Python-first, same as TACM today.
- LLM-based routing or reranking. If needed, those are v2.
- Integration with closed-source agents (Claude Code, Cursor, Copilot). Only open-source targets in v1.

---

## 11. Outstanding concerns to discuss

Things I think are worth flagging even if they don't have clean answers yet:

1. **The "session" is a fuzzy concept.** Agents don't emit session-start/end signals uniformly. We'd have to define it (e.g., "a contiguous shell process" or "up to 30 min of inactivity").
2. **Graph-DB ops complexity is real.** Kuzu is young. Schema migrations, corruption recovery, etc. — add real engineering cost beyond the algorithm.
3. **The locality assumption might vary by agent style.** SWE-agent (plan → navigate → edit) may be more locality-friendly than Aider (ask Claude to rewrite a file). Need to measure per-agent.
4. **Dead subgraphs as archival state** — are they ever revived? If not, archived == deleted. If yes, we need a recall mechanism.
5. **Subgraph signatures drift as nodes are added.** We'd store the spawn-query signature, but the subgraph itself grows. Do we update the routing signature? If yes, old queries that matched it stop matching. If no, the signature gets stale. **Not resolved.**

---

## 12. Your action items for review

1. Read this doc end-to-end.
2. Fill in ✅ / ❌ / ❓ for every section 5 and 6 question with your rationale.
3. Specifically call out anything in section 11 that changes your intuition.
4. Decide: do we spend Week 1 on validation? Or does section 6 already fail on intuition/prior knowledge?
5. Flag any assumption or decision that's missing from this doc but should be here.

---

## 13. Decision to make at end of review

- [ ] **GO:** Week 1 validation. If assumptions hold, proceed through Week 8 build.
- [ ] **MODIFY:** change N design decisions, then GO.
- [ ] **PIVOT:** the design is wrong in a fundamental way. What's the alternative?
- [ ] **STOP:** close out TACM research, write up what exists, move on.
