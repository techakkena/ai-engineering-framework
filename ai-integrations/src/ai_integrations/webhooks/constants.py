"""
Constants for webhook integrations.
"""

from __future__ import annotations

DEFAULT_TIMEOUT: float = 60.0

DEFAULT_MAX_RETRIES: int = 3

DEFAULT_CONTENT_TYPE: str = "application/json"

DEFAULT_SIGNATURE_HEADER: str = "X-Signature"

DEFAULT_USER_AGENT: str = "AI-Engineering-Framework/1.0"

SUPPORTED_HTTP_METHODS: frozenset[str] = frozenset(
    {
        "GET",
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
    }
)

SUPPORTED_CONTENT_TYPES: frozenset[str] = frozenset(
    {
        "application/json",
        "application/x-www-form-urlencoded",
    }
)