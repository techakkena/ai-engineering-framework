import pytest

from ai_evals.reports.exceptions import (
    ReportError,
)


def test_report_error() -> None:
    with pytest.raises(ReportError):
        raise ReportError()
