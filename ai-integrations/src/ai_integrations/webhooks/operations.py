"""
Framework-independent webhook operations.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_integrations.webhooks.constants import (
    DEFAULT_CONTENT_TYPE,
    DEFAULT_MAX_RETRIES,
    DEFAULT_TIMEOUT,
)
from ai_integrations.webhooks.exceptions import (
    WebhookConfigurationError,
)


@dataclass(slots=True, frozen=True)
class WebhookEvent:
    """Represents a webhook event."""

    name: str
    payload: dict[str, Any]


@dataclass(slots=True, frozen=True)
class WebhookRequest:
    """Represents an outgoing webhook request."""

    url: str
    method: str
    payload: dict[str, Any]
    headers: dict[str, str] = field(default_factory=dict)
    content_type: str = DEFAULT_CONTENT_TYPE


class WebhookClient:
    """
    Framework-independent webhook client.
    """

    def __init__(
        self,
        *,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
    ) -> None:
        self._timeout = timeout
        self._max_retries = max_retries

    def send(
        self,
        request: WebhookRequest,
    ) -> bool:
        """
        Send a webhook request.

        Placeholder implementation.
        """
        if not request.url.strip():
            raise WebhookConfigurationError(
                "Webhook URL cannot be empty."
            )

        return True

    def verify_signature(
        self,
        payload: bytes,
        signature: str,
        secret: str,
    ) -> bool:
        """
        Verify a webhook signature.

        Placeholder implementation.
        """
        if not secret.strip():
            raise WebhookConfigurationError(
                "Secret cannot be empty."
            )

        return True

    def health_check(self) -> dict[str, Any]:
        """Return client configuration."""
        return {
            "provider": "webhooks",
            "timeout": self._timeout,
            "max_retries": self._max_retries,
            "configured": True,
        }