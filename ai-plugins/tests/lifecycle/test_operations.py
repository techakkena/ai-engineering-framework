"""Tests for ai_plugins.lifecycle.operations."""

from __future__ import annotations

import pytest

from ai_plugins.lifecycle.constants import (
    DEFAULT_ENABLED,
    DEFAULT_PHASE,
)
from ai_plugins.lifecycle.exceptions import (
    DuplicateLifecycleError,
    LifecycleNotFoundError,
    LifecycleValidationError,
    UnsupportedLifecyclePhaseError,
)
from ai_plugins.lifecycle.operations import (
    LifecycleDefinition,
    LifecycleRegistry,
    build_lifecycle,
)


def test_lifecycle_definition_defaults() -> None:
    lifecycle = LifecycleDefinition(
        name="default",
        order=0,
    )

    assert lifecycle.name == "default"
    assert lifecycle.order == 0
    assert lifecycle.phase == DEFAULT_PHASE
    assert lifecycle.description == ""
    assert lifecycle.enabled is DEFAULT_ENABLED


def test_lifecycle_definition_trims_name() -> None:
    lifecycle = LifecycleDefinition(
        name="  default  ",
        order=1,
    )

    assert lifecycle.name == "default"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_name(name: str) -> None:
    with pytest.raises(LifecycleValidationError):
        LifecycleDefinition(
            name=name,
            order=0,
        )


@pytest.mark.parametrize(
    "order",
    [
        -1,
        -10,
    ],
)
def test_invalid_order(order: int) -> None:
    with pytest.raises(LifecycleValidationError):
        LifecycleDefinition(
            name="default",
            order=order,
        )


def test_invalid_phase() -> None:
    with pytest.raises(
        UnsupportedLifecyclePhaseError,
    ):
        LifecycleDefinition(
            name="default",
            order=0,
            phase="restart",
        )


def test_build_lifecycle() -> None:
    lifecycle = build_lifecycle(
        name="startup",
        order=1,
        phase="start",
        description="Startup phase",
    )

    assert lifecycle.name == "startup"
    assert lifecycle.order == 1
    assert lifecycle.phase == "start"
    assert lifecycle.description == "Startup phase"


def test_registry_register_and_get() -> None:
    registry = LifecycleRegistry()

    lifecycle = build_lifecycle(
        name="default",
        order=0,
    )

    registry.register(lifecycle)

    assert registry.get("default") is lifecycle
    assert registry.exists("default")
    assert len(registry) == 1
    assert "default" in registry


def test_registry_duplicate_registration() -> None:
    registry = LifecycleRegistry()

    lifecycle = build_lifecycle(
        name="default",
        order=0,
    )

    registry.register(lifecycle)

    with pytest.raises(
        DuplicateLifecycleError,
    ):
        registry.register(lifecycle)


def test_registry_unregister() -> None:
    registry = LifecycleRegistry()

    lifecycle = build_lifecycle(
        name="default",
        order=0,
    )

    registry.register(lifecycle)
    registry.unregister("default")

    assert len(registry) == 0
    assert not registry.exists("default")


def test_registry_unregister_missing() -> None:
    registry = LifecycleRegistry()

    with pytest.raises(
        LifecycleNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = LifecycleRegistry()

    with pytest.raises(
        LifecycleNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = LifecycleRegistry()

    registry.register(
        build_lifecycle(
            name="one",
            order=1,
        )
    )
    registry.register(
        build_lifecycle(
            name="two",
            order=2,
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = LifecycleRegistry()

    first = build_lifecycle(
        name="one",
        order=1,
    )
    second = build_lifecycle(
        name="two",
        order=2,
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = LifecycleRegistry()

    assert 123 not in registry