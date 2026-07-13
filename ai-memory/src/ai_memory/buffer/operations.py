"""Operations for the ai_memory.buffer module."""

from __future__ import annotations

from .constants import BufferStrategy
from .constants import BufferType
from .exceptions import BufferValidationError


def validate_buffer_type(buffer_type: BufferType | str) -> BufferType:
    """Validate a buffer type."""
    try:
        return BufferType(buffer_type)
    except ValueError as exc:
        raise BufferValidationError(f"Invalid buffer type: {buffer_type!r}.") from exc


def validate_strategy(strategy: BufferStrategy | str) -> BufferStrategy:
    """Validate a buffer strategy."""
    try:
        return BufferStrategy(strategy)
    except ValueError as exc:
        raise BufferValidationError(f"Invalid buffer strategy: {strategy!r}.") from exc


def is_valid_buffer_type(buffer_type: str) -> bool:
    """Return True if the buffer type is valid."""
    try:
        BufferType(buffer_type)
        return True
    except ValueError:
        return False


def is_valid_strategy(strategy: str) -> bool:
    """Return True if the strategy is valid."""
    try:
        BufferStrategy(strategy)
        return True
    except ValueError:
        return False
