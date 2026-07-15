"""
Constants for the Azure OpenAI provider.
"""

from __future__ import annotations

DEFAULT_ENDPOINT: str = "https://example.openai.azure.com"

DEFAULT_API_VERSION: str = "2025-04-01-preview"

DEFAULT_MODEL: str = "gpt-5"

DEFAULT_EMBEDDING_MODEL: str = "text-embedding-3-small"

DEFAULT_TIMEOUT: float = 60.0

DEFAULT_MAX_RETRIES: int = 3

SUPPORTED_CHAT_MODELS: frozenset[str] = frozenset(
    {
        "gpt-5",
        "gpt-5-mini",
        "gpt-5-nano",
        "gpt-4.1",
        "gpt-4.1-mini",
    }
)

SUPPORTED_EMBEDDING_MODELS: frozenset[str] = frozenset(
    {
        "text-embedding-3-small",
        "text-embedding-3-large",
    }
)