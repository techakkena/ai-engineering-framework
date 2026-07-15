"""
Constants for the ai_api.middleware module.

This module defines immutable constants used throughout the middleware
components of the AI API package.

The constants are framework-independent and provide default values
for middleware configuration, request tracking, priorities, and
supported middleware types.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Request Headers
# ============================================================================

DEFAULT_REQUEST_ID_HEADER: Final[str] = "X-Request-ID"

DEFAULT_CORRELATION_ID_HEADER: Final[str] = "X-Correlation-ID"

DEFAULT_TRACE_ID_HEADER: Final[str] = "X-Trace-ID"

DEFAULT_CLIENT_IP_HEADER: Final[str] = "X-Forwarded-For"

# ============================================================================
# Timeouts
# ============================================================================

DEFAULT_TIMEOUT: Final[int] = 30

DEFAULT_READ_TIMEOUT: Final[int] = 30

DEFAULT_WRITE_TIMEOUT: Final[int] = 30

# ============================================================================
# Middleware Priorities
# ============================================================================

MIDDLEWARE_PRIORITY: Final[dict[str, int]] = {
    "cors": 10,
    "security": 20,
    "request_id": 30,
    "correlation_id": 40,
    "logging": 50,
    "metrics": 60,
    "authentication": 70,
    "authorization": 80,
    "rate_limit": 90,
    "compression": 100,
}

# ============================================================================
# Middleware Types
# ============================================================================

SUPPORTED_MIDDLEWARE_TYPES: Final[frozenset[str]] = frozenset(
    {
        "cors",
        "security",
        "logging",
        "metrics",
        "request_id",
        "correlation_id",
        "authentication",
        "authorization",
        "rate_limit",
        "compression",
        "exception_handler",
        "custom",
    }
)

# ============================================================================
# Default Middleware Names
# ============================================================================

DEFAULT_MIDDLEWARE_NAME: Final[str] = "middleware"

DEFAULT_LOGGING_MIDDLEWARE: Final[str] = "logging"

DEFAULT_AUTH_MIDDLEWARE: Final[str] = "authentication"

DEFAULT_CORS_MIDDLEWARE: Final[str] = "cors"

DEFAULT_METRICS_MIDDLEWARE: Final[str] = "metrics"

# ============================================================================
# Miscellaneous
# ============================================================================

MAX_MIDDLEWARE_NAME_LENGTH: Final[int] = 100

NAME_SEPARATOR: Final[str] = "_"