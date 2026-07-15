"""
Tests for ai_integrations.openai_provider.constants.
"""

from ai_integrations.openai_provider.constants import (
    DEFAULT_API_BASE,
    DEFAULT_EMBEDDING_MODEL,
    DEFAULT_MAX_RETRIES,
    DEFAULT_MAX_TOKENS,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
    DEFAULT_TIMEOUT,
    SUPPORTED_CHAT_MODELS,
    SUPPORTED_EMBEDDING_MODELS,
    SUPPORTED_IMAGE_MODELS,
    SUPPORTED_TRANSCRIPTION_MODELS,
)


def test_default_api_base() -> None:
    """Test the default API base."""
    assert DEFAULT_API_BASE == "https://api.openai.com/v1"


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


def test_default_max_tokens() -> None:
    """Test the default max tokens."""
    assert DEFAULT_MAX_TOKENS == 4096


def test_default_temperature() -> None:
    """Test the default temperature."""
    assert DEFAULT_TEMPERATURE == 0.7


def test_supported_chat_models() -> None:
    """Test supported chat models."""
    assert "gpt-5" in SUPPORTED_CHAT_MODELS
    assert "gpt-5-mini" in SUPPORTED_CHAT_MODELS
    assert "gpt-5-nano" in SUPPORTED_CHAT_MODELS


def test_supported_embedding_models() -> None:
    """Test supported embedding models."""
    assert "text-embedding-3-small" in SUPPORTED_EMBEDDING_MODELS
    assert "text-embedding-3-large" in SUPPORTED_EMBEDDING_MODELS


def test_supported_image_models() -> None:
    """Test supported image models."""
    assert "gpt-image-1" in SUPPORTED_IMAGE_MODELS


def test_supported_transcription_models() -> None:
    """Test supported transcription models."""
    assert "gpt-4o-transcribe" in SUPPORTED_TRANSCRIPTION_MODELS
    assert "gpt-4o-mini-transcribe" in SUPPORTED_TRANSCRIPTION_MODELS