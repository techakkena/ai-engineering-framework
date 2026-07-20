from __future__ import annotations

from ai_rag.embeddings.exceptions import (
    EmbeddingError,
    InvalidEmbeddingModelError,
    InvalidEmbeddingVectorError,
)


def test_embedding_error():
    assert issubclass(
        EmbeddingError,
        Exception,
    )


def test_invalid_model_error():
    assert issubclass(
        InvalidEmbeddingModelError,
        EmbeddingError,
    )


def test_invalid_vector_error():
    assert issubclass(
        InvalidEmbeddingVectorError,
        EmbeddingError,
    )
