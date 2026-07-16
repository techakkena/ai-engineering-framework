"""Tests for ai_testing.snapshots.operations."""

from __future__ import annotations

import pytest

from ai_testing.snapshots.constants import (
    DEFAULT_ENABLED,
    DEFAULT_FORMAT,
)
from ai_testing.snapshots.exceptions import (
    DuplicateSnapshotError,
    SnapshotNotFoundError,
    SnapshotValidationError,
    UnsupportedSnapshotFormatError,
)
from ai_testing.snapshots.operations import (
    SnapshotDefinition,
    SnapshotRegistry,
    build_snapshot,
)


def test_snapshot_definition_defaults() -> None:
    snapshot = SnapshotDefinition(
        name="response",
        content={"value": 1},
    )

    assert snapshot.name == "response"
    assert snapshot.content == {"value": 1}
    assert snapshot.format == DEFAULT_FORMAT
    assert snapshot.enabled is DEFAULT_ENABLED


def test_snapshot_name_trimmed() -> None:
    snapshot = SnapshotDefinition(
        name="  response  ",
        content={},
    )

    assert snapshot.name == "response"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_name(name: str) -> None:
    with pytest.raises(SnapshotValidationError):
        SnapshotDefinition(
            name=name,
            content={},
        )


def test_invalid_format() -> None:
    with pytest.raises(UnsupportedSnapshotFormatError):
        SnapshotDefinition(
            name="snapshot",
            content={},
            format="xml",
        )


def test_build_snapshot() -> None:
    snapshot = build_snapshot(
        name="payload",
        content={"id": 1},
        format="yaml",
    )

    assert snapshot.name == "payload"
    assert snapshot.content == {"id": 1}
    assert snapshot.format == "yaml"


def test_registry_register_get() -> None:
    registry = SnapshotRegistry()

    snapshot = build_snapshot(
        name="response",
        content={},
    )

    registry.register(snapshot)

    assert registry.get("response") is snapshot
    assert registry.exists("response")
    assert len(registry) == 1
    assert "response" in registry


def test_registry_duplicate_registration() -> None:
    registry = SnapshotRegistry()

    snapshot = build_snapshot(
        name="response",
        content={},
    )

    registry.register(snapshot)

    with pytest.raises(DuplicateSnapshotError):
        registry.register(snapshot)


def test_registry_unregister() -> None:
    registry = SnapshotRegistry()

    snapshot = build_snapshot(
        name="response",
        content={},
    )

    registry.register(snapshot)
    registry.unregister("response")

    assert len(registry) == 0
    assert not registry.exists("response")


def test_registry_unregister_missing() -> None:
    registry = SnapshotRegistry()

    with pytest.raises(SnapshotNotFoundError):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = SnapshotRegistry()

    with pytest.raises(SnapshotNotFoundError):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = SnapshotRegistry()

    registry.register(
        build_snapshot(
            name="one",
            content=1,
        )
    )
    registry.register(
        build_snapshot(
            name="two",
            content=2,
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = SnapshotRegistry()

    first = build_snapshot(
        name="one",
        content=1,
    )
    second = build_snapshot(
        name="two",
        content=2,
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (first, second)


def test_registry_contains_unknown_type() -> None:
    registry = SnapshotRegistry()

    assert 123 not in registry