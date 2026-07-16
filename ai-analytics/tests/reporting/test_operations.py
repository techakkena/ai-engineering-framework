"""Tests for ai_analytics.reporting.operations."""

from __future__ import annotations

import pytest

from ai_analytics.reporting.constants import (
    DEFAULT_ENABLED,
    DEFAULT_REPORT_FORMAT,
)
from ai_analytics.reporting.exceptions import (
    DuplicateReportError,
    ReportNotFoundError,
    ReportValidationError,
    UnsupportedReportFormatError,
)
from ai_analytics.reporting.operations import (
    ReportDefinition,
    ReportRegistry,
    build_report,
)


def test_report_definition_defaults() -> None:
    report = ReportDefinition(
        name="summary",
        title="Summary Report",
    )

    assert report.name == "summary"
    assert report.title == "Summary Report"
    assert report.report_format == DEFAULT_REPORT_FORMAT
    assert report.description == ""
    assert report.enabled is DEFAULT_ENABLED


def test_report_definition_trims_values() -> None:
    report = ReportDefinition(
        name="  summary  ",
        title="  Summary Report  ",
    )

    assert report.name == "summary"
    assert report.title == "Summary Report"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_name(name: str) -> None:
    with pytest.raises(ReportValidationError):
        ReportDefinition(
            name=name,
            title="Report",
        )


@pytest.mark.parametrize(
    "title",
    [
        "",
        "   ",
    ],
)
def test_invalid_title(title: str) -> None:
    with pytest.raises(ReportValidationError):
        ReportDefinition(
            name="summary",
            title=title,
        )


def test_invalid_report_format() -> None:
    with pytest.raises(
        UnsupportedReportFormatError,
    ):
        ReportDefinition(
            name="summary",
            title="Summary",
            report_format="xml",
        )


def test_build_report() -> None:
    report = build_report(
        name="sales",
        title="Sales Report",
        report_format="csv",
        description="Monthly sales report",
    )

    assert report.name == "sales"
    assert report.title == "Sales Report"
    assert report.report_format == "csv"
    assert report.description == "Monthly sales report"


def test_registry_register_and_get() -> None:
    registry = ReportRegistry()

    report = build_report(
        name="summary",
        title="Summary",
    )

    registry.register(report)

    assert registry.get("summary") is report
    assert registry.exists("summary")
    assert len(registry) == 1
    assert "summary" in registry


def test_registry_duplicate_registration() -> None:
    registry = ReportRegistry()

    report = build_report(
        name="summary",
        title="Summary",
    )

    registry.register(report)

    with pytest.raises(DuplicateReportError):
        registry.register(report)


def test_registry_unregister() -> None:
    registry = ReportRegistry()

    report = build_report(
        name="summary",
        title="Summary",
    )

    registry.register(report)
    registry.unregister("summary")

    assert len(registry) == 0
    assert not registry.exists("summary")


def test_registry_unregister_missing() -> None:
    registry = ReportRegistry()

    with pytest.raises(ReportNotFoundError):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = ReportRegistry()

    with pytest.raises(ReportNotFoundError):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = ReportRegistry()

    registry.register(
        build_report(
            name="one",
            title="One",
        )
    )
    registry.register(
        build_report(
            name="two",
            title="Two",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = ReportRegistry()

    first = build_report(
        name="one",
        title="One",
    )
    second = build_report(
        name="two",
        title="Two",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (first, second)


def test_registry_contains_unknown_type() -> None:
    registry = ReportRegistry()

    assert 123 not in registry