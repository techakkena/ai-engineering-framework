from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Schedule:
    """Represents a workflow schedule."""

    name: str
    enabled: bool = True


class Scheduler:
    """Simple in-memory scheduler."""

    def __init__(self) -> None:
        self._schedules: dict[str, Schedule] = {}

    def add(
        self,
        schedule: Schedule,
    ) -> None:
        """Add a schedule."""
        self._schedules[schedule.name] = schedule

    def get(
        self,
        name: str,
    ) -> Schedule:
        """Return a schedule."""
        return self._schedules[name]

    def remove(
        self,
        name: str,
    ) -> None:
        """Remove a schedule."""
        del self._schedules[name]

    def exists(
        self,
        name: str,
    ) -> bool:
        """Return whether schedule exists."""
        return name in self._schedules

    def clear(self) -> None:
        """Remove every schedule."""
        self._schedules.clear()

    @property
    def size(self) -> int:
        """Return number of schedules."""
        return len(self._schedules)
