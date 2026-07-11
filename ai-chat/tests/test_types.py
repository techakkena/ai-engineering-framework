"""
AI Engineering Framework
AI Chat Tests

Tests for chat types.

Author : TECHAKKENA
"""

from ai_chat.types import (
    ChatMessage,
    ChatOptions,
    ChatResponse,
    ChatRole,
)


def test_chat_role_values():
    assert ChatRole.SYSTEM.value == "system"
    assert ChatRole.USER.value == "user"
    assert ChatRole.ASSISTANT.value == "assistant"
    assert ChatRole.TOOL.value == "tool"


def test_chat_message_creation():
    message = ChatMessage(
        role=ChatRole.USER,
        content="Hello",
    )

    assert message.role == ChatRole.USER
    assert message.content == "Hello"


def test_chat_message_name():
    message = ChatMessage(
        role=ChatRole.SYSTEM,
        content="You are an AI assistant.",
        name="system",
    )

    assert message.name == "system"


def test_chat_message_metadata():
    message = ChatMessage(
        role=ChatRole.USER,
        content="Hello",
        metadata={
            "language": "en",
            "source": "web",
        },
    )

    assert message.metadata["language"] == "en"
    assert message.metadata["source"] == "web"


def test_chat_message_default_metadata():
    message = ChatMessage(
        role=ChatRole.USER,
        content="Hello",
    )

    assert message.metadata == {}


def test_chat_response_creation():
    response = ChatResponse(
        content="Hi!",
        model="gpt-5.5",
    )

    assert response.content == "Hi!"
    assert response.model == "gpt-5.5"


def test_chat_response_finish_reason():
    response = ChatResponse(
        content="Done",
        model="gpt-5.5",
    )

    assert response.finish_reason == "stop"


def test_chat_response_usage():
    response = ChatResponse(
        content="Hello",
        model="gpt-5.5",
        usage={
            "prompt_tokens": 10,
            "completion_tokens": 20,
        },
    )

    assert response.usage["prompt_tokens"] == 10
    assert response.usage["completion_tokens"] == 20


def test_chat_response_default_usage():
    response = ChatResponse(
        content="Hello",
        model="gpt-5.5",
    )

    assert response.usage == {}


def test_chat_options_defaults():
    options = ChatOptions()

    assert options.model == "gpt-5.5"
    assert options.temperature == 0.2
    assert options.max_tokens == 4096
    assert options.stream is False
    assert options.session_id is None


def test_chat_options_custom_values():
    options = ChatOptions(
        model="gpt-5-mini",
        temperature=0.7,
        max_tokens=2048,
        stream=True,
        session_id="session-001",
    )

    assert options.model == "gpt-5-mini"
    assert options.temperature == 0.7
    assert options.max_tokens == 2048
    assert options.stream is True
    assert options.session_id == "session-001"


def test_chat_options_model_update():
    options = ChatOptions()

    options.model = "gpt-5-mini"

    assert options.model == "gpt-5-mini"
