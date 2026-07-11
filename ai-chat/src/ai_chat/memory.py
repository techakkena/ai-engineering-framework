"""
AI Engineering Framework
Conversation Memory

Author : TECHAKKENA
"""

from .conversation import Conversation


class ConversationMemory:
    """
    Stores conversations by session.
    """

    def __init__(self):

        self._sessions: dict[
            str,
            Conversation,
        ] = {}

    def create(
        self,
        session_id: str,
    ) -> Conversation:
        """
        Create a new conversation.
        """

        conversation = Conversation()

        self._sessions[session_id] = conversation

        return conversation

    def get(
        self,
        session_id: str,
    ) -> Conversation:
        """
        Get a conversation.
        Creates one automatically if missing.
        """

        if session_id not in self._sessions:
            self.create(session_id)

        return self._sessions[session_id]

    def exists(
        self,
        session_id: str,
    ) -> bool:
        """
        Check whether a session exists.
        """

        return session_id in self._sessions

    def delete(
        self,
        session_id: str,
    ) -> bool:
        """
        Delete a session.
        """

        if session_id in self._sessions:
            del self._sessions[session_id]

            return True

        return False

    def clear(
        self,
        session_id: str,
    ) -> bool:
        """
        Clear a conversation.
        """

        if session_id not in self._sessions:
            return False

        self._sessions[session_id].clear()

        return True

    def sessions(
        self,
    ) -> list[str]:
        """
        Return all session ids.
        """

        return list(
            self._sessions.keys(),
        )

    def count(
        self,
    ) -> int:
        """
        Return session count.
        """

        return len(
            self._sessions,
        )
