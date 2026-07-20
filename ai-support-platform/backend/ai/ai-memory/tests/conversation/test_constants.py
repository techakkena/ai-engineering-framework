from __future__ import annotations

"""Tests for ai_memory.conversation.constants."""

from ai_memory.conversation.constants import (
    ConversationRole,
    ConversationState,
    ConversationType,
    DEFAULT_CONVERSATION_NAME,
    DEFAULT_MAX_MESSAGES,
)


def test_conversation_type_values() -> None:
    assert ConversationType.SESSION.value == "session"
    assert ConversationType.PERSISTENT.value == "persistent"


def test_conversation_state_values() -> None:
    assert ConversationState.ACTIVE.value == "active"
    assert ConversationState.INACTIVE.value == "inactive"
    assert ConversationState.ARCHIVED.value == "archived"


def test_conversation_role_values() -> None:
    assert ConversationRole.SYSTEM.value == "system"
    assert ConversationRole.USER.value == "user"
    assert ConversationRole.ASSISTANT.value == "assistant"
    assert ConversationRole.TOOL.value == "tool"


def test_default_values() -> None:
    assert DEFAULT_MAX_MESSAGES == 100
    assert DEFAULT_CONVERSATION_NAME == "conversation"
