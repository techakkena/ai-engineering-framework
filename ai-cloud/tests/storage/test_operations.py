"""Tests for ai_cloud.storage.operations."""

from __future__ import annotations

import pytest

from ai_cloud.storage.constants import (
    DEFAULT_ENABLED,
    DEFAULT_STORAGE_TYPE,
)
from ai_cloud.storage.exceptions import (
    DuplicateStorageError,
    StorageNotFoundError,
    StorageValidationError,
    UnsupportedStorageTypeError,
)
from ai_cloud.storage.operations import (
    StorageDefinition,
    StorageRegistry,
    build_storage,
)


def test_storage_definition_defaults() -> None:
    storage = StorageDefinition(
        name="primary",
        capacity=1024,
    )

    assert storage.name == "primary"
    assert storage.capacity == 1024
    assert storage.storage_type == DEFAULT_STORAGE_TYPE
    assert storage.description == ""
    assert storage.enabled is DEFAULT_ENABLED


def test_storage_definition_trims_name() -> None:
    storage = StorageDefinition(
        name="  primary  ",
        capacity=1024,
    )

    assert storage.name == "primary"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_name(
    name: str,
) -> None:
    with pytest.raises(
        StorageValidationError,
    ):
        StorageDefinition(
            name=name,
            capacity=1024,
        )


@pytest.mark.parametrize(
    "capacity",
    [
        0,
        -1,
        -100,
    ],
)
def test_invalid_capacity(
    capacity: int,
) -> None:
    with pytest.raises(
        StorageValidationError,
    ):
        StorageDefinition(
            name="primary",
            capacity=capacity,
        )


def test_invalid_storage_type() -> None:
    with pytest.raises(
        UnsupportedStorageTypeError,
    ):
        StorageDefinition(
            name="primary",
            capacity=1024,
            storage_type="invalid",
        )


def test_build_storage() -> None:
    storage = build_storage(
        name="archive",
        capacity=4096,
        storage_type="archive",
        description="Archive storage",
    )

    assert storage.name == "archive"
    assert storage.capacity == 4096
    assert storage.storage_type == "archive"
    assert storage.description == "Archive storage"


def test_registry_register_and_get() -> None:
    registry = StorageRegistry()

    storage = build_storage(
        name="primary",
        capacity=1024,
    )

    registry.register(storage)

    assert registry.get("primary") is storage
    assert registry.exists("primary")
    assert len(registry) == 1
    assert "primary" in registry


def test_registry_duplicate_registration() -> None:
    registry = StorageRegistry()

    storage = build_storage(
        name="primary",
        capacity=1024,
    )

    registry.register(storage)

    with pytest.raises(
        DuplicateStorageError,
    ):
        registry.register(storage)


def test_registry_unregister() -> None:
    registry = StorageRegistry()

    storage = build_storage(
        name="primary",
        capacity=1024,
    )

    registry.register(storage)
    registry.unregister("primary")

    assert len(registry) == 0
    assert not registry.exists("primary")


def test_registry_unregister_missing() -> None:
    registry = StorageRegistry()

    with pytest.raises(
        StorageNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = StorageRegistry()

    with pytest.raises(
        StorageNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = StorageRegistry()

    registry.register(
        build_storage(
            name="one",
            capacity=100,
        )
    )
    registry.register(
        build_storage(
            name="two",
            capacity=200,
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = StorageRegistry()

    first = build_storage(
        name="one",
        capacity=100,
    )
    second = build_storage(
        name="two",
        capacity=200,
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = StorageRegistry()

    assert 123 not in registry