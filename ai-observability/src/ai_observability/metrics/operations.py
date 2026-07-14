from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Counter:
    """Simple counter metric."""

    name: str
    value: int = 0

    def increment(
        self,
        amount: int = 1,
    ) -> None:
        """Increment the counter."""
        self.value += amount


@dataclass(slots=True)
class Gauge:
    """Simple gauge metric."""

    name: str
    value: float = 0.0

    def set(
        self,
        value: float,
    ) -> None:
        """Set the gauge value."""
        self.value = value


class MetricsRegistry:
    """Registry for metrics."""

    def __init__(self) -> None:
        self._counters: dict[str, Counter] = {}
        self._gauges: dict[str, Gauge] = {}

    def register_counter(
        self,
        counter: Counter,
    ) -> None:
        self._counters[counter.name] = counter

    def register_gauge(
        self,
        gauge: Gauge,
    ) -> None:
        self._gauges[gauge.name] = gauge

    def get_counter(
        self,
        name: str,
    ) -> Counter | None:
        return self._counters.get(name)

    def get_gauge(
        self,
        name: str,
    ) -> Gauge | None:
        return self._gauges.get(name)

    @property
    def metric_count(self) -> int:
        """Return total registered metrics."""
        return len(self._counters) + len(self._gauges)
