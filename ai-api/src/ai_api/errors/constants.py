"""
Constants for the ai_api.errors module.

This module defines immutable constants used throughout the error
handling components of the AI API package.

The constants are framework-independent and provide standardized
error codes, error types, categories, and default messages.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Default Error Information
# ============================================================================

DEFAULT_ERROR_CODE: Final[str] = "ERR0000"

DEFAULT_ERROR_TYPE: Final[str] = "internal_error"

DEFAULT_ERROR_MESSAGE: Final[str] = "An unexpected error occurred."

# ============================================================================
# Standard Error Codes
# ============================================================================

VALIDATION_ERROR_CODE: Final[str] = "ERR1000"

AUTHENTICATION_ERROR_CODE: Final[str] = "ERR1001"

AUTHORIZATION_ERROR_CODE: Final[str] = "ERR1002"

NOT_FOUND_ERROR_CODE: Final[str] = "ERR1003"

CONFLICT_ERROR_CODE: Final[str] = "ERR1004"

RATE_LIMIT_ERROR_CODE: Final[str] = "ERR1005"

INTERNAL_ERROR_CODE: Final[str] = "ERR5000"

# ============================================================================
# Error Types
# ============================================================================

VALIDATION_ERROR: Final[str] = "validation_error"

AUTHENTICATION_ERROR: Final[str] = "authentication_error"

AUTHORIZATION_ERROR: Final[str] = "authorization_error"

NOT_FOUND_ERROR: Final[str] = "not_found_error"

CONFLICT_ERROR: Final[str] = "conflict_error"

RATE_LIMIT_ERROR: Final[str] = "rate_limit_error"

INTERNAL_ERROR: Final[str] = "internal_error"

SUPPORTED_ERROR_TYPES: Final[frozenset[str]] = frozenset(
    {
        VALIDATION_ERROR,
        AUTHENTICATION_ERROR,
        AUTHORIZATION_ERROR,
        NOT_FOUND_ERROR,
        CONFLICT_ERROR,
        RATE_LIMIT_ERROR,
        INTERNAL_ERROR,
    }
)

# ============================================================================
# Error Categories
# ============================================================================

CLIENT_ERROR_CATEGORY: Final[str] = "client"

SERVER_ERROR_CATEGORY: Final[str] = "server"

SYSTEM_ERROR_CATEGORY: Final[str] = "system"

SUPPORTED_ERROR_CATEGORIES: Final[frozenset[str]] = frozenset(
    {
        CLIENT_ERROR_CATEGORY,
        SERVER_ERROR_CATEGORY,
        SYSTEM_ERROR_CATEGORY,
    }
)

# ============================================================================
# Error Response Keys
# ============================================================================

ERROR_CODE_KEY: Final[str] = "code"

ERROR_TYPE_KEY: Final[str] = "type"

ERROR_MESSAGE_KEY: Final[str] = "message"

ERROR_DETAILS_KEY: Final[str] = "details"

ERROR_TIMESTAMP_KEY: Final[str] = "timestamp"

ERROR_TRACE_ID_KEY: Final[str] = "trace_id"

# ============================================================================
# Error Severity
# ============================================================================

LOW_SEVERITY: Final[str] = "low"

MEDIUM_SEVERITY: Final[str] = "medium"

HIGH_SEVERITY: Final[str] = "high"

CRITICAL_SEVERITY: Final[str] = "critical"

SUPPORTED_SEVERITIES: Final[frozenset[str]] = frozenset(
    {
        LOW_SEVERITY,
        MEDIUM_SEVERITY,
        HIGH_SEVERITY,
        CRITICAL_SEVERITY,
    }
)

# ============================================================================
# HTTP Status Ranges
# ============================================================================

CLIENT_ERROR_MIN_STATUS: Final[int] = 400

CLIENT_ERROR_MAX_STATUS: Final[int] = 499

SERVER_ERROR_MIN_STATUS: Final[int] = 500

SERVER_ERROR_MAX_STATUS: Final[int] = 599