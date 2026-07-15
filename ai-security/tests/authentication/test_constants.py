"""
Unit tests for ai_security.authentication.constants.
"""

from __future__ import annotations

from ai_security.authentication.constants import (
    ACTIVE_DIRECTORY,
    API_KEY,
    BASIC,
    BEARER,
    DEFAULT_AUTH_PROVIDER,
    DEFAULT_AUTH_SCHEME,
    DEFAULT_RETRIES,
    DEFAULT_TIMEOUT,
    DEFAULT_TOKEN_EXPIRY,
    JWT,
    LDAP,
    LOCAL,
    OAUTH2,
    OPENID_CONNECT,
    SUPPORTED_AUTH_PROVIDERS,
    SUPPORTED_AUTH_SCHEMES,
)


def test_authentication_defaults() -> None:
    """Test authentication defaults."""
    assert DEFAULT_AUTH_PROVIDER == LOCAL
    assert DEFAULT_AUTH_SCHEME == BEARER
    assert DEFAULT_TOKEN_EXPIRY == 3600


def test_supported_authentication_providers() -> None:
    """Test supported authentication providers."""
    expected = {
        LOCAL,
        JWT,
        OAUTH2,
        OPENID_CONNECT,
        LDAP,
        ACTIVE_DIRECTORY,
    }

    assert (
        SUPPORTED_AUTH_PROVIDERS
        == expected
    )


def test_supported_authentication_providers_are_immutable() -> None:
    """Supported providers should be immutable."""
    assert isinstance(
        SUPPORTED_AUTH_PROVIDERS,
        frozenset,
    )


def test_supported_authentication_schemes() -> None:
    """Test supported authentication schemes."""
    expected = {
        BEARER,
        BASIC,
        API_KEY,
    }

    assert (
        SUPPORTED_AUTH_SCHEMES
        == expected
    )


def test_supported_authentication_schemes_are_immutable() -> None:
    """Supported schemes should be immutable."""
    assert isinstance(
        SUPPORTED_AUTH_SCHEMES,
        frozenset,
    )


def test_authentication_configuration_defaults() -> None:
    """Test configuration defaults."""
    assert DEFAULT_TIMEOUT == 30
    assert DEFAULT_RETRIES == 3