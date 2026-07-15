"""
Unit tests for ai_models.config.exceptions.
"""

from __future__ import annotations

import pytest

from ai_models.config.exceptions import (
    ConfigurationValidationError,
    InvalidConfigurationValueError,
    InvalidEnvironmentError,
    ModelConfigurationError,
    ModelConfigError,
)


def test_model_config_error_default_message() -> None:
    """Test ModelConfigError default message."""
    error = ModelConfigError()

    assert (
        str(error)
        == "A model configuration error occurred."
    )


def test_model_config_error_custom_message() -> None:
    """Test ModelConfigError custom message."""
    error = ModelConfigError(
        "Custom configuration error.",
    )

    assert (
        str(error)
        == "Custom configuration error."
    )


@pytest.mark.parametrize(
    "environment",
    [
        "",
        "local",
        "uat",
    ],
)
def test_invalid_environment_error(
    environment: str,
) -> None:
    """Test InvalidEnvironmentError."""
    error = InvalidEnvironmentError(
        environment,
    )

    assert isinstance(
        error,
        ModelConfigError,
    )

    assert error.environment == environment

    assert (
        str(error)
        == (
            "Invalid environment: "
            f"'{environment}'."
        )
    )


def test_model_configuration_error() -> None:
    """Test ModelConfigurationError."""
    configuration = "temperature"

    error = ModelConfigurationError(
        configuration,
    )

    assert isinstance(
        error,
        ModelConfigError,
    )

    assert (
        error.configuration
        == configuration
    )

    assert (
        str(error)
        == (
            "Invalid model "
            "configuration: "
            f"'{configuration}'."
        )
    )


def test_configuration_validation_error() -> None:
    """Test ConfigurationValidationError."""
    configuration = "temperature"
    reason = "value exceeds maximum"

    error = ConfigurationValidationError(
        configuration,
        reason,
    )

    assert isinstance(
        error,
        ModelConfigError,
    )

    assert (
        error.configuration
        == configuration
    )

    assert error.reason == reason

    assert (
        str(error)
        == (
            f"Configuration "
            f"'{configuration}' "
            f"validation failed: "
            f"{reason}."
        )
    )


def test_invalid_configuration_value_error() -> None:
    """Test InvalidConfigurationValueError."""
    field = "temperature"
    value = 5.0

    error = InvalidConfigurationValueError(
        field,
        value,
    )

    assert isinstance(
        error,
        ModelConfigError,
    )

    assert error.field == field
    assert error.value == value

    assert (
        str(error)
        == (
            "Invalid configuration "
            f"value for '{field}': "
            f"{value!r}."
        )
    )