"""Tests for ai_optimization.batching.operations."""

from __future__ import annotations

import pytest

from ai_optimization.batching.constants import (
    DEFAULT_BATCH_STRATEGY,
    DEFAULT_ENABLED,
)
from ai_optimization.batching.exceptions import (
    BatchNotFoundError,
    BatchValidationError,
    DuplicateBatchError,
    UnsupportedBatchStrategyError,
)
from ai_optimization.batching.operations import (
    BatchDefinition,
    BatchRegistry,
    build_batch,
)


def test_batch_definition_defaults() -> None:
    batch = BatchDefinition(
        name="default",
        size=32,
    )

    assert batch.name == "default"
    assert batch.size == 32
    assert batch.strategy == DEFAULT_BATCH_STRATEGY
    assert batch.description == ""
    assert batch.enabled is DEFAULT_ENABLED


def test_batch_definition_trims_name() -> None:
    batch = BatchDefinition(
        name="  default  ",
        size=32,
    )

    assert batch.name == "default"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_name(name: str) -> None:
    with pytest.raises(BatchValidationError):
        BatchDefinition(
            name=name,
            size=32,
        )


@pytest.mark.parametrize(
    "size",
    [
        0,
        -1,
        -100,
    ],
)
def test_invalid_size(size: int) -> None:
    with pytest.raises(BatchValidationError):
        BatchDefinition(
            name="batch",
            size=size,
        )


def test_invalid_strategy() -> None:
    with pytest.raises(
        UnsupportedBatchStrategyError,
    ):
        BatchDefinition(
            name="batch",
            size=32,
            strategy="manual",
        )


def test_build_batch() -> None:
    batch = build_batch(
        name="dynamic",
        size=128,
        strategy="dynamic",
        description="Dynamic batching",
    )

    assert batch.name == "dynamic"
    assert batch.size == 128
    assert batch.strategy == "dynamic"
    assert batch.description == "Dynamic batching"


def test_registry_register_and_get() -> None:
    registry = BatchRegistry()

    batch = build_batch(
        name="default",
        size=32,
    )

    registry.register(batch)

    assert registry.get("default") is batch
    assert registry.exists("default")
    assert len(registry) == 1
    assert "default" in registry


def test_registry_duplicate_registration() -> None:
    registry = BatchRegistry()

    batch = build_batch(
        name="default",
        size=32,
    )

    registry.register(batch)

    with pytest.raises(DuplicateBatchError):
        registry.register(batch)


def test_registry_unregister() -> None:
    registry = BatchRegistry()

    batch = build_batch(
        name="default",
        size=32,
    )

    registry.register(batch)
    registry.unregister("default")

    assert len(registry) == 0
    assert not registry.exists("default")


def test_registry_unregister_missing() -> None:
    registry = BatchRegistry()

    with pytest.raises(BatchNotFoundError):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = BatchRegistry()

    with pytest.raises(BatchNotFoundError):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = BatchRegistry()

    registry.register(
        build_batch(
            name="one",
            size=1,
        )
    )
    registry.register(
        build_batch(
            name="two",
            size=2,
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = BatchRegistry()

    first = build_batch(
        name="one",
        size=1,
    )
    second = build_batch(
        name="two",
        size=2,
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (first, second)


def test_registry_contains_unknown_type() -> None:
    registry = BatchRegistry()

    assert 123 not in registry