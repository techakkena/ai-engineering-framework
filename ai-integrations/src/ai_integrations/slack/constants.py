"""
Constants for the Slack integration.
"""

from __future__ import annotations

DEFAULT_API_BASE: str = "https://slack.com/api"

DEFAULT_TIMEOUT: float = 60.0

DEFAULT_MAX_RETRIES: int = 3

DEFAULT_MESSAGE_LIMIT: int = 100

SUPPORTED_MESSAGE_TYPES: frozenset[str] = frozenset(
    {
        "text",
        "markdown",
        "blocks",
    }
)

SUPPORTED_CHANNEL_TYPES: frozenset[str] = frozenset(
    {
        "public",
        "private",
        "direct",
        "group",
    }
)