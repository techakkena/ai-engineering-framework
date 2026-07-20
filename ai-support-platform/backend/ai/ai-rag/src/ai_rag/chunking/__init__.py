from __future__ import annotations

"""Chunking utilities."""

from .constants import (
    DEFAULT_CHUNK_OVERLAP,
    DEFAULT_CHUNK_SIZE,
    MAX_CHUNK_SIZE,
    MIN_CHUNK_SIZE,
)
from .exceptions import (
    ChunkingError,
    InvalidChunkOverlapError,
    InvalidChunkSizeError,
)
from .operations import (
    chunk_count,
    split_text,
)

__all__ = [
    "DEFAULT_CHUNK_SIZE",
    "DEFAULT_CHUNK_OVERLAP",
    "MIN_CHUNK_SIZE",
    "MAX_CHUNK_SIZE",
    "ChunkingError",
    "InvalidChunkSizeError",
    "InvalidChunkOverlapError",
    "split_text",
    "chunk_count",
]
