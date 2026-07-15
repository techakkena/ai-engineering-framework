"""
Google AI provider integration for the AI Engineering Framework.

This package provides a framework-independent implementation of the
Google AI provider interface. It is designed to support Gemini,
Vertex AI, embeddings, vision, and future Google AI services while
exposing a stable API to the framework.
"""

from ai_integrations.google_provider.constants import (
    DEFAULT_API_BASE,
    DEFAULT_MODEL,
    DEFAULT_TIMEOUT,
    SUPPORTED_CHAT_MODELS,
    SUPPORTED_EMBEDDING_MODELS,
)
from ai_integrations.google_provider.exceptions import (
    GoogleAuthenticationError,
    GoogleConfigurationError,
    GoogleError,
    GoogleProviderError,
    GoogleRateLimitError,
)
from ai_integrations.google_provider.operations import (
    ChatCompletionRequest,
    ChatCompletionResponse,
    GoogleProvider,
)

__all__ = [
    "DEFAULT_API_BASE",
    "DEFAULT_MODEL",
    "DEFAULT_TIMEOUT",
    "SUPPORTED_CHAT_MODELS",
    "SUPPORTED_EMBEDDING_MODELS",
    "GoogleError",
    "GoogleConfigurationError",
    "GoogleAuthenticationError",
    "GoogleRateLimitError",
    "GoogleProviderError",
    "ChatCompletionRequest",
    "ChatCompletionResponse",
    "GoogleProvider",
]