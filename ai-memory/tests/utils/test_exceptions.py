"""Tests for ai_memory.utils.exceptions."""

from ai_memory.utils.exceptions import (
    CompressionError,
    SerializationError,
    UtilsError,
    ValidationError,
)


def test_exception_inheritance() -> None:
    assert issubclass(SerializationError, UtilsError)
    assert issubclass(CompressionError, UtilsError)
    assert issubclass(ValidationError, UtilsError)


def test_raise_serialization_error() -> None:
    try:
        raise SerializationError("serialization")
    except SerializationError as exc:
        assert str(exc) == "serialization"


def test_raise_compression_error() -> None:
    try:
        raise CompressionError("compression")
    except CompressionError as exc:
        assert str(exc) == "compression"


def test_raise_validation_error() -> None:
    try:
        raise ValidationError("validation")
    except ValidationError as exc:
        assert str(exc) == "validation"