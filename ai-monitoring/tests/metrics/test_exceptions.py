"""
Unit tests for ai_monitoring.metrics.exceptions.
"""

from __future__ import annotations

import pytest

from ai_monitoring.metrics.exceptions import (
    MetricCollectionError,
    MetricNotFoundError,
    MetricRecordingError,
    MetricValidationError,
    MetricsConfigurationError,
    MetricsError,
    MetricsProviderError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        MetricValidationError,
        MetricNotFoundError,
        MetricCollectionError,
        MetricRecordingError,
        MetricsConfigurationError,
        MetricsProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[MetricsError],
) -> None:
    """Every custom exception should inherit from MetricsError."""
    assert issubclass(
        exception_class,
        MetricsError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        MetricsError,
        match="metrics failure",
    ):
        raise MetricsError(
            "metrics failure",
        )