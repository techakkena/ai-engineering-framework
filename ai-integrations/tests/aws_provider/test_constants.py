"""
Tests for ai_integrations.aws_provider.constants.
"""

from ai_integrations.aws_provider.constants import (
    DEFAULT_EMBEDDING_MODEL,
    DEFAULT_MAX_RETRIES,
    DEFAULT_MAX_TOKENS,
    DEFAULT_MODEL,
    DEFAULT_REGION,
    DEFAULT_TEMPERATURE,
    DEFAULT_TIMEOUT,
    SUPPORTED_CHAT_MODELS,
    SUPPORTED_EMBEDDING_MODELS,
)


def test_default_region() -> None:
    """Test the default AWS region."""
    assert DEFAULT_REGION == "us-east-1"


def test_default_model() -> None:
    """Test the default chat model."""
    assert DEFAULT_MODEL == "amazon.nova-pro-v1:0"


def test_default_embedding_model() -> None:
    """Test the default embedding model."""
    assert (
        DEFAULT_EMBEDDING_MODEL
        == "amazon.titan-embed-text-v2:0"
    )


def test_default_timeout() -> None:
    """Test the default timeout."""
    assert DEFAULT_TIMEOUT == 60.0


def test_default_max_retries() -> None:
    """Test the default retry count."""
    assert DEFAULT_MAX_RETRIES == 3


def test_default_max_tokens() -> None:
    """Test the default maximum tokens."""
    assert DEFAULT_MAX_TOKENS == 4096


def test_default_temperature() -> None:
    """Test the default temperature."""
    assert DEFAULT_TEMPERATURE == 0.7


def test_supported_chat_models() -> None:
    """Test supported chat models."""
    assert "amazon.nova-pro-v1:0" in SUPPORTED_CHAT_MODELS
    assert "amazon.nova-lite-v1:0" in SUPPORTED_CHAT_MODELS
    assert (
        "anthropic.claude-3-7-sonnet"
        in SUPPORTED_CHAT_MODELS
    )


def test_supported_embedding_models() -> None:
    """Test supported embedding models."""
    assert (
        "amazon.titan-embed-text-v2:0"
        in SUPPORTED_EMBEDDING_MODELS
    )
    assert (
        "cohere.embed-english-v3"
        in SUPPORTED_EMBEDDING_MODELS
    )