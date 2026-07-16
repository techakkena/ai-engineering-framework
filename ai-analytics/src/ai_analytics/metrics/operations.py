"""Operations for the ai_analytics.metrics module."""

from __future__ import annotations

from dataclasses import dataclass, field

from ai_analytics.metrics.constants import (
    DEFAULT_ENABLED,
    DEFAULT_METRIC_TYPE,
    MAX_METRIC_NAME_LENGTH,
    MIN_METRIC_NAME_LENGTH,
    SUPPORTED_METRIC_TYPES,
)
from ai_analytics.metrics.exceptions import (
    DuplicateMetricError,
    MetricNotFoundError,
    MetricValidationError,
    UnsupportedMetricTypeError,
)


@dataclass(slots=True, frozen=True)
class MetricDefinition:
    """Represents an analytics metric."""

    name: str
    value: float = 0.0
    metric_type: str = DEFAULT_METRIC_TYPE
    description: str = ""
    tags: tuple[str, ...] = field(default_factory=tuple)
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the metric definition."""
        normalized = self.name.strip()

        if not (
            MIN_METRIC_NAME_LENGTH
            <= len(normalized)
            <= MAX_METRIC_NAME_LENGTH
        ):
            raise MetricValidationError(
                "Metric name length is outside the allowed range."
            )

        if self.metric_type not in SUPPORTED_METRIC_TYPES:
            raise UnsupportedMetricTypeError(
                f"Unsupported metric type: {self.metric_type!r}."
            )

        object.__setattr__(self, "name", normalized)


class MetricRegistry:
    """Registry for metric definitions."""

    __slots__ = ("_metrics",)

    def __init__(self) -> None:
        """Initialize an empty metric registry."""
        self._metrics: dict[str, MetricDefinition] = {}

    def register(self, metric: MetricDefinition) -> None:
        """Register a metric.

        Args:
            metric: Metric definition to register.

        Raises:
            DuplicateMetricError: If the metric already exists.
        """
        if metric.name in self._metrics:
            raise DuplicateMetricError(
                f"Metric {metric.name!r} is already registered."
            )

        self._metrics[metric.name] = metric

    def unregister(self, name: str) -> None:
        """Remove a registered metric.

        Args:
            name: Metric name.

        Raises:
            MetricNotFoundError: If the metric is not registered.
        """
        if name not in self._metrics:
            raise MetricNotFoundError(
                f"Metric {name!r} is not registered."
            )

        del self._metrics[name]

    def get(self, name: str) -> MetricDefinition:
        """Return a registered metric.

        Args:
            name: Metric name.

        Returns:
            The registered metric.

        Raises:
            MetricNotFoundError: If the metric is not registered.
        """
        try:
            return self._metrics[name]
        except KeyError as exc:
            raise MetricNotFoundError(
                f"Metric {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether a metric exists."""
        return name in self._metrics

    def clear(self) -> None:
        """Remove all registered metrics."""
        self._metrics.clear()

    def list(self) -> tuple[MetricDefinition, ...]:
        """Return all registered metrics."""
        return tuple(self._metrics.values())

    def __len__(self) -> int:
        """Return the number of registered metrics."""
        return len(self._metrics)

    def __contains__(self, name: object) -> bool:
        """Return whether a metric exists."""
        return isinstance(name, str) and name in self._metrics


def build_metric(
    *,
    name: str,
    value: float = 0.0,
    metric_type: str = DEFAULT_METRIC_TYPE,
    description: str = "",
    tags: tuple[str, ...] = (),
    enabled: bool = DEFAULT_ENABLED,
) -> MetricDefinition:
    """Build and validate a metric definition.

    Args:
        name: Metric name.
        value: Metric value.
        metric_type: Metric type.
        description: Metric description.
        tags: Metric tags.
        enabled: Whether the metric is enabled.

    Returns:
        A validated metric definition.
    """
    return MetricDefinition(
        name=name,
        value=value,
        metric_type=metric_type,
        description=description,
        tags=tags,
        enabled=enabled,
    )


__all__ = [
    "MetricDefinition",
    "MetricRegistry",
    "build_metric",
]