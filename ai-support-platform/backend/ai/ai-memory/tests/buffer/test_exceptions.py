from __future__ import annotations

"""Tests for ai_memory.buffer.exceptions."""

from ai_memory.buffer.exceptions import (
    BufferEmptyError,
    BufferError,
    BufferOverflowError,
    BufferValidationError,
)


def test_exception_inheritance() -> None:
    assert issubclass(BufferOverflowError, BufferError)
    assert issubclass(BufferEmptyError, BufferError)
    assert issubclass(BufferValidationError, BufferError)


def test_raise_buffer_error() -> None:
    try:
        raise BufferOverflowError("overflow")
    except BufferOverflowError as exc:
        assert str(exc) == "overflow"
