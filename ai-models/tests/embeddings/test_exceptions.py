"""
Unit tests for ai_models.embeddings.exceptions.
"""

from __future__ import annotations

import pytest

from ai_models.embeddings.exceptions import (
    EmbeddingConfigurationError,
    EmbeddingError,
    EmbeddingValidationError,
    InvalidEmbeddingProviderError,
)


def test_embedding_error_default_message() -> None:
    """Test EmbeddingError default message."""
    error = EmbeddingError()

    assert (
        str(error)
        == "An embedding error occurred."
    )


def test_embedding_error_custom_message() -> None:
    """Test EmbeddingError custom message."""
    error = EmbeddingError(
        "Custom embedding error.",
    )

    assert str(error) == "Custom embedding error."


@pytest.mark.parametrize(
    "provider",
    [
        "",
        "azure",
        "bedrock",
    ],
)
def test_invalid_embedding_provider_error(
    provider: str,
) -> None:
    """Test InvalidEmbeddingProviderError."""
    error = InvalidEmbeddingProviderError(
        provider,
    )

    assert isinstance(
        error,
        EmbeddingError,
    )

    assert error.provider == provider

    assert (
        str(error)
        == (
            f"Invalid embedding provider: "
            f"'{provider}'."
        )
    )


def test_embedding_configuration_error() -> None:
    """Test EmbeddingConfigurationError."""
    configuration = "dimensions"

    error = EmbeddingConfigurationError(
        configuration,
    )

    assert isinstance(
        error,
        EmbeddingError,
    )

    assert (
        error.configuration
        == configuration
    )

    assert (
        str(error)
        == (
            "Invalid embedding configuration: "
            f"'{configuration}'."
        )
    )


def test_embedding_validation_error() -> None:
    """Test EmbeddingValidationError."""
    model = "text-embedding-3-small"
    reason = "unsupported dimensions"

    error = EmbeddingValidationError(
        model,
        reason,
    )

    assert isinstance(
        error,
        EmbeddingError,
    )

    assert error.model == model
    assert error.reason == reason

    assert (
        str(error)
        == (
            f"Embedding model '{model}' "
            f"validation failed: {reason}."
        )
    )