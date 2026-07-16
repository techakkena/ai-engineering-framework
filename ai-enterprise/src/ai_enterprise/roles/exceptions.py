"""Exceptions for the ai_enterprise.roles module."""

from __future__ import annotations


class RoleError(Exception):
    """Base exception for role operations."""


class RoleValidationError(RoleError):
    """Raised when role validation fails."""


class RoleRegistrationError(RoleError):
    """Raised when role registration fails."""


class RoleNotFoundError(
    RoleRegistrationError,
):
    """Raised when a role cannot be found."""


class DuplicateRoleError(
    RoleRegistrationError,
):
    """Raised when attempting to register a duplicate role."""


class UnsupportedRoleError(
    RoleValidationError,
):
    """Raised when an unsupported role is specified."""


__all__ = [
    "DuplicateRoleError",
    "RoleError",
    "RoleNotFoundError",
    "RoleRegistrationError",
    "RoleValidationError",
    "UnsupportedRoleError",
]