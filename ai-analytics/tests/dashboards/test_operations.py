"""Tests for ai_analytics.dashboards.operations."""

from __future__ import annotations

import pytest

from ai_analytics.dashboards.constants import (
    DEFAULT_ENABLED,
    DEFAULT_LAYOUT,
)
from ai_analytics.dashboards.exceptions import (
    DashboardNotFoundError,
    DashboardValidationError,
    DuplicateDashboardError,
    UnsupportedLayoutError,
)
from ai_analytics.dashboards.operations import (
    DashboardDefinition,
    DashboardRegistry,
    build_dashboard,
)


def test_dashboard_definition_defaults() -> None:
    dashboard = DashboardDefinition(
        name="overview",
        title="Overview",
    )

    assert dashboard.name == "overview"
    assert dashboard.title == "Overview"
    assert dashboard.layout == DEFAULT_LAYOUT
    assert dashboard.description == ""
    assert dashboard.enabled is DEFAULT_ENABLED


def test_dashboard_definition_trims_values() -> None:
    dashboard = DashboardDefinition(
        name="  overview  ",
        title="  Overview  ",
    )

    assert dashboard.name == "overview"
    assert dashboard.title == "Overview"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_name(name: str) -> None:
    with pytest.raises(DashboardValidationError):
        DashboardDefinition(
            name=name,
            title="Overview",
        )


@pytest.mark.parametrize(
    "title",
    [
        "",
        "   ",
    ],
)
def test_invalid_title(title: str) -> None:
    with pytest.raises(DashboardValidationError):
        DashboardDefinition(
            name="overview",
            title=title,
        )


def test_invalid_layout() -> None:
    with pytest.raises(
        UnsupportedLayoutError,
    ):
        DashboardDefinition(
            name="overview",
            title="Overview",
            layout="invalid",
        )


def test_build_dashboard() -> None:
    dashboard = build_dashboard(
        name="executive",
        title="Executive Dashboard",
        layout="tabs",
        description="Executive metrics",
    )

    assert dashboard.name == "executive"
    assert dashboard.title == "Executive Dashboard"
    assert dashboard.layout == "tabs"
    assert dashboard.description == "Executive metrics"


def test_registry_register_and_get() -> None:
    registry = DashboardRegistry()

    dashboard = build_dashboard(
        name="overview",
        title="Overview",
    )

    registry.register(dashboard)

    assert registry.get("overview") is dashboard
    assert registry.exists("overview")
    assert len(registry) == 1
    assert "overview" in registry


def test_registry_duplicate_registration() -> None:
    registry = DashboardRegistry()

    dashboard = build_dashboard(
        name="overview",
        title="Overview",
    )

    registry.register(dashboard)

    with pytest.raises(DuplicateDashboardError):
        registry.register(dashboard)


def test_registry_unregister() -> None:
    registry = DashboardRegistry()

    dashboard = build_dashboard(
        name="overview",
        title="Overview",
    )

    registry.register(dashboard)
    registry.unregister("overview")

    assert len(registry) == 0
    assert not registry.exists("overview")


def test_registry_unregister_missing() -> None:
    registry = DashboardRegistry()

    with pytest.raises(DashboardNotFoundError):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = DashboardRegistry()

    with pytest.raises(DashboardNotFoundError):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = DashboardRegistry()

    registry.register(
        build_dashboard(
            name="one",
            title="One",
        )
    )
    registry.register(
        build_dashboard(
            name="two",
            title="Two",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = DashboardRegistry()

    first = build_dashboard(
        name="one",
        title="One",
    )
    second = build_dashboard(
        name="two",
        title="Two",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (first, second)


def test_registry_contains_unknown_type() -> None:
    registry = DashboardRegistry()

    assert 123 not in registry