"""
Unit tests for ai_api.authorization.exceptions.
"""

from __future__ import annotations

import pytest

from ai_api.authorization.exceptions import (
    AuthorizationConfigurationError,
    AuthorizationError,
    InsufficientPermissionsError,
    InvalidPermissionError,
    InvalidRoleError,
    InvalidScopeError,
    RoleHierarchyError,
    UnauthorizedAccessError,
)


def test_authorization_error_default_message() -> None:
    """Test AuthorizationError with the default message."""
    error = AuthorizationError()

    assert str(error) == "An authorization error occurred."


def test_authorization_error_custom_message() -> None:
    """Test AuthorizationError with a custom message."""
    error = AuthorizationError("Custom authorization error.")

    assert str(error) == "Custom authorization error."


@pytest.mark.parametrize(
    ("resource", "expected"),
    [
        (
            "users",
            "Unauthorized access to resource 'users'.",
        ),
        (
            "admin/dashboard",
            "Unauthorized access to resource 'admin/dashboard'.",
        ),
        (
            "",
            "Unauthorized access.",
        ),
    ],
)
def test_unauthorized_access_error(
    resource: str,
    expected: str,
) -> None:
    """Test UnauthorizedAccessError."""
    error = UnauthorizedAccessError(resource)

    assert isinstance(error, AuthorizationError)
    assert error.resource == resource
    assert str(error) == expected


@pytest.mark.parametrize(
    "role",
    [
        "",
        "manager",
        "developer",
        "guest-admin",
    ],
)
def test_invalid_role_error(
    role: str,
) -> None:
    """Test InvalidRoleError."""
    error = InvalidRoleError(role)

    assert isinstance(error, AuthorizationError)
    assert error.role == role
    assert str(error) == f"Invalid role: '{role}'."


@pytest.mark.parametrize(
    "permission",
    [
        "",
        "publish",
        "execute_all",
        "manage",
    ],
)
def test_invalid_permission_error(
    permission: str,
) -> None:
    """Test InvalidPermissionError."""
    error = InvalidPermissionError(permission)

    assert isinstance(error, AuthorizationError)
    assert error.permission == permission
    assert (
        str(error)
        == f"Invalid permission: '{permission}'."
    )


@pytest.mark.parametrize(
    "scope",
    [
        "",
        "billing",
        "analytics",
        "custom_scope",
    ],
)
def test_invalid_scope_error(
    scope: str,
) -> None:
    """Test InvalidScopeError."""
    error = InvalidScopeError(scope)

    assert isinstance(error, AuthorizationError)
    assert error.scope == scope
    assert (
        str(error)
        == f"Invalid scope: '{scope}'."
    )


@pytest.mark.parametrize(
    "permission",
    [
        "write",
        "delete",
        "admin",
    ],
)
def test_insufficient_permissions_error(
    permission: str,
) -> None:
    """Test InsufficientPermissionsError."""
    error = InsufficientPermissionsError(permission)

    assert isinstance(error, AuthorizationError)
    assert error.permission == permission
    assert (
        str(error)
        == (
            f"Insufficient permissions: "
            f"'{permission}' required."
        )
    )


@pytest.mark.parametrize(
    "role",
    [
        "guest",
        "user",
        "admin",
    ],
)
def test_role_hierarchy_error(
    role: str,
) -> None:
    """Test RoleHierarchyError."""
    error = RoleHierarchyError(role)

    assert isinstance(error, AuthorizationError)
    assert error.role == role
    assert (
        str(error)
        == f"Invalid role hierarchy for '{role}'."
    )


def test_authorization_configuration_error() -> None:
    """Test AuthorizationConfigurationError."""
    configuration = "policy"

    error = AuthorizationConfigurationError(
        configuration,
    )

    assert isinstance(error, AuthorizationError)
    assert error.configuration == configuration
    assert (
        str(error)
        == (
            "Invalid authorization configuration: "
            f"'{configuration}'."
        )
    )