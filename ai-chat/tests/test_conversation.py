"""
AI Engineering Framework
Conversation Tests

Author : TECHAKKENA
"""

from ai_chat.conversation import Conversation
from ai_chat.types import ChatRole


def test_empty_conversation():
    conversation = Conversation()

    assert conversation.count() == 0
    assert conversation.messages() == []


def test_add_system_message():
    conversation = Conversation()

    conversation.system("You are an AI assistant.")

    assert conversation.count() == 1
    assert conversation.messages()[0].role == ChatRole.SYSTEM


def test_add_user_message():
    conversation = Conversation()

    conversation.user("Hello")

    assert conversation.count() == 1
    assert conversation.messages()[0].role == ChatRole.USER


def test_add_assistant_message():
    conversation = Conversation()

    conversation.assistant("Hi!")

    assert conversation.count() == 1
    assert conversation.messages()[0].role == ChatRole.ASSISTANT


def test_add_tool_message():
    conversation = Conversation()

    conversation.tool("Search completed.")

    assert conversation.count() == 1
    assert conversation.messages()[0].role == ChatRole.TOOL


def test_message_order():
    conversation = Conversation()

    conversation.system("System")
    conversation.user("User")
    conversation.assistant("Assistant")

    messages = conversation.messages()

    assert messages[0].role == ChatRole.SYSTEM
    assert messages[1].role == ChatRole.USER
    assert messages[2].role == ChatRole.ASSISTANT


def test_multiple_messages():
    conversation = Conversation()

    for i in range(5):
        conversation.user(f"Message {i}")

    assert conversation.count() == 5


def test_clear():
    conversation = Conversation()

    conversation.user("Hello")
    conversation.assistant("Hi")

    conversation.clear()

    assert conversation.count() == 0
    assert conversation.messages() == []


def test_messages_return_type():
    conversation = Conversation()

    conversation.user("Hello")

    assert isinstance(
        conversation.messages(),
        list,
    )


def test_message_content():
    conversation = Conversation()

    conversation.user("Python")

    assert conversation.messages()[0].content == "Python"
