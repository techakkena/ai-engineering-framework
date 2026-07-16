"""Tests for ai_cloud.monitoring.operations."""

from __future__ import annotations

import pytest

from ai_cloud.monitoring.constants import (
    DEFAULT_ENABLED,
    DEFAULT_MONITOR_TYPE,
)
from ai_cloud.monitoring.exceptions import (
    DuplicateMonitoringError,
    MonitoringNotFoundError,
    MonitoringValidationError,
    UnsupportedMonitorTypeError,
)
from ai_cloud.monitoring.operations import (
    MonitoringDefinition,
    MonitoringRegistry,
    build_monitor,
)


def test_monitoring_definition_defaults() -> None:
    monitor = MonitoringDefinition(
        name="health-check",
        interval=60,
    )

    assert monitor.name == "health-check"
    assert monitor.interval == 60
    assert monitor.monitor_type == DEFAULT_MONITOR_TYPE
    assert monitor.description == ""
    assert monitor.enabled is DEFAULT_ENABLED


def test_monitoring_definition_trims_name() -> None:
    monitor = MonitoringDefinition(
        name="  health-check  ",
        interval=30,
    )

    assert monitor.name == "health-check"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_name(
    name: str,
) -> None:
    with pytest.raises(
        MonitoringValidationError,
    ):
        MonitoringDefinition(
            name=name,
            interval=60,
        )


@pytest.mark.parametrize(
    "interval",
    [
        0,
        -1,
        -60,
    ],
)
def test_invalid_interval(
    interval: int,
) -> None:
    with pytest.raises(
        MonitoringValidationError,
    ):
        MonitoringDefinition(
            name="health-check",
            interval=interval,
        )


def test_invalid_monitor_type() -> None:
    with pytest.raises(
        UnsupportedMonitorTypeError,
    ):
        MonitoringDefinition(
            name="health-check",
            interval=60,
            monitor_type="invalid",
        )


def test_build_monitor() -> None:
    monitor = build_monitor(
        name="metrics",
        interval=15,
        monitor_type="metrics",
        description="Metrics collector",
    )

    assert monitor.name == "metrics"
    assert monitor.interval == 15
    assert monitor.monitor_type == "metrics"
    assert monitor.description == "Metrics collector"


def test_registry_register_and_get() -> None:
    registry = MonitoringRegistry()

    monitor = build_monitor(
        name="metrics",
        interval=15,
    )

    registry.register(monitor)

    assert registry.get("metrics") is monitor
    assert registry.exists("metrics")
    assert len(registry) == 1
    assert "metrics" in registry


def test_registry_duplicate_registration() -> None:
    registry = MonitoringRegistry()

    monitor = build_monitor(
        name="metrics",
        interval=15,
    )

    registry.register(monitor)

    with pytest.raises(
        DuplicateMonitoringError,
    ):
        registry.register(monitor)


def test_registry_unregister() -> None:
    registry = MonitoringRegistry()

    monitor = build_monitor(
        name="metrics",
        interval=15,
    )

    registry.register(monitor)
    registry.unregister("metrics")

    assert len(registry) == 0
    assert not registry.exists("metrics")


def test_registry_unregister_missing() -> None:
    registry = MonitoringRegistry()

    with pytest.raises(
        MonitoringNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = MonitoringRegistry()

    with pytest.raises(
        MonitoringNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = MonitoringRegistry()

    registry.register(
        build_monitor(
            name="one",
            interval=10,
        )
    )
    registry.register(
        build_monitor(
            name="two",
            interval=20,
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = MonitoringRegistry()

    first = build_monitor(
        name="one",
        interval=10,
    )
    second = build_monitor(
        name="two",
        interval=20,
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = MonitoringRegistry()

    assert 123 not in registry