# TACM In Plain English

## What We Built

We built a system that helps an AI coding assistant understand a software project the way a good engineer would.

Instead of dumping random files into the AI prompt, TACM first organizes the codebase into three levels:

- `Files` — the big containers in the project
- `Classes` — the main structures inside those files
- `Functions` — the individual pieces of behavior where bugs and logic usually live

TACM then decides which pieces are most relevant to a question like:

- "Why is this bug happening?"
- "What part of the code handles this?"
- "How does this system work?"

The result is a focused packet of context that gives the AI a better starting point than plain keyword search alone.

## Why This Matters

Modern coding agents often work by searching code with text similarity:

- keyword search
- embedding search
- hybrid search

Those methods are useful, but they mostly look for text that "sounds similar" to the query.

Our system adds something different:

- it understands the structure of the repository
- it knows which functions call which other functions
- it knows which classes contain which methods
- it can bring related pieces together instead of treating each function as an isolated document

That matters because many real bugs are not easy to find from wording alone. Sometimes the right function is only obvious when you understand how nearby code connects to it.

## What Makes TACM Different

TACM is not just a search engine over source files.

It is a `layered graph-based context selector`.

That means it:

1. turns the repository into a graph of connected code units
2. ranks those units using both text relevance and structural signals
3. chooses context under a token budget so the AI sees the most useful parts first

One important feature is the `containment bonus`.

If TACM already thinks a class is relevant, it gives extra credit to methods inside that class. This helps the AI receive a coherent cluster of related code instead of disconnected snippets.

## What We Found So Far

In retrieval benchmarks, TACM currently performs very well.

It does better than:

- plain BM25 keyword retrieval
- RepoMap-style structural ranking
- the dense and hybrid baselines we tested on the current benchmark

That means TACM is good at finding the right code context for bug localization.

However, retrieval is only part of the full agent problem.

When we test end-to-end bug fixing, the coding agent still fails often. In many cases the issue is no longer "finding the right file." The harder problem becomes:

- understanding enough related code at once
- writing a correct patch
- succeeding within a limited number of agent steps

## The Honest Summary

What we have built is a strong `code understanding and context selection system` for AI coding agents.

It is especially promising for bugs that are structurally hard to find, where text search alone is not enough.

The current research result is:

- strong evidence that TACM improves retrieval quality
- early evidence that it gives unique value on structure-dependent bugs
- not yet proof that it is the best complete coding-agent setup overall

## The Big Picture

You can think of TACM as a better map for the AI.

A normal search system says:
"Here are some files that look textually similar."

TACM says:
"Here is the part of the codebase this question is really about, here are the key files, here is the class that matters, and here are the functions connected to the behavior."

That is the core idea we have built and validated so far.
