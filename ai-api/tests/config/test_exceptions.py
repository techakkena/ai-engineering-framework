"""
Unit tests for ai_api.config.exceptions.
"""

from __future__ import annotations

import pytest

from ai_api.config.exceptions import (
    ConfigError,
    ConfigurationFileError,
    ConfigurationParseError,
    ConfigurationValidationError,
    InvalidConfigurationError,
    InvalidEnvironmentError,
    MissingConfigurationError,
    UnsupportedConfigurationError,
)


def test_config_error_default_message() -> None:
    """Test ConfigError with the default message."""
    error = ConfigError()

    assert str(error) == "A configuration error occurred."


def test_config_error_custom_message() -> None:
    """Test ConfigError with a custom message."""
    error = ConfigError("Custom configuration error.")

    assert str(error) == "Custom configuration error."


@pytest.mark.parametrize(
    ("key", "value"),
    [
        ("host", ""),
        ("port", -1),
        ("timeout", None),
    ],
)
def test_invalid_configuration_error(
    key: str,
    value: object,
) -> None:
    """Test InvalidConfigurationError."""
    error = InvalidConfigurationError(
        key,
        value,
    )

    assert isinstance(error, ConfigError)
    assert error.key == key
    assert error.value == value
    assert (
        str(error)
        == f"Invalid configuration '{key}': {value!r}."
    )


@pytest.mark.parametrize(
    "key",
    [
        "host",
        "port",
        "api_key",
    ],
)
def test_missing_configuration_error(
    key: str,
) -> None:
    """Test MissingConfigurationError."""
    error = MissingConfigurationError(key)

    assert isinstance(error, ConfigError)
    assert error.key == key
    assert (
        str(error)
        == f"Missing required configuration: '{key}'."
    )


@pytest.mark.parametrize(
    "environment",
    [
        "",
        "local",
        "uat",
        "sandbox",
    ],
)
def test_invalid_environment_error(
    environment: str,
) -> None:
    """Test InvalidEnvironmentError."""
    error = InvalidEnvironmentError(
        environment,
    )

    assert isinstance(error, ConfigError)
    assert error.environment == environment
    assert (
        str(error)
        == f"Invalid environment: '{environment}'."
    )


@pytest.mark.parametrize(
    "configuration",
    [
        "yaml",
        "xml",
        "legacy_mode",
    ],
)
def test_unsupported_configuration_error(
    configuration: str,
) -> None:
    """Test UnsupportedConfigurationError."""
    error = UnsupportedConfigurationError(
        configuration,
    )

    assert isinstance(error, ConfigError)
    assert error.configuration == configuration
    assert (
        str(error)
        == (
            f"Unsupported configuration: "
            f"'{configuration}'."
        )
    )


def test_configuration_validation_error() -> None:
    """Test ConfigurationValidationError."""
    key = "timeout"
    reason = "must be greater than zero"

    error = ConfigurationValidationError(
        key,
        reason,
    )

    assert isinstance(error, ConfigError)
    assert error.key == key
    assert error.reason == reason
    assert (
        str(error)
        == (
            f"Configuration validation failed for "
            f"'{key}': {reason}."
        )
    )


@pytest.mark.parametrize(
    "filename",
    [
        "config.toml",
        ".env",
        "settings.toml",
    ],
)
def test_configuration_file_error(
    filename: str,
) -> None:
    """Test ConfigurationFileError."""
    error = ConfigurationFileError(
        filename,
    )

    assert isinstance(error, ConfigError)
    assert error.filename == filename
    assert (
        str(error)
        == (
            f"Unable to load configuration file: "
            f"'{filename}'."
        )
    )


@pytest.mark.parametrize(
    "filename",
    [
        "config.toml",
        ".env",
        "settings.toml",
    ],
)
def test_configuration_parse_error(
    filename: str,
) -> None:
    """Test ConfigurationParseError."""
    error = ConfigurationParseError(
        filename,
    )

    assert isinstance(error, ConfigError)
    assert error.filename == filename
    assert (
        str(error)
        == (
            f"Unable to parse configuration file: "
            f"'{filename}'."
        )
    )