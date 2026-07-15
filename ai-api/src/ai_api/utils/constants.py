"""
Constants for the ai_api.utils module.

This module defines immutable constants used throughout the utility
components of the AI API package.

The constants are framework-independent and provide defaults for
encoding, formatting, identifiers, timing, and string processing.

Author:
    AI Engineering Framework

License:
    MIT
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Encoding
# ============================================================================

DEFAULT_ENCODING: Final[str] = "utf-8"

DEFAULT_ERROR_ENCODING: Final[str] = "utf-8"

SUPPORTED_ENCODINGS: Final[frozenset[str]] = frozenset(
    {
        "utf-8",
        "utf-16",
        "utf-32",
        "ascii",
        "latin-1",
    }
)

# ============================================================================
# Formatting
# ============================================================================

DEFAULT_INDENT: Final[int] = 2

DEFAULT_SEPARATOR: Final[str] = "-"

DEFAULT_LINE_SEPARATOR: Final[str] = "\n"

DEFAULT_KEY_VALUE_SEPARATOR: Final[str] = "="

# ============================================================================
# Time
# ============================================================================

DEFAULT_TIMEOUT: Final[int] = 30

DEFAULT_RETRY_COUNT: Final[int] = 3

DEFAULT_RETRY_DELAY: Final[float] = 1.0

# ============================================================================
# Identifiers
# ============================================================================

UUID_LENGTH: Final[int] = 36

SHORT_ID_LENGTH: Final[int] = 8

REQUEST_ID_PREFIX: Final[str] = "req"

TRACE_ID_PREFIX: Final[str] = "trace"

# ============================================================================
# String Limits
# ============================================================================

DEFAULT_MAX_STRING_LENGTH: Final[int] = 1024

DEFAULT_MIN_STRING_LENGTH: Final[int] = 0

# ============================================================================
# Boolean Strings
# ============================================================================

TRUE_VALUES: Final[frozenset[str]] = frozenset(
    {
        "true",
        "1",
        "yes",
        "on",
    }
)

FALSE_VALUES: Final[frozenset[str]] = frozenset(
    {
        "false",
        "0",
        "no",
        "off",
    }
)

# ============================================================================
# Characters
# ============================================================================

UNDERSCORE: Final[str] = "_"

HYPHEN: Final[str] = "-"

SPACE: Final[str] = " "

EMPTY_STRING: Final[str] = ""

# ============================================================================
# Regular Expressions
# ============================================================================

IDENTIFIER_PATTERN: Final[str] = (
    r"^[A-Za-z_][A-Za-z0-9_]*$"
)

SLUG_PATTERN: Final[str] = (
    r"^[a-z0-9]+(?:-[a-z0-9]+)*$"
)