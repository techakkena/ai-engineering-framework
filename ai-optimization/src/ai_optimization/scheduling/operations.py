"""Operations for the ai_optimization.scheduling module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_optimization.scheduling.constants import (
    DEFAULT_ENABLED,
    DEFAULT_SCHEDULER,
    MAX_SCHEDULE_NAME_LENGTH,
    MIN_SCHEDULE_NAME_LENGTH,
    SUPPORTED_SCHEDULERS,
)
from ai_optimization.scheduling.exceptions import (
    DuplicateScheduleError,
    ScheduleNotFoundError,
    ScheduleValidationError,
    UnsupportedSchedulerError,
)


@dataclass(slots=True, frozen=True)
class ScheduleDefinition:
    """Represents a scheduling configuration."""

    name: str
    max_concurrency: int
    scheduler: str = DEFAULT_SCHEDULER
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the schedule definition."""
        normalized = self.name.strip()

        if not (
            MIN_SCHEDULE_NAME_LENGTH
            <= len(normalized)
            <= MAX_SCHEDULE_NAME_LENGTH
        ):
            raise ScheduleValidationError(
                "Schedule name length is outside the allowed range."
            )

        if self.max_concurrency <= 0:
            raise ScheduleValidationError(
                "Maximum concurrency must be greater than zero."
            )

        if self.scheduler not in SUPPORTED_SCHEDULERS:
            raise UnsupportedSchedulerError(
                f"Unsupported scheduler: {self.scheduler!r}."
            )

        object.__setattr__(self, "name", normalized)


class ScheduleRegistry:
    """Registry for schedule definitions."""

    __slots__ = ("_definitions",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._definitions: dict[str, ScheduleDefinition] = {}

    def register(
        self,
        schedule: ScheduleDefinition,
    ) -> None:
        """Register a schedule definition."""
        if schedule.name in self._definitions:
            raise DuplicateScheduleError(
                f"Schedule {schedule.name!r} is already registered."
            )

        self._definitions[schedule.name] = schedule

    def unregister(self, name: str) -> None:
        """Remove a schedule definition."""
        if name not in self._definitions:
            raise ScheduleNotFoundError(
                f"Schedule {name!r} is not registered."
            )

        del self._definitions[name]

    def get(self, name: str) -> ScheduleDefinition:
        """Return a registered schedule definition."""
        try:
            return self._definitions[name]
        except KeyError as exc:
            raise ScheduleNotFoundError(
                f"Schedule {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether a schedule exists."""
        return name in self._definitions

    def clear(self) -> None:
        """Remove all registered schedules."""
        self._definitions.clear()

    def list(self) -> tuple[ScheduleDefinition, ...]:
        """Return all registered schedules."""
        return tuple(self._definitions.values())

    def __len__(self) -> int:
        """Return the number of registered schedules."""
        return len(self._definitions)

    def __contains__(self, name: object) -> bool:
        """Return whether a schedule exists."""
        return (
            isinstance(name, str)
            and name in self._definitions
        )


def build_schedule(
    *,
    name: str,
    max_concurrency: int,
    scheduler: str = DEFAULT_SCHEDULER,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> ScheduleDefinition:
    """Build and validate a schedule definition."""

    return ScheduleDefinition(
        name=name,
        max_concurrency=max_concurrency,
        scheduler=scheduler,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "ScheduleDefinition",
    "ScheduleRegistry",
    "build_schedule",
]