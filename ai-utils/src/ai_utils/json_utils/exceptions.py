"""
Custom exceptions for JSON utilities.
"""

from __future__ import annotations

__all__ = [
    "JsonUtilsError",
    "JsonReadError",
    "JsonWriteError",
    "JsonDecodeError",
]


class JsonUtilsError(Exception):
    """Base exception for JSON utility errors."""


class JsonReadError(JsonUtilsError):
    """Raised when reading JSON fails."""


class JsonWriteError(JsonUtilsError):
    """Raised when writing JSON fails."""


class JsonDecodeError(JsonUtilsError):
    """Raised when JSON decoding fails."""
