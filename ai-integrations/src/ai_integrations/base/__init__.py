"""
Shared abstractions for AI provider integrations.

This package defines the common models, interfaces, constants, and
exceptions used by all provider implementations within the
AI Engineering Framework.
"""

from ai_integrations.base.constants import (
    DEFAULT_MAX_RETRIES,
    DEFAULT_MAX_TOKENS,
    DEFAULT_TEMPERATURE,
    DEFAULT_TIMEOUT,
)
from ai_integrations.base.exceptions import (
    ProviderAuthenticationError,
    ProviderConfigurationError,
    ProviderError,
    ProviderRateLimitError,
)
from ai_integrations.base.operations import (
    BaseProvider,
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatMessage,
    EmbeddingRequest,
    EmbeddingResponse,
    ProviderConfig,
)

__all__ = [
    "DEFAULT_MAX_RETRIES",
    "DEFAULT_MAX_TOKENS",
    "DEFAULT_TEMPERATURE",
    "DEFAULT_TIMEOUT",
    "ProviderError",
    "ProviderConfigurationError",
    "ProviderAuthenticationError",
    "ProviderRateLimitError",
    "ProviderConfig",
    "ChatMessage",
    "ChatCompletionRequest",
    "ChatCompletionResponse",
    "EmbeddingRequest",
    "EmbeddingResponse",
    "BaseProvider",
]