from __future__ import annotations

"""Exceptions for the ai_memory.vector module."""

from __future__ import annotations


class VectorError(Exception):
    """Base exception for vector operations."""


class VectorNotFoundError(VectorError):
    """Raised when a vector cannot be found."""


class VectorValidationError(VectorError):
    """Raised when vector validation fails."""


class VectorStateError(VectorError):
    """Raised when an invalid vector state is encountered."""
