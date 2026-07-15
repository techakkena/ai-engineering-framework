"""
ai_api.schemas

Framework-independent schema utilities for the AI API package.

This module provides reusable constants, exceptions, and helper
operations for schema validation, serialization, and field handling.

The module is intentionally framework-independent and can be
integrated with Pydantic, dataclasses, Marshmallow, or any future
schema validation library.

Author:
    AI Engineering Framework

License:
    MIT
"""

from ai_api.schemas.constants import (
    DEFAULT_ENCODING,
    DEFAULT_SCHEMA_VERSION,
    DEFAULT_TITLE,
    DEFAULT_TYPE,
    SUPPORTED_FIELD_TYPES,
    SUPPORTED_SCHEMA_TYPES,
)
from ai_api.schemas.exceptions import (
    DuplicateFieldError,
    InvalidFieldError,
    InvalidSchemaError,
    SchemaError,
    SchemaValidationError,
)
from ai_api.schemas.operations import (
    build_schema_name,
    is_supported_field_type,
    normalize_field_name,
    validate_field_name,
    validate_field_type,
    validate_schema_name,
)

__all__ = [
    # Constants
    "DEFAULT_ENCODING",
    "DEFAULT_SCHEMA_VERSION",
    "DEFAULT_TITLE",
    "DEFAULT_TYPE",
    "SUPPORTED_FIELD_TYPES",
    "SUPPORTED_SCHEMA_TYPES",
    # Exceptions
    "SchemaError",
    "DuplicateFieldError",
    "InvalidFieldError",
    "InvalidSchemaError",
    "SchemaValidationError",
    # Operations
    "build_schema_name",
    "is_supported_field_type",
    "normalize_field_name",
    "validate_field_name",
    "validate_field_type",
    "validate_schema_name",
]