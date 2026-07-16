"""Tests for ai_analytics.metrics.operations."""

from __future__ import annotations

import pytest

from ai_analytics.metrics.constants import (
    DEFAULT_ENABLED,
    DEFAULT_METRIC_TYPE,
)
from ai_analytics.metrics.exceptions import (
    DuplicateMetricError,
    MetricNotFoundError,
    MetricValidationError,
    UnsupportedMetricTypeError,
)
from ai_analytics.metrics.operations import (
    MetricDefinition,
    MetricRegistry,
    build_metric,
)


def test_metric_definition_defaults() -> None:
    metric = MetricDefinition(name="requests")

    assert metric.name == "requests"
    assert metric.value == 0.0
    assert metric.metric_type == DEFAULT_METRIC_TYPE
    assert metric.description == ""
    assert metric.tags == ()
    assert metric.enabled is DEFAULT_ENABLED


def test_metric_name_trimmed() -> None:
    metric = MetricDefinition(name="  requests  ")

    assert metric.name == "requests"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_metric_name(name: str) -> None:
    with pytest.raises(MetricValidationError):
        MetricDefinition(name=name)


def test_invalid_metric_type() -> None:
    with pytest.raises(UnsupportedMetricTypeError):
        MetricDefinition(
            name="requests",
            metric_type="timer",
        )


def test_build_metric() -> None:
    metric = build_metric(
        name="latency",
        value=10.5,
        metric_type="gauge",
        description="Average latency",
        tags=("api",),
    )

    assert metric.name == "latency"
    assert metric.value == 10.5
    assert metric.metric_type == "gauge"
    assert metric.description == "Average latency"
    assert metric.tags == ("api",)


def test_registry_register_and_get() -> None:
    registry = MetricRegistry()

    metric = build_metric(name="requests")

    registry.register(metric)

    assert registry.get("requests") is metric
    assert registry.exists("requests")
    assert len(registry) == 1
    assert "requests" in registry


def test_registry_duplicate_registration() -> None:
    registry = MetricRegistry()

    metric = build_metric(name="requests")

    registry.register(metric)

    with pytest.raises(DuplicateMetricError):
        registry.register(metric)


def test_registry_unregister() -> None:
    registry = MetricRegistry()

    metric = build_metric(name="requests")

    registry.register(metric)
    registry.unregister("requests")

    assert len(registry) == 0
    assert not registry.exists("requests")


def test_registry_unregister_missing() -> None:
    registry = MetricRegistry()

    with pytest.raises(MetricNotFoundError):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = MetricRegistry()

    with pytest.raises(MetricNotFoundError):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = MetricRegistry()

    registry.register(build_metric(name="one"))
    registry.register(build_metric(name="two"))

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = MetricRegistry()

    first = build_metric(name="one")
    second = build_metric(name="two")

    registry.register(first)
    registry.register(second)

    assert registry.list() == (first, second)


def test_registry_contains_unknown_type() -> None:
    registry = MetricRegistry()

    assert 123 not in registry