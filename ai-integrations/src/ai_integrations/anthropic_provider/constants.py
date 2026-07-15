"""
Constants for the Anthropic provider.

This module defines framework-independent constants used by the
Anthropic provider implementation.
"""

from __future__ import annotations

DEFAULT_API_BASE: str = "https://api.anthropic.com"

DEFAULT_API_VERSION: str = "2023-06-01"

DEFAULT_MODEL: str = "claude-sonnet-4-0"

DEFAULT_TIMEOUT: float = 60.0

DEFAULT_MAX_RETRIES: int = 3

DEFAULT_MAX_TOKENS: int = 4096

DEFAULT_TEMPERATURE: float = 0.7

SUPPORTED_CHAT_MODELS: frozenset[str] = frozenset(
    {
        "claude-opus-4-1",
        "claude-opus-4-0",
        "claude-sonnet-4-0",
        "claude-3-7-sonnet-latest",
        "claude-3-5-sonnet-latest",
        "claude-3-5-haiku-latest",
    }
)

SUPPORTED_REGIONS: frozenset[str] = frozenset(
    {
        "global",
    }
)