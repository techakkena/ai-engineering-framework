"""
Unit tests for ai_models.embeddings.constants.
"""

from __future__ import annotations

from ai_models.embeddings.constants import (
    BGE,
    COHERE,
    DEFAULT_BATCH_SIZE,
    DEFAULT_EMBEDDING_DIMENSIONS,
    DEFAULT_EMBEDDING_MODEL,
    DEFAULT_EMBEDDING_PROVIDER,
    DEFAULT_RETRIES,
    DEFAULT_TIMEOUT,
    E5,
    INSTRUCTOR,
    OLLAMA,
    OPENAI,
    SUPPORTED_EMBEDDING_PROVIDERS,
    VOYAGE,
)


def test_embedding_defaults() -> None:
    """Test default embedding configuration."""
    assert (
        DEFAULT_EMBEDDING_MODEL
        == "text-embedding-3-small"
    )
    assert DEFAULT_EMBEDDING_PROVIDER == OPENAI
    assert DEFAULT_EMBEDDING_DIMENSIONS == 1536


def test_supported_embedding_providers() -> None:
    """Test supported embedding providers."""
    expected = {
        OPENAI,
        VOYAGE,
        COHERE,
        BGE,
        E5,
        INSTRUCTOR,
        OLLAMA,
    }

    assert SUPPORTED_EMBEDDING_PROVIDERS == expected


def test_supported_embedding_providers_are_immutable() -> None:
    """Supported providers should be immutable."""
    assert isinstance(
        SUPPORTED_EMBEDDING_PROVIDERS,
        frozenset,
    )


def test_embedding_configuration_defaults() -> None:
    """Test embedding configuration defaults."""
    assert DEFAULT_BATCH_SIZE == 100
    assert DEFAULT_TIMEOUT == 60
    assert DEFAULT_RETRIES == 3