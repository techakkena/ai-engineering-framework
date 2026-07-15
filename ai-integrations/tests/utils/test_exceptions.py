"""
Tests for ai_integrations.utils.exceptions.
"""

from ai_integrations.utils.exceptions import (
    IntegrationError,
    RetryError,
    SerializationError,
    ValidationError,
)


def test_integration_error() -> None:
    """IntegrationError should derive from Exception."""
    error = IntegrationError("error")

    assert str(error) == "error"


def test_retry_error() -> None:
    """RetryError should derive from IntegrationError."""
    assert isinstance(
        RetryError("retry"),
        IntegrationError,
    )


def test_validation_error() -> None:
    """ValidationError should derive from IntegrationError."""
    assert isinstance(
        ValidationError("validation"),
        IntegrationError,
    )


def test_serialization_error() -> None:
    """SerializationError should derive from IntegrationError."""
    assert isinstance(
        SerializationError("serialization"),
        IntegrationError,
    )