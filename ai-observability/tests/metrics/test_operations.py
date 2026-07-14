from ai_observability.metrics.operations import (
    Counter,
    Gauge,
    MetricsRegistry,
)


def test_counter_increment() -> None:
    counter = Counter(name="requests")

    counter.increment()
    counter.increment(2)

    assert counter.value == 3


def test_gauge_set() -> None:
    gauge = Gauge(name="latency")

    gauge.set(123.4)

    assert gauge.value == 123.4


def test_registry() -> None:
    registry = MetricsRegistry()

    counter = Counter(name="requests")
    gauge = Gauge(name="latency")

    registry.register_counter(counter)
    registry.register_gauge(gauge)

    assert registry.metric_count == 2
    assert registry.get_counter("requests") is counter
    assert registry.get_gauge("latency") is gauge
