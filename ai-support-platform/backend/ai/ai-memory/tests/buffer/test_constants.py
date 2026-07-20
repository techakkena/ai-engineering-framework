from __future__ import annotations

"""Tests for ai_memory.buffer.constants."""

from ai_memory.buffer.constants import (
    BufferStrategy,
    BufferType,
    DEFAULT_BUFFER_SIZE,
    DEFAULT_TOKEN_LIMIT,
    DEFAULT_WINDOW_SIZE,
)


def test_buffer_type_values() -> None:
    assert BufferType.CONVERSATION.value == "conversation"
    assert BufferType.WINDOW.value == "window"
    assert BufferType.TOKEN.value == "token"


def test_buffer_strategy_values() -> None:
    assert BufferStrategy.FIFO.value == "fifo"
    assert BufferStrategy.LIFO.value == "lifo"
    assert BufferStrategy.SLIDING.value == "sliding"


def test_default_values() -> None:
    assert DEFAULT_BUFFER_SIZE == 100
    assert DEFAULT_WINDOW_SIZE == 20
    assert DEFAULT_TOKEN_LIMIT == 4096
