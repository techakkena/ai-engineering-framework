"""
ai_models.chat

Framework-independent chat model utilities.

This module provides reusable constants, exceptions, and helper
operations for chat models.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_models.chat.constants import (
    DEFAULT_CHAT_MODEL,
    DEFAULT_MAX_OUTPUT_TOKENS,
    DEFAULT_TEMPERATURE,
    SUPPORTED_CHAT_PROVIDERS,
)
from ai_models.chat.exceptions import (
    ChatConfigurationError,
    ChatError,
    ChatValidationError,
    InvalidChatProviderError,
)
from ai_models.chat.operations import (
    build_chat_id,
    is_supported_chat_provider,
    normalize_chat_provider,
    validate_chat_id,
    validate_chat_provider,
)

__all__ = [
    # Constants
    "DEFAULT_CHAT_MODEL",
    "DEFAULT_MAX_OUTPUT_TOKENS",
    "DEFAULT_TEMPERATURE",
    "SUPPORTED_CHAT_PROVIDERS",
    # Exceptions
    "ChatError",
    "InvalidChatProviderError",
    "ChatConfigurationError",
    "ChatValidationError",
    # Operations
    "build_chat_id",
    "is_supported_chat_provider",
    "normalize_chat_provider",
    "validate_chat_id",
    "validate_chat_provider",
]