"""
Tests for ai_integrations.azure_provider.constants.
"""

from ai_integrations.azure_provider.constants import (
    DEFAULT_API_VERSION,
    DEFAULT_EMBEDDING_MODEL,
    DEFAULT_ENDPOINT,
    DEFAULT_MAX_RETRIES,
    DEFAULT_MODEL,
    DEFAULT_TIMEOUT,
    SUPPORTED_CHAT_MODELS,
    SUPPORTED_EMBEDDING_MODELS,
)


def test_default_endpoint() -> None:
    """Test the default endpoint."""
    assert DEFAULT_ENDPOINT == "https://example.openai.azure.com"


def test_default_api_version() -> None:
    """Test the default API version."""
    assert DEFAULT_API_VERSION == "2025-04-01-preview"


def test_default_model() -> None:
    """Test the default chat model."""
    assert DEFAULT_MODEL == "gpt-5"


def test_default_embedding_model() -> None:
    """Test the default embedding model."""
    assert DEFAULT_EMBEDDING_MODEL == "text-embedding-3-small"


def test_default_timeout() -> None:
    """Test the default timeout."""
    assert DEFAULT_TIMEOUT == 60.0


def test_default_max_retries() -> None:
    """Test the default retry count."""
    assert DEFAULT_MAX_RETRIES == 3


def test_supported_chat_models() -> None:
    """Test supported chat models."""
    assert "gpt-5" in SUPPORTED_CHAT_MODELS
    assert "gpt-5-mini" in SUPPORTED_CHAT_MODELS
    assert "gpt-5-nano" in SUPPORTED_CHAT_MODELS


def test_supported_embedding_models() -> None:
    """Test supported embedding models."""
    assert "text-embedding-3-small" in SUPPORTED_EMBEDDING_MODELS
    assert "text-embedding-3-large" in SUPPORTED_EMBEDDING_MODELS