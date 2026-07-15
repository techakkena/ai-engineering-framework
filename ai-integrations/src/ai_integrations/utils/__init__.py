"""
Utility helpers for the AI Integrations package.

This package contains framework-independent utility functions shared
across AI providers and service integrations.

The utilities are intentionally lightweight and reusable by all
integration modules.
"""

from ai_integrations.utils.constants import (
    DEFAULT_BACKOFF_FACTOR,
    DEFAULT_CONNECT_TIMEOUT,
    DEFAULT_READ_TIMEOUT,
    DEFAULT_RETRY_ATTEMPTS,
    DEFAULT_USER_AGENT,
)
from ai_integrations.utils.exceptions import (
    IntegrationError,
    RetryError,
    SerializationError,
    ValidationError,
)
from ai_integrations.utils.operations import (
    RetryPolicy,
    build_user_agent,
    calculate_backoff,
    merge_headers,
    validate_url,
)

__all__ = [
    "DEFAULT_BACKOFF_FACTOR",
    "DEFAULT_CONNECT_TIMEOUT",
    "DEFAULT_READ_TIMEOUT",
    "DEFAULT_RETRY_ATTEMPTS",
    "DEFAULT_USER_AGENT",
    "IntegrationError",
    "RetryError",
    "SerializationError",
    "ValidationError",
    "RetryPolicy",
    "build_user_agent",
    "calculate_backoff",
    "merge_headers",
    "validate_url",
]