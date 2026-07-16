"""Exceptions for the ai_plugins.validation module."""

from __future__ import annotations


class ValidationError(Exception):
    """Base exception for validation operations."""


class ValidationDefinitionError(ValidationError):
    """Raised when validation definition validation fails."""


class ValidationRegistrationError(ValidationError):
    """Raised when validation registration fails."""


class ValidationNotFoundError(
    ValidationRegistrationError,
):
    """Raised when a validation definition cannot be found."""


class DuplicateValidationError(
    ValidationRegistrationError,
):
    """Raised when attempting to register a duplicate validation."""


class UnsupportedValidationLevelError(
    ValidationDefinitionError,
):
    """Raised when an unsupported validation level is specified."""


__all__ = [
    "DuplicateValidationError",
    "UnsupportedValidationLevelError",
    "ValidationDefinitionError",
    "ValidationError",
    "ValidationNotFoundError",
    "ValidationRegistrationError",
]