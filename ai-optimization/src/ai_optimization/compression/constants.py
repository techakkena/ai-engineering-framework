"""Constants for the ai_optimization.compression module."""

from __future__ import annotations

from typing import Final

# Default compression configuration.
DEFAULT_COMPRESSION_NAME: Final[str] = "compression"
DEFAULT_COMPRESSION_TYPE: Final[str] = "gzip"
DEFAULT_ENABLED: Final[bool] = True

# Supported compression algorithms.
GZIP_COMPRESSION: Final[str] = "gzip"
ZSTD_COMPRESSION: Final[str] = "zstd"
LZ4_COMPRESSION: Final[str] = "lz4"
BROTLI_COMPRESSION: Final[str] = "brotli"

SUPPORTED_COMPRESSION_TYPES: Final[frozenset[str]] = frozenset(
    {
        GZIP_COMPRESSION,
        ZSTD_COMPRESSION,
        LZ4_COMPRESSION,
        BROTLI_COMPRESSION,
    }
)

# Validation.
MIN_COMPRESSION_NAME_LENGTH: Final[int] = 1
MAX_COMPRESSION_NAME_LENGTH: Final[int] = 255

# Metadata keys.
NAME_KEY: Final[str] = "name"
TYPE_KEY: Final[str] = "type"
LEVEL_KEY: Final[str] = "level"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "BROTLI_COMPRESSION",
    "DEFAULT_COMPRESSION_NAME",
    "DEFAULT_COMPRESSION_TYPE",
    "DEFAULT_ENABLED",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "GZIP_COMPRESSION",
    "LEVEL_KEY",
    "LZ4_COMPRESSION",
    "MAX_COMPRESSION_NAME_LENGTH",
    "MIN_COMPRESSION_NAME_LENGTH",
    "NAME_KEY",
    "SUPPORTED_COMPRESSION_TYPES",
    "TYPE_KEY",
    "ZSTD_COMPRESSION",
]