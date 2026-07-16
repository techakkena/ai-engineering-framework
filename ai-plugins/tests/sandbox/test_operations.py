"""Tests for ai_plugins.sandbox.operations."""

from __future__ import annotations

import pytest

from ai_plugins.sandbox.constants import (
    DEFAULT_ENABLED,
    DEFAULT_SANDBOX_MODE,
)
from ai_plugins.sandbox.exceptions import (
    DuplicateSandboxError,
    SandboxNotFoundError,
    SandboxValidationError,
    UnsupportedSandboxModeError,
)
from ai_plugins.sandbox.operations import (
    SandboxDefinition,
    SandboxRegistry,
    build_sandbox,
)


def test_sandbox_definition_defaults() -> None:
    sandbox = SandboxDefinition(
        name="default",
        memory_limit=512,
    )

    assert sandbox.name == "default"
    assert sandbox.memory_limit == 512
    assert sandbox.mode == DEFAULT_SANDBOX_MODE
    assert sandbox.description == ""
    assert sandbox.enabled is DEFAULT_ENABLED


def test_sandbox_definition_trims_name() -> None:
    sandbox = SandboxDefinition(
        name="  default  ",
        memory_limit=512,
    )

    assert sandbox.name == "default"


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
        SandboxValidationError,
    ):
        SandboxDefinition(
            name=name,
            memory_limit=512,
        )


@pytest.mark.parametrize(
    "memory_limit",
    [
        0,
        -1,
        -512,
    ],
)
def test_invalid_memory_limit(
    memory_limit: int,
) -> None:
    with pytest.raises(
        SandboxValidationError,
    ):
        SandboxDefinition(
            name="default",
            memory_limit=memory_limit,
        )


def test_invalid_mode() -> None:
    with pytest.raises(
        UnsupportedSandboxModeError,
    ):
        SandboxDefinition(
            name="default",
            memory_limit=512,
            mode="invalid",
        )


def test_build_sandbox() -> None:
    sandbox = build_sandbox(
        name="container",
        memory_limit=2048,
        mode="container",
        description="Container sandbox",
    )

    assert sandbox.name == "container"
    assert sandbox.memory_limit == 2048
    assert sandbox.mode == "container"
    assert sandbox.description == "Container sandbox"


def test_registry_register_and_get() -> None:
    registry = SandboxRegistry()

    sandbox = build_sandbox(
        name="default",
        memory_limit=512,
    )

    registry.register(sandbox)

    assert registry.get("default") is sandbox
    assert registry.exists("default")
    assert len(registry) == 1
    assert "default" in registry


def test_registry_duplicate_registration() -> None:
    registry = SandboxRegistry()

    sandbox = build_sandbox(
        name="default",
        memory_limit=512,
    )

    registry.register(sandbox)

    with pytest.raises(
        DuplicateSandboxError,
    ):
        registry.register(sandbox)


def test_registry_unregister() -> None:
    registry = SandboxRegistry()

    sandbox = build_sandbox(
        name="default",
        memory_limit=512,
    )

    registry.register(sandbox)
    registry.unregister("default")

    assert len(registry) == 0
    assert not registry.exists("default")


def test_registry_unregister_missing() -> None:
    registry = SandboxRegistry()

    with pytest.raises(
        SandboxNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = SandboxRegistry()

    with pytest.raises(
        SandboxNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = SandboxRegistry()

    registry.register(
        build_sandbox(
            name="one",
            memory_limit=256,
        )
    )
    registry.register(
        build_sandbox(
            name="two",
            memory_limit=512,
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = SandboxRegistry()

    first = build_sandbox(
        name="one",
        memory_limit=256,
    )
    second = build_sandbox(
        name="two",
        memory_limit=512,
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = SandboxRegistry()

    assert 123 not in registry