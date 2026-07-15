"""
Unit tests for ai_models.chat.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_models.chat.exceptions import (
    InvalidChatProviderError,
)
from ai_models.chat.operations import (
    build_chat_id,
    is_supported_chat_provider,
    normalize_chat_provider,
    validate_chat_id,
    validate_chat_provider,
)


# ============================================================================
# normalize_chat_provider
# ============================================================================


@pytest.mark.parametrize(
    ("provider", "expected"),
    [
        ("OPENAI", "openai"),
        (" Anthropic ", "anthropic"),
        ("Google", "google"),
        ("Groq", "groq"),
    ],
)
def test_normalize_chat_provider(
    provider: str,
    expected: str,
) -> None:
    """Test provider normalization."""
    assert (
        normalize_chat_provider(provider)
        == expected
    )


# ============================================================================
# validate_chat_provider
# ============================================================================


@pytest.mark.parametrize(
    "provider",
    [
        "openai",
        "anthropic",
        "google",
        "groq",
        "mistral",
        "ollama",
        "deepseek",
    ],
)
def test_validate_chat_provider(
    provider: str,
) -> None:
    """Test valid providers."""
    assert (
        validate_chat_provider(provider)
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
def test_validate_chat_provider_invalid(
    provider: str,
) -> None:
    """Invalid providers should raise."""
    with pytest.raises(
        InvalidChatProviderError,
    ):
        validate_chat_provider(provider)


# ============================================================================
# is_supported_chat_provider
# ============================================================================


@pytest.mark.parametrize(
    ("provider", "expected"),
    [
        ("openai", True),
        ("anthropic", True),
        ("google", True),
        ("groq", True),
        ("mistral", True),
        ("ollama", True),
        ("deepseek", True),
        ("azure", False),
        ("bedrock", False),
    ],
)
def test_is_supported_chat_provider(
    provider: str,
    expected: bool,
) -> None:
    """Test provider support detection."""
    assert (
        is_supported_chat_provider(provider)
        is expected
    )


# ============================================================================
# validate_chat_id
# ============================================================================


@pytest.mark.parametrize(
    "chat_id",
    [
        "chat",
        "chat_01",
        "chat-01",
        "runtime123",
    ],
)
def test_validate_chat_id(
    chat_id: str,
) -> None:
    """Test valid chat identifiers."""
    assert (
        validate_chat_id(chat_id)
        == chat_id.lower()
    )


@pytest.mark.parametrize(
    "chat_id",
    [
        "",
        "123chat",
        "chat room",
        "@chat",
    ],
)
def test_validate_chat_id_invalid(
    chat_id: str,
) -> None:
    """Invalid chat identifiers should raise."""
    with pytest.raises(ValueError):
        validate_chat_id(chat_id)


# ============================================================================
# build_chat_id
# ============================================================================


def test_build_chat_id() -> None:
    """Test chat ID generation."""
    chat_id = build_chat_id()

    assert chat_id.startswith("chat-")

    pattern = re.compile(
        (
            r"^chat-"
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert pattern.fullmatch(chat_id) is not None