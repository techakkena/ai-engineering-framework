"""
Tests for ai_integrations.webhooks.constants.
"""

from ai_integrations.webhooks.constants import (
    DEFAULT_CONTENT_TYPE,
    DEFAULT_MAX_RETRIES,
    DEFAULT_SIGNATURE_HEADER,
    DEFAULT_TIMEOUT,
    DEFAULT_USER_AGENT,
    SUPPORTED_CONTENT_TYPES,
    SUPPORTED_HTTP_METHODS,
)


def test_default_timeout() -> None:
    """Test default timeout."""
    assert DEFAULT_TIMEOUT == 60.0


def test_default_max_retries() -> None:
    """Test default retry count."""
    assert DEFAULT_MAX_RETRIES == 3


def test_default_content_type() -> None:
    """Test default content type."""
    assert DEFAULT_CONTENT_TYPE == "application/json"


def test_default_signature_header() -> None:
    """Test default signature header."""
    assert DEFAULT_SIGNATURE_HEADER == "X-Signature"


def test_default_user_agent() -> None:
    """Test default user agent."""
    assert DEFAULT_USER_AGENT == "AI-Engineering-Framework/1.0"


def test_supported_http_methods() -> None:
    """Test supported HTTP methods."""
    assert "GET" in SUPPORTED_HTTP_METHODS
    assert "POST" in SUPPORTED_HTTP_METHODS
    assert "PUT" in SUPPORTED_HTTP_METHODS
    assert "PATCH" in SUPPORTED_HTTP_METHODS
    assert "DELETE" in SUPPORTED_HTTP_METHODS


def test_supported_content_types() -> None:
    """Test supported content types."""
    assert "application/json" in SUPPORTED_CONTENT_TYPES
    assert (
        "application/x-www-form-urlencoded"
        in SUPPORTED_CONTENT_TYPES
    )