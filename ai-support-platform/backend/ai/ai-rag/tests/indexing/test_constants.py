from __future__ import annotations

from ai_rag.indexing.constants import (
    DEFAULT_BATCH_SIZE,
    DEFAULT_INDEX_NAME,
    DEFAULT_OVERWRITE,
    MAX_BATCH_SIZE,
    MIN_BATCH_SIZE,
)


def test_default_index_name():
    assert DEFAULT_INDEX_NAME == "default"


def test_default_batch_size():
    assert DEFAULT_BATCH_SIZE == 100


def test_batch_limits():
    assert MIN_BATCH_SIZE < MAX_BATCH_SIZE


def test_default_overwrite():
    assert DEFAULT_OVERWRITE is False
