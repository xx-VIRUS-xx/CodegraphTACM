# THESIS.md — CodeGraph-TACM Research Claim

## One-Sentence Thesis

> CodeGraph-TACM introduces a query-adaptive resolver that dynamically weights four graph signal layers — syntactic, causal, semantic, and historical — to construct the minimum-token, maximum-value context payload for any LLM query about a codebase, without the LLM ever touching raw source code.

---

## The Research Question

**What is the minimal structured representation of a codebase that enables correct LLM reasoning, and which graph signal layers are necessary to achieve it?**

This is a representation research question, not a prompt engineering question. The system is the instrument. The answer to the research question is the contribution.

---

## The Claim (Precise)

1. **Four graph layers are necessary and sufficient** for code intelligence retrieval. Remove any one and measurable quality drops. This is demonstrated via ablation.

2. **Query-adaptive weighting outperforms static weighting** across code reasoning task types. Different tasks (bug localisation, similarity search, explanation, completion) require different signal emphasis.

3. **Two-phase skeleton/payload resolution** reduces retrieval token cost by an additional 3x–5x over single-phase graph retrieval, with no quality loss.

4. **The resolver's selectivity — not the LLM's capability — determines answer quality** for repository-scale code reasoning tasks.

---

## What This Is Not

- Not a new LLM architecture
- Not a fine-tuning approach
- Not a prompt template system
- Not a "better chunking" strategy

It is a **code knowledge representation + retrieval architecture** that sits between a codebase and any LLM.

---

## Positioning Against Prior Work

| System | Graph layers | Pointer/address layer | Query-adaptive weights | Two-phase resolution |
|---|---|---|---|---|
| GraphRAG | 1 (ML-extracted) | No | No | No |
| CodexGraph | 1 (AST) | No | No | No |
| CGM | 1 (AST) | No | No | No |
| GraphCoder | 1 (AST) | No | No | No |
| **CodeGraph-TACM** | **4 (AST+CFG+DFG+Semantic+Historical)** | **Yes (internal)** | **Yes** | **Yes** |

---

## Success Criteria

The thesis is validated if:
1. Four-graph resolver outperforms single-graph (G1 only) on bug localisation P@5 by ≥15%
2. Query-adaptive weights outperform static equal weights by ≥10% on mixed-task benchmark
3. Token usage is ≤30% of naive RAG at equal or better answer quality (GPT-4o judge)
4. Each graph contributes independently — removing any single graph degrades performance

---

## Updated Framing (Post Discussion)

The original framing — "pointer-addressed context memory" — was architecturally correct but the pointer concept needed clarification:

- Pointers exist **internally** between graphs and the resolver (Phase 1 skeleton)
- Pointers are **never exposed** to the LLM
- The LLM always receives resolved natural text
- The innovation is the **two-phase resolver + four-graph scoring**, not a novel prompt encoding

This does not weaken the claim. It makes it more precise and more defensible.
