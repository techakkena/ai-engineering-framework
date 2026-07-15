"""
Unit tests for ai_api.config.constants.
"""

from __future__ import annotations

from ai_api.config.constants import (
    API_PREFIX_KEY,
    API_VERSION_KEY,
    DEFAULT_API_NAME,
    DEFAULT_API_PREFIX,
    DEFAULT_API_VERSION,
    DEFAULT_CONFIG_FILE,
    DEFAULT_ENV_FILE,
    DEFAULT_HOST,
    DEFAULT_HTTPS_SCHEME,
    DEFAULT_KEEP_ALIVE,
    DEFAULT_LOG_LEVEL,
    DEFAULT_MAX_REQUEST_SIZE,
    DEFAULT_PORT,
    DEFAULT_SCHEME,
    DEFAULT_SETTINGS_FILE,
    DEFAULT_TIMEOUT,
    DEFAULT_WORKERS,
    DEVELOPMENT_ENVIRONMENT,
    ENVIRONMENT_KEY,
    HOST_KEY,
    LOG_LEVEL_KEY,
    PORT_KEY,
    PRODUCTION_ENVIRONMENT,
    STAGING_ENVIRONMENT,
    SUPPORTED_ENVIRONMENTS,
    SUPPORTED_LOG_LEVELS,
    TESTING_ENVIRONMENT,
    TIMEOUT_KEY,
)


def test_api_defaults() -> None:
    """Test API default constants."""
    assert DEFAULT_API_VERSION == "v1"
    assert DEFAULT_API_PREFIX == "/api"
    assert DEFAULT_API_NAME == "AI API"
    assert DEFAULT_TIMEOUT == 30


def test_network_defaults() -> None:
    """Test network defaults."""
    assert DEFAULT_HOST == "127.0.0.1"
    assert DEFAULT_PORT == 8000
    assert DEFAULT_SCHEME == "http"
    assert DEFAULT_HTTPS_SCHEME == "https"


def test_supported_environments() -> None:
    """Test supported runtime environments."""
    expected = {
        DEVELOPMENT_ENVIRONMENT,
        TESTING_ENVIRONMENT,
        STAGING_ENVIRONMENT,
        PRODUCTION_ENVIRONMENT,
    }

    assert SUPPORTED_ENVIRONMENTS == expected


def test_supported_environments_are_immutable() -> None:
    """Supported environments should be immutable."""
    assert isinstance(
        SUPPORTED_ENVIRONMENTS,
        frozenset,
    )


def test_logging_defaults() -> None:
    """Test logging defaults."""
    assert DEFAULT_LOG_LEVEL == "INFO"

    expected = {
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL",
    }

    assert SUPPORTED_LOG_LEVELS == expected


def test_supported_log_levels_are_immutable() -> None:
    """Supported log levels should be immutable."""
    assert isinstance(
        SUPPORTED_LOG_LEVELS,
        frozenset,
    )


def test_server_defaults() -> None:
    """Test server defaults."""
    assert DEFAULT_WORKERS == 1
    assert DEFAULT_KEEP_ALIVE == 5
    assert DEFAULT_MAX_REQUEST_SIZE == (
        10 * 1024 * 1024
    )


def test_configuration_keys() -> None:
    """Test configuration keys."""
    assert HOST_KEY == "host"
    assert PORT_KEY == "port"
    assert ENVIRONMENT_KEY == "environment"
    assert API_PREFIX_KEY == "api_prefix"
    assert API_VERSION_KEY == "api_version"
    assert TIMEOUT_KEY == "timeout"
    assert LOG_LEVEL_KEY == "log_level"


def test_configuration_files() -> None:
    """Test configuration filenames."""
    assert DEFAULT_CONFIG_FILE == "config.toml"
    assert DEFAULT_ENV_FILE == ".env"
    assert DEFAULT_SETTINGS_FILE == "settings.toml"