"""semantic.py — G3: semantic embedding search as a retrieval signal.

Uses sentence-transformers/all-MiniLM-L6-v2 (384-dim) via transformers+torch.
MiniLM is fine-tuned with contrastive loss for sentence similarity — produces
well-spread embeddings. CodeBERT was tried but produces collapsed embeddings
(all cosine sims ~0.97) without task-specific fine-tuning.

Do NOT use sentence_transformers package — broken TF import on NumPy 2.x.

Design:
- Corpus embeddings are pre-computed once and cached to .npy alongside the DB.
- Cache filename includes model slug to avoid cross-model collisions.
- At query time: embed the query, compute cosine similarities, inject scores.
- Result: per-node semantic_score in [0, 1] — highest similarity to the query.

This is G3: a 5th scoring signal for the hybrid_full resolver strategy.
Addresses Mode B misses (lexical gap between NL symptom and function name).
"""

from __future__ import annotations

import hashlib
import logging
import os
from pathlib import Path
from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from code_review_graph.graph import GraphNode

logger = logging.getLogger(__name__)

# Set before transformers is imported so its lazy loader skips TF
os.environ.setdefault("TRANSFORMERS_NO_TF", "1")
os.environ.setdefault("USE_TF", "0")

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
_model = None
_tokenizer = None


def _get_device():
    import torch
    if torch.backends.mps.is_available():
        return torch.device("mps")
    if torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")


def _load_model():
    global _model, _tokenizer
    if _model is not None:
        return _model, _tokenizer
    try:
        import torch
        from transformers import AutoModel, AutoTokenizer

        _tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        _model = AutoModel.from_pretrained(MODEL_NAME)
        _model.eval()
        logger.debug("G3 semantic: model loaded")
        return _model, _tokenizer
    except Exception as exc:
        logger.warning("G3 semantic embeddings unavailable: %s", exc)
        return None, None


def _best_device() -> "torch.device":
    """Return MPS > CUDA > CPU. MiniLM works correctly on all; use fastest."""
    import torch
    if torch.backends.mps.is_available():
        return torch.device("mps")
    if torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")


def _embed(texts: list[str], batch_size: int = 32) -> np.ndarray | None:
    """Embed a list of texts. Returns float32 array shape (N, 384) or None."""
    if not texts:
        return None
    model, tok = _load_model()
    if model is None:
        return None

    import torch

    # Use MPS/CUDA for large batch corpus builds; CPU for single-query inference
    # (MPS launch overhead ~500ms dominates for 1-text batches).
    use_gpu = len(texts) >= 32
    device = _best_device() if use_gpu else torch.device("cpu")
    all_vecs: list[np.ndarray] = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        inputs = tok(
            batch,
            padding=True,
            truncation=True,
            max_length=256,
            return_tensors="pt",
        )
        inputs = {k: v.to(device) for k, v in inputs.items()}
        with torch.no_grad():
            out = model.to(device)(**inputs)
        mask = inputs["attention_mask"].unsqueeze(-1).float()
        vecs = (out.last_hidden_state * mask).sum(1) / mask.sum(1)
        vecs = torch.nn.functional.normalize(vecs, dim=1).cpu().numpy().astype(np.float32)
        all_vecs.append(vecs)
    model.to("cpu")  # return to CPU so next single-query embed is fast
    return np.vstack(all_vecs)


def _node_text(n: "GraphNode") -> str:
    """Build a text representation for a node to embed."""
    parts = [n.name, n.qualified_name]
    if n.params:
        parts.append(n.params[:200])
    if n.return_type:
        parts.append(n.return_type)
    # Include source text from the node's file (first 400 chars)
    if n.file_path and n.line_start and n.line_end:
        try:
            lines = Path(n.file_path).read_text(errors="replace").splitlines()
            body = "\n".join(lines[max(0, n.line_start - 1) : min(len(lines), n.line_end)])
            parts.append(body[:400])
        except OSError:
            pass
    return " ".join(parts)


def _model_slug() -> str:
    """Short slug for the current model, used in cache filenames."""
    return MODEL_NAME.replace("/", "--").replace(".", "_")


def _corpus_cache_path(db_path: str | Path) -> Path:
    """Path for cached corpus embeddings (.npy) alongside the DB."""
    db = Path(db_path)
    return db.parent / f"tacm_corpus_embeddings_{_model_slug()}.npy"


def _corpus_meta_path(db_path: str | Path) -> Path:
    db = Path(db_path)
    return db.parent / f"tacm_corpus_meta_{_model_slug()}.txt"


def _corpus_hash(nodes: list["GraphNode"]) -> str:
    """Fast hash of node qualified_names + line ranges for cache invalidation."""
    h = hashlib.sha256()
    for n in sorted(nodes, key=lambda x: x.qualified_name):
        h.update(f"{n.qualified_name}:{n.line_start}:{n.line_end}\n".encode())
    return h.hexdigest()[:16]


class SemanticIndex:
    """Pre-computed embedding index for a production node corpus.

    Usage:
        idx = SemanticIndex.build(db_path, prod_nodes)
        scores = idx.query("session always hits database", top_k=20)
        # scores: dict[qualified_name, float] with cosine similarity [0..1]
    """

    def __init__(
        self,
        qualified_names: list[str],
        vectors: np.ndarray,
    ) -> None:
        self.qualified_names = qualified_names
        self.vectors = vectors  # shape (N, 384), float32, unit-normed

    @classmethod
    def build(
        cls,
        db_path: str | Path,
        prod_nodes: list["GraphNode"],
        force_rebuild: bool = False,
    ) -> "SemanticIndex | None":
        """Build or load a cached corpus index.

        Returns None if embeddings are unavailable (model load failure).
        """
        if not prod_nodes:
            return None

        cache_npy = _corpus_cache_path(db_path)
        cache_meta = _corpus_meta_path(db_path)
        corpus_hash = _corpus_hash(prod_nodes)

        # Load from cache if valid
        if not force_rebuild and cache_npy.exists() and cache_meta.exists():
            try:
                cached_hash = cache_meta.read_text().strip()
                if cached_hash == corpus_hash:
                    vecs = np.load(str(cache_npy))
                    qnames = [n.qualified_name for n in sorted(prod_nodes, key=lambda x: x.qualified_name)]
                    logger.debug("SemanticIndex: loaded %d embeddings from cache", len(qnames))
                    return cls(qnames, vecs)
            except Exception as exc:
                logger.warning("SemanticIndex cache load failed, rebuilding: %s", exc)

        # Build from scratch
        sorted_nodes = sorted(prod_nodes, key=lambda x: x.qualified_name)
        texts = [_node_text(n) for n in sorted_nodes]
        vecs = _embed(texts, batch_size=128)
        if vecs is None:
            return None

        # Save to cache
        try:
            np.save(str(cache_npy), vecs)
            cache_meta.write_text(corpus_hash)
        except Exception as exc:
            logger.warning("SemanticIndex: could not save cache: %s", exc)

        qnames = [n.qualified_name for n in sorted_nodes]
        logger.debug("SemanticIndex: built %d embeddings", len(qnames))
        return cls(qnames, vecs)

    def query(self, query_text: str, top_k: int = 30) -> dict[str, float]:
        """Return top_k nodes by cosine similarity. Scores are in [0, 1]."""
        qvec = _embed([query_text])
        if qvec is None:
            return {}
        sims = (self.vectors @ qvec.T).flatten()
        # Shift from [-1, 1] to [0, 1]
        sims_norm = (sims + 1.0) / 2.0
        top_idx = np.argsort(-sims_norm)[:top_k]
        return {self.qualified_names[i]: float(sims_norm[i]) for i in top_idx}
