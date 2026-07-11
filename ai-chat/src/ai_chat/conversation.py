"""
AI Engineering Framework
Conversation Manager

Author : TECHAKKENA
"""

from .types import ChatMessage, ChatRole


class Conversation:
    """
    Manages a chat conversation.
    """

    def __init__(self):

        self._messages: list[ChatMessage] = []

    def system(
        self,
        content: str,
    ) -> None:
        """
        Add a system message.
        """

        self._messages.append(
            ChatMessage(
                role=ChatRole.SYSTEM,
                content=content,
            )
        )

    def user(
        self,
        content: str,
    ) -> None:
        """
        Add a user message.
        """

        self._messages.append(
            ChatMessage(
                role=ChatRole.USER,
                content=content,
            )
        )

    def assistant(
        self,
        content: str,
    ) -> None:
        """
        Add an assistant message.
        """

        self._messages.append(
            ChatMessage(
                role=ChatRole.ASSISTANT,
                content=content,
            )
        )

    def tool(
        self,
        content: str,
    ) -> None:
        """
        Add a tool message.
        """

        self._messages.append(
            ChatMessage(
                role=ChatRole.TOOL,
                content=content,
            )
        )

    def messages(
        self,
    ) -> list[ChatMessage]:
        """
        Return all messages.
        """

        return self._messages

    def count(
        self,
    ) -> int:
        """
        Return message count.
        """

        return len(
            self._messages,
        )

    def clear(
        self,
    ) -> None:
        """
        Clear conversation.
        """

        self._messages.clear()
