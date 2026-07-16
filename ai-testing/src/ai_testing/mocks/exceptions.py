"""Exceptions for the ai_testing.mocks module."""

from __future__ import annotations


class MockError(Exception):
    """Base exception for mock operations."""


class MockValidationError(MockError):
    """Raised when mock configuration is invalid."""


class MockRegistrationError(MockError):
    """Raised when mock registration fails."""


class MockNotFoundError(MockRegistrationError):
    """Raised when a requested mock cannot be found."""


class DuplicateMockError(MockRegistrationError):
    """Raised when attempting to register a duplicate mock."""


__all__ = [
    "DuplicateMockError",
    "MockError",
    "MockNotFoundError",
    "MockRegistrationError",
    "MockValidationError",
]