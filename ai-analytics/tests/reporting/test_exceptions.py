"""Tests for ai_analytics.reporting.exceptions."""

from __future__ import annotations

import pytest

from ai_analytics.reporting.exceptions import (
    DuplicateReportError,
    ReportError,
    ReportNotFoundError,
    ReportRegistrationError,
    ReportValidationError,
    UnsupportedReportFormatError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(ReportValidationError, ReportError)
    assert issubclass(
        ReportRegistrationError,
        ReportError,
    )
    assert issubclass(
        ReportNotFoundError,
        ReportRegistrationError,
    )
    assert issubclass(
        DuplicateReportError,
        ReportRegistrationError,
    )
    assert issubclass(
        UnsupportedReportFormatError,
        ReportValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (ReportError, "base"),
        (ReportValidationError, "validation"),
        (ReportRegistrationError, "registration"),
        (ReportNotFoundError, "missing"),
        (DuplicateReportError, "duplicate"),
        (UnsupportedReportFormatError, "format"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)