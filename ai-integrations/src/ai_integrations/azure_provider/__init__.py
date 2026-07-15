"""
Azure OpenAI provider integration for the AI Engineering Framework.

This package provides a framework-independent implementation of Azure
OpenAI while exposing a stable provider interface to the framework.
"""

from ai_integrations.azure_provider.constants import (
    DEFAULT_API_VERSION,
    DEFAULT_ENDPOINT,
    DEFAULT_MODEL,
    DEFAULT_TIMEOUT,
    SUPPORTED_CHAT_MODELS,
    SUPPORTED_EMBEDDING_MODELS,
)
from ai_integrations.azure_provider.exceptions import (
    AzureAuthenticationError,
    AzureConfigurationError,
    AzureError,
    AzureProviderError,
    AzureRateLimitError,
)
from ai_integrations.azure_provider.operations import (
    AzureProvider,
    ChatCompletionRequest,
    ChatCompletionResponse,
)

__all__ = [
    "DEFAULT_API_VERSION",
    "DEFAULT_ENDPOINT",
    "DEFAULT_MODEL",
    "DEFAULT_TIMEOUT",
    "SUPPORTED_CHAT_MODELS",
    "SUPPORTED_EMBEDDING_MODELS",
    "AzureError",
    "AzureConfigurationError",
    "AzureAuthenticationError",
    "AzureRateLimitError",
    "AzureProviderError",
    "ChatCompletionRequest",
    "ChatCompletionResponse",
    "AzureProvider",
]