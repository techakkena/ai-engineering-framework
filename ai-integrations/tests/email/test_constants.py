"""
Tests for ai_integrations.email.constants.
"""

from ai_integrations.email.constants import (
    DEFAULT_ENCODING,
    DEFAULT_MAX_RETRIES,
    DEFAULT_PORT,
    DEFAULT_SMTP_HOST,
    DEFAULT_TIMEOUT,
    SUPPORTED_CONTENT_TYPES,
    SUPPORTED_PROVIDERS,
)


def test_default_smtp_host() -> None:
    """Test the default SMTP host."""
    assert DEFAULT_SMTP_HOST == "localhost"


def test_default_port() -> None:
    """Test the default SMTP port."""
    assert DEFAULT_PORT == 587


def test_default_timeout() -> None:
    """Test the default timeout."""
    assert DEFAULT_TIMEOUT == 60.0


def test_default_max_retries() -> None:
    """Test the default retry count."""
    assert DEFAULT_MAX_RETRIES == 3


def test_default_encoding() -> None:
    """Test the default encoding."""
    assert DEFAULT_ENCODING == "utf-8"


def test_supported_content_types() -> None:
    """Test supported content types."""
    assert "text/plain" in SUPPORTED_CONTENT_TYPES
    assert "text/html" in SUPPORTED_CONTENT_TYPES
    assert "multipart/mixed" in SUPPORTED_CONTENT_TYPES


def test_supported_providers() -> None:
    """Test supported providers."""
    assert "smtp" in SUPPORTED_PROVIDERS
    assert "sendgrid" in SUPPORTED_PROVIDERS
    assert "ses" in SUPPORTED_PROVIDERS
    assert "azure" in SUPPORTED_PROVIDERS