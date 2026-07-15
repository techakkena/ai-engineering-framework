"""
Tests for ai_security.config.exceptions.
"""

from ai_security.config.exceptions import (
    ConfigurationError,
    ConfigurationValidationError,
    MissingConfigurationError,
)


def test_configuration_error() -> None:
    """ConfigurationError should derive from Exception."""
    error = ConfigurationError("configuration error")

    assert str(error) == "configuration error"


def test_configuration_validation_error() -> None:
    """ConfigurationValidationError should derive from ConfigurationError."""
    error = ConfigurationValidationError("validation error")

    assert isinstance(error, ConfigurationError)


def test_missing_configuration_error() -> None:
    """MissingConfigurationError should derive from ConfigurationError."""
    error = MissingConfigurationError("missing configuration")

    assert isinstance(error, ConfigurationError)