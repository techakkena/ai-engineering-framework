"""
Tests for ai_security.permissions.exceptions.
"""

from ai_security.permissions.exceptions import (
    PermissionConfigurationError,
    PermissionDeniedError,
    PermissionError,
    RoleNotFoundError,
)


def test_permission_error() -> None:
    """PermissionError should derive from Exception."""
    error = PermissionError("permission error")
    assert str(error) == "permission error"


def test_permission_configuration_error() -> None:
    """PermissionConfigurationError should derive from PermissionError."""
    error = PermissionConfigurationError("configuration error")
    assert isinstance(error, PermissionError)


def test_permission_denied_error() -> None:
    """PermissionDeniedError should derive from PermissionError."""
    error = PermissionDeniedError("permission denied")
    assert isinstance(error, PermissionError)


def test_role_not_found_error() -> None:
    """RoleNotFoundError should derive from PermissionError."""
    error = RoleNotFoundError("role not found")
    assert isinstance(error, PermissionError)