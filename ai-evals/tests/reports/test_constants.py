from ai_evals.reports.constants import (
    DEFAULT_REPORT_NAME,
)


def test_default_report_name() -> None:
    assert DEFAULT_REPORT_NAME == "evaluation-report"
