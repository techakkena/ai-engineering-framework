from __future__ import annotations

"""Exceptions for the ai_memory.utils module."""

from __future__ import annotations


class UtilsError(Exception):
    """Base exception for utility operations."""


class SerializationError(UtilsError):
    """Raised when serialization fails."""


class CompressionError(UtilsError):
    """Raised when compression fails."""


class ValidationError(UtilsError):
    """Raised when validation fails."""
