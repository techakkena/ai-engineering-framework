"""
Unit tests for ai_security.authorization.constants.
"""

from __future__ import annotations

from ai_security.authorization.constants import (
    ABAC,
    ACL,
    CASBIN,
    DEFAULT_AUTHORIZATION_PROVIDER,
    DEFAULT_POLICY,
    DEFAULT_RETRIES,
    DEFAULT_ROLE,
    DEFAULT_TIMEOUT,
    OPA,
    RBAC,
    SUPPORTED_AUTHORIZATION_PROVIDERS,
)


def test_authorization_defaults() -> None:
    """Test authorization defaults."""
    assert DEFAULT_AUTHORIZATION_PROVIDER == RBAC
    assert DEFAULT_ROLE == "user"
    assert DEFAULT_POLICY == "default"


def test_supported_authorization_providers() -> None:
    """Test supported authorization providers."""
    expected = {
        RBAC,
        ABAC,
        ACL,
        OPA,
        CASBIN,
    }

    assert (
        SUPPORTED_AUTHORIZATION_PROVIDERS
        == expected
    )


def test_supported_authorization_providers_are_immutable() -> None:
    """Supported providers should be immutable."""
    assert isinstance(
        SUPPORTED_AUTHORIZATION_PROVIDERS,
        frozenset,
    )


def test_authorization_configuration_defaults() -> None:
    """Test configuration defaults."""
    assert DEFAULT_TIMEOUT == 30
    assert DEFAULT_RETRIES == 3