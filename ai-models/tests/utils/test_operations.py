"""
Unit tests for ai_models.utils.operations.
"""

from __future__ import annotations

import re

import pytest

from ai_models.utils.exceptions import (
    InvalidEncodingError,
)
from ai_models.utils.operations import (
    build_model_uuid,
    is_supported_encoding,
    normalize_encoding,
    validate_encoding,
    validate_model_name,
)


# ============================================================================
# normalize_encoding
# ============================================================================


@pytest.mark.parametrize(
    ("encoding", "expected"),
    [
        ("UTF-8", "utf-8"),
        (" Utf-16 ", "utf-16"),
        ("ASCII", "ascii"),
        ("LATIN-1", "latin-1"),
    ],
)
def test_normalize_encoding(
    encoding: str,
    expected: str,
) -> None:
    """Test encoding normalization."""
    assert (
        normalize_encoding(
            encoding,
        )
        == expected
    )


# ============================================================================
# validate_encoding
# ============================================================================


@pytest.mark.parametrize(
    "encoding",
    [
        "utf-8",
        "utf-16",
        "ascii",
        "latin-1",
    ],
)
def test_validate_encoding(
    encoding: str,
) -> None:
    """Test valid encodings."""
    assert (
        validate_encoding(
            encoding,
        )
        == encoding
    )


@pytest.mark.parametrize(
    "encoding",
    [
        "",
        "utf-32",
        "cp1252",
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
        validate_encoding(
            encoding,
        )


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
        ("utf-32", False),
        ("cp1252", False),
    ],
)
def test_is_supported_encoding(
    encoding: str,
    expected: bool,
) -> None:
    """Test encoding support detection."""
    assert (
        is_supported_encoding(
            encoding,
        )
        is expected
    )


# ============================================================================
# validate_model_name
# ============================================================================


@pytest.mark.parametrize(
    "model_name",
    [
        "gpt-5",
        "claude-4",
        "gemini_2.5",
        "model.v1",
        "runtime123",
    ],
)
def test_validate_model_name(
    model_name: str,
) -> None:
    """Test valid model names."""
    assert (
        validate_model_name(
            model_name,
        )
        == model_name
    )


@pytest.mark.parametrize(
    "model_name",
    [
        "",
        " ",
        "model name",
        "@model",
        "gpt/5",
        "a" * 129,
    ],
)
def test_validate_model_name_invalid(
    model_name: str,
) -> None:
    """Invalid model names should raise."""
    with pytest.raises(ValueError):
        validate_model_name(
            model_name,
        )


# ============================================================================
# build_model_uuid
# ============================================================================


def test_build_model_uuid() -> None:
    """Test model UUID generation."""
    model_uuid = build_model_uuid()

    assert model_uuid.startswith(
        "model-",
    )

    pattern = re.compile(
        (
            r"^model-"
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{4}-"
            r"[0-9a-f]{12}$"
        )
    )

    assert (
        pattern.fullmatch(
            model_uuid,
        )
        is not None
    )