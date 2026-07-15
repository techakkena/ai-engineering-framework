"""
Framework-independent Anthropic provider.

This module provides the Anthropic implementation of the framework's
LLM provider abstraction. It intentionally isolates the Anthropic SDK
behind a stable enterprise API.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_integrations.anthropic_provider.constants import (
    DEFAULT_API_BASE,
    DEFAULT_MAX_RETRIES,
    DEFAULT_MAX_TOKENS,
    DEFAULT_MODEL,
    DEFAULT_TIMEOUT,
    DEFAULT_TEMPERATURE,
    SUPPORTED_CHAT_MODELS,
)
from ai_integrations.anthropic_provider.exceptions import (
    AnthropicConfigurationError,
    AnthropicModelError,
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
    stop_reason: str
    usage: dict[str, int] = field(default_factory=dict)


class AnthropicProvider:
    """
    Framework-independent Anthropic provider.

    This implementation defines the provider API without directly
    depending on the Anthropic SDK.
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
            raise AnthropicConfigurationError(
                "API key cannot be empty."
            )

        if model not in SUPPORTED_CHAT_MODELS:
            raise AnthropicModelError(
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

        Concrete SDK implementations should override this method.
        """
        
        if not request.messages:
            raise AnthropicConfigurationError(
                "At least one message is required."
            )

        if request.model not in SUPPORTED_CHAT_MODELS:
            raise AnthropicModelError(
                f"Unsupported model: {request.model}"
            )

        if request.max_tokens <= 0:
            raise AnthropicConfigurationError(
                "max_tokens must be greater than zero."
            )

        if not 0.0 <= request.temperature <= 1.0:
            raise AnthropicConfigurationError(
                "temperature must be between 0.0 and 1.0."
            )

        raise NotImplementedError(
            "Concrete Anthropic SDK implementation "
            "is not installed."
        )

    def health_check(self) -> dict[str, Any]:
        """
        Return provider configuration.

        This method performs no network calls.
        """
        return {
            "provider": "anthropic",
            "model": self._model,
            "api_base": self._api_base,
            "timeout": self._timeout,
            "max_retries": self._max_retries,
            "configured": True,
        }