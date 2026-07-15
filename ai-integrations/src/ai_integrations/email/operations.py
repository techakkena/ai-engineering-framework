"""
Framework-independent email operations.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_integrations.email.constants import (
    DEFAULT_MAX_RETRIES,
    DEFAULT_PORT,
    DEFAULT_SMTP_HOST,
    DEFAULT_TIMEOUT,
)
from ai_integrations.email.exceptions import (
    EmailConfigurationError,
)


@dataclass(slots=True, frozen=True)
class EmailAttachment:
    """Represents an email attachment."""

    filename: str
    content_type: str
    data: bytes


@dataclass(slots=True, frozen=True)
class EmailMessage:
    """Represents an email message."""

    sender: str
    recipients: tuple[str, ...]
    subject: str
    body: str
    attachments: tuple[EmailAttachment, ...] = field(
        default_factory=tuple
    )


class EmailClient:
    """
    Framework-independent email client.
    """

    def __init__(
        self,
        *,
        username: str,
        password: str,
        host: str = DEFAULT_SMTP_HOST,
        port: int = DEFAULT_PORT,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
    ) -> None:
        if not username.strip():
            raise EmailConfigurationError(
                "Username cannot be empty."
            )

        if not password.strip():
            raise EmailConfigurationError(
                "Password cannot be empty."
            )

        self._host = host
        self._port = port
        self._timeout = timeout
        self._max_retries = max_retries

    def send(
        self,
        message: EmailMessage,
    ) -> bool:
        """
        Send an email.

        Placeholder implementation.
        """
        if not message.recipients:
            raise EmailConfigurationError(
                "At least one recipient is required."
            )

        if not message.subject.strip():
            raise EmailConfigurationError(
                "Subject cannot be empty."
            )

        return True

    def health_check(self) -> dict[str, Any]:
        """Return client configuration."""
        return {
            "provider": "email",
            "host": self._host,
            "port": self._port,
            "timeout": self._timeout,
            "max_retries": self._max_retries,
            "configured": True,
        }