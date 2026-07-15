"""
Unit tests for ai_api.utils.constants.
"""

from __future__ import annotations

from ai_api.utils.constants import (
    DEFAULT_ENCODING,
    DEFAULT_ERROR_ENCODING,
    DEFAULT_INDENT,
    DEFAULT_KEY_VALUE_SEPARATOR,
    DEFAULT_LINE_SEPARATOR,
    DEFAULT_MAX_STRING_LENGTH,
    DEFAULT_MIN_STRING_LENGTH,
    DEFAULT_RETRY_COUNT,
    DEFAULT_RETRY_DELAY,
    DEFAULT_SEPARATOR,
    DEFAULT_TIMEOUT,
    EMPTY_STRING,
    FALSE_VALUES,
    HYPHEN,
    IDENTIFIER_PATTERN,
    REQUEST_ID_PREFIX,
    SHORT_ID_LENGTH,
    SLUG_PATTERN,
    SPACE,
    SUPPORTED_ENCODINGS,
    TRACE_ID_PREFIX,
    TRUE_VALUES,
    UNDERSCORE,
    UUID_LENGTH,
)


def test_encoding_defaults() -> None:
    """Test encoding defaults."""
    assert DEFAULT_ENCODING == "utf-8"
    assert DEFAULT_ERROR_ENCODING == "utf-8"


def test_supported_encodings() -> None:
    """Test supported encodings."""
    expected = {
        "utf-8",
        "utf-16",
        "utf-32",
        "ascii",
        "latin-1",
    }

    assert SUPPORTED_ENCODINGS == expected


def test_supported_encodings_are_immutable() -> None:
    """Supported encodings should be immutable."""
    assert isinstance(
        SUPPORTED_ENCODINGS,
        frozenset,
    )


def test_formatting_defaults() -> None:
    """Test formatting defaults."""
    assert DEFAULT_INDENT == 2
    assert DEFAULT_SEPARATOR == "-"
    assert DEFAULT_LINE_SEPARATOR == "\n"
    assert DEFAULT_KEY_VALUE_SEPARATOR == "="


def test_timeout_defaults() -> None:
    """Test timeout defaults."""
    assert DEFAULT_TIMEOUT == 30
    assert DEFAULT_RETRY_COUNT == 3
    assert DEFAULT_RETRY_DELAY == 1.0


def test_identifier_defaults() -> None:
    """Test identifier defaults."""
    assert UUID_LENGTH == 36
    assert SHORT_ID_LENGTH == 8
    assert REQUEST_ID_PREFIX == "req"
    assert TRACE_ID_PREFIX == "trace"


def test_string_limits() -> None:
    """Test string limits."""
    assert DEFAULT_MAX_STRING_LENGTH == 1024
    assert DEFAULT_MIN_STRING_LENGTH == 0


def test_boolean_values() -> None:
    """Test boolean string values."""
    assert TRUE_VALUES == {
        "true",
        "1",
        "yes",
        "on",
    }

    assert FALSE_VALUES == {
        "false",
        "0",
        "no",
        "off",
    }


def test_boolean_sets_are_immutable() -> None:
    """Boolean value collections should be immutable."""
    assert isinstance(TRUE_VALUES, frozenset)
    assert isinstance(FALSE_VALUES, frozenset)


def test_character_constants() -> None:
    """Test character constants."""
    assert UNDERSCORE == "_"
    assert HYPHEN == "-"
    assert SPACE == " "
    assert EMPTY_STRING == ""


def test_regex_patterns() -> None:
    """Test regex pattern constants."""
    assert IDENTIFIER_PATTERN == (
        r"^[A-Za-z_][A-Za-z0-9_]*$"
    )

    assert SLUG_PATTERN == (
        r"^[a-z0-9]+(?:-[a-z0-9]+)*$"
    )