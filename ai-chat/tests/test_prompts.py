"""
AI Engineering Framework
AI Chat Prompt Tests

Author : TECHAKKENA
"""

from ai_chat.prompts import ChatPrompts
from ai_chat.types import ChatRole


def test_system_prompt():
    prompt = ChatPrompts.system()

    assert prompt.role == ChatRole.SYSTEM
    assert len(prompt.content) > 0


def test_assistant_prompt():
    prompt = ChatPrompts.assistant()

    assert prompt.role == ChatRole.ASSISTANT
    assert "help" in prompt.content.lower()


def test_summarize_prompt():
    prompt = ChatPrompts.summarize()

    assert prompt.role == ChatRole.SYSTEM
    assert "summarize" in prompt.content.lower()


def test_explain_prompt():
    prompt = ChatPrompts.explain()

    assert prompt.role == ChatRole.SYSTEM
    assert "explain" in prompt.content.lower()


def test_translate_prompt():
    prompt = ChatPrompts.translate("French")

    assert prompt.role == ChatRole.SYSTEM
    assert "French" in prompt.content


def test_code_prompt():
    prompt = ChatPrompts.code("Python")

    assert prompt.role == ChatRole.SYSTEM
    assert "Python" in prompt.content


def test_custom_prompt():
    prompt = ChatPrompts.custom("You are a cricket expert.")

    assert prompt.role == ChatRole.SYSTEM
    assert prompt.content == "You are a cricket expert."
