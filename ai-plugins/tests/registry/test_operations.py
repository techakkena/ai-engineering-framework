"""Tests for ai_plugins.registry.operations."""

from __future__ import annotations

import pytest

from ai_plugins.registry.constants import (
    DEFAULT_ENABLED,
    DEFAULT_PLUGIN_VERSION,
    REGISTERED_STATE,
)
from ai_plugins.registry.exceptions import (
    DuplicatePluginError,
    PluginNotFoundError,
    PluginValidationError,
    UnsupportedPluginStateError,
)
from ai_plugins.registry.operations import (
    PluginDefinition,
    PluginRegistry,
    build_plugin,
)


def test_plugin_definition_defaults() -> None:
    plugin = PluginDefinition(
        name="sample-plugin",
    )

    assert plugin.name == "sample-plugin"
    assert plugin.version == DEFAULT_PLUGIN_VERSION
    assert plugin.state == REGISTERED_STATE
    assert plugin.description == ""
    assert plugin.enabled is DEFAULT_ENABLED


def test_plugin_definition_trims_values() -> None:
    plugin = PluginDefinition(
        name="  sample-plugin  ",
        version=" 2.0.0 ",
    )

    assert plugin.name == "sample-plugin"
    assert plugin.version == "2.0.0"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_plugin_name(
    name: str,
) -> None:
    with pytest.raises(
        PluginValidationError,
    ):
        PluginDefinition(name=name)


@pytest.mark.parametrize(
    "version",
    [
        "",
        "   ",
    ],
)
def test_invalid_plugin_version(
    version: str,
) -> None:
    with pytest.raises(
        PluginValidationError,
    ):
        PluginDefinition(
            name="plugin",
            version=version,
        )


def test_invalid_plugin_state() -> None:
    with pytest.raises(
        UnsupportedPluginStateError,
    ):
        PluginDefinition(
            name="plugin",
            state="invalid",
        )


def test_build_plugin() -> None:
    plugin = build_plugin(
        name="analytics",
        version="2.1.0",
        state="loaded",
        description="Analytics plugin",
    )

    assert plugin.name == "analytics"
    assert plugin.version == "2.1.0"
    assert plugin.state == "loaded"
    assert plugin.description == "Analytics plugin"


def test_registry_register_and_get() -> None:
    registry = PluginRegistry()

    plugin = build_plugin(name="sample")

    registry.register(plugin)

    assert registry.get("sample") is plugin
    assert registry.exists("sample")
    assert len(registry) == 1
    assert "sample" in registry


def test_registry_duplicate_registration() -> None:
    registry = PluginRegistry()

    plugin = build_plugin(name="sample")

    registry.register(plugin)

    with pytest.raises(
        DuplicatePluginError,
    ):
        registry.register(plugin)


def test_registry_unregister() -> None:
    registry = PluginRegistry()

    plugin = build_plugin(name="sample")

    registry.register(plugin)
    registry.unregister("sample")

    assert len(registry) == 0
    assert not registry.exists("sample")


def test_registry_unregister_missing() -> None:
    registry = PluginRegistry()

    with pytest.raises(
        PluginNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = PluginRegistry()

    with pytest.raises(
        PluginNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = PluginRegistry()

    registry.register(build_plugin(name="one"))
    registry.register(build_plugin(name="two"))

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = PluginRegistry()

    first = build_plugin(name="one")
    second = build_plugin(name="two")

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = PluginRegistry()

    assert 123 not in registry