"""cochange.py — G4-E: git co-change signal.

Mines the git history of a repository to build a co-change index:
functions that are frequently modified together in fix commits are
likely structurally related even if the call graph doesn't connect them.

Use case:
  sbug04 requires touching both _AbstractEntityRegistry._getitem AND
  SelectInLoad.create_row_processor — they always co-change in ORM fixes
  but have no direct call edge. A co-change index surfaces both from one hit.

Design:
  1. Walk git log (fix commits — merges excluded)
  2. For each commit, extract changed Python functions via diff hunk parsing
  3. Build a co-occurrence matrix: count(A, B) = times A and B changed together
  4. At query time: given a set of FTS5 hit functions, expand with their
     most frequent co-change partners

Index is cached to .json alongside the DB. Rebuild when HEAD changes.

Performance:
  - git log + diff parsing: ~2-10s for repos with <10k commits
  - Index size: typically <1MB for medium repos
  - Query time: O(hits * max_partners) — negligible
"""

from __future__ import annotations

import hashlib
import json
import logging
import subprocess
from collections import defaultdict
from pathlib import Path

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Git parsing
# ---------------------------------------------------------------------------

def _get_commits(repo_root: Path, max_commits: int = 2000) -> list[str]:
    """Return list of commit SHAs (no merges, most recent first)."""
    try:
        result = subprocess.run(
            ["git", "log", "--no-merges", "--format=%H", f"-{max_commits}"],
            cwd=repo_root, capture_output=True, text=True, timeout=30,
        )
        return [s.strip() for s in result.stdout.splitlines() if s.strip()]
    except Exception as exc:
        logger.warning("cochange: git log failed: %s", exc)
        return []


def _get_changed_functions(repo_root: Path, commit: str) -> list[str]:
    """Return list of 'ClassName.method' changed in a commit (heuristic)."""
    try:
        result = subprocess.run(
            ["git", "show", "--unified=3", "--no-color", commit, "--", "*.py"],
            cwd=repo_root, capture_output=True, text=True, timeout=15,
        )
    except Exception:
        return []

    import re
    hunk_re = re.compile(r"^@@ .+ @@ ?(.*)$")
    func_re = re.compile(r"([\w.]+)\(")

    functions: list[str] = []
    for line in result.stdout.splitlines():
        m = hunk_re.match(line)
        if m:
            context = m.group(1).strip()
            # context often looks like "def foo(..." or "class Foo" or "def bar(self"
            fm = func_re.search(context)
            if fm:
                name = fm.group(1).rstrip(".")
                if name and not name.startswith("test_"):
                    functions.append(name)
    return list(set(functions))


def _repo_head(repo_root: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo_root, capture_output=True, text=True, timeout=5,
        )
        return result.stdout.strip()[:16]
    except Exception:
        return "unknown"


# ---------------------------------------------------------------------------
# Index
# ---------------------------------------------------------------------------

class CoChangeIndex:
    """Co-change frequency index for a repository.

    Usage:
        idx = CoChangeIndex.build(repo_root, db_path)
        partners = idx.expand(["Session.get"], top_k=5)
        # partners: ["Session._get_impl", "IdentityMap.__contains__", ...]
    """

    def __init__(self, counts: dict[str, dict[str, int]]) -> None:
        # counts[A][B] = number of commits where A and B both changed
        self._counts = counts

    @classmethod
    def build(
        cls,
        repo_root: Path,
        db_path: str | Path,
        max_commits: int = 2000,
        force_rebuild: bool = False,
    ) -> "CoChangeIndex":
        cache_path = _cache_path(db_path)
        head = _repo_head(repo_root)

        # Load from cache if HEAD hasn't changed
        if not force_rebuild and cache_path.exists():
            try:
                data = json.loads(cache_path.read_text())
                if data.get("head") == head:
                    logger.debug("CoChangeIndex: loaded from cache (%s)", cache_path.name)
                    return cls(data["counts"])
            except Exception as exc:
                logger.warning("CoChangeIndex cache load failed: %s", exc)

        # Build from scratch
        logger.debug("CoChangeIndex: building from git history (max %d commits)...", max_commits)
        commits = _get_commits(repo_root, max_commits)
        counts: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))

        for sha in commits:
            funcs = _get_changed_functions(repo_root, sha)
            # Record all pairs
            for i, a in enumerate(funcs):
                for b in funcs[i + 1:]:
                    counts[a][b] += 1
                    counts[b][a] += 1

        # Serialize (defaultdict -> plain dict for JSON)
        plain = {k: dict(v) for k, v in counts.items()}
        try:
            cache_path.write_text(json.dumps({"head": head, "counts": plain}))
        except Exception as exc:
            logger.warning("CoChangeIndex: could not save cache: %s", exc)

        logger.debug("CoChangeIndex: built index over %d commits, %d functions", len(commits), len(plain))
        return cls(plain)

    def expand(self, function_names: list[str], top_k: int = 5, min_count: int = 2) -> list[str]:
        """Return top_k co-change partners for the given function names.

        Args:
            function_names: Simple names or "Class.method" strings to expand.
            top_k: Max partners to return.
            min_count: Minimum co-change count to be included.

        Returns:
            List of function names (simple or Class.method), sorted by frequency.
        """
        partner_scores: dict[str, int] = defaultdict(int)
        for name in function_names:
            # Try exact match, then just the method name part
            for key in [name, name.split(".")[-1]]:
                if key in self._counts:
                    for partner, count in self._counts[key].items():
                        if count >= min_count and partner not in function_names:
                            partner_scores[partner] += count

        sorted_partners = sorted(partner_scores.items(), key=lambda x: -x[1])
        return [p for p, _ in sorted_partners[:top_k]]


def _cache_path(db_path: str | Path) -> Path:
    db = Path(db_path)
    return db.parent / "tacm_cochange.json"


# ---------------------------------------------------------------------------
# Integration with crg_adapter
# ---------------------------------------------------------------------------

_cochange_cache: dict[str, "CoChangeIndex | None"] = {}


def get_cochange_index(repo_root: Path, db_path: str | Path) -> "CoChangeIndex | None":
    """Lazily build or load the co-change index. Returns None on failure."""
    key = str(db_path)
    if key not in _cochange_cache:
        try:
            _cochange_cache[key] = CoChangeIndex.build(repo_root, db_path)
        except Exception as exc:
            logger.warning("CoChangeIndex unavailable: %s", exc)
            _cochange_cache[key] = None
    return _cochange_cache[key]
