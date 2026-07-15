"""
Unit tests for ai_models.registry.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_models.registry.exceptions import (
    InvalidRegistryProviderError,
)
from ai_models.registry.operations import (
    build_registry_id,
    is_supported_registry_provider,
    normalize_registry_provider,
    validate_registry_id,
    validate_registry_provider,
)


# ============================================================================
# normalize_registry_provider
# ============================================================================


@pytest.mark.parametrize(
    ("provider", "expected"),
    [
        ("LOCAL", "local"),
        (" OpenAI ", "openai"),
        ("OLLAMA", "ollama"),
        ("HuggingFace", "huggingface"),
        ("Azure", "azure"),
    ],
)
def test_normalize_registry_provider(
    provider: str,
    expected: str,
) -> None:
    """Test provider normalization."""
    assert (
        normalize_registry_provider(
            provider,
        )
        == expected
    )


# ============================================================================
# validate_registry_provider
# ============================================================================


@pytest.mark.parametrize(
    "provider",
    [
        "local",
        "openai",
        "ollama",
        "huggingface",
        "azure",
    ],
)
def test_validate_registry_provider(
    provider: str,
) -> None:
    """Test valid providers."""
    assert (
        validate_registry_provider(
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
def test_validate_registry_provider_invalid(
    provider: str,
) -> None:
    """Invalid providers should raise."""
    with pytest.raises(
        InvalidRegistryProviderError,
    ):
        validate_registry_provider(
            provider,
        )


# ============================================================================
# is_supported_registry_provider
# ============================================================================


@pytest.mark.parametrize(
    ("provider", "expected"),
    [
        ("local", True),
        ("openai", True),
        ("ollama", True),
        ("huggingface", True),
        ("azure", True),
        ("bedrock", False),
        ("vertex", False),
    ],
)
def test_is_supported_registry_provider(
    provider: str,
    expected: bool,
) -> None:
    """Test provider support detection."""
    assert (
        is_supported_registry_provider(
            provider,
        )
        is expected
    )


# ============================================================================
# validate_registry_id
# ============================================================================


@pytest.mark.parametrize(
    "registry_id",
    [
        "registry",
        "registry_01",
        "registry-01",
        "runtime123",
    ],
)
def test_validate_registry_id(
    registry_id: str,
) -> None:
    """Test valid registry identifiers."""
    assert (
        validate_registry_id(
            registry_id,
        )
        == registry_id.lower()
    )


@pytest.mark.parametrize(
    "registry_id",
    [
        "",
        "123registry",
        "registry name",
        "@registry",
    ],
)
def test_validate_registry_id_invalid(
    registry_id: str,
) -> None:
    """Invalid identifiers should raise."""
    with pytest.raises(ValueError):
        validate_registry_id(
            registry_id,
        )


# ============================================================================
# build_registry_id
# ============================================================================


def test_build_registry_id() -> None:
    """Test registry ID generation."""
    registry_id = build_registry_id()

    assert registry_id.startswith(
        "registry-",
    )

    pattern = re.compile(
        (
            r"^registry-"
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert (
        pattern.fullmatch(
            registry_id,
        )
        is not None
    )