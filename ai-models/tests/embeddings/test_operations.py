"""
Unit tests for ai_models.embeddings.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_models.embeddings.exceptions import (
    InvalidEmbeddingProviderError,
)
from ai_models.embeddings.operations import (
    build_embedding_id,
    is_supported_embedding_provider,
    normalize_embedding_provider,
    validate_embedding_id,
    validate_embedding_provider,
)


# ============================================================================
# normalize_embedding_provider
# ============================================================================


@pytest.mark.parametrize(
    ("provider", "expected"),
    [
        ("OPENAI", "openai"),
        (" Voyage ", "voyage"),
        ("COHERE", "cohere"),
        ("BGE", "bge"),
        ("Instructor", "instructor"),
    ],
)
def test_normalize_embedding_provider(
    provider: str,
    expected: str,
) -> None:
    """Test provider normalization."""
    assert (
        normalize_embedding_provider(
            provider,
        )
        == expected
    )


# ============================================================================
# validate_embedding_provider
# ============================================================================


@pytest.mark.parametrize(
    "provider",
    [
        "openai",
        "voyage",
        "cohere",
        "bge",
        "e5",
        "instructor",
        "ollama",
    ],
)
def test_validate_embedding_provider(
    provider: str,
) -> None:
    """Test valid providers."""
    assert (
        validate_embedding_provider(
            provider,
        )
        == provider
    )


@pytest.mark.parametrize(
    "provider",
    [
        "",
        "azure",
        "bedrock",
        "vertex",
    ],
)
def test_validate_embedding_provider_invalid(
    provider: str,
) -> None:
    """Invalid providers should raise."""
    with pytest.raises(
        InvalidEmbeddingProviderError,
    ):
        validate_embedding_provider(
            provider,
        )


# ============================================================================
# is_supported_embedding_provider
# ============================================================================


@pytest.mark.parametrize(
    ("provider", "expected"),
    [
        ("openai", True),
        ("voyage", True),
        ("cohere", True),
        ("bge", True),
        ("e5", True),
        ("instructor", True),
        ("ollama", True),
        ("azure", False),
        ("bedrock", False),
    ],
)
def test_is_supported_embedding_provider(
    provider: str,
    expected: bool,
) -> None:
    """Test provider support detection."""
    assert (
        is_supported_embedding_provider(
            provider,
        )
        is expected
    )


# ============================================================================
# validate_embedding_id
# ============================================================================


@pytest.mark.parametrize(
    "embedding_id",
    [
        "embedding",
        "embedding_01",
        "embedding-01",
        "runtime123",
    ],
)
def test_validate_embedding_id(
    embedding_id: str,
) -> None:
    """Test valid embedding identifiers."""
    assert (
        validate_embedding_id(
            embedding_id,
        )
        == embedding_id.lower()
    )


@pytest.mark.parametrize(
    "embedding_id",
    [
        "",
        "123embedding",
        "embedding name",
        "@embedding",
    ],
)
def test_validate_embedding_id_invalid(
    embedding_id: str,
) -> None:
    """Invalid embedding identifiers should raise."""
    with pytest.raises(ValueError):
        validate_embedding_id(
            embedding_id,
        )


# ============================================================================
# build_embedding_id
# ============================================================================


def test_build_embedding_id() -> None:
    """Test embedding ID generation."""
    embedding_id = build_embedding_id()

    assert embedding_id.startswith(
        "embedding-",
    )

    pattern = re.compile(
        (
            r"^embedding-"
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert (
        pattern.fullmatch(
            embedding_id,
        )
        is not None
    )