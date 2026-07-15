"""
Tests for ai_security.oauth.exceptions.
"""

from ai_security.oauth.exceptions import (
    OAuthAuthenticationError,
    OAuthAuthorizationError,
    OAuthConfigurationError,
    OAuthError,
    OAuthTokenError,
)


def test_oauth_error() -> None:
    """Test OAuthError."""
    error = OAuthError("oauth error")
    assert str(error) == "oauth error"


def test_configuration_error() -> None:
    """Test OAuthConfigurationError."""
    error = OAuthConfigurationError("configuration")
    assert isinstance(error, OAuthError)


def test_authentication_error() -> None:
    """Test OAuthAuthenticationError."""
    error = OAuthAuthenticationError("authentication")
    assert isinstance(error, OAuthError)


def test_authorization_error() -> None:
    """Test OAuthAuthorizationError."""
    error = OAuthAuthorizationError("authorization")
    assert isinstance(error, OAuthError)


def test_token_error() -> None:
    """Test OAuthTokenError."""
    error = OAuthTokenError("token")
    assert isinstance(error, OAuthError)