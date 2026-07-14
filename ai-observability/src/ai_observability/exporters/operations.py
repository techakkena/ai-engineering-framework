from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ExportRecord:
    """Represents an exported item."""

    name: str
    payload: dict[str, Any]


class MemoryExporter:
    """Simple in-memory exporter."""

    def __init__(self) -> None:
        self._records: list[ExportRecord] = []

    def export(
        self,
        record: ExportRecord,
    ) -> None:
        """Export a record."""
        self._records.append(record)

    @property
    def records(self) -> tuple[ExportRecord, ...]:
        """Return exported records."""
        return tuple(self._records)

    @property
    def count(self) -> int:
        """Return number of exported records."""
        return len(self._records)

    def clear(self) -> None:
        """Remove all exported records."""
        self._records.clear()
