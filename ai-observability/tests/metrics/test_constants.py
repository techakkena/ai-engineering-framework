from ai_observability.metrics.constants import (
    MetricType,
)


def test_metric_types() -> None:
    assert MetricType.COUNTER.value == "counter"
    assert MetricType.GAUGE.value == "gauge"


def test_metric_type_count() -> None:
    assert len(MetricType) == 2
