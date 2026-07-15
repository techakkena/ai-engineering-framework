"""
Unit tests for ai_api.schemas.constants.
"""

from __future__ import annotations

from ai_api.schemas.constants import (
    DEFAULT_DESCRIPTION,
    DEFAULT_ENCODING,
    DEFAULT_INDENT,
    DEFAULT_MAX_ITEMS,
    DEFAULT_MAX_LENGTH,
    DEFAULT_MIN_ITEMS,
    DEFAULT_MIN_LENGTH,
    DEFAULT_NULLABLE,
    DEFAULT_READ_ONLY,
    DEFAULT_REQUIRED,
    DEFAULT_SCHEMA_VERSION,
    DEFAULT_SORT_KEYS,
    DEFAULT_TITLE,
    DEFAULT_TYPE,
    DEFAULT_WRITE_ONLY,
    FIELD_SEPARATOR,
    RESERVED_FIELD_NAMES,
    SCHEMA_SEPARATOR,
    SUPPORTED_FIELD_TYPES,
    SUPPORTED_SCHEMA_TYPES,
)


def test_default_schema_metadata() -> None:
    """Test schema metadata defaults."""
    assert DEFAULT_SCHEMA_VERSION == "1.0.0"
    assert DEFAULT_TITLE == "Schema"
    assert DEFAULT_DESCRIPTION == ""
    assert DEFAULT_TYPE == "object"
    assert DEFAULT_ENCODING == "utf-8"


def test_supported_schema_types() -> None:
    """Test supported schema types."""
    expected = {
        "object",
        "array",
        "string",
        "integer",
        "number",
        "boolean",
        "null",
    }

    assert SUPPORTED_SCHEMA_TYPES == expected


def test_supported_schema_types_are_immutable() -> None:
    """Supported schema types should be immutable."""
    assert isinstance(
        SUPPORTED_SCHEMA_TYPES,
        frozenset,
    )


def test_supported_field_types() -> None:
    """Test supported field types."""
    expected = {
        "str",
        "int",
        "float",
        "bool",
        "list",
        "dict",
        "tuple",
        "set",
        "bytes",
        "datetime",
        "date",
        "time",
        "uuid",
    }

    assert SUPPORTED_FIELD_TYPES == expected


def test_supported_field_types_are_immutable() -> None:
    """Supported field types should be immutable."""
    assert isinstance(
        SUPPORTED_FIELD_TYPES,
        frozenset,
    )


def test_default_field_options() -> None:
    """Test field option defaults."""
    assert DEFAULT_REQUIRED is False
    assert DEFAULT_NULLABLE is False
    assert DEFAULT_READ_ONLY is False
    assert DEFAULT_WRITE_ONLY is False


def test_default_validation_limits() -> None:
    """Test validation limits."""
    assert DEFAULT_MIN_LENGTH == 0
    assert DEFAULT_MAX_LENGTH == 1024
    assert DEFAULT_MIN_ITEMS == 0
    assert DEFAULT_MAX_ITEMS == 1000


def test_default_serialization_options() -> None:
    """Test serialization defaults."""
    assert DEFAULT_INDENT == 2
    assert DEFAULT_SORT_KEYS is True


def test_separators() -> None:
    """Test separator constants."""
    assert FIELD_SEPARATOR == "."
    assert SCHEMA_SEPARATOR == "_"


def test_reserved_field_names() -> None:
    """Test reserved field names."""
    expected = {
        "id",
        "created_at",
        "updated_at",
        "deleted_at",
    }

    assert RESERVED_FIELD_NAMES == expected


def test_reserved_field_names_are_immutable() -> None:
    """Reserved field names should be immutable."""
    assert isinstance(
        RESERVED_FIELD_NAMES,
        frozenset,
    )