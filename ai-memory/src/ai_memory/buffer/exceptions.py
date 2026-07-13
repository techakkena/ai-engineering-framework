"""Exceptions for the ai_memory.buffer module."""

from __future__ import annotations


class BufferError(Exception):
    """Base exception for buffer operations."""


class BufferOverflowError(BufferError):
    """Raised when a buffer exceeds its capacity."""


class BufferEmptyError(BufferError):
    """Raised when a buffer is empty."""


class BufferValidationError(BufferError):
    """Raised when buffer validation fails."""
