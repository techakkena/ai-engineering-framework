"""
AI Engineering Framework
Conversation Memory Tests

Author : TECHAKKENA
"""

from ai_chat.conversation import Conversation
from ai_chat.memory import ConversationMemory


def test_create_session():
    memory = ConversationMemory()

    conversation = memory.create("session1")

    assert isinstance(conversation, Conversation)
    assert memory.exists("session1")


def test_get_session():
    memory = ConversationMemory()

    memory.create("session1")

    conversation = memory.get("session1")

    assert isinstance(conversation, Conversation)


def test_auto_create_session():
    memory = ConversationMemory()

    conversation = memory.get("session2")

    assert isinstance(conversation, Conversation)
    assert memory.exists("session2")


def test_delete_session():
    memory = ConversationMemory()

    memory.create("session1")

    assert memory.delete("session1") is True
    assert memory.exists("session1") is False


def test_delete_missing_session():
    memory = ConversationMemory()

    assert memory.delete("missing") is False


def test_clear_session():
    memory = ConversationMemory()

    conversation = memory.create("session1")

    conversation.user("Hello")

    assert conversation.count() == 1

    assert memory.clear("session1") is True

    assert conversation.count() == 0


def test_clear_missing_session():
    memory = ConversationMemory()

    assert memory.clear("missing") is False


def test_sessions():
    memory = ConversationMemory()

    memory.create("a")
    memory.create("b")

    sessions = memory.sessions()

    assert "a" in sessions
    assert "b" in sessions


def test_count():
    memory = ConversationMemory()

    memory.create("1")
    memory.create("2")
    memory.create("3")

    assert memory.count() == 3


def test_independent_conversations():
    memory = ConversationMemory()

    first = memory.create("one")
    second = memory.create("two")

    first.user("Hello")

    assert first.count() == 1
    assert second.count() == 0
