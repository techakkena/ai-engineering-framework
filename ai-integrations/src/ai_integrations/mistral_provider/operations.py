"""
Framework-independent Mistral AI provider.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_integrations.mistral_provider.constants import (
    DEFAULT_API_BASE,
    DEFAULT_MAX_RETRIES,
    DEFAULT_MODEL,
    DEFAULT_TIMEOUT,
    SUPPORTED_CHAT_MODELS,
)
from ai_integrations.mistral_provider.exceptions import (
    MistralConfigurationError,
    MistralModelError,
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


class MistralProvider:
    """Framework-independent Mistral provider."""

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
            raise MistralConfigurationError(
                "API key cannot be empty."
            )

        if model not in SUPPORTED_CHAT_MODELS:
            raise MistralModelError(
                f"Unsupported model: {model}"
            )

        self._model = model
        self._api_base = api_base
        self._timeout = timeout
        self._max_retries = max_retries

    @property
    def model(self) -> str:
        """Return the configured model."""
        return self._model

    def chat(
        self,
        request: ChatCompletionRequest,
    ) -> ChatCompletionResponse:
        """Execute a chat completion."""
        if not request.messages:
            raise MistralConfigurationError(
                "At least one message is required."
            )

        raise NotImplementedError(
            "Concrete Mistral SDK implementation is not installed."
        )

    def health_check(self) -> dict[str, Any]:
        """Return provider configuration."""
        return {
            "provider": "mistral",
            "model": self._model,
            "api_base": self._api_base,
            "timeout": self._timeout,
            "max_retries": self._max_retries,
            "configured": True,
        }