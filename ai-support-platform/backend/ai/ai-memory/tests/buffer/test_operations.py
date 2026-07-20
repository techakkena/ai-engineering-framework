from __future__ import annotations

"""Tests for ai_memory.buffer.operations."""

import pytest

from ai_memory.buffer.constants import BufferStrategy
from ai_memory.buffer.constants import BufferType
from ai_memory.buffer.exceptions import BufferValidationError
from ai_memory.buffer.operations import (
    is_valid_buffer_type,
    is_valid_strategy,
    validate_buffer_type,
    validate_strategy,
)


def test_validate_buffer_type() -> None:
    assert validate_buffer_type("conversation") is BufferType.CONVERSATION


def test_validate_strategy() -> None:
    assert validate_strategy("fifo") is BufferStrategy.FIFO


@pytest.mark.parametrize(
    ("value", "validator"),
    [
        ("invalid", validate_buffer_type),
        ("invalid", validate_strategy),
    ],
)
def test_validation_error(value: str, validator) -> None:
    with pytest.raises(BufferValidationError):
        validator(value)


def test_is_valid_buffer_type() -> None:
    assert is_valid_buffer_type("window")
    assert not is_valid_buffer_type("invalid")


def test_is_valid_strategy() -> None:
    assert is_valid_strategy("sliding")
    assert not is_valid_strategy("invalid")
