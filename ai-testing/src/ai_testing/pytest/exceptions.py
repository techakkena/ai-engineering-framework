"""Exceptions for the ai_testing.pytest module."""

from __future__ import annotations


class PytestError(Exception):
    """Base exception for pytest integration."""


class PytestValidationError(PytestError):
    """Raised when a pytest configuration is invalid."""


__all__ = [
    "PytestError",
    "PytestValidationError",
]