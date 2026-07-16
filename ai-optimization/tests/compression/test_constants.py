"""Tests for ai_optimization.compression.constants."""

from __future__ import annotations

from ai_optimization.compression import constants


def test_default_values() -> None:
    assert constants.DEFAULT_COMPRESSION_NAME == "compression"
    assert constants.DEFAULT_COMPRESSION_TYPE == "gzip"
    assert constants.DEFAULT_ENABLED is True


def test_supported_compression_types() -> None:
    assert constants.SUPPORTED_COMPRESSION_TYPES == frozenset(
        {
            "gzip",
            "zstd",
            "lz4",
            "brotli",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_COMPRESSION_NAME_LENGTH == 1
    assert constants.MAX_COMPRESSION_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.TYPE_KEY == "type"
    assert constants.LEVEL_KEY == "level"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"