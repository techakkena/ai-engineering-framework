"""
Unit tests for ai_models.chat.constants.
"""

from __future__ import annotations

from ai_models.chat.constants import (
    ANTHROPIC,
    DEFAULT_CHAT_MODEL,
    DEFAULT_MAX_OUTPUT_TOKENS,
    DEFAULT_RETRIES,
    DEFAULT_TEMPERATURE,
    DEFAULT_TIMEOUT,
    DEEPSEEK,
    GOOGLE,
    GROQ,
    MISTRAL,
    OLLAMA,
    OPENAI,
    SUPPORTED_CHAT_PROVIDERS,
)


def test_chat_defaults() -> None:
    """Test default chat configuration."""
    assert DEFAULT_CHAT_MODEL == "gpt-5"
    assert DEFAULT_TEMPERATURE == 0.7
    assert DEFAULT_MAX_OUTPUT_TOKENS == 4096


def test_supported_chat_providers() -> None:
    """Test supported chat providers."""
    expected = {
        OPENAI,
        ANTHROPIC,
        GOOGLE,
        GROQ,
        MISTRAL,
        OLLAMA,
        DEEPSEEK,
    }

    assert SUPPORTED_CHAT_PROVIDERS == expected


def test_supported_chat_providers_are_immutable() -> None:
    """Supported providers should be immutable."""
    assert isinstance(
        SUPPORTED_CHAT_PROVIDERS,
        frozenset,
    )


def test_chat_configuration_defaults() -> None:
    """Test chat configuration defaults."""
    assert DEFAULT_TIMEOUT == 60
    assert DEFAULT_RETRIES == 3