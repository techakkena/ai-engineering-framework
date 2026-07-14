from ai_evals.metrics.operations import (
    Metric,
    MetricRegistry,
)


def test_metric_defaults() -> None:
    metric = Metric()

    assert metric.name == "score"
    assert metric.value == 0.0


def test_register_metric() -> None:
    registry = MetricRegistry()

    metric = Metric(
        name="accuracy",
        value=0.95,
    )

    registry.register(metric)

    assert registry.count == 1
    assert registry.get("accuracy") is metric


def test_missing_metric() -> None:
    registry = MetricRegistry()

    assert registry.get("missing") is None
