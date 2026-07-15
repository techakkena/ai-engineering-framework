"""
Shared utility constants for integrations.
"""

from __future__ import annotations

DEFAULT_CONNECT_TIMEOUT: float = 30.0

DEFAULT_READ_TIMEOUT: float = 60.0

DEFAULT_RETRY_ATTEMPTS: int = 3

DEFAULT_BACKOFF_FACTOR: float = 2.0

DEFAULT_USER_AGENT: str = (
    "AI-Engineering-Framework/1.0"
)

DEFAULT_ENCODING: str = "utf-8"

DEFAULT_CONTENT_TYPE: str = "application/json"

SUPPORTED_HTTP_SCHEMES: frozenset[str] = frozenset(
    {
        "http",
        "https",
    }
)