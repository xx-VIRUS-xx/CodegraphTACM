# EXPERIMENT_01.md — Graph 1 Only vs Naive RAG

## Run This First

This is the only experiment that matters right now.
Before building G2, G3, G4, or the resolver — prove that G1 alone beats naive RAG.
If it doesn't, understand why before going further.

---

## Hypothesis

Graph 1 (AST-based structural retrieval) outperforms naive RAG (LlamaIndex chunking)
on bug localisation tasks at equal token budget.

**Null hypothesis:** G1 and naive RAG produce equivalent retrieval quality.
If we cannot reject the null, the entire four-graph approach needs rethinking.

---

## Setup

### Codebase to Use
`psf/requests` library — well-known, medium size (~8k lines Python), good bug history.

### Task Set
10 real GitHub issues from the requests repo that involve a specific bug.
Ground truth = the function(s) modified in the fixing commit.

Start with these 10 (find them in requests issue tracker, filter by "bug" label + closed PR):
1. Unicode handling in URL encoding
2. SSL certificate verification edge case
3. Session cookie handling bug
4. Redirect loop detection
5. Proxy authentication header
6. Timeout handling in streaming
7. Content-type header parsing
8. Response encoding detection
9. Form data encoding
10. Connection pool exhaustion

### Token Budget
800 tokens of retrieved context per query (same for both systems).

### LLM
GPT-4o (gpt-4o-2024-08-06), temperature=0, max_tokens=512.

---

## Baseline A — Naive RAG (LlamaIndex)

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# Index the requests library
docs = SimpleDirectoryReader('./requests').load_data()
index = VectorStoreIndex.from_documents(docs)
retriever = index.as_retriever(similarity_top_k=5)

# For each query:
nodes = retriever.retrieve(query)
context = "\n".join(n.text for n in nodes)
# context is passed to GPT-4o
```

Record:
- Which functions appear in retrieved context?
- Are ground-truth functions present? At what rank?
- Total tokens used?

---

## Baseline B — G1 + TACM Resolver (code-review-graph)

G1 is provided by `code-review-graph` (https://github.com/tirth8205/code-review-graph).
No custom AST parser — call `get_review_context_tool` directly.

```python
# Setup (once per repo):
#   pip install code-review-graph
#   code-review-graph build ./requests
#   code-review-graph serve   # starts MCP server

from tacm.resolver import ScoredNode, resolve
from tacm.crg_adapter import crg_output_to_scored_nodes

# For each query — call get_review_context_tool via MCP, then:
crg_result = get_review_context_tool(query=query, repo="./requests")
nodes = crg_output_to_scored_nodes(crg_result)
selected = resolve(nodes, token_budget=800)
context = serialise_nodes(selected)
# context is passed to GPT-4o
```

`crg_adapter.py` maps `code-review-graph` output fields to `ScoredNode`:
- `changed_nodes` + `impacted_nodes` → nodes (set `in_blast_radius=True` for impacted)
- edge count from `edges` → `degree`
- TESTED_BY edges → `has_test`
- `source_snippets` → `source_text` (used for `token_cost` estimate)

Record:
- Same metrics as Baseline A

---

## Metrics to Collect

For each of the 10 tasks, for each system:

| Metric | How to measure |
|---|---|
| Ground truth present | Is the buggy function in the retrieved context? (0/1) |
| Ground truth rank | Position of buggy function in retrieval ranking |
| MRR | 1/rank, averaged over 10 tasks |
| P@5 | Fraction of top-5 nodes that are relevant |
| Tokens used | Count tokens in final context |
| Answer quality | GPT-4o judge: does the answer correctly identify the bug location? (1-5) |

---

## Expected Results Table

Fill this in after running the experiment:

| Metric | Naive RAG | G1 Only | Delta |
|---|---|---|---|
| GT Present (%) | ? | ? | ? |
| MRR | ? | ? | ? |
| P@5 | ? | ? | ? |
| Avg tokens used | ? | ? | ? |
| Answer quality (1-5) | ? | ? | ? |

---

## Interpretation

**If G1 >> Naive RAG:**
Graph-based retrieval works. Build G2, G3, G4 incrementally.
Write up results as Experiment 01 baseline in the paper.

**If G1 ≈ Naive RAG:**
Graph structure alone doesn't help. Need to understand why.
Possible causes: cross-file resolution broken (P02), token serialisation suboptimal (P11), test tasks too easy.
Fix the most likely cause and re-run before building more.

**If G1 << Naive RAG:**
Something is wrong with G1 retrieval. Debug before anything else.
Possible causes: BM25 on signatures is worse than embedding similarity on chunks, graph traversal adding noise.

---

## Success Criteria

Experiment 01 is a success if:
- G1 MRR ≥ Naive RAG MRR + 0.1
- G1 P@5 ≥ Naive RAG P@5 + 0.05
- G1 tokens used ≤ Naive RAG tokens used

Any one of these being true justifies continuing to build G2.
All three being true justifies writing the paper.

---

## Agent Instructions

If you are running this experiment:
1. Clone psf/requests at a specific commit (use commit from 2023 — stable)
2. Run ast_parser.py on it — confirm you get nodes with correct line ranges
3. Manually identify 10 bug issues from GitHub with clear buggy function in fix commit
4. Implement both baselines exactly as described above
5. Run both on all 10 tasks with identical GPT-4o call
6. Fill in the results table
7. Write 1 paragraph interpretation
8. Do NOT proceed to build G2 until this experiment is complete and results are understood
