"""
Unit tests for ai_models.vision.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_models.vision.exceptions import (
    InvalidVisionProviderError,
)
from ai_models.vision.operations import (
    build_vision_id,
    is_supported_vision_provider,
    normalize_vision_provider,
    validate_vision_id,
    validate_vision_provider,
)


# ============================================================================
# normalize_vision_provider
# ============================================================================


@pytest.mark.parametrize(
    ("provider", "expected"),
    [
        ("OPENAI", "openai"),
        (" Google ", "google"),
        ("Anthropic", "anthropic"),
        ("OLLAMA", "ollama"),
    ],
)
def test_normalize_vision_provider(
    provider: str,
    expected: str,
) -> None:
    """Test provider normalization."""
    assert (
        normalize_vision_provider(provider)
        == expected
    )


# ============================================================================
# validate_vision_provider
# ============================================================================


@pytest.mark.parametrize(
    "provider",
    [
        "openai",
        "google",
        "anthropic",
        "ollama",
    ],
)
def test_validate_vision_provider(
    provider: str,
) -> None:
    """Test valid providers."""
    assert (
        validate_vision_provider(provider)
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
def test_validate_vision_provider_invalid(
    provider: str,
) -> None:
    """Invalid providers should raise."""
    with pytest.raises(
        InvalidVisionProviderError,
    ):
        validate_vision_provider(provider)


# ============================================================================
# is_supported_vision_provider
# ============================================================================


@pytest.mark.parametrize(
    ("provider", "expected"),
    [
        ("openai", True),
        ("google", True),
        ("anthropic", True),
        ("ollama", True),
        ("azure", False),
        ("bedrock", False),
    ],
)
def test_is_supported_vision_provider(
    provider: str,
    expected: bool,
) -> None:
    """Test provider support detection."""
    assert (
        is_supported_vision_provider(provider)
        is expected
    )


# ============================================================================
# validate_vision_id
# ============================================================================


@pytest.mark.parametrize(
    "vision_id",
    [
        "vision",
        "vision_01",
        "vision-01",
        "runtime123",
    ],
)
def test_validate_vision_id(
    vision_id: str,
) -> None:
    """Test valid vision identifiers."""
    assert (
        validate_vision_id(vision_id)
        == vision_id.lower()
    )


@pytest.mark.parametrize(
    "vision_id",
    [
        "",
        "123vision",
        "vision name",
        "@vision",
    ],
)
def test_validate_vision_id_invalid(
    vision_id: str,
) -> None:
    """Invalid identifiers should raise."""
    with pytest.raises(ValueError):
        validate_vision_id(vision_id)


# ============================================================================
# build_vision_id
# ============================================================================


def test_build_vision_id() -> None:
    """Test vision ID generation."""
    vision_id = build_vision_id()

    assert vision_id.startswith("vision-")

    pattern = re.compile(
        (
            r"^vision-"
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert pattern.fullmatch(vision_id) is not None