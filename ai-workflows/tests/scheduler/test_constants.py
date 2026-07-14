from ai_workflows.scheduler.constants import (
    DEFAULT_SCHEDULE_NAME,
    DEFAULT_SCHEDULER_NAME,
)


def test_scheduler_name() -> None:
    assert DEFAULT_SCHEDULER_NAME == "scheduler"


def test_schedule_name() -> None:
    assert DEFAULT_SCHEDULE_NAME == "default"
