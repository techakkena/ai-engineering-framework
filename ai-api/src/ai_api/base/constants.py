"""
Constants for the ai_api.base module.

This module defines framework-agnostic constants used throughout the
AI API package. These values provide consistent defaults for API
configuration, routing, content negotiation, and HTTP method validation.

The constants are intentionally immutable and reusable across different
web frameworks.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# API Configuration
# ============================================================================

DEFAULT_API_VERSION: Final[str] = "v1"

DEFAULT_PREFIX: Final[str] = "/api"

DEFAULT_TIMEOUT: Final[int] = 30

# ============================================================================
# Content Types
# ============================================================================

JSON_MEDIA_TYPE: Final[str] = "application/json"

DEFAULT_CONTENT_TYPE: Final[str] = JSON_MEDIA_TYPE

# ============================================================================
# Documentation Routes
# ============================================================================

DEFAULT_OPENAPI_PATH: Final[str] = "/openapi.json"

DEFAULT_DOCS_PATH: Final[str] = "/docs"

DEFAULT_REDOC_PATH: Final[str] = "/redoc"

# ============================================================================
# HTTP Methods
# ============================================================================

SUPPORTED_HTTP_METHODS: Final[frozenset[str]] = frozenset(
    {
        "GET",
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
        "HEAD",
        "OPTIONS",
    }
)

# ============================================================================
# Route Defaults
# ============================================================================

ROOT_PATH: Final[str] = "/"

PATH_SEPARATOR: Final[str] = "/"

VERSION_PREFIX: Final[str] = "/v"

# ============================================================================
# Response Defaults
# ============================================================================

DEFAULT_SUCCESS_STATUS_CODE: Final[int] = 200

DEFAULT_CREATED_STATUS_CODE: Final[int] = 201

DEFAULT_NO_CONTENT_STATUS_CODE: Final[int] = 204

DEFAULT_BAD_REQUEST_STATUS_CODE: Final[int] = 400

DEFAULT_UNAUTHORIZED_STATUS_CODE: Final[int] = 401

DEFAULT_FORBIDDEN_STATUS_CODE: Final[int] = 403

DEFAULT_NOT_FOUND_STATUS_CODE: Final[int] = 404

DEFAULT_INTERNAL_SERVER_ERROR_STATUS_CODE: Final[int] = 500
