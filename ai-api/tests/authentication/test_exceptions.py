"""
Unit tests for ai_api.authentication.exceptions.
"""

from __future__ import annotations

import pytest

from ai_api.authentication.exceptions import (
    AuthenticationConfigurationError,
    AuthenticationError,
    AuthenticationRequiredError,
    AuthenticationTimeoutError,
    ExpiredTokenError,
    InvalidCredentialsError,
    InvalidTokenError,
    MissingAuthorizationHeaderError,
    UnsupportedAuthenticationSchemeError,
)


def test_authentication_error_default_message() -> None:
    """Test AuthenticationError with the default message."""
    error = AuthenticationError()

    assert str(error) == "An authentication error occurred."


def test_authentication_error_custom_message() -> None:
    """Test AuthenticationError with a custom message."""
    error = AuthenticationError("Custom authentication error.")

    assert str(error) == "Custom authentication error."


@pytest.mark.parametrize(
    ("username", "expected"),
    [
        ("john", "Invalid credentials for user 'john'."),
        ("admin", "Invalid credentials for user 'admin'."),
        ("", "Invalid credentials."),
    ],
)
def test_invalid_credentials_error(
    username: str,
    expected: str,
) -> None:
    """Test InvalidCredentialsError."""
    error = InvalidCredentialsError(username)

    assert isinstance(error, AuthenticationError)
    assert error.username == username
    assert str(error) == expected


def test_invalid_token_error() -> None:
    """Test InvalidTokenError."""
    token = "abc123"

    error = InvalidTokenError(token)

    assert isinstance(error, AuthenticationError)
    assert error.token == token
    assert str(error) == "Invalid authentication token."


def test_expired_token_error() -> None:
    """Test ExpiredTokenError."""
    token = "expired-token"

    error = ExpiredTokenError(token)

    assert isinstance(error, AuthenticationError)
    assert error.token == token
    assert str(error) == "Authentication token has expired."


def test_missing_authorization_header_error() -> None:
    """Test MissingAuthorizationHeaderError."""
    error = MissingAuthorizationHeaderError()

    assert isinstance(error, AuthenticationError)
    assert str(error) == "Authorization header is missing."


@pytest.mark.parametrize(
    "scheme",
    [
        "oauth1",
        "ntlm",
        "kerberos",
        "custom",
    ],
)
def test_unsupported_authentication_scheme_error(
    scheme: str,
) -> None:
    """Test UnsupportedAuthenticationSchemeError."""
    error = UnsupportedAuthenticationSchemeError(scheme)

    assert isinstance(error, AuthenticationError)
    assert error.scheme == scheme
    assert (
        str(error)
        == f"Unsupported authentication scheme: '{scheme}'."
    )


def test_authentication_configuration_error() -> None:
    """Test AuthenticationConfigurationError."""
    configuration = "secret_key"

    error = AuthenticationConfigurationError(configuration)

    assert isinstance(error, AuthenticationError)
    assert error.configuration == configuration
    assert (
        str(error)
        == (
            "Invalid authentication configuration: "
            f"'{configuration}'."
        )
    )


def test_authentication_required_error() -> None:
    """Test AuthenticationRequiredError."""
    error = AuthenticationRequiredError()

    assert isinstance(error, AuthenticationError)
    assert str(error) == "Authentication is required."


@pytest.mark.parametrize(
    "timeout",
    [
        10,
        30,
        60,
    ],
)
def test_authentication_timeout_error(
    timeout: int,
) -> None:
    """Test AuthenticationTimeoutError."""
    error = AuthenticationTimeoutError(timeout)

    assert isinstance(error, AuthenticationError)
    assert error.timeout == timeout
    assert (
        str(error)
        == (
            f"Authentication operation timed out "
            f"after {timeout} seconds."
        )
    )