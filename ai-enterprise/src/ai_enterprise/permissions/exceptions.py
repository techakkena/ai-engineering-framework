"""Exceptions for the ai_enterprise.permissions module."""

from __future__ import annotations


class PermissionError(Exception):
    """Base exception for permission operations."""


class PermissionValidationError(PermissionError):
    """Raised when permission validation fails."""


class PermissionRegistrationError(PermissionError):
    """Raised when permission registration fails."""


class PermissionNotFoundError(
    PermissionRegistrationError,
):
    """Raised when a permission cannot be found."""


class DuplicatePermissionError(
    PermissionRegistrationError,
):
    """Raised when attempting to register a duplicate permission."""


class UnsupportedPermissionError(
    PermissionValidationError,
):
    """Raised when an unsupported permission is specified."""


__all__ = [
    "DuplicatePermissionError",
    "PermissionError",
    "PermissionNotFoundError",
    "PermissionRegistrationError",
    "PermissionValidationError",
    "UnsupportedPermissionError",
]