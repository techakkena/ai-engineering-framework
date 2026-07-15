"""
Tests for ai_integrations.anthropic_provider.constants.
"""

from ai_integrations.anthropic_provider.constants import (
    DEFAULT_API_BASE,
    DEFAULT_API_VERSION,
    DEFAULT_MAX_RETRIES,
    DEFAULT_MAX_TOKENS,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
    DEFAULT_TIMEOUT,
    SUPPORTED_CHAT_MODELS,
    SUPPORTED_REGIONS,
)


def test_default_api_base() -> None:
    """Test the default API base."""
    assert DEFAULT_API_BASE == "https://api.anthropic.com"


def test_default_api_version() -> None:
    """Test the default API version."""
    assert DEFAULT_API_VERSION == "2023-06-01"


def test_default_model() -> None:
    """Test the default model."""
    assert DEFAULT_MODEL == "claude-sonnet-4-0"


def test_default_timeout() -> None:
    """Test the default timeout."""
    assert DEFAULT_TIMEOUT == 60.0


def test_default_max_retries() -> None:
    """Test the default retry count."""
    assert DEFAULT_MAX_RETRIES == 3


def test_default_max_tokens() -> None:
    """Test the default max tokens."""
    assert DEFAULT_MAX_TOKENS == 4096


def test_default_temperature() -> None:
    """Test the default temperature."""
    assert DEFAULT_TEMPERATURE == 0.7


def test_supported_chat_models() -> None:
    """Test supported chat models."""
    assert "claude-opus-4-1" in SUPPORTED_CHAT_MODELS
    assert "claude-opus-4-0" in SUPPORTED_CHAT_MODELS
    assert "claude-sonnet-4-0" in SUPPORTED_CHAT_MODELS
    assert "claude-3-7-sonnet-latest" in SUPPORTED_CHAT_MODELS


def test_supported_regions() -> None:
    """Test supported regions."""
    assert "global" in SUPPORTED_REGIONS