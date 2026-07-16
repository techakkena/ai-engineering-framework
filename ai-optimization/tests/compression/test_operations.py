"""Tests for ai_optimization.compression.operations."""

from __future__ import annotations

import pytest

from ai_optimization.compression.constants import (
    DEFAULT_COMPRESSION_TYPE,
    DEFAULT_ENABLED,
)
from ai_optimization.compression.exceptions import (
    CompressionNotFoundError,
    CompressionValidationError,
    DuplicateCompressionError,
    UnsupportedCompressionTypeError,
)
from ai_optimization.compression.operations import (
    CompressionDefinition,
    CompressionRegistry,
    build_compression,
)


def test_compression_definition_defaults() -> None:
    compression = CompressionDefinition(
        name="default",
        level=6,
    )

    assert compression.name == "default"
    assert compression.level == 6
    assert compression.compression_type == (
        DEFAULT_COMPRESSION_TYPE
    )
    assert compression.description == ""
    assert compression.enabled is DEFAULT_ENABLED


def test_compression_definition_trims_name() -> None:
    compression = CompressionDefinition(
        name="  default  ",
        level=6,
    )

    assert compression.name == "default"


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
        CompressionValidationError,
    ):
        CompressionDefinition(
            name=name,
            level=6,
        )


@pytest.mark.parametrize(
    "level",
    [
        0,
        -1,
        10,
        99,
    ],
)
def test_invalid_level(level: int) -> None:
    with pytest.raises(
        CompressionValidationError,
    ):
        CompressionDefinition(
            name="compression",
            level=level,
        )


def test_invalid_compression_type() -> None:
    with pytest.raises(
        UnsupportedCompressionTypeError,
    ):
        CompressionDefinition(
            name="compression",
            level=6,
            compression_type="zip",
        )


def test_build_compression() -> None:
    compression = build_compression(
        name="fast",
        level=3,
        compression_type="lz4",
        description="Fast compression",
    )

    assert compression.name == "fast"
    assert compression.level == 3
    assert compression.compression_type == "lz4"
    assert compression.description == "Fast compression"


def test_registry_register_and_get() -> None:
    registry = CompressionRegistry()

    compression = build_compression(
        name="default",
        level=6,
    )

    registry.register(compression)

    assert registry.get("default") is compression
    assert registry.exists("default")
    assert len(registry) == 1
    assert "default" in registry


def test_registry_duplicate_registration() -> None:
    registry = CompressionRegistry()

    compression = build_compression(
        name="default",
        level=6,
    )

    registry.register(compression)

    with pytest.raises(
        DuplicateCompressionError,
    ):
        registry.register(compression)


def test_registry_unregister() -> None:
    registry = CompressionRegistry()

    compression = build_compression(
        name="default",
        level=6,
    )

    registry.register(compression)
    registry.unregister("default")

    assert len(registry) == 0
    assert not registry.exists("default")


def test_registry_unregister_missing() -> None:
    registry = CompressionRegistry()

    with pytest.raises(
        CompressionNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = CompressionRegistry()

    with pytest.raises(
        CompressionNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = CompressionRegistry()

    registry.register(
        build_compression(
            name="one",
            level=1,
        )
    )
    registry.register(
        build_compression(
            name="two",
            level=2,
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = CompressionRegistry()

    first = build_compression(
        name="one",
        level=1,
    )
    second = build_compression(
        name="two",
        level=2,
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (first, second)


def test_registry_contains_unknown_type() -> None:
    registry = CompressionRegistry()

    assert 123 not in registry