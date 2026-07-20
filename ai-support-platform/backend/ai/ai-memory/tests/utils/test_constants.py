from __future__ import annotations

"""Tests for ai_memory.utils.constants."""

from ai_memory.utils.constants import (
    CompressionType,
    DEFAULT_ENCODING,
    DEFAULT_INDENT,
    SerializationFormat,
)


def test_serialization_format_values() -> None:
    assert SerializationFormat.JSON.value == "json"
    assert SerializationFormat.YAML.value == "yaml"
    assert SerializationFormat.PICKLE.value == "pickle"


def test_compression_type_values() -> None:
    assert CompressionType.NONE.value == "none"
    assert CompressionType.GZIP.value == "gzip"
    assert CompressionType.ZLIB.value == "zlib"


def test_default_values() -> None:
    assert DEFAULT_ENCODING == "utf-8"
    assert DEFAULT_INDENT == 4
