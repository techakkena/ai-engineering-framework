from __future__ import annotations

from ai_rag.chunking.constants import (
    DEFAULT_CHUNK_OVERLAP,
    DEFAULT_CHUNK_SIZE,
    MAX_CHUNK_SIZE,
    MIN_CHUNK_SIZE,
)


def test_default_chunk_size():
    assert DEFAULT_CHUNK_SIZE == 1000


def test_default_overlap():
    assert DEFAULT_CHUNK_OVERLAP == 200


def test_chunk_limits():
    assert MIN_CHUNK_SIZE < MAX_CHUNK_SIZE
