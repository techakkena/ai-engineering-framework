from __future__ import annotations

"""Custom exceptions for the ai_memory.base module."""

from __future__ import annotations


class MemoryError(Exception):
    """Base exception for all memory-related errors."""


class MemoryValidationError(MemoryError):
    """Raised when memory validation fails."""


class MemoryNotFoundError(MemoryError):
    """Raised when a requested memory object cannot be found."""


class MemoryStorageError(MemoryError):
    """Raised when memory storage operations fail."""


class MemorySerializationError(MemoryError):
    """Raised when serialization or deserialization fails."""


class MemoryConfigurationError(MemoryError):
    """Raised when memory configuration is invalid."""


class MemoryCapacityError(MemoryError):
    """Raised when a memory instance exceeds its capacity."""
