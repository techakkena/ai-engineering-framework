"""
OpenAI provider integration for the AI Engineering Framework.

This package provides a framework-independent implementation of the
OpenAI provider interface. It is designed to work with the official
OpenAI Python SDK while exposing a stable API to the framework.
"""

from ai_integrations.openai_provider.constants import (
    DEFAULT_API_BASE,
    DEFAULT_MODEL,
    DEFAULT_TIMEOUT,
    SUPPORTED_CHAT_MODELS,
    SUPPORTED_EMBEDDING_MODELS,
)
from ai_integrations.openai_provider.exceptions import (
    OpenAIAuthenticationError,
    OpenAIConfigurationError,
    OpenAIError,
    OpenAIProviderError,
    OpenAIRateLimitError,
)
from ai_integrations.openai_provider.operations import (
    ChatCompletionRequest,
    ChatCompletionResponse,
    OpenAIProvider,
)

__all__ = [
    "DEFAULT_API_BASE",
    "DEFAULT_MODEL",
    "DEFAULT_TIMEOUT",
    "SUPPORTED_CHAT_MODELS",
    "SUPPORTED_EMBEDDING_MODELS",
    "OpenAIError",
    "OpenAIConfigurationError",
    "OpenAIAuthenticationError",
    "OpenAIRateLimitError",
    "OpenAIProviderError",
    "ChatCompletionRequest",
    "ChatCompletionResponse",
    "OpenAIProvider",
]