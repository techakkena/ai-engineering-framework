"""
Constants for email integrations.
"""

from __future__ import annotations

DEFAULT_SMTP_HOST: str = "localhost"

DEFAULT_PORT: int = 587

DEFAULT_TIMEOUT: float = 60.0

DEFAULT_MAX_RETRIES: int = 3

DEFAULT_ENCODING: str = "utf-8"

SUPPORTED_CONTENT_TYPES: frozenset[str] = frozenset(
    {
        "text/plain",
        "text/html",
        "multipart/mixed",
    }
)

SUPPORTED_PROVIDERS: frozenset[str] = frozenset(
    {
        "smtp",
        "sendgrid",
        "ses",
        "azure",
    }
)