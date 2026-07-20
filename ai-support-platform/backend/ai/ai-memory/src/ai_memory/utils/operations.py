from __future__ import annotations

"""Operations for the ai_memory.utils module."""

from __future__ import annotations

from .constants import CompressionType
from .constants import SerializationFormat
from .exceptions import ValidationError


def validate_serialization_format(
    value: SerializationFormat | str,
) -> SerializationFormat:
    """Validate a serialization format."""
    try:
        return SerializationFormat(value)
    except ValueError as exc:
        raise ValidationError(
            f"Invalid serialization format: {value!r}."
        ) from exc


def validate_compression_type(
    value: CompressionType | str,
) -> CompressionType:
    """Validate a compression type."""
    try:
        return CompressionType(value)
    except ValueError as exc:
        raise ValidationError(
            f"Invalid compression type: {value!r}."
        ) from exc


def is_valid_serialization_format(value: str) -> bool:
    """Return True if serialization format is valid."""
    try:
        SerializationFormat(value)
        return True
    except ValueError:
        return False


def is_valid_compression_type(value: str) -> bool:
    """Return True if compression type is valid."""
    try:
        CompressionType(value)
        return True
    except ValueError:
        return False
