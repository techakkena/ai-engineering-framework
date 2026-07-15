"""
Unit tests for ai_api.middleware.constants.
"""

from __future__ import annotations

from ai_api.middleware.constants import (
    DEFAULT_AUTH_MIDDLEWARE,
    DEFAULT_CLIENT_IP_HEADER,
    DEFAULT_CORRELATION_ID_HEADER,
    DEFAULT_CORS_MIDDLEWARE,
    DEFAULT_LOGGING_MIDDLEWARE,
    DEFAULT_METRICS_MIDDLEWARE,
    DEFAULT_MIDDLEWARE_NAME,
    DEFAULT_READ_TIMEOUT,
    DEFAULT_REQUEST_ID_HEADER,
    DEFAULT_TIMEOUT,
    DEFAULT_TRACE_ID_HEADER,
    DEFAULT_WRITE_TIMEOUT,
    MAX_MIDDLEWARE_NAME_LENGTH,
    MIDDLEWARE_PRIORITY,
    NAME_SEPARATOR,
    SUPPORTED_MIDDLEWARE_TYPES,
)


def test_default_request_id_header() -> None:
    """Test the default request ID header."""
    assert DEFAULT_REQUEST_ID_HEADER == "X-Request-ID"


def test_default_correlation_id_header() -> None:
    """Test the default correlation ID header."""
    assert DEFAULT_CORRELATION_ID_HEADER == "X-Correlation-ID"


def test_default_trace_id_header() -> None:
    """Test the default trace ID header."""
    assert DEFAULT_TRACE_ID_HEADER == "X-Trace-ID"


def test_default_client_ip_header() -> None:
    """Test the default client IP header."""
    assert DEFAULT_CLIENT_IP_HEADER == "X-Forwarded-For"


def test_default_timeouts() -> None:
    """Test default timeout values."""
    assert DEFAULT_TIMEOUT == 30
    assert DEFAULT_READ_TIMEOUT == 30
    assert DEFAULT_WRITE_TIMEOUT == 30


def test_supported_middleware_types() -> None:
    """Test supported middleware types."""
    assert "logging" in SUPPORTED_MIDDLEWARE_TYPES
    assert "authentication" in SUPPORTED_MIDDLEWARE_TYPES
    assert "authorization" in SUPPORTED_MIDDLEWARE_TYPES
    assert "cors" in SUPPORTED_MIDDLEWARE_TYPES
    assert "metrics" in SUPPORTED_MIDDLEWARE_TYPES


def test_supported_middleware_types_are_immutable() -> None:
    """Supported middleware types should be immutable."""
    assert isinstance(
        SUPPORTED_MIDDLEWARE_TYPES,
        frozenset,
    )


def test_default_middleware_names() -> None:
    """Test default middleware names."""
    assert DEFAULT_MIDDLEWARE_NAME == "middleware"
    assert DEFAULT_LOGGING_MIDDLEWARE == "logging"
    assert DEFAULT_AUTH_MIDDLEWARE == "authentication"
    assert DEFAULT_CORS_MIDDLEWARE == "cors"
    assert DEFAULT_METRICS_MIDDLEWARE == "metrics"


def test_max_middleware_name_length() -> None:
    """Test maximum middleware name length."""
    assert MAX_MIDDLEWARE_NAME_LENGTH == 100


def test_name_separator() -> None:
    """Test middleware name separator."""
    assert NAME_SEPARATOR == "_"


def test_middleware_priority() -> None:
    """Test middleware priorities."""
    assert MIDDLEWARE_PRIORITY["cors"] == 10
    assert MIDDLEWARE_PRIORITY["logging"] == 50
    assert MIDDLEWARE_PRIORITY["authentication"] == 70
    assert MIDDLEWARE_PRIORITY["authorization"] == 80
    assert MIDDLEWARE_PRIORITY["compression"] == 100