"""file_router.py — G4-F: two-stage file→function retrieval.

For large codebases (>5k nodes), function-level FTS5 drowns in irrelevant hits
because every subsystem has functions with common names (get, set, update, execute).

Two-stage approach:
  Stage 1 — File routing: embed each source file's path + module docstring,
             find the top-K most relevant files to the query.
  Stage 2 — Function retrieval: run FTS5 + semantic search restricted to
             functions within the top-K files only.

This reduces the effective corpus from 15k nodes to ~200-500 nodes before
scoring, dramatically improving precision without hurting recall
(assuming the GT file is retrieved in Stage 1).

Design:
  - File embeddings use the same CodeBERT model as semantic.py
  - File text = file path + module docstring + all function names in file
  - Cache file embeddings to .npy alongside DB (separate from corpus cache)
  - At query time: cosine similarity to get top-K files, then restrict pool

Integration:
  Activated when token_budget < FULL_CORPUS_BUDGET_THRESHOLD AND
  corpus size > FILE_ROUTER_MIN_NODES (default 3000).
"""

from __future__ import annotations

import hashlib
import logging
from pathlib import Path
from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from code_review_graph.graph import GraphStore

logger = logging.getLogger(__name__)

FILE_ROUTER_MIN_NODES = 3000   # only activate for large corpora
FILE_ROUTER_TOP_K_FILES = 15   # how many files to route to in Stage 1

_file_router_cache: dict[str, "FileRouter | None"] = {}


def _file_text(file_path: str, func_names: list[str]) -> str:
    """Build text representation for a source file."""
    parts = [file_path.replace("/", " ").replace("_", " ").replace(".py", "")]
    # Add module docstring if available
    try:
        src = Path(file_path).read_text(errors="replace")
        lines = src.splitlines()
        # Grab first non-empty lines up to 8 (likely module docstring)
        doc_lines = []
        in_doc = False
        for line in lines[:30]:
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith('"""') or stripped.startswith("'''"):
                in_doc = not in_doc
                doc_lines.append(stripped)
                if not in_doc and len(doc_lines) > 1:
                    break
            elif in_doc:
                doc_lines.append(stripped)
            elif doc_lines:
                break
        if doc_lines:
            parts.append(" ".join(doc_lines)[:200])
    except OSError:
        pass
    # Add all function names in the file (tells the embedder what subsystem this is)
    parts.append(" ".join(func_names[:30]))
    return " ".join(parts)


def _file_hash(file_groups: dict[str, list[str]]) -> str:
    h = hashlib.sha256()
    for fp in sorted(file_groups.keys()):
        h.update(f"{fp}:{','.join(sorted(file_groups[fp]))}\n".encode())
    return h.hexdigest()[:16]


class FileRouter:
    """Stage-1 file-level router for large codebases."""

    def __init__(self, file_paths: list[str], vectors: np.ndarray) -> None:
        self.file_paths = file_paths
        self.vectors = vectors  # (N_files, 768), unit-normed

    @classmethod
    def build(
        cls,
        db_path: str | Path,
        prod_nodes,
        force_rebuild: bool = False,
    ) -> "FileRouter | None":
        """Build or load file-level embedding index."""
        # Group nodes by file
        file_groups: dict[str, list[str]] = {}
        for n in prod_nodes:
            if n.file_path:
                file_groups.setdefault(n.file_path, []).append(n.name)

        if len(file_groups) < 10:
            return None  # too small to bother

        cache_npy = _cache_path_npy(db_path)
        cache_meta = _cache_path_meta(db_path)
        fhash = _file_hash(file_groups)

        if not force_rebuild and cache_npy.exists() and cache_meta.exists():
            try:
                if cache_meta.read_text().strip() == fhash:
                    vecs = np.load(str(cache_npy))
                    fps = sorted(file_groups.keys())
                    logger.debug("FileRouter: loaded %d file embeddings from cache", len(fps))
                    return cls(fps, vecs)
            except Exception as exc:
                logger.warning("FileRouter cache load failed: %s", exc)

        # Build from scratch
        from .semantic import _embed
        sorted_fps = sorted(file_groups.keys())
        texts = [_file_text(fp, file_groups[fp]) for fp in sorted_fps]
        vecs = _embed(texts, batch_size=64)
        if vecs is None:
            return None

        try:
            np.save(str(cache_npy), vecs)
            cache_meta.write_text(fhash)
        except Exception as exc:
            logger.warning("FileRouter: could not save cache: %s", exc)

        logger.debug("FileRouter: built embeddings for %d files", len(sorted_fps))
        return cls(sorted_fps, vecs)

    def route(self, query: str, top_k: int = FILE_ROUTER_TOP_K_FILES) -> set[str]:
        """Return top_k file paths most relevant to the query."""
        from .semantic import _embed
        qvec = _embed([query])
        if qvec is None:
            return set(self.file_paths)  # fail open — return all files
        sims = (self.vectors @ qvec.T).flatten()
        sims_norm = (sims + 1.0) / 2.0
        top_idx = np.argsort(-sims_norm)[:top_k]
        result = {self.file_paths[i] for i in top_idx}
        logger.debug("FileRouter: routed to %d files: %s", len(result),
                     [Path(p).name for p in list(result)[:5]])
        return result


def _cache_path_npy(db_path: str | Path) -> Path:
    db = Path(db_path)
    return db.parent / "tacm_file_router.npy"


def _cache_path_meta(db_path: str | Path) -> Path:
    db = Path(db_path)
    return db.parent / "tacm_file_router_meta.txt"


def get_file_router(store: "GraphStore", prod_nodes) -> "FileRouter | None":
    """Lazily build or load the file router for this store."""
    key = store.db_path
    if key not in _file_router_cache:
        try:
            _file_router_cache[key] = FileRouter.build(store.db_path, prod_nodes)
        except Exception as exc:
            logger.warning("FileRouter unavailable: %s", exc)
            _file_router_cache[key] = None
    return _file_router_cache[key]
