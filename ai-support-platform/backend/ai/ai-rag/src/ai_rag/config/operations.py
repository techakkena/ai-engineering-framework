from __future__ import annotations

"""Operations for ai-rag configuration."""

from .constants import (
    DEFAULT_CHUNK_OVERLAP,
    DEFAULT_CHUNK_SIZE,
    DEFAULT_EMBEDDING_MODEL,
    DEFAULT_RERANKER,
    DEFAULT_RETRIEVER,
    DEFAULT_TOP_K,
    DEFAULT_VECTOR_STORE,
)


def default_chunk_size() -> int:
    """Return the default chunk size."""

    return DEFAULT_CHUNK_SIZE


def default_chunk_overlap() -> int:
    """Return the default chunk overlap."""

    return DEFAULT_CHUNK_OVERLAP


def default_embedding_model() -> str:
    """Return the default embedding model."""

    return DEFAULT_EMBEDDING_MODEL


def default_vector_store() -> str:
    """Return the default vector store."""

    return DEFAULT_VECTOR_STORE


def default_retriever() -> str:
    """Return the default retriever."""

    return DEFAULT_RETRIEVER


def default_reranker() -> str:
    """Return the default reranker."""

    return DEFAULT_RERANKER


def default_top_k() -> int:
    """Return the default retrieval count."""

    return DEFAULT_TOP_K
