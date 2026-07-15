"""
Framework-independent Azure OpenAI provider.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_integrations.azure_provider.constants import (
    DEFAULT_API_VERSION,
    DEFAULT_ENDPOINT,
    DEFAULT_MAX_RETRIES,
    DEFAULT_MODEL,
    DEFAULT_TIMEOUT,
    SUPPORTED_CHAT_MODELS,
)
from ai_integrations.azure_provider.exceptions import (
    AzureConfigurationError,
    AzureModelError,
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


class AzureProvider:
    """
    Framework-independent Azure OpenAI provider.
    """

    def __init__(
        self,
        *,
        api_key: str,
        endpoint: str = DEFAULT_ENDPOINT,
        api_version: str = DEFAULT_API_VERSION,
        model: str = DEFAULT_MODEL,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
    ) -> None:
        if not api_key.strip():
            raise AzureConfigurationError(
                "API key cannot be empty."
            )

        if model not in SUPPORTED_CHAT_MODELS:
            raise AzureModelError(
                f"Unsupported model: {model}"
            )

        self._api_key = api_key
        self._endpoint = endpoint
        self._api_version = api_version
        self._model = model
        self._timeout = timeout
        self._max_retries = max_retries

    @property
    def model(self) -> str:
        """Return the configured model."""
        return self._model

    @property
    def endpoint(self) -> str:
        """Return the configured endpoint."""
        return self._endpoint

    @property
    def api_version(self) -> str:
        """Return the configured API version."""
        return self._api_version

    def chat(
        self,
        request: ChatCompletionRequest,
    ) -> ChatCompletionResponse:
        """Execute a chat completion."""
        if not request.messages:
            raise AzureConfigurationError(
                "At least one message is required."
            )

        if request.model not in SUPPORTED_CHAT_MODELS:
            raise AzureModelError(
                f"Unsupported model: {request.model}"
            )

        raise NotImplementedError(
            "Concrete Azure OpenAI implementation is not installed."
        )

    def health_check(self) -> dict[str, Any]:
        """Return provider configuration."""
        return {
            "provider": "azure",
            "endpoint": self._endpoint,
            "api_version": self._api_version,
            "model": self._model,
            "timeout": self._timeout,
            "max_retries": self._max_retries,
            "configured": True,
        }