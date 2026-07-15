"""
Constants for the Mistral AI provider.
"""

from __future__ import annotations

DEFAULT_API_BASE: str = "https://api.mistral.ai"

DEFAULT_MODEL: str = "mistral-large-latest"

DEFAULT_EMBEDDING_MODEL: str = "mistral-embed"

DEFAULT_TIMEOUT: float = 60.0

DEFAULT_MAX_RETRIES: int = 3

DEFAULT_MAX_TOKENS: int = 8192

DEFAULT_TEMPERATURE: float = 0.7

SUPPORTED_CHAT_MODELS: frozenset[str] = frozenset(
    {
        "mistral-large-latest",
        "mistral-medium-latest",
        "ministral-8b-latest",
        "ministral-3b-latest",
    }
)

SUPPORTED_EMBEDDING_MODELS: frozenset[str] = frozenset(
    {
        "mistral-embed",
    }
)