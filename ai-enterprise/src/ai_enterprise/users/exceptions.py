"""Exceptions for the ai_enterprise.users module."""

from __future__ import annotations


class UserError(Exception):
    """Base exception for user operations."""


class UserValidationError(UserError):
    """Raised when user validation fails."""


class UserRegistrationError(UserError):
    """Raised when user registration fails."""


class UserNotFoundError(
    UserRegistrationError,
):
    """Raised when a user cannot be found."""


class DuplicateUserError(
    UserRegistrationError,
):
    """Raised when attempting to register a duplicate user."""


class UnsupportedUserRoleError(
    UserValidationError,
):
    """Raised when an unsupported user role is specified."""


__all__ = [
    "DuplicateUserError",
    "UnsupportedUserRoleError",
    "UserError",
    "UserNotFoundError",
    "UserRegistrationError",
    "UserValidationError",
]