"""
Constants for the GitHub integration.
"""

from __future__ import annotations

DEFAULT_API_BASE: str = "https://api.github.com"

DEFAULT_BRANCH: str = "main"

DEFAULT_TIMEOUT: float = 60.0

DEFAULT_MAX_RETRIES: int = 3

DEFAULT_PER_PAGE: int = 100

SUPPORTED_VISIBILITIES: frozenset[str] = frozenset(
    {
        "public",
        "private",
        "internal",
    }
)

SUPPORTED_PR_STATES: frozenset[str] = frozenset(
    {
        "open",
        "closed",
        "all",
    }
)