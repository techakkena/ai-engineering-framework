"""Exceptions for the ai_cloud.authentication module."""

from __future__ import annotations


class AuthenticationError(Exception):
    """Base exception for authentication operations."""


class AuthenticationValidationError(AuthenticationError):
    """Raised when authentication validation fails."""


class AuthenticationRegistrationError(AuthenticationError):
    """Raised when authentication registration fails."""


class AuthenticationNotFoundError(
    AuthenticationRegistrationError,
):
    """Raised when an authentication definition cannot be found."""


class DuplicateAuthenticationError(
    AuthenticationRegistrationError,
):
    """Raised when attempting to register a duplicate authentication."""
    

class UnsupportedAuthenticationTypeError(
    AuthenticationValidationError,
):
    """Raised when an unsupported authentication type is specified."""


__all__ = [
    "AuthenticationError",
    "AuthenticationNotFoundError",
    "AuthenticationRegistrationError",
    "AuthenticationValidationError",
    "DuplicateAuthenticationError",
    "UnsupportedAuthenticationTypeError",
]