"""
Unit tests for ai_api.schemas.exceptions.
"""

from __future__ import annotations

import pytest

from ai_api.schemas.exceptions import (
    DuplicateFieldError,
    InvalidFieldError,
    InvalidSchemaError,
    ReservedFieldNameError,
    SchemaConfigurationError,
    SchemaError,
    SchemaValidationError,
    UnsupportedFieldTypeError,
)


def test_schema_error_default_message() -> None:
    """Test SchemaError with the default message."""
    error = SchemaError()

    assert str(error) == "A schema error occurred."


def test_schema_error_custom_message() -> None:
    """Test SchemaError with a custom message."""
    error = SchemaError("Custom schema error.")

    assert str(error) == "Custom schema error."


@pytest.mark.parametrize(
    "schema_name",
    [
        "",
        "user",
        "invalid_schema",
    ],
)
def test_invalid_schema_error(
    schema_name: str,
) -> None:
    """Test InvalidSchemaError."""
    error = InvalidSchemaError(schema_name)

    assert isinstance(error, SchemaError)
    assert error.schema_name == schema_name
    assert str(error) == f"Invalid schema: '{schema_name}'."


def test_schema_validation_error() -> None:
    """Test SchemaValidationError."""
    schema_name = "UserSchema"
    reason = "Missing required field."

    error = SchemaValidationError(
        schema_name,
        reason,
    )

    assert isinstance(error, SchemaError)
    assert error.schema_name == schema_name
    assert error.reason == reason
    assert (
        str(error)
        == f"Schema '{schema_name}' validation failed: {reason}."
    )


@pytest.mark.parametrize(
    "field_name",
    [
        "",
        "123field",
        "field-name",
    ],
)
def test_invalid_field_error(
    field_name: str,
) -> None:
    """Test InvalidFieldError."""
    error = InvalidFieldError(field_name)

    assert isinstance(error, SchemaError)
    assert error.field_name == field_name
    assert str(error) == f"Invalid field: '{field_name}'."


@pytest.mark.parametrize(
    "field_name",
    [
        "email",
        "username",
        "status",
    ],
)
def test_duplicate_field_error(
    field_name: str,
) -> None:
    """Test DuplicateFieldError."""
    error = DuplicateFieldError(field_name)

    assert isinstance(error, SchemaError)
    assert error.field_name == field_name
    assert str(error) == f"Duplicate field: '{field_name}'."


@pytest.mark.parametrize(
    "field_type",
    [
        "decimal",
        "objectid",
        "binary",
    ],
)
def test_unsupported_field_type_error(
    field_type: str,
) -> None:
    """Test UnsupportedFieldTypeError."""
    error = UnsupportedFieldTypeError(field_type)

    assert isinstance(error, SchemaError)
    assert error.field_type == field_type
    assert (
        str(error)
        == f"Unsupported field type: '{field_type}'."
    )


@pytest.mark.parametrize(
    "field_name",
    [
        "id",
        "created_at",
        "updated_at",
    ],
)
def test_reserved_field_name_error(
    field_name: str,
) -> None:
    """Test ReservedFieldNameError."""
    error = ReservedFieldNameError(field_name)

    assert isinstance(error, SchemaError)
    assert error.field_name == field_name
    assert (
        str(error)
        == f"Reserved field name: '{field_name}'."
    )


def test_schema_configuration_error() -> None:
    """Test SchemaConfigurationError."""
    configuration = "encoding"

    error = SchemaConfigurationError(
        configuration,
    )

    assert isinstance(error, SchemaError)
    assert error.configuration == configuration
    assert (
        str(error)
        == (
            "Invalid schema configuration: "
            f"'{configuration}'."
        )
    )