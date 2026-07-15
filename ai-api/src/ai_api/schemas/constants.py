"""
Constants for the ai_api.schemas module.

This module defines immutable constants used throughout the schema
components of the AI API package.

The constants are framework-independent and provide sensible defaults
for schema metadata, field types, validation, and serialization.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Schema Metadata
# ============================================================================

DEFAULT_SCHEMA_VERSION: Final[str] = "1.0.0"

DEFAULT_TITLE: Final[str] = "Schema"

DEFAULT_DESCRIPTION: Final[str] = ""

DEFAULT_TYPE: Final[str] = "object"

DEFAULT_ENCODING: Final[str] = "utf-8"

# ============================================================================
# Supported Schema Types
# ============================================================================

SUPPORTED_SCHEMA_TYPES: Final[frozenset[str]] = frozenset(
    {
        "object",
        "array",
        "string",
        "integer",
        "number",
        "boolean",
        "null",
    }
)

# ============================================================================
# Supported Field Types
# ============================================================================

SUPPORTED_FIELD_TYPES: Final[frozenset[str]] = frozenset(
    {
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
)

# ============================================================================
# Required Field Options
# ============================================================================

DEFAULT_REQUIRED: Final[bool] = False

DEFAULT_NULLABLE: Final[bool] = False

DEFAULT_READ_ONLY: Final[bool] = False

DEFAULT_WRITE_ONLY: Final[bool] = False

# ============================================================================
# Validation Limits
# ============================================================================

DEFAULT_MIN_LENGTH: Final[int] = 0

DEFAULT_MAX_LENGTH: Final[int] = 1024

DEFAULT_MIN_ITEMS: Final[int] = 0

DEFAULT_MAX_ITEMS: Final[int] = 1000

# ============================================================================
# Serialization
# ============================================================================

DEFAULT_INDENT: Final[int] = 2

DEFAULT_SORT_KEYS: Final[bool] = True

# ============================================================================
# Naming
# ============================================================================

FIELD_SEPARATOR: Final[str] = "."

SCHEMA_SEPARATOR: Final[str] = "_"

# ============================================================================
# Reserved Fields
# ============================================================================

RESERVED_FIELD_NAMES: Final[frozenset[str]] = frozenset(
    {
        "id",
        "created_at",
        "updated_at",
        "deleted_at",
    }
)