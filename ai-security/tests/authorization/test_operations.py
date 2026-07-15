"""
Unit tests for ai_security.authorization.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_security.authorization.exceptions import (
    InvalidAuthorizationProviderError,
)
from ai_security.authorization.operations import (
    build_authorization_id,
    is_supported_authorization_provider,
    normalize_authorization_provider,
    validate_authorization_id,
    validate_authorization_provider,
)


# ============================================================================
# normalize_authorization_provider
# ============================================================================


@pytest.mark.parametrize(
    ("provider", "expected"),
    [
        ("RBAC", "rbac"),
        (" AbAc ", "abac"),
        ("ACL", "acl"),
        ("OPA", "opa"),
        ("Casbin", "casbin"),
    ],
)
def test_normalize_authorization_provider(
    provider: str,
    expected: str,
) -> None:
    """Test provider normalization."""
    assert (
        normalize_authorization_provider(
            provider,
        )
        == expected
    )


# ============================================================================
# validate_authorization_provider
# ============================================================================


@pytest.mark.parametrize(
    "provider",
    [
        "rbac",
        "abac",
        "acl",
        "opa",
        "casbin",
    ],
)
def test_validate_authorization_provider(
    provider: str,
) -> None:
    """Test valid providers."""
    assert (
        validate_authorization_provider(
            provider,
        )
        == provider
    )


@pytest.mark.parametrize(
    "provider",
    [
        "",
        "iam",
        "custom",
        "policy",
    ],
)
def test_validate_authorization_provider_invalid(
    provider: str,
) -> None:
    """Invalid providers should raise."""
    with pytest.raises(
        InvalidAuthorizationProviderError,
    ):
        validate_authorization_provider(
            provider,
        )


# ============================================================================
# is_supported_authorization_provider
# ============================================================================


@pytest.mark.parametrize(
    ("provider", "expected"),
    [
        ("rbac", True),
        ("abac", True),
        ("acl", True),
        ("opa", True),
        ("casbin", True),
        ("iam", False),
        ("custom", False),
    ],
)
def test_is_supported_authorization_provider(
    provider: str,
    expected: bool,
) -> None:
    """Test provider support detection."""
    assert (
        is_supported_authorization_provider(
            provider,
        )
        is expected
    )


# ============================================================================
# validate_authorization_id
# ============================================================================


@pytest.mark.parametrize(
    "authorization_id",
    [
        "authorization",
        "authorization_01",
        "authorization-01",
        "runtime123",
    ],
)
def test_validate_authorization_id(
    authorization_id: str,
) -> None:
    """Test valid authorization identifiers."""
    assert (
        validate_authorization_id(
            authorization_id,
        )
        == authorization_id.lower()
    )


@pytest.mark.parametrize(
    "authorization_id",
    [
        "",
        "123authorization",
        "authorization name",
        "@authorization",
    ],
)
def test_validate_authorization_id_invalid(
    authorization_id: str,
) -> None:
    """Invalid identifiers should raise."""
    with pytest.raises(ValueError):
        validate_authorization_id(
            authorization_id,
        )


# ============================================================================
# build_authorization_id
# ============================================================================


def test_build_authorization_id() -> None:
    """Test authorization ID generation."""
    authorization_id = (
        build_authorization_id()
    )

    assert authorization_id.startswith(
        "authorization-",
    )

    pattern = re.compile(
        (
            r"^authorization-"
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert (
        pattern.fullmatch(
            authorization_id,
        )
        is not None
    )