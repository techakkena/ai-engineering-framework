"""
Custom exceptions for the datetime utilities package.
"""

from __future__ import annotations

__all__ = [
    "DateTimeUtilsError",
    "DateTimeParseError",
    "DateTimeFormatError",
]


class DateTimeUtilsError(Exception):
    """Base exception for datetime utility errors."""


class DateTimeParseError(DateTimeUtilsError):
    """Raised when parsing a datetime fails."""


class DateTimeFormatError(DateTimeUtilsError):
    """Raised when formatting a datetime fails."""
