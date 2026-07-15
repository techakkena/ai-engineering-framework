"""
Custom exceptions for the ai_api.schemas module.

This module defines the exception hierarchy used throughout the
schema components of the AI API package.

All schema-related exceptions inherit from ``SchemaError`` to provide
consistent error handling.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations


class SchemaError(Exception):
    """
    Base exception for all schema-related errors.
    """

    def __init__(
        self,
        message: str = "A schema error occurred.",
    ) -> None:
        """
        Initialize the exception.

        Args:
            message: Error message.
        """
        super().__init__(message)


class InvalidSchemaError(SchemaError):
    """
    Raised when a schema definition is invalid.
    """

    def __init__(
        self,
        schema_name: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            schema_name: Invalid schema name.
        """
        self.schema_name = schema_name

        super().__init__(
            f"Invalid schema: '{schema_name}'."
        )


class SchemaValidationError(SchemaError):
    """
    Raised when schema validation fails.
    """

    def __init__(
        self,
        schema_name: str,
        reason: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            schema_name: Schema name.
            reason: Validation failure reason.
        """
        self.schema_name = schema_name
        self.reason = reason

        super().__init__(
            f"Schema '{schema_name}' validation failed: {reason}."
        )


class InvalidFieldError(SchemaError):
    """
    Raised when a schema field is invalid.
    """

    def __init__(
        self,
        field_name: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            field_name: Invalid field name.
        """
        self.field_name = field_name

        super().__init__(
            f"Invalid field: '{field_name}'."
        )


class DuplicateFieldError(SchemaError):
    """
    Raised when duplicate fields are detected.
    """

    def __init__(
        self,
        field_name: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            field_name: Duplicate field.
        """
        self.field_name = field_name

        super().__init__(
            f"Duplicate field: '{field_name}'."
        )


class UnsupportedFieldTypeError(SchemaError):
    """
    Raised when an unsupported field type is used.
    """

    def __init__(
        self,
        field_type: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            field_type: Unsupported field type.
        """
        self.field_type = field_type

        super().__init__(
            f"Unsupported field type: '{field_type}'."
        )


class ReservedFieldNameError(SchemaError):
    """
    Raised when a reserved field name is used.
    """

    def __init__(
        self,
        field_name: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            field_name: Reserved field name.
        """
        self.field_name = field_name

        super().__init__(
            f"Reserved field name: '{field_name}'."
        )


class SchemaConfigurationError(SchemaError):
    """
    Raised when schema configuration is invalid.
    """

    def __init__(
        self,
        configuration: str,
    ) -> None:
        """
        Initialize the exception.

        Args:
            configuration: Invalid configuration.
        """
        self.configuration = configuration

        super().__init__(
            f"Invalid schema configuration: '{configuration}'."
        )