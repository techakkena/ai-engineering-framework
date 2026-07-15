"""
Tests for ai_security.config.constants.
"""

from ai_security.config.constants import (
    DEFAULT_ENVIRONMENT,
    DEFAULT_LOG_LEVEL,
    DEFAULT_TIMEOUT_SECONDS,
)


def test_default_environment() -> None:
    """Test the default environment."""
    assert DEFAULT_ENVIRONMENT == "production"


def test_default_log_level() -> None:
    """Test the default log level."""
    assert DEFAULT_LOG_LEVEL == "INFO"


def test_default_timeout_seconds() -> None:
    """Test the default timeout."""
    assert DEFAULT_TIMEOUT_SECONDS == 30