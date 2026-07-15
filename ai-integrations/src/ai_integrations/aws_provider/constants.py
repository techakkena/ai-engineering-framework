"""
Constants for the AWS provider.
"""

from __future__ import annotations

DEFAULT_REGION: str = "us-east-1"

DEFAULT_MODEL: str = "amazon.nova-pro-v1:0"

DEFAULT_EMBEDDING_MODEL: str = "amazon.titan-embed-text-v2:0"

DEFAULT_TIMEOUT: float = 60.0

DEFAULT_MAX_RETRIES: int = 3

DEFAULT_MAX_TOKENS: int = 4096

DEFAULT_TEMPERATURE: float = 0.7

SUPPORTED_CHAT_MODELS: frozenset[str] = frozenset(
    {
        "amazon.nova-lite-v1:0",
        "amazon.nova-pro-v1:0",
        "amazon.nova-micro-v1:0",
        "anthropic.claude-3-7-sonnet",
        "meta.llama3-3-70b-instruct-v1:0",
    }
)

SUPPORTED_EMBEDDING_MODELS: frozenset[str] = frozenset(
    {
        "amazon.titan-embed-text-v2:0",
        "cohere.embed-english-v3",
    }
)