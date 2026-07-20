from __future__ import annotations

import pytest

from ai_rag.chunking.operations import (
    chunk_count,
    split_text,
)


def test_split_text():

    text = "A" * 2500

    chunks = split_text(text)

    assert len(chunks) > 1


def test_empty_text():

    assert split_text("") == []


def test_invalid_chunk_size():

    with pytest.raises(ValueError):
        split_text(
            "hello",
            chunk_size=0,
        )


def test_invalid_overlap():

    with pytest.raises(ValueError):
        split_text(
            "hello",
            chunk_size=100,
            chunk_overlap=100,
        )


def test_chunk_count():

    text = "A" * 3000

    assert chunk_count(text) > 1
