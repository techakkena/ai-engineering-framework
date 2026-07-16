"""Tests for ai_plugins.loading.operations."""

from __future__ import annotations

import pytest

from ai_plugins.loading.constants import (
    DEFAULT_ENABLED,
    DEFAULT_LOADING_MODE,
)
from ai_plugins.loading.exceptions import (
    DuplicateLoaderError,
    LoaderNotFoundError,
    LoaderValidationError,
    UnsupportedLoadingModeError,
)
from ai_plugins.loading.operations import (
    LoaderDefinition,
    LoaderRegistry,
    build_loader,
)


def test_loader_definition_defaults() -> None:
    loader = LoaderDefinition(
        name="default",
        timeout=30.0,
    )

    assert loader.name == "default"
    assert loader.timeout == 30.0
    assert loader.mode == DEFAULT_LOADING_MODE
    assert loader.description == ""
    assert loader.enabled is DEFAULT_ENABLED


def test_loader_definition_trims_name() -> None:
    loader = LoaderDefinition(
        name="  default  ",
        timeout=30.0,
    )

    assert loader.name == "default"


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
        LoaderValidationError,
    ):
        LoaderDefinition(
            name=name,
            timeout=30.0,
        )


@pytest.mark.parametrize(
    "timeout",
    [
        0.0,
        -1.0,
        -10.0,
    ],
)
def test_invalid_timeout(
    timeout: float,
) -> None:
    with pytest.raises(
        LoaderValidationError,
    ):
        LoaderDefinition(
            name="default",
            timeout=timeout,
        )


def test_invalid_loading_mode() -> None:
    with pytest.raises(
        UnsupportedLoadingModeError,
    ):
        LoaderDefinition(
            name="default",
            timeout=30.0,
            mode="invalid",
        )


def test_build_loader() -> None:
    loader = build_loader(
        name="fast-loader",
        timeout=10.0,
        mode="eager",
        description="Eager loader",
    )

    assert loader.name == "fast-loader"
    assert loader.timeout == 10.0
    assert loader.mode == "eager"
    assert loader.description == "Eager loader"


def test_registry_register_and_get() -> None:
    registry = LoaderRegistry()

    loader = build_loader(
        name="default",
        timeout=30.0,
    )

    registry.register(loader)

    assert registry.get("default") is loader
    assert registry.exists("default")
    assert len(registry) == 1
    assert "default" in registry


def test_registry_duplicate_registration() -> None:
    registry = LoaderRegistry()

    loader = build_loader(
        name="default",
        timeout=30.0,
    )

    registry.register(loader)

    with pytest.raises(
        DuplicateLoaderError,
    ):
        registry.register(loader)


def test_registry_unregister() -> None:
    registry = LoaderRegistry()

    loader = build_loader(
        name="default",
        timeout=30.0,
    )

    registry.register(loader)
    registry.unregister("default")

    assert len(registry) == 0
    assert not registry.exists("default")


def test_registry_unregister_missing() -> None:
    registry = LoaderRegistry()

    with pytest.raises(
        LoaderNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = LoaderRegistry()

    with pytest.raises(
        LoaderNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = LoaderRegistry()

    registry.register(
        build_loader(
            name="one",
            timeout=5.0,
        )
    )
    registry.register(
        build_loader(
            name="two",
            timeout=10.0,
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = LoaderRegistry()

    first = build_loader(
        name="one",
        timeout=5.0,
    )
    second = build_loader(
        name="two",
        timeout=10.0,
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = LoaderRegistry()

    assert 123 not in registry