"""reranker.py — G4-D: LLM cross-encoder re-ranking.

Takes the top-K candidates after G1+G2+G3 scoring and re-ranks them by
asking Claude to score each (bug_report, function_signature+body) pair.

Why this matters:
  BM25 + semantic retrieval gets the GT function *into* the candidate pool.
  But MRR is low because the GT is ranked #20-50 behind irrelevant but
  lexically similar functions. A cross-encoder that jointly reads the bug
  report AND the function body can push the GT to rank #1-5.

Design:
  - Re-rank top-K (default 20) candidates by relevance score from Claude
  - Returns candidates with updated hybrid_score = rerank_score
  - Falls back to original ordering on API failure
  - Caches scores in memory per (query_hash, node_id)

Cost: ~1-3K tokens per query at top-20. Use claude-haiku for speed/cost.
"""

from __future__ import annotations

import hashlib
import json
import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .resolver import ScoredNode

logger = logging.getLogger(__name__)

RERANK_MODEL = "claude-haiku-4-5-20251001"
RERANK_TOP_K = 20  # candidates to re-rank

# In-memory cache: (query_hash, node_id) -> float score
_rerank_cache: dict[tuple[str, str], float] = {}

RERANK_SYSTEM = """\
You are a code relevance scorer. Given a bug report and a Python function, \
output a JSON object with a single key "score" from 0.0 to 1.0 indicating how \
likely this function contains or directly causes the described bug.

Scoring guide:
  1.0 = this is almost certainly the buggy function
  0.7 = this function is closely related to the bug
  0.4 = this function is in the same subsystem but probably not buggy
  0.1 = this function is unrelated
  0.0 = completely unrelated

Output ONLY valid JSON: {"score": 0.XX}
"""


def _query_hash(query: str) -> str:
    return hashlib.sha256(query.encode()).hexdigest()[:12]


def _rerank_one(client, query: str, node: "ScoredNode", model: str) -> float:
    """Score a single (query, node) pair. Returns cached result if available."""
    qh = _query_hash(query)
    cache_key = (qh, node.node_id)
    if cache_key in _rerank_cache:
        return _rerank_cache[cache_key]

    # Build a compact function representation
    func_repr = f"Function: {node.node_id}\n"
    if node.source_text:
        # Truncate to ~400 chars to keep tokens low
        body = node.source_text[:400]
        if len(node.source_text) > 400:
            body += "\n    # ..."
        func_repr += body
    else:
        func_repr += f"(no source — {node.name})"

    prompt = f"Bug report:\n{query}\n\n{func_repr}"

    try:
        response = client.messages.create(
            model=model,
            max_tokens=32,
            system=RERANK_SYSTEM,
            messages=[{"role": "user", "content": prompt}],
        )
        raw = response.content[0].text.strip()
        score = float(json.loads(raw)["score"])
        score = max(0.0, min(1.0, score))
    except Exception as exc:
        logger.debug("Reranker score failed for %s: %s", node.node_id, exc)
        score = node.hybrid_score  # fall back to existing score

    _rerank_cache[cache_key] = score
    return score


def rerank(
    query: str,
    candidates: list["ScoredNode"],
    top_k: int = RERANK_TOP_K,
    model: str = RERANK_MODEL,
) -> list["ScoredNode"]:
    """Re-rank the top_k candidates by LLM relevance score.

    Returns the full candidate list with top_k re-ranked at the front,
    remaining candidates appended in original order. Falls back to
    original list on import/API failure.

    Args:
        query: The original NL bug report.
        candidates: Sorted candidate list (already scored by G1+G2+G3).
        top_k: How many top candidates to re-rank (rest kept as-is).
        model: Claude model to use.

    Returns:
        New candidate list with re-ranked top_k at front.
    """
    if not candidates:
        return candidates

    try:
        import anthropic
        client = anthropic.Anthropic()
    except Exception as exc:
        logger.warning("Reranker unavailable (anthropic import failed): %s", exc)
        return candidates

    to_rerank = candidates[:top_k]
    rest = candidates[top_k:]

    # Score each candidate
    scored_rerank: list[tuple[float, "ScoredNode"]] = []
    for node in to_rerank:
        score = _rerank_one(client, query, node, model)
        # Return a copy with updated hybrid_score so resolver uses new ranking
        import dataclasses
        updated = dataclasses.replace(node, hybrid_score=score)
        scored_rerank.append((score, updated))

    scored_rerank.sort(key=lambda x: -x[0])
    reranked = [node for _, node in scored_rerank]

    logger.debug(
        "Reranker: top-3 after rerank = %s",
        [n.node_id for n in reranked[:3]],
    )
    return reranked + rest
