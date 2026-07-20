from __future__ import annotations

"""Tests for ai_memory.base.operations."""

import pytest

from ai_memory.base.constants import MemoryFormat
from ai_memory.base.constants import MemoryScope
from ai_memory.base.constants import MemoryType
from ai_memory.base.constants import MessageRole
from ai_memory.base.exceptions import MemoryValidationError
from ai_memory.base.operations import is_valid_format
from ai_memory.base.operations import is_valid_memory_type
from ai_memory.base.operations import is_valid_role
from ai_memory.base.operations import is_valid_scope
from ai_memory.base.operations import validate_format
from ai_memory.base.operations import validate_memory_type
from ai_memory.base.operations import validate_role
from ai_memory.base.operations import validate_scope


def test_validate_memory_type() -> None:
    """Test validate_memory_type."""
    assert validate_memory_type("buffer") is MemoryType.BUFFER


def test_validate_role() -> None:
    """Test validate_role."""
    assert validate_role("user") is MessageRole.USER


def test_validate_scope() -> None:
    """Test validate_scope."""
    assert validate_scope("session") is MemoryScope.SESSION


def test_validate_format() -> None:
    """Test validate_format."""
    assert validate_format("json") is MemoryFormat.JSON


@pytest.mark.parametrize(
    ("value", "function"),
    [
        ("invalid", validate_memory_type),
        ("invalid", validate_role),
        ("invalid", validate_scope),
        ("invalid", validate_format),
    ],
)
def test_validation_errors(value: str, function) -> None:
    """Test validation errors."""
    with pytest.raises(MemoryValidationError):
        function(value)


def test_is_valid_memory_type() -> None:
    """Test is_valid_memory_type."""
    assert is_valid_memory_type("buffer")
    assert not is_valid_memory_type("invalid")


def test_is_valid_role() -> None:
    """Test is_valid_role."""
    assert is_valid_role("assistant")
    assert not is_valid_role("invalid")


def test_is_valid_scope() -> None:
    """Test is_valid_scope."""
    assert is_valid_scope("global")
    assert not is_valid_scope("invalid")


def test_is_valid_format() -> None:
    """Test is_valid_format."""
    assert is_valid_format("text")
    assert not is_valid_format("invalid")
