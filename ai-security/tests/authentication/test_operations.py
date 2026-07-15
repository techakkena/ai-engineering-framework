"""
Unit tests for ai_security.authentication.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_security.authentication.exceptions import (
    InvalidAuthenticationProviderError,
)
from ai_security.authentication.operations import (
    build_authentication_id,
    is_supported_authentication_provider,
    normalize_authentication_provider,
    validate_authentication_id,
    validate_authentication_provider,
)


# ============================================================================
# normalize_authentication_provider
# ============================================================================


@pytest.mark.parametrize(
    ("provider", "expected"),
    [
        ("LOCAL", "local"),
        (" Jwt ", "jwt"),
        ("OAuth2", "oauth2"),
        (
            "OpenID-Connect",
            "openid-connect",
        ),
        ("LDAP", "ldap"),
        (
            "Active-Directory",
            "active-directory",
        ),
    ],
)
def test_normalize_authentication_provider(
    provider: str,
    expected: str,
) -> None:
    """Test provider normalization."""
    assert (
        normalize_authentication_provider(
            provider,
        )
        == expected
    )


# ============================================================================
# validate_authentication_provider
# ============================================================================


@pytest.mark.parametrize(
    "provider",
    [
        "local",
        "jwt",
        "oauth2",
        "openid-connect",
        "ldap",
        "active-directory",
    ],
)
def test_validate_authentication_provider(
    provider: str,
) -> None:
    """Test valid providers."""
    assert (
        validate_authentication_provider(
            provider,
        )
        == provider
    )


@pytest.mark.parametrize(
    "provider",
    [
        "",
        "saml",
        "kerberos",
        "azure-ad",
    ],
)
def test_validate_authentication_provider_invalid(
    provider: str,
) -> None:
    """Invalid providers should raise."""
    with pytest.raises(
        InvalidAuthenticationProviderError,
    ):
        validate_authentication_provider(
            provider,
        )


# ============================================================================
# is_supported_authentication_provider
# ============================================================================


@pytest.mark.parametrize(
    ("provider", "expected"),
    [
        ("local", True),
        ("jwt", True),
        ("oauth2", True),
        ("openid-connect", True),
        ("ldap", True),
        ("active-directory", True),
        ("saml", False),
        ("kerberos", False),
    ],
)
def test_is_supported_authentication_provider(
    provider: str,
    expected: bool,
) -> None:
    """Test provider support detection."""
    assert (
        is_supported_authentication_provider(
            provider,
        )
        is expected
    )


# ============================================================================
# validate_authentication_id
# ============================================================================


@pytest.mark.parametrize(
    "authentication_id",
    [
        "auth",
        "auth_01",
        "auth-01",
        "runtime123",
    ],
)
def test_validate_authentication_id(
    authentication_id: str,
) -> None:
    """Test valid authentication identifiers."""
    assert (
        validate_authentication_id(
            authentication_id,
        )
        == authentication_id.lower()
    )


@pytest.mark.parametrize(
    "authentication_id",
    [
        "",
        "123auth",
        "auth name",
        "@auth",
    ],
)
def test_validate_authentication_id_invalid(
    authentication_id: str,
) -> None:
    """Invalid identifiers should raise."""
    with pytest.raises(ValueError):
        validate_authentication_id(
            authentication_id,
        )


# ============================================================================
# build_authentication_id
# ============================================================================


def test_build_authentication_id() -> None:
    """Test authentication ID generation."""
    authentication_id = (
        build_authentication_id()
    )

    assert authentication_id.startswith(
        "auth-",
    )

    pattern = re.compile(
        (
            r"^auth-"
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert (
        pattern.fullmatch(
            authentication_id,
        )
        is not None
    )