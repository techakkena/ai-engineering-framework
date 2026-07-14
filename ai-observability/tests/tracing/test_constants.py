from ai_observability.tracing.constants import (
    SpanStatus,
)


def test_status_values() -> None:
    assert SpanStatus.CREATED.value == "created"
    assert SpanStatus.COMPLETED.value == "completed"


def test_status_count() -> None:
    assert len(SpanStatus) == 4
