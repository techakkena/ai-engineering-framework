"""
Framework-independent Google AI provider.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_integrations.google_provider.constants import (
    DEFAULT_API_BASE,
    DEFAULT_MAX_RETRIES,
    DEFAULT_MAX_TOKENS,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
    DEFAULT_TIMEOUT,
    SUPPORTED_CHAT_MODELS,
)
from ai_integrations.google_provider.exceptions import (
    GoogleConfigurationError,
    GoogleModelError,
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
    max_tokens: int = DEFAULT_MAX_TOKENS
    temperature: float = DEFAULT_TEMPERATURE


@dataclass(slots=True, frozen=True)
class ChatCompletionResponse:
    """Represents a chat completion response."""

    model: str
    content: str
    finish_reason: str
    usage: dict[str, int] = field(default_factory=dict)


class GoogleProvider:
    """
    Framework-independent Google AI provider.
    """

    def __init__(
        self,
        *,
        api_key: str,
        model: str = DEFAULT_MODEL,
        api_base: str = DEFAULT_API_BASE,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
    ) -> None:
        if not api_key.strip():
            raise GoogleConfigurationError(
                "API key cannot be empty."
            )

        if model not in SUPPORTED_CHAT_MODELS:
            raise GoogleModelError(
                f"Unsupported model: {model}"
            )

        self._api_key = api_key
        self._model = model
        self._api_base = api_base
        self._timeout = timeout
        self._max_retries = max_retries

    @property
    def model(self) -> str:
        """Return the configured model."""
        return self._model

    @property
    def api_base(self) -> str:
        """Return the configured API base."""
        return self._api_base

    @property
    def timeout(self) -> float:
        """Return the configured timeout."""
        return self._timeout

    @property
    def max_retries(self) -> int:
        """Return the configured retry count."""
        return self._max_retries

    def chat(
        self,
        request: ChatCompletionRequest,
    ) -> ChatCompletionResponse:
        """
        Execute a chat completion.

        Concrete Google AI SDK implementations should override this
        method.
        """
        if not request.messages:
            raise GoogleConfigurationError(
                "At least one message is required."
            )

        if request.model not in SUPPORTED_CHAT_MODELS:
            raise GoogleModelError(
                f"Unsupported model: {request.model}"
            )

        raise NotImplementedError(
            "Concrete Google AI SDK implementation "
            "is not installed."
        )

    def health_check(self) -> dict[str, Any]:
        """
        Return provider configuration without contacting the API.
        """
        return {
            "provider": "google",
            "model": self._model,
            "api_base": self._api_base,
            "timeout": self._timeout,
            "max_retries": self._max_retries,
            "configured": True,
        }