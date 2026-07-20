from __future__ import annotations

from ai_rag.chunking.exceptions import (
    ChunkingError,
    InvalidChunkOverlapError,
    InvalidChunkSizeError,
)


def test_chunking_error():
    assert issubclass(
        ChunkingError,
        Exception,
    )


def test_invalid_chunk_size_error():
    assert issubclass(
        InvalidChunkSizeError,
        ChunkingError,
    )


def test_invalid_chunk_overlap_error():
    assert issubclass(
        InvalidChunkOverlapError,
        ChunkingError,
    )
