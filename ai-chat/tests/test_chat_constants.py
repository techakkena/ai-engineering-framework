"""
AI Engineering Framework
AI Chat Constants Tests

Author : TECHAKKENA
"""

from ai_chat.constants.chat_constants import (
    ChatConstants,
)


def test_default_model():
    assert ChatConstants.DEFAULT_MODEL == "gpt-5.5"


def test_temperature():
    assert ChatConstants.DEFAULT_TEMPERATURE == 0.2


def test_max_tokens():
    assert ChatConstants.DEFAULT_MAX_TOKENS == 4096


def test_stream():
    assert ChatConstants.DEFAULT_STREAM is False


def test_session():
    assert ChatConstants.DEFAULT_SESSION_ID is None


def test_roles():
    assert ChatConstants.SYSTEM_ROLE == "system"
    assert ChatConstants.USER_ROLE == "user"
    assert ChatConstants.ASSISTANT_ROLE == "assistant"
    assert ChatConstants.TOOL_ROLE == "tool"


def test_history_limit():
    assert ChatConstants.MAX_HISTORY == 100


def test_system_prompt():
    assert ChatConstants.DEFAULT_SYSTEM_PROMPT == "You are a helpful AI assistant."


def test_finish_reason():
    assert ChatConstants.DEFAULT_FINISH_REASON == "stop"


def test_service_info():
    assert ChatConstants.SERVICE_NAME == "ai-chat"

    assert ChatConstants.SERVICE_VERSION == "0.1.0"
