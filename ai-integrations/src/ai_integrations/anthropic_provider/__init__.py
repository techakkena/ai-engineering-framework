"""
Anthropic provider integration for the AI Engineering Framework.

This package provides a framework-independent implementation of the
Anthropic provider interface. It is designed to work with the official
Anthropic Python SDK while exposing a stable API to the framework.
"""

from ai_integrations.anthropic_provider.constants import (
    DEFAULT_API_BASE,
    DEFAULT_MAX_RETRIES,
    DEFAULT_MODEL,
    DEFAULT_TIMEOUT,
    SUPPORTED_CHAT_MODELS,
)
from ai_integrations.anthropic_provider.exceptions import (
    AnthropicAuthenticationError,
    AnthropicConfigurationError,
    AnthropicError,
    AnthropicProviderError,
    AnthropicRateLimitError,
)
from ai_integrations.anthropic_provider.operations import (
    AnthropicProvider,
    ChatCompletionRequest,
    ChatCompletionResponse,
)

__all__ = [
    "DEFAULT_API_BASE",
    "DEFAULT_MAX_RETRIES",
    "DEFAULT_MODEL",
    "DEFAULT_TIMEOUT",
    "SUPPORTED_CHAT_MODELS",
    "AnthropicError",
    "AnthropicConfigurationError",
    "AnthropicAuthenticationError",
    "AnthropicRateLimitError",
    "AnthropicProviderError",
    "ChatCompletionRequest",
    "ChatCompletionResponse",
    "AnthropicProvider",
]