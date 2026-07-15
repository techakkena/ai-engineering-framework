"""
Unit tests for ai_api.utils.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_api.utils.constants import (
    REQUEST_ID_PREFIX,
    UUID_LENGTH,
)
from ai_api.utils.exceptions import (
    InvalidEncodingError,
    InvalidIdentifierError,
)
from ai_api.utils.operations import (
    generate_request_id,
    generate_uuid,
    is_supported_encoding,
    is_valid_uuid,
    normalize_encoding,
    slugify,
    validate_encoding,
    validate_identifier,
)


# ============================================================================
# normalize_encoding
# ============================================================================


@pytest.mark.parametrize(
    ("encoding", "expected"),
    [
        ("UTF-8", "utf-8"),
        (" UTF-16 ", "utf-16"),
        ("ASCII", "ascii"),
        ("latin-1", "latin-1"),
    ],
)
def test_normalize_encoding(
    encoding: str,
    expected: str,
) -> None:
    """Test encoding normalization."""
    assert normalize_encoding(encoding) == expected


# ============================================================================
# validate_encoding
# ============================================================================


@pytest.mark.parametrize(
    "encoding",
    [
        "utf-8",
        "utf-16",
        "utf-32",
        "ascii",
        "latin-1",
    ],
)
def test_validate_encoding(
    encoding: str,
) -> None:
    """Test supported encodings."""
    assert validate_encoding(encoding) == encoding


@pytest.mark.parametrize(
    "encoding",
    [
        "",
        "utf-64",
        "ansi",
        "binary",
    ],
)
def test_validate_encoding_invalid(
    encoding: str,
) -> None:
    """Unsupported encodings should raise."""
    with pytest.raises(InvalidEncodingError):
        validate_encoding(encoding)


# ============================================================================
# is_supported_encoding
# ============================================================================


@pytest.mark.parametrize(
    ("encoding", "expected"),
    [
        ("utf-8", True),
        ("utf-16", True),
        ("ascii", True),
        ("latin-1", True),
        ("utf-64", False),
        ("binary", False),
    ],
)
def test_is_supported_encoding(
    encoding: str,
    expected: bool,
) -> None:
    """Test supported encoding detection."""
    assert is_supported_encoding(encoding) is expected


# ============================================================================
# validate_identifier
# ============================================================================


@pytest.mark.parametrize(
    "identifier",
    [
        "user",
        "user_id",
        "request123",
        "_private",
    ],
)
def test_validate_identifier(
    identifier: str,
) -> None:
    """Test valid identifiers."""
    assert validate_identifier(identifier) == identifier


@pytest.mark.parametrize(
    "identifier",
    [
        "",
        "123user",
        "user-name",
        "user name",
        "@identifier",
    ],
)
def test_validate_identifier_invalid(
    identifier: str,
) -> None:
    """Invalid identifiers should raise."""
    with pytest.raises(InvalidIdentifierError):
        validate_identifier(identifier)


# ============================================================================
# slugify
# ============================================================================


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("Hello World", "hello-world"),
        ("AI API Framework", "ai-api-framework"),
        ("Hello___World", "hello-world"),
        ("Python@3.14", "python-3-14"),
        ("  Test Value  ", "test-value"),
    ],
)
def test_slugify(
    value: str,
    expected: str,
) -> None:
    """Test slug generation."""
    assert slugify(value) == expected


# ============================================================================
# generate_request_id
# ============================================================================


def test_generate_request_id() -> None:
    """Test request ID generation."""
    request_id = generate_request_id()

    assert request_id.startswith(
        f"{REQUEST_ID_PREFIX}-"
    )

    uuid_part = request_id.removeprefix(
        f"{REQUEST_ID_PREFIX}-"
    )

    assert len(uuid_part) == UUID_LENGTH
    assert is_valid_uuid(uuid_part)


# ============================================================================
# generate_uuid
# ============================================================================


def test_generate_uuid() -> None:
    """Test UUID generation."""
    value = generate_uuid()

    assert len(value) == UUID_LENGTH
    assert is_valid_uuid(value)


# ============================================================================
# is_valid_uuid
# ============================================================================


def test_is_valid_uuid_true() -> None:
    """Test valid UUID detection."""
    value = generate_uuid()

    assert is_valid_uuid(value) is True


@pytest.mark.parametrize(
    "value",
    [
        "",
        "abc",
        "12345",
        "not-a-uuid",
    ],
)
def test_is_valid_uuid_false(
    value: str,
) -> None:
    """Test invalid UUID detection."""
    assert is_valid_uuid(value) is False


# ============================================================================
# UUID format
# ============================================================================


def test_generated_uuid_matches_pattern() -> None:
    """Generated UUID should match canonical format."""
    pattern = re.compile(
        (
            r"^[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert pattern.fullmatch(generate_uuid()) is not None