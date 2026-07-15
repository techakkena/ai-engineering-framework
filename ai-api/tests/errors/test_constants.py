"""
Unit tests for ai_api.errors.constants.
"""

from __future__ import annotations

from ai_api.errors.constants import (
    AUTHENTICATION_ERROR,
    AUTHENTICATION_ERROR_CODE,
    AUTHORIZATION_ERROR,
    AUTHORIZATION_ERROR_CODE,
    CLIENT_ERROR_CATEGORY,
    CLIENT_ERROR_MAX_STATUS,
    CLIENT_ERROR_MIN_STATUS,
    CONFLICT_ERROR,
    CONFLICT_ERROR_CODE,
    CRITICAL_SEVERITY,
    DEFAULT_ERROR_CODE,
    DEFAULT_ERROR_MESSAGE,
    DEFAULT_ERROR_TYPE,
    ERROR_CODE_KEY,
    ERROR_DETAILS_KEY,
    ERROR_MESSAGE_KEY,
    ERROR_TIMESTAMP_KEY,
    ERROR_TRACE_ID_KEY,
    ERROR_TYPE_KEY,
    HIGH_SEVERITY,
    INTERNAL_ERROR,
    INTERNAL_ERROR_CODE,
    LOW_SEVERITY,
    MEDIUM_SEVERITY,
    NOT_FOUND_ERROR,
    NOT_FOUND_ERROR_CODE,
    RATE_LIMIT_ERROR,
    RATE_LIMIT_ERROR_CODE,
    SERVER_ERROR_CATEGORY,
    SERVER_ERROR_MAX_STATUS,
    SERVER_ERROR_MIN_STATUS,
    SUPPORTED_ERROR_CATEGORIES,
    SUPPORTED_ERROR_TYPES,
    SUPPORTED_SEVERITIES,
    SYSTEM_ERROR_CATEGORY,
    VALIDATION_ERROR,
    VALIDATION_ERROR_CODE,
)


def test_default_error_values() -> None:
    """Test default error values."""
    assert DEFAULT_ERROR_CODE == "ERR0000"
    assert DEFAULT_ERROR_TYPE == "internal_error"
    assert DEFAULT_ERROR_MESSAGE == "An unexpected error occurred."


def test_standard_error_codes() -> None:
    """Test standard error codes."""
    assert VALIDATION_ERROR_CODE == "ERR1000"
    assert AUTHENTICATION_ERROR_CODE == "ERR1001"
    assert AUTHORIZATION_ERROR_CODE == "ERR1002"
    assert NOT_FOUND_ERROR_CODE == "ERR1003"
    assert CONFLICT_ERROR_CODE == "ERR1004"
    assert RATE_LIMIT_ERROR_CODE == "ERR1005"
    assert INTERNAL_ERROR_CODE == "ERR5000"


def test_error_types() -> None:
    """Test supported error types."""
    expected = {
        VALIDATION_ERROR,
        AUTHENTICATION_ERROR,
        AUTHORIZATION_ERROR,
        NOT_FOUND_ERROR,
        CONFLICT_ERROR,
        RATE_LIMIT_ERROR,
        INTERNAL_ERROR,
    }

    assert SUPPORTED_ERROR_TYPES == expected


def test_supported_error_types_are_immutable() -> None:
    """Supported error types should be immutable."""
    assert isinstance(
        SUPPORTED_ERROR_TYPES,
        frozenset,
    )


def test_error_categories() -> None:
    """Test supported error categories."""
    expected = {
        CLIENT_ERROR_CATEGORY,
        SERVER_ERROR_CATEGORY,
        SYSTEM_ERROR_CATEGORY,
    }

    assert SUPPORTED_ERROR_CATEGORIES == expected


def test_supported_error_categories_are_immutable() -> None:
    """Supported error categories should be immutable."""
    assert isinstance(
        SUPPORTED_ERROR_CATEGORIES,
        frozenset,
    )


def test_error_response_keys() -> None:
    """Test response dictionary keys."""
    assert ERROR_CODE_KEY == "code"
    assert ERROR_TYPE_KEY == "type"
    assert ERROR_MESSAGE_KEY == "message"
    assert ERROR_DETAILS_KEY == "details"
    assert ERROR_TIMESTAMP_KEY == "timestamp"
    assert ERROR_TRACE_ID_KEY == "trace_id"


def test_error_severities() -> None:
    """Test supported severity levels."""
    expected = {
        LOW_SEVERITY,
        MEDIUM_SEVERITY,
        HIGH_SEVERITY,
        CRITICAL_SEVERITY,
    }

    assert SUPPORTED_SEVERITIES == expected


def test_supported_severities_are_immutable() -> None:
    """Supported severities should be immutable."""
    assert isinstance(
        SUPPORTED_SEVERITIES,
        frozenset,
    )


def test_http_status_ranges() -> None:
    """Test HTTP status ranges."""
    assert CLIENT_ERROR_MIN_STATUS == 400
    assert CLIENT_ERROR_MAX_STATUS == 499
    assert SERVER_ERROR_MIN_STATUS == 500
    assert SERVER_ERROR_MAX_STATUS == 599