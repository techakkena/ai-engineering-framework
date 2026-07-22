"""
Exceptions for the ai_monitoring.tracing package.
"""

from __future__ import annotations


class TracingError(Exception):
    """Base exception for tracing errors."""


class TraceValidationError(TracingError):
    """Raised when trace validation fails."""


class TraceNotFoundError(TracingError):
    """Raised when a trace cannot be found."""


class TraceStartError(TracingError):
    """Raised when starting a trace fails."""


class TraceSpanError(TracingError):
    """Raised when recording a span fails."""


class TraceEndError(TracingError):
    """Raised when ending a trace fails."""


class TracingConfigurationError(TracingError):
    """Raised when tracing configuration is invalid."""


class TracingProviderError(TracingError):
    """Raised when an underlying tracing provider fails."""