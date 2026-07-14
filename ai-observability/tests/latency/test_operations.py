from ai_observability.latency.operations import (
    LatencyMeasurement,
    LatencyRegistry,
)


def test_measurement() -> None:
    measurement = LatencyMeasurement(
        duration=100,
    )

    assert measurement.duration == 100
    assert measurement.unit == "ms"


def test_registry_statistics() -> None:
    registry = LatencyRegistry()

    registry.add(
        LatencyMeasurement(
            duration=100,
        )
    )

    registry.add(
        LatencyMeasurement(
            duration=300,
        )
    )

    assert registry.count == 2
    assert registry.total == 400
    assert registry.average == 200
    assert registry.minimum == 100
    assert registry.maximum == 300


def test_empty_registry() -> None:
    registry = LatencyRegistry()

    assert registry.count == 0
    assert registry.average == 0.0
    assert registry.minimum == 0.0
    assert registry.maximum == 0.0
