from ai_observability.base.constants import (
    ObservationStatus,
)


def test_status_values() -> None:
    assert ObservationStatus.CREATED.value == "created"

    assert ObservationStatus.STARTED.value == "started"

    assert ObservationStatus.COMPLETED.value == "completed"

    assert ObservationStatus.FAILED.value == "failed"


def test_status_count() -> None:
    assert len(ObservationStatus) == 4
