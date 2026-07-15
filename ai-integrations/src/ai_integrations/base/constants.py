"""
Shared constants for AI provider integrations.

This module contains framework-independent constants used by all
provider implementations.
"""

from __future__ import annotations

DEFAULT_TIMEOUT: float = 60.0

DEFAULT_MAX_RETRIES: int = 3

DEFAULT_MAX_TOKENS: int = 4096

DEFAULT_TEMPERATURE: float = 0.7

DEFAULT_TOP_P: float = 1.0

DEFAULT_FREQUENCY_PENALTY: float = 0.0

DEFAULT_PRESENCE_PENALTY: float = 0.0

MIN_TEMPERATURE: float = 0.0

MAX_TEMPERATURE: float = 2.0

MIN_TOP_P: float = 0.0

MAX_TOP_P: float = 1.0

DEFAULT_EMBEDDING_DIMENSIONS: int = 1536

DEFAULT_BATCH_SIZE: int = 100

DEFAULT_ENCODING: str = "utf-8"

DEFAULT_STREAM: bool = False

DEFAULT_SEED: int | None = None

DEFAULT_USER_AGENT: str = (
    "AI-Engineering-Framework/1.0"
)

SUPPORTED_MESSAGE_ROLES: frozenset[str] = frozenset(
    {
        "system",
        "user",
        "assistant",
        "tool",
        "developer",
    }
)

SUPPORTED_FINISH_REASONS: frozenset[str] = frozenset(
    {
        "stop",
        "length",
        "tool_calls",
        "content_filter",
    }
)