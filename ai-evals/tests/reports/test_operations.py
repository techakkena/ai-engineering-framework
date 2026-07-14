from ai_evals.reports.operations import (
    Report,
    ReportRegistry,
)


def test_report_defaults() -> None:
    report = Report()

    assert report.name == "evaluation-report"
    assert report.sections == {}


def test_add_section() -> None:
    report = Report()

    report.add_section(
        "accuracy",
        0.95,
    )

    assert report.sections["accuracy"] == 0.95


def test_registry() -> None:
    registry = ReportRegistry()

    report = Report(
        name="rag-report",
    )

    registry.register(report)

    assert registry.count == 1
    assert registry.get("rag-report") is report


def test_missing_report() -> None:
    registry = ReportRegistry()

    assert registry.get("missing") is None
