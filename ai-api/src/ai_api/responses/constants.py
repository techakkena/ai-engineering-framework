"""
Constants for the ai_api.responses module.

This module defines immutable constants used throughout the response
components of the AI API package.

The constants are framework-independent and provide sensible defaults
for response serialization, content types, HTTP status categories,
and response metadata.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Response Defaults
# ============================================================================

DEFAULT_VERSION: Final[str] = "1.0.0"

DEFAULT_SUCCESS_MESSAGE: Final[str] = "Request completed successfully."

DEFAULT_ERROR_MESSAGE: Final[str] = "An unexpected error occurred."

DEFAULT_CONTENT_TYPE: Final[str] = "application/json"

# ============================================================================
# Content Types
# ============================================================================

JSON_CONTENT_TYPE: Final[str] = "application/json"

TEXT_CONTENT_TYPE: Final[str] = "text/plain"

HTML_CONTENT_TYPE: Final[str] = "text/html"

XML_CONTENT_TYPE: Final[str] = "application/xml"

CSV_CONTENT_TYPE: Final[str] = "text/csv"

OCTET_STREAM_CONTENT_TYPE: Final[str] = (
    "application/octet-stream"
)

SUPPORTED_CONTENT_TYPES: Final[frozenset[str]] = frozenset(
    {
        JSON_CONTENT_TYPE,
        TEXT_CONTENT_TYPE,
        HTML_CONTENT_TYPE,
        XML_CONTENT_TYPE,
        CSV_CONTENT_TYPE,
        OCTET_STREAM_CONTENT_TYPE,
    }
)

# ============================================================================
# Response Status
# ============================================================================

SUCCESS_STATUS: Final[str] = "success"

ERROR_STATUS: Final[str] = "error"

WARNING_STATUS: Final[str] = "warning"

INFO_STATUS: Final[str] = "info"

SUPPORTED_RESPONSE_STATUSES: Final[frozenset[str]] = frozenset(
    {
        SUCCESS_STATUS,
        ERROR_STATUS,
        WARNING_STATUS,
        INFO_STATUS,
    }
)

# ============================================================================
# Serialization
# ============================================================================

DEFAULT_ENCODING: Final[str] = "utf-8"

DEFAULT_INDENT: Final[int] = 2

DEFAULT_SORT_KEYS: Final[bool] = True

# ============================================================================
# Response Keys
# ============================================================================

STATUS_KEY: Final[str] = "status"

MESSAGE_KEY: Final[str] = "message"

DATA_KEY: Final[str] = "data"

ERROR_KEY: Final[str] = "error"

METADATA_KEY: Final[str] = "metadata"

TIMESTAMP_KEY: Final[str] = "timestamp"

# ============================================================================
# Pagination Keys
# ============================================================================

PAGE_KEY: Final[str] = "page"

PAGE_SIZE_KEY: Final[str] = "page_size"

TOTAL_ITEMS_KEY: Final[str] = "total_items"

TOTAL_PAGES_KEY: Final[str] = "total_pages"

# ============================================================================
# Headers
# ============================================================================

CONTENT_TYPE_HEADER: Final[str] = "Content-Type"

CACHE_CONTROL_HEADER: Final[str] = "Cache-Control"

ETAG_HEADER: Final[str] = "ETag"

LOCATION_HEADER: Final[str] = "Location"

REQUEST_ID_HEADER: Final[str] = "X-Request-ID"

# ============================================================================
# Limits
# ============================================================================

MAX_RESPONSE_SIZE: Final[int] = 10 * 1024 * 1024  # 10 MB

DEFAULT_HTTP_STATUS: Final[int] = 200