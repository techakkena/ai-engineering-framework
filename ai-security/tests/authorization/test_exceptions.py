"""
Unit tests for ai_security.authorization.exceptions.
"""

from __future__ import annotations

import pytest

from ai_security.authorization.exceptions import (
    AuthorizationConfigurationError,
    AuthorizationError,
    AuthorizationValidationError,
    InvalidAuthorizationProviderError,
)


def test_authorization_error_default_message() -> None:
    """Test AuthorizationError default message."""
    error = AuthorizationError()

    assert (
        str(error)
        == "An authorization error occurred."
    )


def test_authorization_error_custom_message() -> None:
    """Test AuthorizationError custom message."""
    error = AuthorizationError(
        "Custom authorization error.",
    )

    assert (
        str(error)
        == "Custom authorization error."
    )


@pytest.mark.parametrize(
    "provider",
    [
        "",
        "iam",
        "custom",
    ],
)
def test_invalid_authorization_provider_error(
    provider: str,
) -> None:
    """Test InvalidAuthorizationProviderError."""
    error = InvalidAuthorizationProviderError(
        provider,
    )

    assert isinstance(
        error,
        AuthorizationError,
    )

    assert error.provider == provider

    assert (
        str(error)
        == (
            "Invalid authorization "
            f"provider: '{provider}'."
        )
    )


def test_authorization_configuration_error() -> None:
    """Test AuthorizationConfigurationError."""
    configuration = "role"

    error = AuthorizationConfigurationError(
        configuration,
    )

    assert isinstance(
        error,
        AuthorizationError,
    )

    assert (
        error.configuration
        == configuration
    )

    assert (
        str(error)
        == (
            "Invalid authorization "
            f"configuration: "
            f"'{configuration}'."
        )
    )


def test_authorization_validation_error() -> None:
    """Test AuthorizationValidationError."""
    subject = "alice"
    reason = "permission denied"

    error = AuthorizationValidationError(
        subject,
        reason,
    )

    assert isinstance(
        error,
        AuthorizationError,
    )

    assert error.subject == subject
    assert error.reason == reason

    assert (
        str(error)
        == (
            f"Authorization for "
            f"'{subject}' failed: "
            f"{reason}."
        )
    )