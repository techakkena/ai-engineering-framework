from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True, frozen=True)
class ConversationMessage:
    """Represents one message in a conversation."""

    role: str
    content: str


@dataclass(slots=True)
class Conversation:
    """Represents a conversation."""

    messages: list[ConversationMessage] = field(default_factory=list)

    def add_message(
        self,
        message: ConversationMessage,
    ) -> None:
        """Add a message."""
        self.messages.append(message)

    def clear(self) -> None:
        """Remove all messages."""
        self.messages.clear()

    @property
    def size(self) -> int:
        """Return number of messages."""
        return len(self.messages)
