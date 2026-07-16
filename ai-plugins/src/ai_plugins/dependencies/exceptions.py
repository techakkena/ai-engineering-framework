"""Exceptions for the ai_plugins.dependencies module."""

from __future__ import annotations


class DependencyError(Exception):
    """Base exception for dependency operations."""


class DependencyValidationError(DependencyError):
    """Raised when dependency validation fails."""


class DependencyRegistrationError(DependencyError):
    """Raised when dependency registration fails."""


class DependencyNotFoundError(
    DependencyRegistrationError,
):
    """Raised when a dependency definition cannot be found."""


class DuplicateDependencyError(
    DependencyRegistrationError,
):
    """Raised when attempting to register a duplicate dependency."""


class UnsupportedDependencyTypeError(
    DependencyValidationError,
):
    """Raised when an unsupported dependency type is specified."""


__all__ = [
    "DependencyError",
    "DependencyNotFoundError",
    "DependencyRegistrationError",
    "DependencyValidationError",
    "DuplicateDependencyError",
    "UnsupportedDependencyTypeError",
]