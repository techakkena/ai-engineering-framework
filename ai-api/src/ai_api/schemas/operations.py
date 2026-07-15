"""
Utility operations for the ai_api.schemas module.

This module provides framework-independent helper functions for
schema names, field names, field types, and schema validation.

All functions are deterministic, side-effect free, and easily testable.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations

import re

from ai_api.schemas.constants import (
    RESERVED_FIELD_NAMES,
    SUPPORTED_FIELD_TYPES,
    SUPPORTED_SCHEMA_TYPES,
)
from ai_api.schemas.exceptions import (
    InvalidFieldError,
    InvalidSchemaError,
    ReservedFieldNameError,
    UnsupportedFieldTypeError,
)


def normalize_field_name(field_name: str) -> str:
    """
    Normalize a field name.

    Args:
        field_name: Field name.

    Returns:
        Normalized field name.
    """
    return field_name.strip().lower()


def validate_field_name(field_name: str) -> str:
    """
    Validate a field name.

    Args:
        field_name: Field name.

    Returns:
        Validated field name.

    Raises:
        InvalidFieldError:
            If the field name is invalid.

        ReservedFieldNameError:
            If the field name is reserved.
    """
    normalized = normalize_field_name(field_name)

    if not normalized:
        raise InvalidFieldError(field_name)

    if not re.fullmatch(
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        normalized,
    ):
        raise InvalidFieldError(field_name)

    if normalized in RESERVED_FIELD_NAMES:
        raise ReservedFieldNameError(normalized)

    return normalized


def validate_field_type(field_type: str) -> str:
    """
    Validate a field type.

    Args:
        field_type: Field type.

    Returns:
        Validated field type.

    Raises:
        UnsupportedFieldTypeError:
            If the field type is unsupported.
    """
    normalized = field_type.strip().lower()

    if normalized not in SUPPORTED_FIELD_TYPES:
        raise UnsupportedFieldTypeError(field_type)

    return normalized


def validate_schema_name(schema_name: str) -> str:
    """
    Validate a schema name.

    Args:
        schema_name: Schema name.

    Returns:
        Validated schema name.

    Raises:
        InvalidSchemaError:
            If the schema name is invalid.
    """
    normalized = schema_name.strip()

    if not normalized:
        raise InvalidSchemaError(schema_name)

    if not re.fullmatch(
        r"[A-Z][A-Za-z0-9_]*",
        normalized,
    ):
        raise InvalidSchemaError(schema_name)

    return normalized


def validate_schema_type(schema_type: str) -> str:
    """
    Validate a schema type.

    Args:
        schema_type: Schema type.

    Returns:
        Validated schema type.

    Raises:
        InvalidSchemaError:
            If the schema type is unsupported.
    """
    normalized = schema_type.strip().lower()

    if normalized not in SUPPORTED_SCHEMA_TYPES:
        raise InvalidSchemaError(schema_type)

    return normalized


def build_schema_name(name: str) -> str:
    """
    Build a normalized schema name.

    Args:
        name: Base schema name.

    Returns:
        Schema name in PascalCase.
    """
    words = re.split(r"[_\-\s]+", name.strip())

    return "".join(
        word.capitalize()
        for word in words
        if word
    )


def is_supported_field_type(field_type: str) -> bool:
    """
    Determine whether a field type is supported.

    Args:
        field_type: Field type.

    Returns:
        True if supported.
    """
    return (
        field_type.strip().lower()
        in SUPPORTED_FIELD_TYPES
    )


def is_supported_schema_type(schema_type: str) -> bool:
    """
    Determine whether a schema type is supported.

    Args:
        schema_type: Schema type.

    Returns:
        True if supported.
    """
    return (
        schema_type.strip().lower()
        in SUPPORTED_SCHEMA_TYPES
    )