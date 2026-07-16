"""Tests for ai_plugins.discovery.operations."""

from __future__ import annotations

import pytest

from ai_plugins.discovery.constants import (
    DEFAULT_DISCOVERY_STRATEGY,
    DEFAULT_ENABLED,
)
from ai_plugins.discovery.exceptions import (
    DiscoveryNotFoundError,
    DiscoveryValidationError,
    DuplicateDiscoveryError,
    UnsupportedDiscoveryStrategyError,
)
from ai_plugins.discovery.operations import (
    DiscoveryDefinition,
    DiscoveryRegistry,
    build_discovery,
)


def test_discovery_definition_defaults() -> None:
    discovery = DiscoveryDefinition(
        name="plugins",
        path="./plugins",
    )

    assert discovery.name == "plugins"
    assert discovery.path == "./plugins"
    assert discovery.strategy == DEFAULT_DISCOVERY_STRATEGY
    assert discovery.description == ""
    assert discovery.enabled is DEFAULT_ENABLED


def test_discovery_definition_trims_values() -> None:
    discovery = DiscoveryDefinition(
        name="  plugins  ",
        path="  ./plugins  ",
    )

    assert discovery.name == "plugins"
    assert discovery.path == "./plugins"


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
        DiscoveryValidationError,
    ):
        DiscoveryDefinition(
            name=name,
            path="./plugins",
        )


@pytest.mark.parametrize(
    "path",
    [
        "",
        "   ",
    ],
)
def test_invalid_path(path: str) -> None:
    with pytest.raises(
        DiscoveryValidationError,
    ):
        DiscoveryDefinition(
            name="plugins",
            path=path,
        )


def test_invalid_strategy() -> None:
    with pytest.raises(
        UnsupportedDiscoveryStrategyError,
    ):
        DiscoveryDefinition(
            name="plugins",
            path="./plugins",
            strategy="network",
        )


def test_build_discovery() -> None:
    discovery = build_discovery(
        name="entrypoints",
        path="pkg.plugins",
        strategy="entry_points",
        description="Entry point discovery",
    )

    assert discovery.name == "entrypoints"
    assert discovery.path == "pkg.plugins"
    assert discovery.strategy == "entry_points"
    assert discovery.description == "Entry point discovery"


def test_registry_register_and_get() -> None:
    registry = DiscoveryRegistry()

    discovery = build_discovery(
        name="plugins",
        path="./plugins",
    )

    registry.register(discovery)

    assert registry.get("plugins") is discovery
    assert registry.exists("plugins")
    assert len(registry) == 1
    assert "plugins" in registry


def test_registry_duplicate_registration() -> None:
    registry = DiscoveryRegistry()

    discovery = build_discovery(
        name="plugins",
        path="./plugins",
    )

    registry.register(discovery)

    with pytest.raises(
        DuplicateDiscoveryError,
    ):
        registry.register(discovery)


def test_registry_unregister() -> None:
    registry = DiscoveryRegistry()

    discovery = build_discovery(
        name="plugins",
        path="./plugins",
    )

    registry.register(discovery)
    registry.unregister("plugins")

    assert len(registry) == 0
    assert not registry.exists("plugins")


def test_registry_unregister_missing() -> None:
    registry = DiscoveryRegistry()

    with pytest.raises(
        DiscoveryNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = DiscoveryRegistry()

    with pytest.raises(
        DiscoveryNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = DiscoveryRegistry()

    registry.register(
        build_discovery(
            name="one",
            path="./one",
        )
    )
    registry.register(
        build_discovery(
            name="two",
            path="./two",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = DiscoveryRegistry()

    first = build_discovery(
        name="one",
        path="./one",
    )
    second = build_discovery(
        name="two",
        path="./two",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = DiscoveryRegistry()

    assert 123 not in registry