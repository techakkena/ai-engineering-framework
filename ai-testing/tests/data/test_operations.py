"""Tests for ai_testing.data.operations."""

from __future__ import annotations

import pytest

from ai_testing.data.constants import DEFAULT_ENABLED
from ai_testing.data.exceptions import (
    DataNotFoundError,
    DataValidationError,
    DuplicateDataError,
)
from ai_testing.data.operations import (
    DataRegistry,
    DataSet,
    build_dataset,
)


def test_dataset_defaults() -> None:
    dataset = DataSet(
        name="users",
        data=(1, 2, 3),
    )

    assert dataset.name == "users"
    assert dataset.data == (1, 2, 3)
    assert dataset.description == ""
    assert dataset.enabled is DEFAULT_ENABLED
    assert dataset.metadata == {}


def test_dataset_name_trimmed() -> None:
    dataset = DataSet(
        name="  users  ",
        data=(),
    )

    assert dataset.name == "users"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_dataset_name(name: str) -> None:
    with pytest.raises(DataValidationError):
        DataSet(
            name=name,
            data=(),
        )


def test_build_dataset() -> None:
    dataset = build_dataset(
        name="records",
        data=(1, 2),
        metadata={"version": 1},
    )

    assert dataset.name == "records"
    assert dataset.data == (1, 2)
    assert dataset.metadata == {"version": 1}


def test_build_dataset_default_metadata() -> None:
    dataset = build_dataset(
        name="records",
        data=(),
    )

    assert dataset.metadata == {}


def test_registry_register_and_get() -> None:
    registry = DataRegistry()

    dataset = build_dataset(
        name="users",
        data=(1,),
    )

    registry.register(dataset)

    assert registry.get("users") is dataset
    assert registry.exists("users")
    assert len(registry) == 1
    assert "users" in registry


def test_registry_duplicate_registration() -> None:
    registry = DataRegistry()

    dataset = build_dataset(
        name="users",
        data=(1,),
    )

    registry.register(dataset)

    with pytest.raises(DuplicateDataError):
        registry.register(dataset)


def test_registry_unregister() -> None:
    registry = DataRegistry()

    dataset = build_dataset(
        name="users",
        data=(1,),
    )

    registry.register(dataset)
    registry.unregister("users")

    assert len(registry) == 0
    assert not registry.exists("users")


def test_registry_unregister_missing() -> None:
    registry = DataRegistry()

    with pytest.raises(DataNotFoundError):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = DataRegistry()

    with pytest.raises(DataNotFoundError):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = DataRegistry()

    registry.register(
        build_dataset(
            name="one",
            data=(1,),
        )
    )
    registry.register(
        build_dataset(
            name="two",
            data=(2,),
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = DataRegistry()

    first = build_dataset(
        name="one",
        data=(1,),
    )
    second = build_dataset(
        name="two",
        data=(2,),
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (first, second)


def test_registry_contains_unknown_type() -> None:
    registry = DataRegistry()

    assert 123 not in registry