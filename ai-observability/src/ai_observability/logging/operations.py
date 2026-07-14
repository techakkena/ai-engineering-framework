from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .constants import LogLevel


@dataclass(slots=True)
class LogEntry:
    """Represents a log entry."""

    level: LogLevel
    message: str
    attributes: dict[str, Any] = field(
        default_factory=dict,
    )


class MemoryLogger:
    """Simple in-memory logger."""

    def __init__(self) -> None:
        self._entries: list[LogEntry] = []

    def log(
        self,
        level: LogLevel,
        message: str,
        **attributes: Any,
    ) -> None:
        """Record a log entry."""

        self._entries.append(
            LogEntry(
                level=level,
                message=message,
                attributes=attributes,
            )
        )

    @property
    def entries(self) -> tuple[LogEntry, ...]:
        """Return recorded entries."""

        return tuple(self._entries)

    @property
    def count(self) -> int:
        """Return number of entries."""

        return len(self._entries)

    def clear(self) -> None:
        """Remove all log entries."""

        self._entries.clear()
