"""
Constants for the OpenAI provider.

This module defines framework-independent constants used by the
OpenAI provider implementation.
"""

from __future__ import annotations

DEFAULT_API_BASE: str = "https://api.openai.com/v1"

DEFAULT_MODEL: str = "gpt-5"

DEFAULT_EMBEDDING_MODEL: str = "text-embedding-3-small"

DEFAULT_TIMEOUT: float = 60.0

DEFAULT_MAX_RETRIES: int = 3

DEFAULT_MAX_TOKENS: int = 4096

DEFAULT_TEMPERATURE: float = 0.7

SUPPORTED_CHAT_MODELS: frozenset[str] = frozenset(
    {
        "gpt-5",
        "gpt-5-mini",
        "gpt-5-nano",
        "gpt-4.1",
        "gpt-4.1-mini",
        "gpt-4.1-nano",
    }
)

SUPPORTED_EMBEDDING_MODELS: frozenset[str] = frozenset(
    {
        "text-embedding-3-small",
        "text-embedding-3-large",
    }
)

SUPPORTED_IMAGE_MODELS: frozenset[str] = frozenset(
    {
        "gpt-image-1",
    }
)

SUPPORTED_TRANSCRIPTION_MODELS: frozenset[str] = frozenset(
    {
        "gpt-4o-transcribe",
        "gpt-4o-mini-transcribe",
    }
)