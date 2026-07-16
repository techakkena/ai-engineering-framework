"""Tests for ai_optimization.scheduling.operations."""

from __future__ import annotations

import pytest

from ai_optimization.scheduling.constants import (
    DEFAULT_ENABLED,
    DEFAULT_SCHEDULER,
)
from ai_optimization.scheduling.exceptions import (
    DuplicateScheduleError,
    ScheduleNotFoundError,
    ScheduleValidationError,
    UnsupportedSchedulerError,
)
from ai_optimization.scheduling.operations import (
    ScheduleDefinition,
    ScheduleRegistry,
    build_schedule,
)


def test_schedule_definition_defaults() -> None:
    schedule = ScheduleDefinition(
        name="default",
        max_concurrency=4,
    )

    assert schedule.name == "default"
    assert schedule.max_concurrency == 4
    assert schedule.scheduler == DEFAULT_SCHEDULER
    assert schedule.description == ""
    assert schedule.enabled is DEFAULT_ENABLED


def test_schedule_definition_trims_name() -> None:
    schedule = ScheduleDefinition(
        name="  default  ",
        max_concurrency=4,
    )

    assert schedule.name == "default"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_name(name: str) -> None:
    with pytest.raises(
        ScheduleValidationError,
    ):
        ScheduleDefinition(
            name=name,
            max_concurrency=4,
        )


@pytest.mark.parametrize(
    "max_concurrency",
    [
        0,
        -1,
        -10,
    ],
)
def test_invalid_max_concurrency(
    max_concurrency: int,
) -> None:
    with pytest.raises(
        ScheduleValidationError,
    ):
        ScheduleDefinition(
            name="default",
            max_concurrency=max_concurrency,
        )


def test_invalid_scheduler() -> None:
    with pytest.raises(
        UnsupportedSchedulerError,
    ):
        ScheduleDefinition(
            name="default",
            max_concurrency=4,
            scheduler="random",
        )


def test_build_schedule() -> None:
    schedule = build_schedule(
        name="priority",
        max_concurrency=8,
        scheduler="priority",
        description="Priority scheduler",
    )

    assert schedule.name == "priority"
    assert schedule.max_concurrency == 8
    assert schedule.scheduler == "priority"
    assert schedule.description == "Priority scheduler"


def test_registry_register_and_get() -> None:
    registry = ScheduleRegistry()

    schedule = build_schedule(
        name="default",
        max_concurrency=4,
    )

    registry.register(schedule)

    assert registry.get("default") is schedule
    assert registry.exists("default")
    assert len(registry) == 1
    assert "default" in registry


def test_registry_duplicate_registration() -> None:
    registry = ScheduleRegistry()

    schedule = build_schedule(
        name="default",
        max_concurrency=4,
    )

    registry.register(schedule)

    with pytest.raises(
        DuplicateScheduleError,
    ):
        registry.register(schedule)


def test_registry_unregister() -> None:
    registry = ScheduleRegistry()

    schedule = build_schedule(
        name="default",
        max_concurrency=4,
    )

    registry.register(schedule)
    registry.unregister("default")

    assert len(registry) == 0
    assert not registry.exists("default")


def test_registry_unregister_missing() -> None:
    registry = ScheduleRegistry()

    with pytest.raises(
        ScheduleNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = ScheduleRegistry()

    with pytest.raises(
        ScheduleNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = ScheduleRegistry()

    registry.register(
        build_schedule(
            name="one",
            max_concurrency=1,
        )
    )
    registry.register(
        build_schedule(
            name="two",
            max_concurrency=2,
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = ScheduleRegistry()

    first = build_schedule(
        name="one",
        max_concurrency=1,
    )
    second = build_schedule(
        name="two",
        max_concurrency=2,
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (first, second)


def test_registry_contains_unknown_type() -> None:
    registry = ScheduleRegistry()

    assert 123 not in registry