"""
Tests for ai_integrations.slack.constants.
"""

from ai_integrations.slack.constants import (
    DEFAULT_API_BASE,
    DEFAULT_MAX_RETRIES,
    DEFAULT_MESSAGE_LIMIT,
    DEFAULT_TIMEOUT,
    SUPPORTED_CHANNEL_TYPES,
    SUPPORTED_MESSAGE_TYPES,
)


def test_default_api_base() -> None:
    """Test the default API base."""
    assert DEFAULT_API_BASE == "https://slack.com/api"


def test_default_timeout() -> None:
    """Test the default timeout."""
    assert DEFAULT_TIMEOUT == 60.0


def test_default_max_retries() -> None:
    """Test the default retry count."""
    assert DEFAULT_MAX_RETRIES == 3


def test_default_message_limit() -> None:
    """Test the default message limit."""
    assert DEFAULT_MESSAGE_LIMIT == 100


def test_supported_message_types() -> None:
    """Test supported message types."""
    assert "text" in SUPPORTED_MESSAGE_TYPES
    assert "markdown" in SUPPORTED_MESSAGE_TYPES
    assert "blocks" in SUPPORTED_MESSAGE_TYPES


def test_supported_channel_types() -> None:
    """Test supported channel types."""
    assert "public" in SUPPORTED_CHANNEL_TYPES
    assert "private" in SUPPORTED_CHANNEL_TYPES
    assert "direct" in SUPPORTED_CHANNEL_TYPES
    assert "group" in SUPPORTED_CHANNEL_TYPES