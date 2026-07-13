"""Constants for the ai_memory.utils module."""

from __future__ import annotations

from enum import Enum


class SerializationFormat(str, Enum):
    """Supported serialization formats."""

    JSON = "json"
    YAML = "yaml"
    PICKLE = "pickle"


class CompressionType(str, Enum):
    """Supported compression algorithms."""

    NONE = "none"
    GZIP = "gzip"
    ZLIB = "zlib"


DEFAULT_ENCODING = "utf-8"
DEFAULT_INDENT = 4