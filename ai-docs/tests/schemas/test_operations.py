"""Tests for ai_docs.schemas.operations."""

from __future__ import annotations

import pytest

from ai_docs.schemas.constants import (
    DEFAULT_ENABLED,
    DEFAULT_SCHEMA_FORMAT,
)
from ai_docs.schemas.exceptions import (
    DuplicateSchemaError,
    SchemaNotFoundError,
    SchemaValidationError,
    UnsupportedSchemaFormatError,
)
from ai_docs.schemas.operations import (
    SchemaDefinition,
    SchemaRegistry,
    build_schema,
)


def test_schema_defaults() -> None:
    schema = SchemaDefinition(
        name="user",
        content='{"type":"object"}',
    )

    assert schema.name == "user"
    assert schema.content == '{"type":"object"}'
    assert schema.schema_format == DEFAULT_SCHEMA_FORMAT
    assert schema.description == ""
    assert schema.enabled is DEFAULT_ENABLED


def test_schema_trims_name() -> None:
    schema = SchemaDefinition(
        name="  user  ",
        content='{"type":"object"}',
    )

    assert schema.name == "user"


@pytest.mark.parametrize(
    "name",
    [
        "",
        " ",
        "ab",
        "a" * 256,
    ],
)
def test_invalid_name(
    name: str,
) -> None:
    with pytest.raises(
        SchemaValidationError,
    ):
        SchemaDefinition(
            name=name,
            content='{}',
        )


@pytest.mark.parametrize(
    "content",
    [
        "",
        "   ",
    ],
)
def test_invalid_content(
    content: str,
) -> None:
    with pytest.raises(
        SchemaValidationError,
    ):
        SchemaDefinition(
            name="user",
            content=content,
        )


def test_invalid_schema_format() -> None:
    with pytest.raises(
        UnsupportedSchemaFormatError,
    ):
        SchemaDefinition(
            name="user",
            content="{}",
            schema_format="xml",
        )


def test_build_schema() -> None:
    schema = build_schema(
        name="order",
        content='{"type":"object"}',
        schema_format="openapi",
        description="Order schema",
    )

    assert schema.name == "order"
    assert schema.content == '{"type":"object"}'
    assert schema.schema_format == "openapi"
    assert schema.description == "Order schema"


def test_registry_register_and_get() -> None:
    registry = SchemaRegistry()

    schema = build_schema(
        name="user",
        content="{}",
    )

    registry.register(schema)

    assert registry.get("user") is schema
    assert registry.exists("user")
    assert len(registry) == 1
    assert "user" in registry


def test_registry_duplicate_registration() -> None:
    registry = SchemaRegistry()

    schema = build_schema(
        name="user",
        content="{}",
    )

    registry.register(schema)

    with pytest.raises(
        DuplicateSchemaError,
    ):
        registry.register(schema)


def test_registry_unregister() -> None:
    registry = SchemaRegistry()

    schema = build_schema(
        name="user",
        content="{}",
    )

    registry.register(schema)
    registry.unregister("user")

    assert len(registry) == 0
    assert not registry.exists("user")


def test_registry_unregister_missing() -> None:
    registry = SchemaRegistry()

    with pytest.raises(
        SchemaNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = SchemaRegistry()

    with pytest.raises(
        SchemaNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = SchemaRegistry()

    registry.register(
        build_schema(
            name="user",
            content="{}",
        )
    )
    registry.register(
        build_schema(
            name="order",
            content="{}",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = SchemaRegistry()

    first = build_schema(
        name="user",
        content="{}",
    )
    second = build_schema(
        name="order",
        content="{}",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = SchemaRegistry()

    assert 123 not in registry