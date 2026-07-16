"""Exceptions for the ai_optimization.compression module."""

from __future__ import annotations


class CompressionError(Exception):
    """Base exception for compression operations."""


class CompressionValidationError(CompressionError):
    """Raised when compression validation fails."""


class CompressionRegistrationError(CompressionError):
    """Raised when compression registration fails."""


class CompressionNotFoundError(
    CompressionRegistrationError,
):
    """Raised when a compression definition cannot be found."""


class DuplicateCompressionError(
    CompressionRegistrationError,
):
    """Raised when attempting to register a duplicate compression."""


class UnsupportedCompressionTypeError(
    CompressionValidationError,
):
    """Raised when an unsupported compression type is specified."""


__all__ = [
    "CompressionError",
    "CompressionNotFoundError",
    "CompressionRegistrationError",
    "CompressionValidationError",
    "DuplicateCompressionError",
    "UnsupportedCompressionTypeError",
]