"""
Unit tests for ai_security.authentication.exceptions.
"""

from __future__ import annotations

import pytest

from ai_security.authentication.exceptions import (
    AuthenticationConfigurationError,
    AuthenticationError,
    AuthenticationValidationError,
    InvalidAuthenticationProviderError,
)


def test_authentication_error_default_message() -> None:
    """Test AuthenticationError default message."""
    error = AuthenticationError()

    assert (
        str(error)
        == "An authentication error occurred."
    )


def test_authentication_error_custom_message() -> None:
    """Test AuthenticationError custom message."""
    error = AuthenticationError(
        "Custom authentication error.",
    )

    assert (
        str(error)
        == "Custom authentication error."
    )


@pytest.mark.parametrize(
    "provider",
    [
        "",
        "saml",
        "kerberos",
    ],
)
def test_invalid_authentication_provider_error(
    provider: str,
) -> None:
    """Test InvalidAuthenticationProviderError."""
    error = InvalidAuthenticationProviderError(
        provider,
    )

    assert isinstance(
        error,
        AuthenticationError,
    )

    assert error.provider == provider

    assert (
        str(error)
        == (
            "Invalid authentication "
            f"provider: '{provider}'."
        )
    )


def test_authentication_configuration_error() -> None:
    """Test AuthenticationConfigurationError."""
    configuration = "token_expiry"

    error = AuthenticationConfigurationError(
        configuration,
    )

    assert isinstance(
        error,
        AuthenticationError,
    )

    assert (
        error.configuration
        == configuration
    )

    assert (
        str(error)
        == (
            "Invalid authentication "
            f"configuration: "
            f"'{configuration}'."
        )
    )


def test_authentication_validation_error() -> None:
    """Test AuthenticationValidationError."""
    identity = "user@example.com"
    reason = "invalid credentials"

    error = AuthenticationValidationError(
        identity,
        reason,
    )

    assert isinstance(
        error,
        AuthenticationError,
    )

    assert error.identity == identity
    assert error.reason == reason

    assert (
        str(error)
        == (
            f"Authentication for "
            f"'{identity}' failed: "
            f"{reason}."
        )
    )