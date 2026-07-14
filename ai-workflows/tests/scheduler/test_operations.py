import pytest

from ai_workflows.scheduler.operations import (
    Schedule,
    Scheduler,
)


def test_create_schedule() -> None:
    schedule = Schedule(
        name="daily",
    )

    assert schedule.name == "daily"
    assert schedule.enabled


def test_add_schedule() -> None:
    scheduler = Scheduler()

    scheduler.add(
        Schedule(name="daily"),
    )

    assert scheduler.size == 1


def test_get_schedule() -> None:
    scheduler = Scheduler()

    scheduler.add(
        Schedule(name="daily"),
    )

    schedule = scheduler.get("daily")

    assert schedule.name == "daily"


def test_exists() -> None:
    scheduler = Scheduler()

    scheduler.add(
        Schedule(name="daily"),
    )

    assert scheduler.exists("daily")
    assert not scheduler.exists("weekly")


def test_remove_schedule() -> None:
    scheduler = Scheduler()

    scheduler.add(
        Schedule(name="daily"),
    )

    scheduler.remove("daily")

    assert scheduler.size == 0


def test_clear_scheduler() -> None:
    scheduler = Scheduler()

    scheduler.add(
        Schedule(name="a"),
    )

    scheduler.add(
        Schedule(name="b"),
    )

    scheduler.clear()

    assert scheduler.size == 0


def test_get_missing_schedule() -> None:
    scheduler = Scheduler()

    with pytest.raises(KeyError):
        scheduler.get("missing")
