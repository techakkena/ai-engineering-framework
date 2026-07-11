"""
AI Engineering Framework
AI Chat Schema Tests

Author : TECHAKKENA
"""

from ai_chat.schemas import (
    ChatRequest,
    ChatResponseSchema,
    HealthResponse,
)
from ai_chat.types import ChatOptions


def test_chat_request_creation():
    request = ChatRequest(
        message="Hello",
    )

    assert request.message == "Hello"


def test_chat_request_default_options():
    request = ChatRequest(
        message="Hello",
    )

    assert isinstance(
        request.options,
        ChatOptions,
    )


def test_chat_request_custom_options():
    options = ChatOptions(
        model="gpt-5-mini",
        temperature=0.5,
    )

    request = ChatRequest(
        message="Hello",
        options=options,
    )

    assert request.options.model == "gpt-5-mini"
    assert request.options.temperature == 0.5


def test_chat_response_schema():
    response = ChatResponseSchema(
        response="Hi!",
        model="gpt-5.5",
    )

    assert response.response == "Hi!"
    assert response.model == "gpt-5.5"


def test_chat_response_session():
    response = ChatResponseSchema(
        response="Hi!",
        model="gpt-5.5",
        session_id="session-001",
    )

    assert response.session_id == "session-001"


def test_chat_response_finish_reason():
    response = ChatResponseSchema(
        response="Done",
        model="gpt-5.5",
    )

    assert response.finish_reason == "stop"


def test_health_response_defaults():
    health = HealthResponse()

    assert health.status == "healthy"
    assert health.service == "ai-chat"
    assert health.version == "0.1.0"


def test_health_response_custom():
    health = HealthResponse(
        status="running",
        version="0.2.0",
    )

    assert health.status == "running"
    assert health.version == "0.2.0"
