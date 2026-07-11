"""
AI Engineering Framework
AI Chat Prompts

Author : TECHAKKENA
"""

from .constants.chat_constants import ChatConstants
from .types import ChatMessage, ChatRole


class ChatPrompts:
    """
    Built-in reusable chat prompts.
    """

    @staticmethod
    def system() -> ChatMessage:
        """
        Default system prompt.
        """
        return ChatMessage(
            role=ChatRole.SYSTEM,
            content=ChatConstants.DEFAULT_SYSTEM_PROMPT,
        )

    @staticmethod
    def assistant() -> ChatMessage:
        """
        Assistant introduction.
        """
        return ChatMessage(
            role=ChatRole.ASSISTANT,
            content="How can I help you today?",
        )

    @staticmethod
    def summarize() -> ChatMessage:
        """
        Summarization prompt.
        """
        return ChatMessage(
            role=ChatRole.SYSTEM,
            content="Summarize the following content clearly and concisely.",
        )

    @staticmethod
    def explain() -> ChatMessage:
        """
        Explanation prompt.
        """
        return ChatMessage(
            role=ChatRole.SYSTEM,
            content="Explain the following topic in a simple and detailed way.",
        )

    @staticmethod
    def translate(
        language: str,
    ) -> ChatMessage:
        """
        Translation prompt.
        """
        return ChatMessage(
            role=ChatRole.SYSTEM,
            content=f"Translate the following text into {language}.",
        )

    @staticmethod
    def code(
        language: str,
    ) -> ChatMessage:
        """
        Code generation prompt.
        """
        return ChatMessage(
            role=ChatRole.SYSTEM,
            content=f"You are an expert {language} programmer.",
        )

    @staticmethod
    def custom(
        prompt: str,
    ) -> ChatMessage:
        """
        Custom system prompt.
        """
        return ChatMessage(
            role=ChatRole.SYSTEM,
            content=prompt,
        )
