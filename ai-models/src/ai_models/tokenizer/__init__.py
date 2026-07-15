"""
ai_models.tokenizer

Framework-independent tokenizer utilities.

This module provides reusable constants, exceptions, and helper
operations for tokenizer management across AI model providers.

Supported providers include OpenAI, Anthropic, Google, Ollama,
Mistral, Groq, and other tokenizer-compatible models.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_models.tokenizer.constants import (
    DEFAULT_CONTEXT_WINDOW,
    DEFAULT_TOKENIZER,
    DEFAULT_TOKENIZER_PROVIDER,
    SUPPORTED_TOKENIZER_PROVIDERS,
)
from ai_models.tokenizer.exceptions import (
    InvalidTokenizerProviderError,
    TokenizerConfigurationError,
    TokenizerError,
    TokenizerValidationError,
)
from ai_models.tokenizer.operations import (
    build_tokenizer_id,
    is_supported_tokenizer_provider,
    normalize_tokenizer_provider,
    validate_tokenizer_id,
    validate_tokenizer_provider,
)

__all__ = [
    # Constants
    "DEFAULT_CONTEXT_WINDOW",
    "DEFAULT_TOKENIZER",
    "DEFAULT_TOKENIZER_PROVIDER",
    "SUPPORTED_TOKENIZER_PROVIDERS",
    # Exceptions
    "TokenizerError",
    "InvalidTokenizerProviderError",
    "TokenizerConfigurationError",
    "TokenizerValidationError",
    # Operations
    "build_tokenizer_id",
    "is_supported_tokenizer_provider",
    "normalize_tokenizer_provider",
    "validate_tokenizer_id",
    "validate_tokenizer_provider",
]