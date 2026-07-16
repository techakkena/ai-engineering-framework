"""Tests for ai_optimization.routing.operations."""

from __future__ import annotations

import pytest

from ai_optimization.routing.constants import (
    DEFAULT_ENABLED,
    DEFAULT_ROUTING_STRATEGY,
)
from ai_optimization.routing.exceptions import (
    DuplicateRouteError,
    RouteNotFoundError,
    RouteValidationError,
    UnsupportedRoutingStrategyError,
)
from ai_optimization.routing.operations import (
    RouteDefinition,
    RouteRegistry,
    build_route,
)


def test_route_definition_defaults() -> None:
    route = RouteDefinition(
        name="default",
        weight=1,
    )

    assert route.name == "default"
    assert route.weight == 1
    assert route.strategy == DEFAULT_ROUTING_STRATEGY
    assert route.description == ""
    assert route.enabled is DEFAULT_ENABLED


def test_route_definition_trims_name() -> None:
    route = RouteDefinition(
        name="  default  ",
        weight=1,
    )

    assert route.name == "default"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_name(name: str) -> None:
    with pytest.raises(RouteValidationError):
        RouteDefinition(
            name=name,
            weight=1,
        )


@pytest.mark.parametrize(
    "weight",
    [
        0,
        -1,
        -10,
    ],
)
def test_invalid_weight(weight: int) -> None:
    with pytest.raises(RouteValidationError):
        RouteDefinition(
            name="default",
            weight=weight,
        )


def test_invalid_strategy() -> None:
    with pytest.raises(
        UnsupportedRoutingStrategyError,
    ):
        RouteDefinition(
            name="default",
            weight=1,
            strategy="invalid",
        )


def test_build_route() -> None:
    route = build_route(
        name="weighted",
        weight=5,
        strategy="weighted",
        description="Weighted route",
    )

    assert route.name == "weighted"
    assert route.weight == 5
    assert route.strategy == "weighted"
    assert route.description == "Weighted route"


def test_registry_register_and_get() -> None:
    registry = RouteRegistry()

    route = build_route(
        name="default",
        weight=1,
    )

    registry.register(route)

    assert registry.get("default") is route
    assert registry.exists("default")
    assert len(registry) == 1
    assert "default" in registry


def test_registry_duplicate_registration() -> None:
    registry = RouteRegistry()

    route = build_route(
        name="default",
        weight=1,
    )

    registry.register(route)

    with pytest.raises(DuplicateRouteError):
        registry.register(route)


def test_registry_unregister() -> None:
    registry = RouteRegistry()

    route = build_route(
        name="default",
        weight=1,
    )

    registry.register(route)
    registry.unregister("default")

    assert len(registry) == 0
    assert not registry.exists("default")


def test_registry_unregister_missing() -> None:
    registry = RouteRegistry()

    with pytest.raises(RouteNotFoundError):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = RouteRegistry()

    with pytest.raises(RouteNotFoundError):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = RouteRegistry()

    registry.register(
        build_route(
            name="one",
            weight=1,
        )
    )
    registry.register(
        build_route(
            name="two",
            weight=2,
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = RouteRegistry()

    first = build_route(
        name="one",
        weight=1,
    )
    second = build_route(
        name="two",
        weight=2,
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (first, second)


def test_registry_contains_unknown_type() -> None:
    registry = RouteRegistry()

    assert 123 not in registry