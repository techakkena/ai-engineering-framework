from __future__ import annotations

from ai_rag.embeddings.constants import (
    DEFAULT_EMBEDDING_DIMENSIONS,
    DEFAULT_EMBEDDING_MODEL,
    MODEL_DIMENSIONS,
    SUPPORTED_EMBEDDING_MODELS,
)


def test_default_model():
    assert DEFAULT_EMBEDDING_MODEL == "text-embedding-3-small"


def test_supported_models():
    assert "text-embedding-3-small" in SUPPORTED_EMBEDDING_MODELS


def test_dimensions():
    assert DEFAULT_EMBEDDING_DIMENSIONS == 1536
    assert MODEL_DIMENSIONS["text-embedding-3-large"] == 3072
