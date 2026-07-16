"""Tests for ai_analytics.events.operations."""

from __future__ import annotations

import pytest

from ai_analytics.events.constants import (
    DEFAULT_ENABLED,
    DEFAULT_EVENT_TYPE,
)
from ai_analytics.events.exceptions import (
    DuplicateEventError,
    EventNotFoundError,
    EventValidationError,
    UnsupportedEventTypeError,
)
from ai_analytics.events.operations import (
    EventDefinition,
    EventRegistry,
    build_event,
)


def test_event_definition_defaults() -> None:
    event = EventDefinition(name="login")

    assert event.name == "login"
    assert event.payload == {}
    assert event.event_type == DEFAULT_EVENT_TYPE
    assert event.description == ""
    assert event.tags == ()
    assert event.enabled is DEFAULT_ENABLED


def test_event_name_trimmed() -> None:
    event = EventDefinition(name="  login  ")

    assert event.name == "login"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_event_name(name: str) -> None:
    with pytest.raises(EventValidationError):
        EventDefinition(name=name)


def test_invalid_event_type() -> None:
    with pytest.raises(UnsupportedEventTypeError):
        EventDefinition(
            name="login",
            event_type="audit",
        )


def test_build_event() -> None:
    event = build_event(
        name="signup",
        payload={"user": "alice"},
        event_type="user",
        description="User registration",
        tags=("auth",),
    )

    assert event.name == "signup"
    assert event.payload == {"user": "alice"}
    assert event.event_type == "user"
    assert event.description == "User registration"
    assert event.tags == ("auth",)


def test_registry_register_and_get() -> None:
    registry = EventRegistry()

    event = build_event(name="login")

    registry.register(event)

    assert registry.get("login") is event
    assert registry.exists("login")
    assert len(registry) == 1
    assert "login" in registry


def test_registry_duplicate_registration() -> None:
    registry = EventRegistry()

    event = build_event(name="login")

    registry.register(event)

    with pytest.raises(DuplicateEventError):
        registry.register(event)


def test_registry_unregister() -> None:
    registry = EventRegistry()

    event = build_event(name="login")

    registry.register(event)
    registry.unregister("login")

    assert len(registry) == 0
    assert not registry.exists("login")


def test_registry_unregister_missing() -> None:
    registry = EventRegistry()

    with pytest.raises(EventNotFoundError):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = EventRegistry()

    with pytest.raises(EventNotFoundError):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = EventRegistry()

    registry.register(build_event(name="one"))
    registry.register(build_event(name="two"))

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = EventRegistry()

    first = build_event(name="one")
    second = build_event(name="two")

    registry.register(first)
    registry.register(second)

    assert registry.list() == (first, second)


def test_registry_contains_unknown_type() -> None:
    registry = EventRegistry()

    assert 123 not in registry