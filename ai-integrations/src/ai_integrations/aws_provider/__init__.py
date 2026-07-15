"""
AWS AI provider integration for the AI Engineering Framework.

This package provides a framework-independent implementation of AWS AI
services, primarily Amazon Bedrock, while exposing a stable provider
interface to the framework.
"""

from ai_integrations.aws_provider.constants import (
    DEFAULT_MODEL,
    DEFAULT_REGION,
    DEFAULT_TIMEOUT,
    SUPPORTED_CHAT_MODELS,
    SUPPORTED_EMBEDDING_MODELS,
)
from ai_integrations.aws_provider.exceptions import (
    AWSAuthenticationError,
    AWSConfigurationError,
    AWSError,
    AWSProviderError,
    AWSRateLimitError,
)
from ai_integrations.aws_provider.operations import (
    AWSProvider,
    ChatCompletionRequest,
    ChatCompletionResponse,
)

__all__ = [
    "DEFAULT_MODEL",
    "DEFAULT_REGION",
    "DEFAULT_TIMEOUT",
    "SUPPORTED_CHAT_MODELS",
    "SUPPORTED_EMBEDDING_MODELS",
    "AWSError",
    "AWSConfigurationError",
    "AWSAuthenticationError",
    "AWSRateLimitError",
    "AWSProviderError",
    "ChatCompletionRequest",
    "ChatCompletionResponse",
    "AWSProvider",
]