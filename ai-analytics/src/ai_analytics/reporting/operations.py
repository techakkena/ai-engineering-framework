"""Operations for the ai_analytics.reporting module."""

from __future__ import annotations

from dataclasses import dataclass

from ai_analytics.reporting.constants import (
    DEFAULT_ENABLED,
    DEFAULT_REPORT_FORMAT,
    MAX_REPORT_NAME_LENGTH,
    MIN_REPORT_NAME_LENGTH,
    SUPPORTED_REPORT_FORMATS,
)
from ai_analytics.reporting.exceptions import (
    DuplicateReportError,
    ReportNotFoundError,
    ReportValidationError,
    UnsupportedReportFormatError,
)


@dataclass(slots=True, frozen=True)
class ReportDefinition:
    """Represents a report definition."""

    name: str
    title: str
    report_format: str = DEFAULT_REPORT_FORMAT
    description: str = ""
    enabled: bool = DEFAULT_ENABLED

    def __post_init__(self) -> None:
        """Validate the report definition."""
        normalized = self.name.strip()

        if not (
            MIN_REPORT_NAME_LENGTH
            <= len(normalized)
            <= MAX_REPORT_NAME_LENGTH
        ):
            raise ReportValidationError(
                "Report name length is outside the allowed range."
            )

        if not self.title.strip():
            raise ReportValidationError(
                "Report title cannot be empty."
            )

        if self.report_format not in SUPPORTED_REPORT_FORMATS:
            raise UnsupportedReportFormatError(
                f"Unsupported report format: {self.report_format!r}."
            )

        object.__setattr__(self, "name", normalized)
        object.__setattr__(self, "title", self.title.strip())


class ReportRegistry:
    """Registry for report definitions."""

    __slots__ = ("_reports",)

    def __init__(self) -> None:
        """Initialize an empty registry."""
        self._reports: dict[str, ReportDefinition] = {}

    def register(self, report: ReportDefinition) -> None:
        """Register a report."""
        if report.name in self._reports:
            raise DuplicateReportError(
                f"Report {report.name!r} is already registered."
            )

        self._reports[report.name] = report

    def unregister(self, name: str) -> None:
        """Remove a report."""
        if name not in self._reports:
            raise ReportNotFoundError(
                f"Report {name!r} is not registered."
            )

        del self._reports[name]

    def get(self, name: str) -> ReportDefinition:
        """Return a registered report."""
        try:
            return self._reports[name]
        except KeyError as exc:
            raise ReportNotFoundError(
                f"Report {name!r} is not registered."
            ) from exc

    def exists(self, name: str) -> bool:
        """Return whether a report exists."""
        return name in self._reports

    def clear(self) -> None:
        """Remove all reports."""
        self._reports.clear()

    def list(self) -> tuple[ReportDefinition, ...]:
        """Return all registered reports."""
        return tuple(self._reports.values())

    def __len__(self) -> int:
        """Return registry size."""
        return len(self._reports)

    def __contains__(self, name: object) -> bool:
        """Return whether a report exists."""
        return isinstance(name, str) and name in self._reports


def build_report(
    *,
    name: str,
    title: str,
    report_format: str = DEFAULT_REPORT_FORMAT,
    description: str = "",
    enabled: bool = DEFAULT_ENABLED,
) -> ReportDefinition:
    """Build a validated report."""

    return ReportDefinition(
        name=name,
        title=title,
        report_format=report_format,
        description=description,
        enabled=enabled,
    )


__all__ = [
    "ReportDefinition",
    "ReportRegistry",
    "build_report",
]