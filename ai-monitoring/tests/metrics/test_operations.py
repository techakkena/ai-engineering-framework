"""
Unit tests for ai_monitoring.metrics.operations.
"""

from __future__ import annotations

import pytest

from ai_monitoring.metrics.exceptions import (
    MetricValidationError,
)
from ai_monitoring.metrics.operations import (
    MetricResult,
    collect_metric,
    get_metric,
    list_metrics,
    record_metric,
    reset_metrics,
)


def test_collect_metric_success() -> None:
    """Metric collection should succeed."""
    result = collect_metric("latency")

    assert isinstance(result, MetricResult)
    assert result.success is True
    assert result.task == "collect_metric"


def test_collect_metric_empty_name() -> None:
    """Empty metric names should raise."""
    with pytest.raises(MetricValidationError):
        collect_metric("")


def test_record_metric_success() -> None:
    """Metric recording should succeed."""
    result = record_metric(
        "latency",
        123.45,
    )

    assert result.success is True
    assert result.task == "record_metric"
    assert result.data["value"] == 123.45


def test_get_metric_success() -> None:
    """Getting a metric should succeed."""
    result = get_metric("latency")

    assert result.success is True
    assert result.task == "get_metric"


def test_list_metrics_success() -> None:
    """Listing metrics should succeed."""
    result = list_metrics()

    assert result.success is True
    assert result.task == "list_metrics"
    assert isinstance(
        result.data["metrics"],
        list,
    )


def test_reset_metrics_success() -> None:
    """Resetting metrics should succeed."""
    result = reset_metrics()

    assert result.success is True
    assert result.task == "reset_metrics"
    assert result.data["reset"] is True


@pytest.mark.parametrize(
    "operation",
    [
        collect_metric,
        get_metric,
    ],
)
def test_name_validation(
    operation,
) -> None:
    """Operations requiring a metric name should reject empty names."""
    with pytest.raises(MetricValidationError):
        operation("")


def test_record_metric_empty_name() -> None:
    """Recording with an empty metric name should raise."""
    with pytest.raises(MetricValidationError):
        record_metric(
            "",
            1.0,
        )