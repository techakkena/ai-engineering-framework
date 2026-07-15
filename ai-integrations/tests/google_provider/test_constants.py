"""
Tests for ai_integrations.google_provider.constants.
"""

from ai_integrations.google_provider.constants import (
    DEFAULT_API_BASE,
    DEFAULT_EMBEDDING_MODEL,
    DEFAULT_MAX_RETRIES,
    DEFAULT_MAX_TOKENS,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
    DEFAULT_TIMEOUT,
    SUPPORTED_CHAT_MODELS,
    SUPPORTED_EMBEDDING_MODELS,
    SUPPORTED_VISION_MODELS,
)


def test_default_api_base() -> None:
    """Test the default API base."""
    assert DEFAULT_API_BASE == "https://generativelanguage.googleapis.com"


def test_default_model() -> None:
    """Test the default model."""
    assert DEFAULT_MODEL == "gemini-2.5-pro"


def test_default_embedding_model() -> None:
    """Test the default embedding model."""
    assert DEFAULT_EMBEDDING_MODEL == "text-embedding-004"


def test_default_timeout() -> None:
    """Test the default timeout."""
    assert DEFAULT_TIMEOUT == 60.0


def test_default_max_retries() -> None:
    """Test the default retry count."""
    assert DEFAULT_MAX_RETRIES == 3


def test_default_max_tokens() -> None:
    """Test the default maximum tokens."""
    assert DEFAULT_MAX_TOKENS == 8192


def test_default_temperature() -> None:
    """Test the default temperature."""
    assert DEFAULT_TEMPERATURE == 0.7


def test_supported_chat_models() -> None:
    """Test supported chat models."""
    assert "gemini-2.5-pro" in SUPPORTED_CHAT_MODELS
    assert "gemini-2.5-flash" in SUPPORTED_CHAT_MODELS
    assert "gemini-2.0-flash" in SUPPORTED_CHAT_MODELS


def test_supported_embedding_models() -> None:
    """Test supported embedding models."""
    assert "text-embedding-004" in SUPPORTED_EMBEDDING_MODELS
    assert "embedding-001" in SUPPORTED_EMBEDDING_MODELS


def test_supported_vision_models() -> None:
    """Test supported vision models."""
    assert "gemini-2.5-pro" in SUPPORTED_VISION_MODELS
    assert "gemini-2.5-flash" in SUPPORTED_VISION_MODELS