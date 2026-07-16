"""Tests for ai_analytics.tracking.operations."""

from __future__ import annotations

import pytest

from ai_analytics.tracking.constants import (
    DEFAULT_ENABLED,
    DEFAULT_TRACKING_TYPE,
)
from ai_analytics.tracking.exceptions import (
    DuplicateTrackingError,
    TrackingNotFoundError,
    TrackingValidationError,
    UnsupportedTrackingTypeError,
)
from ai_analytics.tracking.operations import (
    TrackingDefinition,
    TrackingRegistry,
    build_tracking,
)


def test_tracking_definition_defaults() -> None:
    tracking = TrackingDefinition(
        name="session",
        identifier="session-001",
    )

    assert tracking.name == "session"
    assert tracking.identifier == "session-001"
    assert tracking.tracking_type == DEFAULT_TRACKING_TYPE
    assert tracking.description == ""
    assert tracking.tags == ()
    assert tracking.enabled is DEFAULT_ENABLED


def test_tracking_definition_trims_values() -> None:
    tracking = TrackingDefinition(
        name="  session  ",
        identifier="  session-001  ",
    )

    assert tracking.name == "session"
    assert tracking.identifier == "session-001"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_tracking_name(name: str) -> None:
    with pytest.raises(TrackingValidationError):
        TrackingDefinition(
            name=name,
            identifier="id",
        )


@pytest.mark.parametrize(
    "identifier",
    [
        "",
        "   ",
    ],
)
def test_invalid_identifier(identifier: str) -> None:
    with pytest.raises(TrackingValidationError):
        TrackingDefinition(
            name="tracking",
            identifier=identifier,
        )


def test_invalid_tracking_type() -> None:
    with pytest.raises(UnsupportedTrackingTypeError):
        TrackingDefinition(
            name="tracking",
            identifier="id",
            tracking_type="invalid",
        )


def test_build_tracking() -> None:
    tracking = build_tracking(
        name="user",
        identifier="user-001",
        tracking_type="user",
        description="User tracking",
        tags=("analytics",),
    )

    assert tracking.name == "user"
    assert tracking.identifier == "user-001"
    assert tracking.tracking_type == "user"
    assert tracking.description == "User tracking"
    assert tracking.tags == ("analytics",)


def test_registry_register_and_get() -> None:
    registry = TrackingRegistry()

    tracking = build_tracking(
        name="session",
        identifier="session-001",
    )

    registry.register(tracking)

    assert registry.get("session") is tracking
    assert registry.exists("session")
    assert len(registry) == 1
    assert "session" in registry


def test_registry_duplicate_registration() -> None:
    registry = TrackingRegistry()

    tracking = build_tracking(
        name="session",
        identifier="session-001",
    )

    registry.register(tracking)

    with pytest.raises(DuplicateTrackingError):
        registry.register(tracking)


def test_registry_unregister() -> None:
    registry = TrackingRegistry()

    tracking = build_tracking(
        name="session",
        identifier="session-001",
    )

    registry.register(tracking)
    registry.unregister("session")

    assert len(registry) == 0
    assert not registry.exists("session")


def test_registry_unregister_missing() -> None:
    registry = TrackingRegistry()

    with pytest.raises(TrackingNotFoundError):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = TrackingRegistry()

    with pytest.raises(TrackingNotFoundError):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = TrackingRegistry()

    registry.register(
        build_tracking(
            name="one",
            identifier="1",
        )
    )
    registry.register(
        build_tracking(
            name="two",
            identifier="2",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = TrackingRegistry()

    first = build_tracking(
        name="one",
        identifier="1",
    )
    second = build_tracking(
        name="two",
        identifier="2",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (first, second)


def test_registry_contains_unknown_type() -> None:
    registry = TrackingRegistry()

    assert 123 not in registry