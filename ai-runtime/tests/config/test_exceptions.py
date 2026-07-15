"""
Unit tests for ai_runtime.config.exceptions.
"""

from __future__ import annotations

import pytest

from ai_runtime.config.exceptions import (
    ConfigConfigurationError,
    ConfigError,
    ConfigValidationError,
    InvalidEnvironmentError,
)


def test_config_error_default_message() -> None:
    """Test ConfigError default message."""
    error = ConfigError()

    assert str(error) == (
        "A configuration error occurred."
    )


def test_config_error_custom_message() -> None:
    """Test ConfigError custom message."""
    error = ConfigError(
        "Custom configuration error.",
    )

    assert str(error) == (
        "Custom configuration error."
    )


@pytest.mark.parametrize(
    "environment",
    [
        "",
        "local",
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
        == (
            f"Invalid environment: "
            f"'{environment}'."
        )
    )


def test_config_configuration_error() -> None:
    """Test ConfigConfigurationError."""
    configuration = "workers"

    error = ConfigConfigurationError(
        configuration,
    )

    assert isinstance(error, ConfigError)
    assert error.configuration == configuration

    assert (
        str(error)
        == (
            "Invalid configuration: "
            f"'{configuration}'."
        )
    )


def test_config_validation_error() -> None:
    """Test ConfigValidationError."""
    configuration = "runtime"

    reason = "missing required value"

    error = ConfigValidationError(
        configuration,
        reason,
    )

    assert isinstance(error, ConfigError)
    assert error.configuration == configuration
    assert error.reason == reason

    assert (
        str(error)
        == (
            f"Configuration '{configuration}' "
            f"validation failed: {reason}."
        )
    )