"""Exceptions for the ai_testing.assertions module."""

from __future__ import annotations


class AssertionErrorBase(Exception):
    """Base exception for assertion operations."""


class AssertionValidationError(AssertionErrorBase):
    """Raised when assertion metadata is invalid."""


class AssertionExecutionError(AssertionErrorBase):
    """Raised when assertion execution fails."""


class UnsupportedAssertionStatusError(AssertionValidationError):
    """Raised when an unsupported assertion status is supplied."""


__all__ = [
    "AssertionErrorBase",
    "AssertionExecutionError",
    "AssertionValidationError",
    "UnsupportedAssertionStatusError",
]