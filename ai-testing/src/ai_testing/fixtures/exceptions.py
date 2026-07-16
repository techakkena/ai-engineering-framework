"""Exceptions for the ai_testing.fixtures module."""

from __future__ import annotations


class FixtureError(Exception):
    """Base exception for all fixture-related errors."""


class FixtureValidationError(FixtureError):
    """Raised when fixture configuration fails validation."""


class FixtureRegistrationError(FixtureError):
    """Raised when fixture registration fails."""


class FixtureNotFoundError(FixtureError):
    """Raised when a requested fixture cannot be found."""


class DuplicateFixtureError(FixtureRegistrationError):
    """Raised when attempting to register a duplicate fixture."""


class UnsupportedFixtureScopeError(FixtureValidationError):
    """Raised when an unsupported fixture scope is specified."""


__all__ = [
    "DuplicateFixtureError",
    "FixtureError",
    "FixtureNotFoundError",
    "FixtureRegistrationError",
    "FixtureValidationError",
    "UnsupportedFixtureScopeError",
]