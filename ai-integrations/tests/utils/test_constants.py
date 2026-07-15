"""
Shared utility operations for integrations.
"""

from __future__ import annotations

from dataclasses import dataclass
from urllib.parse import urlparse

from ai_integrations.utils.constants import (
    DEFAULT_BACKOFF_FACTOR,
    DEFAULT_RETRY_ATTEMPTS,
    DEFAULT_USER_AGENT,
    SUPPORTED_HTTP_SCHEMES,
)
from ai_integrations.utils.exceptions import (
    ValidationError,
)


@dataclass(slots=True, frozen=True)
class RetryPolicy:
    """Represents a retry policy."""

    attempts: int = DEFAULT_RETRY_ATTEMPTS
    backoff_factor: float = DEFAULT_BACKOFF_FACTOR


def calculate_backoff(
    attempt: int,
    factor: float = DEFAULT_BACKOFF_FACTOR,
) -> float:
    """
    Calculate exponential backoff.

    Args:
        attempt: Current retry attempt.
        factor: Exponential backoff factor.

    Returns:
        Backoff delay in seconds.
    """
    if attempt < 0:
        raise ValidationError(
            "Attempt cannot be negative."
        )

    return factor**attempt


def build_user_agent(
    application: str,
    version: str,
) -> str:
    """
    Build a user-agent string.
    """
    return (
        f"{application}/{version} "
        f"({DEFAULT_USER_AGENT})"
    )


def merge_headers(
    default_headers: dict[str, str],
    custom_headers: dict[str, str] | None = None,
) -> dict[str, str]:
    """
    Merge HTTP headers.
    """
    headers = dict(default_headers)

    if custom_headers:
        headers.update(custom_headers)

    return headers


def validate_url(url: str) -> bool:
    """
    Validate an HTTP/HTTPS URL.
    """
    parsed = urlparse(url)

    if parsed.scheme not in SUPPORTED_HTTP_SCHEMES:
        raise ValidationError(
            f"Unsupported scheme: {parsed.scheme}"
        )

    if not parsed.netloc:
        raise ValidationError(
            "URL must contain a host."
        )

    return True