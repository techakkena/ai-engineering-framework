"""
Shared provider abstractions for the AI Engineering Framework.

This module defines the common data models and abstract base classes
used by all AI provider implementations.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from ai_integrations.base.constants import (
    DEFAULT_MAX_RETRIES,
    DEFAULT_MAX_TOKENS,
    DEFAULT_STREAM,
    DEFAULT_TEMPERATURE,
    DEFAULT_TIMEOUT,
    SUPPORTED_MESSAGE_ROLES,
)
from ai_integrations.base.exceptions import (
    ProviderConfigurationError,
)


@dataclass(slots=True, frozen=True)
class ProviderConfig:
    """Configuration for an AI provider."""

    api_key: str
    model: str
    api_base: str
    timeout: float = DEFAULT_TIMEOUT
    max_retries: int = DEFAULT_MAX_RETRIES


@dataclass(slots=True, frozen=True)
class ChatMessage:
    """Represents a chat message."""

    role: str
    content: str

    def __post_init__(self) -> None:
        """Validate the message."""
        if self.role not in SUPPORTED_MESSAGE_ROLES:
            raise ProviderConfigurationError(
                f"Unsupported role: {self.role}"
            )

        if not self.content.strip():
            raise ProviderConfigurationError(
                "Message content cannot be empty."
            )


@dataclass(slots=True, frozen=True)
class ChatCompletionRequest:
    """Represents a chat completion request."""

    messages: tuple[ChatMessage, ...]
    model: str
    max_tokens: int = DEFAULT_MAX_TOKENS
    temperature: float = DEFAULT_TEMPERATURE
    stream: bool = DEFAULT_STREAM

    def __post_init__(self) -> None:
        """Validate the request."""
        if not self.messages:
            raise ProviderConfigurationError(
                "At least one message is required."
            )

        if self.max_tokens <= 0:
            raise ProviderConfigurationError(
                "max_tokens must be greater than zero."
            )

        if not 0.0 <= self.temperature <= 2.0:
            raise ProviderConfigurationError(
                "temperature must be between 0.0 and 2.0."
            )


@dataclass(slots=True, frozen=True)
class ChatCompletionResponse:
    """Represents a chat completion response."""

    model: str
    content: str
    finish_reason: str
    usage: dict[str, int] = field(default_factory=dict)


@dataclass(slots=True, frozen=True)
class EmbeddingRequest:
    """Represents an embedding request."""

    input: tuple[str, ...]
    model: str

    def __post_init__(self) -> None:
        """Validate the request."""
        if not self.input:
            raise ProviderConfigurationError(
                "At least one input is required."
            )


@dataclass(slots=True, frozen=True)
class EmbeddingResponse:
    """Represents an embedding response."""

    model: str
    embeddings: tuple[tuple[float, ...], ...]
    usage: dict[str, int] = field(default_factory=dict)


class BaseProvider(ABC):
    """
    Abstract base class for all AI providers.
    """

    def __init__(
        self,
        config: ProviderConfig,
    ) -> None:
        self._config = config

    @property
    def config(self) -> ProviderConfig:
        """Return the provider configuration."""
        return self._config

    @property
    def model(self) -> str:
        """Return the configured model."""
        return self._config.model

    @abstractmethod
    def chat(
        self,
        request: ChatCompletionRequest,
    ) -> ChatCompletionResponse:
        """
        Execute a chat completion.
        """

    @abstractmethod
    def embeddings(
        self,
        request: EmbeddingRequest,
    ) -> EmbeddingResponse:
        """
        Generate embeddings.
        """

    @abstractmethod
    def health_check(self) -> dict[str, Any]:
        """
        Return provider health information.
        """

    def is_configured(self) -> bool:
        """Return whether the provider is configured."""
        return bool(self._config.api_key.strip())

    def provider_info(self) -> dict[str, Any]:
        """Return provider metadata."""
        return {
            "provider": self.__class__.__name__,
            "model": self._config.model,
            "api_base": self._config.api_base,
            "timeout": self._config.timeout,
            "max_retries": self._config.max_retries,
        }