from __future__ import annotations

"""Tests for ai_memory.utils.operations."""

import pytest

from ai_memory.utils.constants import (
    CompressionType,
    SerializationFormat,
)
from ai_memory.utils.exceptions import ValidationError
from ai_memory.utils.operations import (
    is_valid_compression_type,
    is_valid_serialization_format,
    validate_compression_type,
    validate_serialization_format,
)


def test_validate_serialization_format() -> None:
    assert validate_serialization_format("json") is SerializationFormat.JSON


def test_validate_compression_type() -> None:
    assert validate_compression_type("gzip") is CompressionType.GZIP


@pytest.mark.parametrize(
    ("value", "validator"),
    [
        ("invalid", validate_serialization_format),
        ("invalid", validate_compression_type),
    ],
)
def test_validation_errors(value: str, validator) -> None:
    with pytest.raises(ValidationError):
        validator(value)


def test_is_valid_serialization_format() -> None:
    assert is_valid_serialization_format("yaml")
    assert not is_valid_serialization_format("invalid")


def test_is_valid_compression_type() -> None:
    assert is_valid_compression_type("zlib")
    assert not is_valid_compression_type("invalid")
