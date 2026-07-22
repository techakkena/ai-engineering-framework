"""
Unit tests for ai_monitoring.reporting.operations.
"""

from __future__ import annotations

import pytest

from ai_monitoring.reporting.constants import SUMMARY
from ai_monitoring.reporting.exceptions import (
    ReportValidationError,
)
from ai_monitoring.reporting.operations import (
    ReportResult,
    create_report,
    delete_report,
    export_report,
    get_report,
    list_reports,
)


def test_create_report_success() -> None:
    """Creating a report should succeed."""
    result = create_report("daily-monitoring")

    assert isinstance(result, ReportResult)
    assert result.success is True
    assert result.task == "create_report"
    assert result.data["type"] == SUMMARY


def test_create_report_empty_name() -> None:
    """Empty report names should raise."""
    with pytest.raises(ReportValidationError):
        create_report("")


def test_export_report_success() -> None:
    """Exporting a report should succeed."""
    result = export_report("daily-monitoring")

    assert result.success is True
    assert result.task == "export_report"


def test_get_report_success() -> None:
    """Getting a report should succeed."""
    result = get_report("daily-monitoring")

    assert result.success is True
    assert result.task == "get_report"


def test_delete_report_success() -> None:
    """Deleting a report should succeed."""
    result = delete_report("daily-monitoring")

    assert result.success is True
    assert result.task == "delete_report"


def test_list_reports_success() -> None:
    """Listing reports should succeed."""
    result = list_reports()

    assert result.success is True
    assert result.task == "list_reports"
    assert isinstance(result.data["reports"], list)


@pytest.mark.parametrize(
    "operation",
    [
        export_report,
        get_report,
        delete_report,
    ],
)
def test_name_validation(
    operation,
) -> None:
    """Operations requiring a report name should reject empty values."""
    with pytest.raises(ReportValidationError):
        operation("")