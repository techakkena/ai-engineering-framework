from __future__ import annotations

from dataclasses import dataclass

from .constants import DEFAULT_EMAIL_SUBJECT


@dataclass(slots=True)
class EmailMessage:
    """Represents an email message."""

    to: str
    body: str
    subject: str = DEFAULT_EMAIL_SUBJECT


class EmailClient:
    """Simple in-memory email client."""

    def __init__(self) -> None:
        self._messages: list[EmailMessage] = []

    def send(
        self,
        message: EmailMessage,
    ) -> None:
        """Store a sent email."""
        self._messages.append(message)

    def list_messages(
        self,
    ) -> tuple[EmailMessage, ...]:
        """Return sent messages."""
        return tuple(self._messages)

    @property
    def message_count(self) -> int:
        """Return number of sent messages."""
        return len(self._messages)
