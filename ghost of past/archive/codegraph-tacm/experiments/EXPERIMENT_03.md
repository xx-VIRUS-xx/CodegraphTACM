# EXPERIMENT_03 — Retriever-in-Agent: Does Better Context → More Solved Bugs?

**Date:** 2026-04-10
**Status:** Harness built — ready to run
**Depends on:** EXPERIMENT_02 (retrieval evaluation complete)

---

## Why this experiment

Experiment 02 proved TACM-v2 retrieves better context than BM25, dense, and hybrid
baselines under strict function-level matching (p<0.05 vs BM25; p=0.23 vs Dense-MiniLM,
direction consistent). But retrieval MRR does not prove agent task success.

The gap to close: **does better context actually help the agent fix more bugs?**

A retriever that ranks ground-truth functions higher might still fail if:
- the agent can't navigate the context to identify the right edit
- the context is coherent but too compressed to apply a patch
- the baseline retriever happens to include enough context through noise

This experiment closes that gap by swapping only the context provider across otherwise
identical agent runs, measuring task success (tests pass) rather than retrieval rank.

---

## Design principle: one variable

Every element of the agent loop is held fixed across all retrieval conditions.
Only the context provider changes. This is the minimum requirement for a causal claim.

**Fixed across all runs:**
- Model: claude-sonnet-4-6 (same API tier, same system prompt)
- Max iterations: 5 (agent can call tools up to 5 times before giving up)
- Tool budget: read file, search, write patch — no test execution within the loop
- Patch acceptance: tests pass = success
- Task: same BugsInPy bug, same failing test, same repo state
- Query: same commit message NL query used in Experiment 02

**Variable:**
- Context provider (retrieval condition, see below)

---

## Retrieval conditions

| Condition | Description | Context given to agent |
|-----------|-------------|------------------------|
| Naive | No retriever — agent gets repo file tree only | `find .py` listing, no code |
| BM25-Body | Top-K function bodies by BM25, greedy fill | raw source bodies |
| Dense-MiniLM | Top-K by all-MiniLM-L6-v2 cosine, greedy fill | raw source bodies |
| Hybrid-BM25-MiniLM | Top-K by RRF(BM25, MiniLM), greedy fill | raw source bodies |
| TACM-v2 | Budget=4000 token layered selection | TACM serialized context |
| TACM-v2+L4 | TACM-v2 + Layer 04 (variable dynamic layer) | TACM context + call-chain snippets |

All flat-retriever conditions serve the same token budget as TACM-v2 by concatenating
top-K function bodies until the budget is reached — not unlimited raw dump.
This makes the comparison token-budget-fair, not just rank-fair.

---

## Agent loop

```
for bug in tasks:
    query = bug.commit_message
    context = retriever.get_context(query, repo, budget=4000)

    messages = [system_prompt, task_prompt(bug, context)]
    for step in range(MAX_ITER):
        response = claude(messages, tools=[read_file, write_patch, search_symbol])
        if response.tool == "write_patch":
            apply(response.patch)
            result = run_tests(bug.test_file)
            if result.passed:
                record(success=True, steps=step+1, tokens=total_tokens)
                break
            else:
                messages.append(tool_result(result.stderr))
        elif response.tool in ["read_file", "search_symbol"]:
            messages.append(tool_result(execute(response)))
        else:
            # Agent gave up or produced a final answer without patch
            record(success=False, steps=step+1, tokens=total_tokens)
            break
    else:
        record(success=False, steps=MAX_ITER, tokens=total_tokens)
```

**System prompt** (fixed across all conditions):
```
You are a code debugging assistant. You will be given a bug description and
relevant repository context. Your job is to produce a correct patch that fixes
the bug and passes the failing test. You may read additional files if needed,
but work within the provided context first. When confident, write the patch.
```

**Task prompt** includes:
- bug description (commit message, same as query)
- retrieved context block (varies by condition)
- failing test name
- instruction to write a unified diff patch

---

## Metrics

| Metric | Definition | Why it matters |
|--------|-----------|----------------|
| Solve rate | % tasks where tests pass | Primary: does it work? |
| First-attempt solve | % solved on step 1 (no recovery) | Context quality proxy |
| Mean steps to solve | avg iterations for successful tasks | Efficiency |
| Total tokens used | prompt + completion tokens across all steps | Cost proxy |
| Solve rate per budget | solve rate at token budgets 800, 2000, 4000 | Budget sensitivity |

Report mean and 95% CI (bootstrap) for solve rate. Report mean ± std for steps/tokens.

---

## Dataset

Same as Experiment 02: thefuck (n=26) + scrapy (n=19), n=45 total.

For agent evaluation, tasks must additionally have:
- a runnable test environment (Python version available, deps installable)
- a single-file or small multi-file fix (agent has limited tool budget)

Expected attrition: ~30% of tasks may fail due to environment setup or multi-file
patches too large for 5-step agent. Target n≥30 evaluable tasks.

Each task run 3 times per condition (LLM output is stochastic). Report mean solve rate.
Total runs: 5 conditions × 45 tasks × 3 seeds = 675 agent calls.

---

## Copilot agent as external baseline

GitHub Copilot coding agent can be invoked on GitHub issues. This provides an
end-to-end external product baseline, though not a clean retrieval-only comparison.

**Setup:**
1. Mirror thefuck and scrapy to GitHub repos
2. Create one issue per BugsInPy task with the commit message as bug description
3. Invoke Copilot coding agent on each issue
4. Score: PR produced? Tests pass? Time to first passing PR?

**What this proves if TACM wins:**
"Our coding-agent setup solves more BugsInPy bugs than Copilot coding agent under
this evaluation protocol." Not a retrieval claim — an end-to-end agent claim.

**What it cannot prove:**
Whether Copilot's retrieval is better or worse — its internals are opaque.

Copilot results are reported as a separate column, clearly marked as a product baseline
with no mechanistic attribution.

---

## Broader task roadmap (post-Experiment 03)

Bugs are one lane. The full case for "best coding-agent setup" requires task diversity.

| Track | Example tasks | Verification |
|-------|--------------|-------------|
| Bug fix | BugsInPy tasks | tests pass |
| Feature addition | add a new CLI flag, add an endpoint | tests pass, API contract |
| Refactor | rename a class across call sites | no regressions |
| Test generation | write tests for an untested module | coverage delta |
| Code explanation | describe how a subsystem works | human eval / LLM judge |
| Root-cause analysis | identify the fault without fixing | GT file/function hit |

For tracks with executable verification (bug, feature, refactor, test gen), use the
same agent harness with task-appropriate prompts.

For tracks requiring judgment (explanation, root cause), use LLM-as-judge with a
fixed judge prompt, or human eval on a small subset.

**Priority:** run Experiment 03 first (bug track, same data we have). Add feature/refactor
tracks only after the agent harness is validated on the bug track.

---

## Files (all built)

| File | Description | Status |
|------|-------------|--------|
| `agent_harness.py` | Fixed agent loop: retrieval → context → Claude API → patch → test | Done |
| `context_providers.py` | All 6 conditions + Layer 04 variable layer | Done |
| `patch_utils.py` | Apply/revert unified diff, restore repo via `git checkout` | Done |
| `test_runner.py` | Run BugsInPy test file with pytest, capture pass/fail + stderr | Done |

### Layer 04 — Variable Layer (implemented in context_providers.py)

Layer 04 is a dynamic context layer generated on-the-fly from graph edges, not pre-serialized.
It adapts its content based on query intent:

- **BUG intent** (default for commit-message queries): adds top-2 callers of each selected
  FUNCTION node as short call-chain snippets. Example:
  ```
  # call-chain context
    called by: get_new_command [pip_unknown_command.py]
    called by: is_match [types.py]
  ```
  Rationale: knowing what calls the buggy function helps the agent understand blast radius
  and write a fix that doesn't break callers.

- **EXPLAIN intent**: adds cross-file import chains showing which modules import each selected FILE.

- **STRUCTURE intent**: adds module-level docstrings for selected FILE nodes.

Budget: Layer 04 takes 10% of total budget (400 tok at budget=4000), reducing base TACM fill.
Net effect: slightly less FUNCTION body content, plus caller context chains.
Experiment 03 ablates this: TACM vs TACM+L4 measures whether caller context helps the agent.

---

## Expected result table

```
=== Experiment 03: Agent solve rate by retrieval condition ===
  n=XX evaluable tasks (from thefuck+scrapy), 3 seeds each

  Condition          Solve%   CI95        Steps  Tokens   vs TACM
  ---------------------------------------------------------------
  Naive              XX%      [XX, XX]    X.X    XXXK     -XX%
  BM25-Body          XX%      [XX, XX]    X.X    XXXK     -XX%
  Dense-MiniLM       XX%      [XX, XX]    X.X    XXXK     -XX%
  Hybrid-BM25+MiniLM XX%      [XX, XX]    X.X    XXXK     -XX%
  TACM-v2            XX%      [XX, XX]    X.X    XXXK       —

  [External baseline]
  Copilot agent      XX%      (no CI — external product)   —
```

If TACM-v2 solve rate > Dense-MiniLM solve rate (p < 0.05), the agent-level claim is
established. If not, retrieval MRR improvement does not translate to agent improvement
at this task complexity and n — an honest and important null result.

---

## Success criteria

| Criterion | Target |
|-----------|--------|
| TACM-v2 solve rate > BM25 (p < 0.05) | primary |
| TACM-v2 solve rate > Dense-MiniLM | primary (may need larger n) |
| TACM-v2 first-attempt solve rate > baselines | secondary (context quality) |
| TACM-v2 mean steps ≤ baselines | secondary (efficiency) |
| Copilot solve rate measured | external baseline |
