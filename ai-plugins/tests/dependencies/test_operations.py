"""Tests for ai_plugins.dependencies.operations."""

from __future__ import annotations

import pytest

from ai_plugins.dependencies.constants import (
    DEFAULT_DEPENDENCY_TYPE,
    DEFAULT_ENABLED,
)
from ai_plugins.dependencies.exceptions import (
    DependencyNotFoundError,
    DependencyValidationError,
    DuplicateDependencyError,
    UnsupportedDependencyTypeError,
)
from ai_plugins.dependencies.operations import (
    DependencyDefinition,
    DependencyRegistry,
    build_dependency,
)


def test_dependency_definition_defaults() -> None:
    dependency = DependencyDefinition(
        name="requests",
        version="2.32.0",
    )

    assert dependency.name == "requests"
    assert dependency.version == "2.32.0"
    assert (
        dependency.dependency_type
        == DEFAULT_DEPENDENCY_TYPE
    )
    assert dependency.description == ""
    assert dependency.enabled is DEFAULT_ENABLED


def test_dependency_definition_trims_values() -> None:
    dependency = DependencyDefinition(
        name="  requests  ",
        version=" 2.32.0 ",
    )

    assert dependency.name == "requests"
    assert dependency.version == "2.32.0"


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
        DependencyValidationError,
    ):
        DependencyDefinition(
            name=name,
            version="1.0.0",
        )


@pytest.mark.parametrize(
    "version",
    [
        "",
        "   ",
    ],
)
def test_invalid_version(version: str) -> None:
    with pytest.raises(
        DependencyValidationError,
    ):
        DependencyDefinition(
            name="requests",
            version=version,
        )


def test_invalid_dependency_type() -> None:
    with pytest.raises(
        UnsupportedDependencyTypeError,
    ):
        DependencyDefinition(
            name="requests",
            version="1.0.0",
            dependency_type="invalid",
        )


def test_build_dependency() -> None:
    dependency = build_dependency(
        name="numpy",
        version="2.0.0",
        dependency_type="runtime",
        description="Runtime dependency",
    )

    assert dependency.name == "numpy"
    assert dependency.version == "2.0.0"
    assert dependency.dependency_type == "runtime"
    assert (
        dependency.description
        == "Runtime dependency"
    )


def test_registry_register_and_get() -> None:
    registry = DependencyRegistry()

    dependency = build_dependency(
        name="numpy",
        version="2.0.0",
    )

    registry.register(dependency)

    assert registry.get("numpy") is dependency
    assert registry.exists("numpy")
    assert len(registry) == 1
    assert "numpy" in registry


def test_registry_duplicate_registration() -> None:
    registry = DependencyRegistry()

    dependency = build_dependency(
        name="numpy",
        version="2.0.0",
    )

    registry.register(dependency)

    with pytest.raises(
        DuplicateDependencyError,
    ):
        registry.register(dependency)


def test_registry_unregister() -> None:
    registry = DependencyRegistry()

    dependency = build_dependency(
        name="numpy",
        version="2.0.0",
    )

    registry.register(dependency)
    registry.unregister("numpy")

    assert len(registry) == 0
    assert not registry.exists("numpy")


def test_registry_unregister_missing() -> None:
    registry = DependencyRegistry()

    with pytest.raises(
        DependencyNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = DependencyRegistry()

    with pytest.raises(
        DependencyNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = DependencyRegistry()

    registry.register(
        build_dependency(
            name="one",
            version="1.0.0",
        )
    )
    registry.register(
        build_dependency(
            name="two",
            version="2.0.0",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = DependencyRegistry()

    first = build_dependency(
        name="one",
        version="1.0.0",
    )
    second = build_dependency(
        name="two",
        version="2.0.0",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = DependencyRegistry()

    assert 123 not in registry