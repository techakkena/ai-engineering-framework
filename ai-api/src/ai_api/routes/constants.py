"""
Constants for the ai_api.routes module.

This module defines immutable constants used throughout the routing
components of the AI API package.

The constants are framework-independent and provide sensible defaults
for route naming, prefixes, validation, and dynamic route parameters.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Route Defaults
# ============================================================================

DEFAULT_ROUTE_PREFIX: Final[str] = "/"

DEFAULT_ROUTE_NAME: Final[str] = "root"

DEFAULT_TAG: Final[str] = "default"

# ============================================================================
# Route Validation
# ============================================================================

MAX_ROUTE_LENGTH: Final[int] = 256

MIN_ROUTE_LENGTH: Final[int] = 1

# ============================================================================
# Dynamic Route Parameters
# ============================================================================

DYNAMIC_PARAMETER_START: Final[str] = "{"

DYNAMIC_PARAMETER_END: Final[str] = "}"

DYNAMIC_PARAMETER_PATTERN: Final[str] = (
    r"\{([a-zA-Z_][a-zA-Z0-9_]*)\}"
)

# ============================================================================
# Reserved Route Names
# ============================================================================

RESERVED_ROUTE_NAMES: Final[frozenset[str]] = frozenset(
    {
        "docs",
        "redoc",
        "openapi",
        "static",
        "health",
        "metrics",
        "favicon.ico",
    }
)

# ============================================================================
# HTTP Route Separators
# ============================================================================

PATH_SEPARATOR: Final[str] = "/"

NAME_SEPARATOR: Final[str] = "_"

# ============================================================================
# Common Tags
# ============================================================================

SYSTEM_TAG: Final[str] = "system"

API_TAG: Final[str] = "api"

HEALTH_TAG: Final[str] = "health"

ADMIN_TAG: Final[str] = "admin"

AUTH_TAG: Final[str] = "auth"

USER_TAG: Final[str] = "user"