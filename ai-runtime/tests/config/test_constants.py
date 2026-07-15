"""
Unit tests for ai_runtime.config.constants.
"""

from __future__ import annotations

from ai_runtime.config.constants import (
    DEFAULT_CONFIG_NAME,
    DEFAULT_CONFIG_VERSION,
    DEFAULT_DEBUG,
    DEFAULT_ENVIRONMENT,
    DEFAULT_HOST,
    DEFAULT_LOG_LEVEL,
    DEFAULT_PORT,
    DEFAULT_WORKERS,
    DEVELOPMENT,
    PRODUCTION,
    STAGING,
    SUPPORTED_ENVIRONMENTS,
    TESTING,
)


def test_config_defaults() -> None:
    """Test configuration defaults."""
    assert DEFAULT_CONFIG_NAME == "runtime-config"
    assert DEFAULT_CONFIG_VERSION == "1.0.0"
    assert DEFAULT_ENVIRONMENT == DEVELOPMENT


def test_supported_environments() -> None:
    """Test supported environments."""
    expected = {
        DEVELOPMENT,
        TESTING,
        STAGING,
        PRODUCTION,
    }

    assert SUPPORTED_ENVIRONMENTS == expected


def test_supported_environments_are_immutable() -> None:
    """Supported environments should be immutable."""
    assert isinstance(
        SUPPORTED_ENVIRONMENTS,
        frozenset,
    )


def test_runtime_configuration_defaults() -> None:
    """Test runtime configuration defaults."""
    assert DEFAULT_HOST == "127.0.0.1"
    assert DEFAULT_PORT == 8000
    assert DEFAULT_LOG_LEVEL == "INFO"
    assert DEFAULT_WORKERS == 4
    assert DEFAULT_DEBUG is False