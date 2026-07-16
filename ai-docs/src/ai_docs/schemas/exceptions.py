"""Exceptions for the ai_docs.schemas module."""

from __future__ import annotations


class SchemaError(Exception):
    """Base exception for schema operations."""


class SchemaValidationError(SchemaError):
    """Raised when schema validation fails."""


class SchemaRegistrationError(SchemaError):
    """Raised when schema registration fails."""


class SchemaNotFoundError(
    SchemaRegistrationError,
):
    """Raised when a schema cannot be found."""


class DuplicateSchemaError(
    SchemaRegistrationError,
):
    """Raised when attempting to register a duplicate schema."""


class UnsupportedSchemaFormatError(
    SchemaValidationError,
):
    """Raised when an unsupported schema format is specified."""


__all__ = [
    "DuplicateSchemaError",
    "SchemaError",
    "SchemaNotFoundError",
    "SchemaRegistrationError",
    "SchemaValidationError",
    "UnsupportedSchemaFormatError",
]