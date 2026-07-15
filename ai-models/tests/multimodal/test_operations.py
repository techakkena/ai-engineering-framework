"""
Unit tests for ai_models.multimodal.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_models.multimodal.exceptions import (
    InvalidMultimodalProviderError,
)
from ai_models.multimodal.operations import (
    build_multimodal_id,
    is_supported_multimodal_provider,
    normalize_multimodal_provider,
    validate_multimodal_id,
    validate_multimodal_provider,
)


# ============================================================================
# normalize_multimodal_provider
# ============================================================================


@pytest.mark.parametrize(
    ("provider", "expected"),
    [
        ("OPENAI", "openai"),
        (" Google ", "google"),
        ("Anthropic", "anthropic"),
        ("OLLAMA", "ollama"),
        ("Azure", "azure"),
    ],
)
def test_normalize_multimodal_provider(
    provider: str,
    expected: str,
) -> None:
    """Test provider normalization."""
    assert (
        normalize_multimodal_provider(
            provider,
        )
        == expected
    )


# ============================================================================
# validate_multimodal_provider
# ============================================================================


@pytest.mark.parametrize(
    "provider",
    [
        "openai",
        "google",
        "anthropic",
        "ollama",
        "azure",
    ],
)
def test_validate_multimodal_provider(
    provider: str,
) -> None:
    """Test valid providers."""
    assert (
        validate_multimodal_provider(
            provider,
        )
        == provider
    )


@pytest.mark.parametrize(
    "provider",
    [
        "",
        "bedrock",
        "vertex",
        "groq",
    ],
)
def test_validate_multimodal_provider_invalid(
    provider: str,
) -> None:
    """Invalid providers should raise."""
    with pytest.raises(
        InvalidMultimodalProviderError,
    ):
        validate_multimodal_provider(
            provider,
        )


# ============================================================================
# is_supported_multimodal_provider
# ============================================================================


@pytest.mark.parametrize(
    ("provider", "expected"),
    [
        ("openai", True),
        ("google", True),
        ("anthropic", True),
        ("ollama", True),
        ("azure", True),
        ("bedrock", False),
        ("vertex", False),
    ],
)
def test_is_supported_multimodal_provider(
    provider: str,
    expected: bool,
) -> None:
    """Test provider support detection."""
    assert (
        is_supported_multimodal_provider(
            provider,
        )
        is expected
    )


# ============================================================================
# validate_multimodal_id
# ============================================================================


@pytest.mark.parametrize(
    "multimodal_id",
    [
        "multimodal",
        "multimodal_01",
        "multimodal-01",
        "runtime123",
    ],
)
def test_validate_multimodal_id(
    multimodal_id: str,
) -> None:
    """Test valid multimodal identifiers."""
    assert (
        validate_multimodal_id(
            multimodal_id,
        )
        == multimodal_id.lower()
    )


@pytest.mark.parametrize(
    "multimodal_id",
    [
        "",
        "123multimodal",
        "multimodal name",
        "@multimodal",
    ],
)
def test_validate_multimodal_id_invalid(
    multimodal_id: str,
) -> None:
    """Invalid identifiers should raise."""
    with pytest.raises(ValueError):
        validate_multimodal_id(
            multimodal_id,
        )


# ============================================================================
# build_multimodal_id
# ============================================================================


def test_build_multimodal_id() -> None:
    """Test multimodal ID generation."""
    multimodal_id = build_multimodal_id()

    assert multimodal_id.startswith(
        "multimodal-",
    )

    pattern = re.compile(
        (
            r"^multimodal-"
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert (
        pattern.fullmatch(
            multimodal_id,
        )
        is not None
    )