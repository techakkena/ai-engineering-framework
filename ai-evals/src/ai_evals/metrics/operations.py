from __future__ import annotations

from dataclasses import dataclass

from .constants import DEFAULT_METRIC_NAME


@dataclass(slots=True)
class Metric:
    """Represents an evaluation metric."""

    name: str = DEFAULT_METRIC_NAME
    value: float = 0.0


class MetricRegistry:
    """Registry of evaluation metrics."""

    def __init__(self) -> None:
        self._metrics: dict[str, Metric] = {}

    def register(
        self,
        metric: Metric,
    ) -> None:
        """Register a metric."""
        self._metrics[metric.name] = metric

    def get(
        self,
        name: str,
    ) -> Metric | None:
        """Return a metric."""
        return self._metrics.get(name)

    @property
    def count(self) -> int:
        """Return number of metrics."""
        return len(self._metrics)
