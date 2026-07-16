"""Operations for the ai_cloud.monitoring module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_cloud.monitoring.constants import (
    DEFAULT_ENABLED,
    DEFAULT_MONITOR_TYPE,
    MAX_MONITOR_NAME_LENGTH,
    MIN_MONITOR_NAME_LENGTH,
    SUPPORTED_MONITOR_TYPES,
)
from ai_cloud.monitoring.exceptions import (
    DuplicateMonitoringError,
    MonitoringNotFoundError,
    MonitoringValidationError,
    UnsupportedMonitorTypeError,
)


@dataclass(slots=True, frozen=True)
class MonitoringDefinition:
    """Represents a monitoring configuration."""

    name: str
    interval: int
    monitor_type: str = DEFAULT_MONITOR_TYPE
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the monitoring definition."""
        normalized = self.name.strip()

        if not (
            MIN_MONITOR_NAME_LENGTH
            <= len(normalized)
            <= MAX_MONITOR_NAME_LENGTH
        ):
            raise MonitoringValidationError(
                "Monitor name length is outside the allowed range."
            )

        if self.interval <= 0:
            raise MonitoringValidationError(
                "Monitoring interval must be greater than zero."
            )

        if self.monitor_type not in SUPPORTED_MONITOR_TYPES:
            raise UnsupportedMonitorTypeError(
                f"Unsupported monitor type: {self.monitor_type!r}."
            )

        object.__setattr__(self, "name", normalized)


class MonitoringRegistry:
    """Registry for monitoring definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        self._definitions: dict[str, MonitoringDefinition] = {}

    def register(
        self,
        monitor: MonitoringDefinition,
    ) -> None:
        if monitor.name in self._definitions:
            raise DuplicateMonitoringError(
                f"Monitor {monitor.name!r} is already registered."
            )

        self._definitions[monitor.name] = monitor

    def unregister(self, name: str) -> None:
        if name not in self._definitions:
            raise MonitoringNotFoundError(
                f"Monitor {name!r} is not registered."
            )

        del self._definitions[name]

    def get(self, name: str) -> MonitoringDefinition:
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise MonitoringNotFoundError(
                f"Monitor {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        return name in self._definitions

    def clear(self) -> None:
        self._definitions.clear()

    def list(self) -> tuple[MonitoringDefinition, ...]:
        return tuple(self._definitions.values())

    def __len__(self) -> int:
        return len(self._definitions)

    def __contains__(self, name: object) -> bool:
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_monitor(
    *,
    name: str,
    interval: int,
    monitor_type: str = DEFAULT_MONITOR_TYPE,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> MonitoringDefinition:
    """Build a validated monitoring definition."""

    return MonitoringDefinition(
        name=name,
        interval=interval,
        monitor_type=monitor_type,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "MonitoringDefinition",
    "MonitoringRegistry",
    "build_monitor",
]