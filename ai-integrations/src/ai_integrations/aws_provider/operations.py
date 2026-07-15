"""
Framework-independent AWS provider.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_integrations.aws_provider.constants import (
    DEFAULT_MAX_RETRIES,
    DEFAULT_MODEL,
    DEFAULT_REGION,
    DEFAULT_TIMEOUT,
    SUPPORTED_CHAT_MODELS,
)
from ai_integrations.aws_provider.exceptions import (
    AWSConfigurationError,
    AWSModelError,
)


@dataclass(slots=True, frozen=True)
class ChatMessage:
    """Represents a chat message."""

    role: str
    content: str


@dataclass(slots=True, frozen=True)
class ChatCompletionRequest:
    """Represents a chat completion request."""

    messages: tuple[ChatMessage, ...]
    model: str = DEFAULT_MODEL


@dataclass(slots=True, frozen=True)
class ChatCompletionResponse:
    """Represents a chat completion response."""

    model: str
    content: str
    finish_reason: str
    usage: dict[str, int] = field(default_factory=dict)


class AWSProvider:
    """
    Framework-independent AWS AI provider.

    Intended to support Amazon Bedrock and other AWS AI services.
    """

    def __init__(
        self,
        *,
        access_key_id: str,
        secret_access_key: str,
        region: str = DEFAULT_REGION,
        model: str = DEFAULT_MODEL,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
    ) -> None:
        if not access_key_id.strip():
            raise AWSConfigurationError(
                "Access key ID cannot be empty."
            )

        if not secret_access_key.strip():
            raise AWSConfigurationError(
                "Secret access key cannot be empty."
            )

        if model not in SUPPORTED_CHAT_MODELS:
            raise AWSModelError(
                f"Unsupported model: {model}"
            )

        self._region = region
        self._model = model
        self._timeout = timeout
        self._max_retries = max_retries

    @property
    def model(self) -> str:
        """Return the configured model."""
        return self._model

    @property
    def region(self) -> str:
        """Return the configured AWS region."""
        return self._region

    def chat(
        self,
        request: ChatCompletionRequest,
    ) -> ChatCompletionResponse:
        """Execute a chat completion."""
        if not request.messages:
            raise AWSConfigurationError(
                "At least one message is required."
            )

        if request.model not in SUPPORTED_CHAT_MODELS:
            raise AWSModelError(
                f"Unsupported model: {request.model}"
            )

        raise NotImplementedError(
            "Concrete AWS Bedrock implementation is not installed."
        )

    def health_check(self) -> dict[str, Any]:
        """Return provider configuration."""
        return {
            "provider": "aws",
            "region": self._region,
            "model": self._model,
            "timeout": self._timeout,
            "max_retries": self._max_retries,
            "configured": True,
        }