"""Exceptions for the ai_testing.data module."""

from __future__ import annotations


class DataError(Exception):
    """Base exception for data operations."""


class DataValidationError(DataError):
    """Raised when dataset validation fails."""


class DataRegistrationError(DataError):
    """Raised when dataset registration fails."""


class DataNotFoundError(DataRegistrationError):
    """Raised when a dataset cannot be found."""


class DuplicateDataError(DataRegistrationError):
    """Raised when attempting to register a duplicate dataset."""


__all__ = [
    "DataError",
    "DataNotFoundError",
    "DataRegistrationError",
    "DataValidationError",
    "DuplicateDataError",
]