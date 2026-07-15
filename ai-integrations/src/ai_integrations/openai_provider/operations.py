"""
Framework-independent OpenAI provider.

This module provides the OpenAI implementation of the framework's
provider abstraction. It intentionally hides the OpenAI SDK behind a
stable interface so applications depend only on the framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_integrations.openai_provider.constants import (
    DEFAULT_API_BASE,
    DEFAULT_MAX_RETRIES,
    DEFAULT_MAX_TOKENS,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
    DEFAULT_TIMEOUT,
    SUPPORTED_CHAT_MODELS,
)
from ai_integrations.openai_provider.exceptions import (
    OpenAIConfigurationError,
    OpenAIModelError,
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


class OpenAIProvider:
    """
    Framework-independent OpenAI provider.

    This class validates requests and defines the public API. Concrete
    OpenAI SDK calls can be implemented later without changing the
    framework interface.
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
            raise OpenAIConfigurationError(
                "API key cannot be empty."
            )

        if model not in SUPPORTED_CHAT_MODELS:
            raise OpenAIModelError(
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
        """Return the configured API base URL."""
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

        This framework implementation intentionally does not call the
        OpenAI SDK directly. A future adapter will translate this request
        into an SDK call.
        """
        if request.model not in SUPPORTED_CHAT_MODELS:
            raise OpenAIModelError(
                f"Unsupported model: {request.model}"
            )

        if not request.messages:
            raise OpenAIConfigurationError(
                "At least one message is required."
            )

        raise NotImplementedError(
            "Concrete OpenAI SDK implementation is not installed."
        )

    def embeddings(
        self,
        texts: list[str],
    ) -> list[list[float]]:
        """
        Generate embeddings.

        Placeholder for a future SDK-backed implementation.
        """
        if not texts:
            raise OpenAIConfigurationError(
                "At least one input text is required."
            )

        raise NotImplementedError(
            "Embedding generation is not implemented."
        )

    def health_check(self) -> dict[str, Any]:
        """
        Return provider configuration information.

        This method does not contact the OpenAI API.
        """
        return {
            "provider": "openai",
            "model": self._model,
            "api_base": self._api_base,
            "timeout": self._timeout,
            "max_retries": self._max_retries,
            "configured": True,
        }