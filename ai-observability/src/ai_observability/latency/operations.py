from __future__ import annotations

from dataclasses import dataclass

from .constants import DEFAULT_LATENCY_UNIT


@dataclass(slots=True)
class LatencyMeasurement:
    """Represents a latency measurement."""

    duration: float
    unit: str = DEFAULT_LATENCY_UNIT


class LatencyRegistry:
    """Stores latency measurements."""

    def __init__(self) -> None:
        self._measurements: list[LatencyMeasurement] = []

    def add(
        self,
        measurement: LatencyMeasurement,
    ) -> None:
        self._measurements.append(
            measurement,
        )

    @property
    def count(self) -> int:
        return len(self._measurements)

    @property
    def total(self) -> float:
        return sum(item.duration for item in self._measurements)

    @property
    def average(self) -> float:
        if not self._measurements:
            return 0.0

        return self.total / self.count

    @property
    def minimum(self) -> float:
        if not self._measurements:
            return 0.0

        return min(item.duration for item in self._measurements)

    @property
    def maximum(self) -> float:
        if not self._measurements:
            return 0.0

        return max(item.duration for item in self._measurements)
