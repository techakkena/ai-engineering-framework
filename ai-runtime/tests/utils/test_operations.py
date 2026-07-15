"""
Unit tests for ai_runtime.utils.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_runtime.utils.constants import (
    REQUEST_ID_PREFIX,
    RUNTIME_ID_PREFIX,
    UUID_LENGTH,
)
from ai_runtime.utils.exceptions import (
    InvalidEncodingError,
)
from ai_runtime.utils.operations import (
    generate_request_id,
    generate_runtime_id,
    is_supported_encoding,
    normalize_encoding,
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
    """Test valid encodings."""
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
    """Invalid encodings should raise."""
    with pytest.raises(
        InvalidEncodingError,
    ):
        validate_encoding(encoding)


# ============================================================================
# is_supported_encoding
# ============================================================================


@pytest.mark.parametrize(
    ("encoding", "expected"),
    [
        ("utf-8", True),
        ("utf-16", True),
        ("utf-32", True),
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
    assert (
        is_supported_encoding(encoding)
        is expected
    )


# ============================================================================
# validate_identifier
# ============================================================================


@pytest.mark.parametrize(
    "identifier",
    [
        "runtime",
        "runtime_01",
        "runtime-01",
        "_runtime",
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
        "123runtime",
        "runtime name",
        "@runtime",
    ],
)
def test_validate_identifier_invalid(
    identifier: str,
) -> None:
    """Invalid identifiers should raise."""
    with pytest.raises(ValueError):
        validate_identifier(identifier)


# ============================================================================
# generate_request_id
# ============================================================================


def test_generate_request_id() -> None:
    """Test request ID generation."""
    request_id = generate_request_id()

    assert request_id.startswith(
        f"{REQUEST_ID_PREFIX}-"
    )

    pattern = re.compile(
        (
            rf"^{REQUEST_ID_PREFIX}-"
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert pattern.fullmatch(request_id) is not None


# ============================================================================
# generate_runtime_id
# ============================================================================


def test_generate_runtime_id() -> None:
    """Test runtime ID generation."""
    runtime_id = generate_runtime_id()

    assert runtime_id.startswith(
        f"{RUNTIME_ID_PREFIX}-"
    )

    pattern = re.compile(
        (
            rf"^{RUNTIME_ID_PREFIX}-"
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert pattern.fullmatch(runtime_id) is not None

    uuid_part = runtime_id.removeprefix(
        f"{RUNTIME_ID_PREFIX}-"
    )

    assert len(uuid_part) == UUID_LENGTH