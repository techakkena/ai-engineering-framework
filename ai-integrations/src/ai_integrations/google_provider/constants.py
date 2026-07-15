"""
Constants for the Google AI provider.
"""

from __future__ import annotations

DEFAULT_API_BASE: str = "https://generativelanguage.googleapis.com"

DEFAULT_MODEL: str = "gemini-2.5-pro"

DEFAULT_EMBEDDING_MODEL: str = "text-embedding-004"

DEFAULT_TIMEOUT: float = 60.0

DEFAULT_MAX_RETRIES: int = 3

DEFAULT_MAX_TOKENS: int = 8192

DEFAULT_TEMPERATURE: float = 0.7

SUPPORTED_CHAT_MODELS: frozenset[str] = frozenset(
    {
        "gemini-2.5-pro",
        "gemini-2.5-flash",
        "gemini-2.5-flash-lite",
        "gemini-2.0-flash",
    }
)

SUPPORTED_EMBEDDING_MODELS: frozenset[str] = frozenset(
    {
        "text-embedding-004",
        "embedding-001",
    }
)

SUPPORTED_VISION_MODELS: frozenset[str] = frozenset(
    {
        "gemini-2.5-pro",
        "gemini-2.5-flash",
    }
)