"""Exceptions for the ai_optimization.profiling module."""

from __future__ import annotations


class ProfileError(Exception):
    """Base exception for profiling operations."""


class ProfileValidationError(ProfileError):
    """Raised when profile validation fails."""


class ProfileRegistrationError(ProfileError):
    """Raised when profile registration fails."""


class ProfileNotFoundError(ProfileRegistrationError):
    """Raised when a profile definition cannot be found."""


class DuplicateProfileError(ProfileRegistrationError):
    """Raised when attempting to register a duplicate profile."""


class UnsupportedProfileTypeError(ProfileValidationError):
    """Raised when an unsupported profile type is specified."""


__all__ = [
    "DuplicateProfileError",
    "ProfileError",
    "ProfileNotFoundError",
    "ProfileRegistrationError",
    "ProfileValidationError",
    "UnsupportedProfileTypeError",
]