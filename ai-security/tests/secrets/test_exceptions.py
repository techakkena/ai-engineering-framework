"""
Tests for ai_security.secrets.exceptions.
"""

from ai_security.secrets.exceptions import (
    SecretConfigurationError,
    SecretError,
    SecretGenerationError,
    SecretNotFoundError,
)


def test_secret_error() -> None:
    """SecretError should derive from Exception."""
    error = SecretError("secret error")
    assert str(error) == "secret error"


def test_configuration_error() -> None:
    """SecretConfigurationError should derive from SecretError."""
    error = SecretConfigurationError("configuration")
    assert isinstance(error, SecretError)


def test_generation_error() -> None:
    """SecretGenerationError should derive from SecretError."""
    error = SecretGenerationError("generation")
    assert isinstance(error, SecretError)


def test_not_found_error() -> None:
    """SecretNotFoundError should derive from SecretError."""
    error = SecretNotFoundError("missing")
    assert isinstance(error, SecretError)