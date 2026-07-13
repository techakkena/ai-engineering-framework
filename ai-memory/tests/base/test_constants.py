"""Tests for ai_memory.base.constants."""

from ai_memory.base.constants import MemoryFormat
from ai_memory.base.constants import MemoryScope
from ai_memory.base.constants import MemoryType
from ai_memory.base.constants import MessageRole


def test_memory_type_values() -> None:
    """Test MemoryType values."""
    assert MemoryType.BUFFER.value == "buffer"
    assert MemoryType.CONVERSATION.value == "conversation"
    assert MemoryType.SUMMARY.value == "summary"
    assert MemoryType.ENTITY.value == "entity"
    assert MemoryType.VECTOR.value == "vector"


def test_message_role_values() -> None:
    """Test MessageRole values."""
    assert MessageRole.SYSTEM.value == "system"
    assert MessageRole.USER.value == "user"
    assert MessageRole.ASSISTANT.value == "assistant"
    assert MessageRole.TOOL.value == "tool"


def test_memory_scope_values() -> None:
    """Test MemoryScope values."""
    assert MemoryScope.SESSION.value == "session"
    assert MemoryScope.USER.value == "user"
    assert MemoryScope.GLOBAL.value == "global"


def test_memory_format_values() -> None:
    """Test MemoryFormat values."""
    assert MemoryFormat.TEXT.value == "text"
    assert MemoryFormat.JSON.value == "json"
