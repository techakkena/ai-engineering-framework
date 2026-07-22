"""
Unit tests for ai_monitoring.tracing.exceptions.
"""

from __future__ import annotations

import pytest

from ai_monitoring.tracing.exceptions import (
    TraceEndError,
    TraceNotFoundError,
    TraceSpanError,
    TraceStartError,
    TraceValidationError,
    TracingConfigurationError,
    TracingError,
    TracingProviderError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        TraceValidationError,
        TraceNotFoundError,
        TraceStartError,
        TraceSpanError,
        TraceEndError,
        TracingConfigurationError,
        TracingProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[TracingError],
) -> None:
    """Every custom exception should inherit from TracingError."""
    assert issubclass(
        exception_class,
        TracingError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        TracingError,
        match="tracing failure",
    ):
        raise TracingError(
            "tracing failure",
        )