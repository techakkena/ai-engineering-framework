"""Exceptions for the ai_cloud.secrets module."""

from __future__ import annotations


class SecretError(Exception):
    """Base exception for secret operations."""


class SecretValidationError(SecretError):
    """Raised when secret validation fails."""


class SecretRegistrationError(SecretError):
    """Raised when secret registration fails."""


class SecretNotFoundError(
    SecretRegistrationError,
):
    """Raised when a secret definition cannot be found."""


class DuplicateSecretError(
    SecretRegistrationError,
):
    """Raised when attempting to register a duplicate secret."""


class UnsupportedSecretTypeError(
    SecretValidationError,
):
    """Raised when an unsupported secret type is specified."""


__all__ = [
    "DuplicateSecretError",
    "SecretError",
    "SecretNotFoundError",
    "SecretRegistrationError",
    "SecretValidationError",
    "UnsupportedSecretTypeError",
]