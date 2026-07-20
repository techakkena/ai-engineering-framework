from __future__ import annotations

from ai_agents.conversations.operations import (
    Conversation,
    ConversationMessage,
)


def test_message_creation() -> None:
    message = ConversationMessage(
        role="user",
        content="Hello",
    )

    assert message.role == "user"
    assert message.content == "Hello"


def test_empty_conversation() -> None:
    conversation = Conversation()

    assert conversation.size == 0


def test_add_message() -> None:
    conversation = Conversation()

    conversation.add_message(
        ConversationMessage(
            role="user",
            content="Hello",
        )
    )

    assert conversation.size == 1


def test_clear_conversation() -> None:
    conversation = Conversation()

    conversation.add_message(
        ConversationMessage(
            role="user",
            content="Hello",
        )
    )

    conversation.clear()

    assert conversation.size == 0


def test_multiple_messages() -> None:
    conversation = Conversation()

    conversation.add_message(
        ConversationMessage(
            role="user",
            content="Hi",
        )
    )

    conversation.add_message(
        ConversationMessage(
            role="assistant",
            content="Hello",
        )
    )

    assert conversation.size == 2
    assert conversation.messages[0].role == "user"
    assert conversation.messages[1].role == "assistant"
