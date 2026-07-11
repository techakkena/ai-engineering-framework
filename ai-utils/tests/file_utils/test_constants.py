"""
Unit tests for file utility constants.
"""

from __future__ import annotations

from ai_utils.file_utils import constants


def test_default_encoding() -> None:
    assert constants.DEFAULT_ENCODING == "utf-8"


def test_default_buffer_size() -> None:
    assert constants.DEFAULT_BUFFER_SIZE > 0


def test_default_chunk_size() -> None:
    assert constants.DEFAULT_CHUNK_SIZE > 0


def test_default_newline() -> None:
    assert constants.DEFAULT_NEWLINE == "\n"
