from __future__ import annotations

"""Exceptions for chunking."""


class ChunkingError(Exception):
    """Base chunking exception."""


class InvalidChunkSizeError(ChunkingError):
    """Raised when an invalid chunk size is provided."""


class InvalidChunkOverlapError(ChunkingError):
    """Raised when an invalid chunk overlap is provided."""
