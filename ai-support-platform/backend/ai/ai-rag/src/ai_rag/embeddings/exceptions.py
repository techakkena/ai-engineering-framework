from __future__ import annotations

"""Exceptions for embeddings."""


class EmbeddingError(Exception):
    """Base embedding exception."""


class InvalidEmbeddingModelError(EmbeddingError):
    """Raised when an embedding model is unsupported."""


class InvalidEmbeddingVectorError(EmbeddingError):
    """Raised when an embedding vector is invalid."""
