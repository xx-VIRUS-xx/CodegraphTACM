"""query_rewriter.py — G4-A: LLM-based query decomposition.

Converts a natural-language bug report into a set of targeted sub-queries
phrased as implementation actions rather than user symptoms.

Design:
- Single Claude API call with a structured prompt
- Returns 3-5 sub-queries, each targeting a different aspect of the bug
- Caches results in memory per (query, model) to avoid redundant API calls
- Falls back to original query if API call fails
- Sub-queries are joined back into the FTS5 search in crg_adapter

Why this matters (Mode B):
  NL symptom: "session always hits database even when already in identity map"
  FTS5 finds:  nothing (no token overlap with Session.get)
  Sub-queries: ["get object from identity map", "session identity map lookup",
                "bypass database fetch cached instance", "session get primary key"]
  FTS5 finds:  Session.get, Session._get_impl, IdentityMap.__getitem__
"""

from __future__ import annotations

import hashlib
import logging
import os

logger = logging.getLogger(__name__)

# In-memory cache: sha256(query+model) -> list[str]
_rewrite_cache: dict[str, list[str]] = {}

REWRITE_MODEL = "claude-haiku-4-5-20251001"  # fast + cheap; sub-queries don't need Opus

SYSTEM_PROMPT = """\
You are a code search assistant. Given a natural-language bug report, generate \
3 to 5 short search queries that a developer would use to find the buggy function \
in source code.

Rules:
- Each query must be 3-8 words phrased as an implementation action or code concept, \
not a user symptom
- Do NOT include function names, file names, or class names
- Do NOT repeat the same concept in multiple queries
- Output ONLY the queries, one per line, no numbering, no punctuation at end
- Think about: the operation being performed, the data structure involved, \
the condition that triggers the bug, the subsystem or component
"""


def _cache_key(query: str, model: str) -> str:
    return hashlib.sha256(f"{model}:{query}".encode()).hexdigest()[:16]


def rewrite_query(query: str, model: str = REWRITE_MODEL) -> list[str]:
    """Return a list of targeted sub-queries for the given NL bug report.

    Returns [query] (original only) on API failure so callers degrade gracefully.
    """
    key = _cache_key(query, model)
    if key in _rewrite_cache:
        return _rewrite_cache[key]

    try:
        import anthropic

        client = anthropic.Anthropic()
        response = client.messages.create(
            model=model,
            max_tokens=256,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": query}],
        )
        raw = response.content[0].text.strip()
        sub_queries = [line.strip() for line in raw.splitlines() if line.strip()]
        # Sanity: keep 2-8 sub-queries, reject empties or ones that are too long
        sub_queries = [q for q in sub_queries if 2 <= len(q.split()) <= 12][:8]
        if not sub_queries:
            sub_queries = [query]
        logger.debug("Query rewriter: %d sub-queries for %r", len(sub_queries), query[:60])
        _rewrite_cache[key] = sub_queries
        return sub_queries
    except Exception as exc:
        logger.warning("Query rewriter unavailable: %s", exc)
        _rewrite_cache[key] = [query]
        return [query]


def rewrite_query_if_enabled(query: str, use_rewriter: bool = True) -> list[str]:
    """Wrapper that respects the use_rewriter flag and TACM_NO_REWRITE env var."""
    if not use_rewriter or os.environ.get("TACM_NO_REWRITE"):
        return [query]
    return rewrite_query(query)

