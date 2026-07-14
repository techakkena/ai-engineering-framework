from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .constants import DEFAULT_REPORT_NAME


@dataclass(slots=True)
class Report:
    """Represents an evaluation report."""

    name: str = DEFAULT_REPORT_NAME

    sections: dict[str, Any] = field(
        default_factory=dict,
    )

    def add_section(
        self,
        name: str,
        value: Any,
    ) -> None:
        """Add a report section."""
        self.sections[name] = value


class ReportRegistry:
    """Registry of reports."""

    def __init__(self) -> None:
        self._reports: dict[str, Report] = {}

    def register(
        self,
        report: Report,
    ) -> None:
        """Register a report."""
        self._reports[report.name] = report

    def get(
        self,
        name: str,
    ) -> Report | None:
        """Return a report."""
        return self._reports.get(name)

    @property
    def count(self) -> int:
        """Return number of reports."""
        return len(self._reports)
