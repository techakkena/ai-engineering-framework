"""
Unit tests for ai_datasets.loaders.constants.
"""

from __future__ import annotations

from ai_datasets.loaders import constants


def test_supported_loaders() -> None:
    """Supported loaders should contain all loader types."""
    assert constants.LOADER_CSV in constants.SUPPORTED_LOADERS
    assert constants.LOADER_JSON in constants.SUPPORTED_LOADERS
    assert constants.LOADER_PARQUET in constants.SUPPORTED_LOADERS
    assert constants.LOADER_TEXT in constants.SUPPORTED_LOADERS
    assert constants.LOADER_DATABASE in constants.SUPPORTED_LOADERS


def test_file_extensions() -> None:
    """File extensions should match expected values."""
    assert constants.CSV_EXTENSION == ".csv"
    assert constants.JSON_EXTENSION == ".json"
    assert constants.PARQUET_EXTENSION == ".parquet"
    assert constants.TEXT_EXTENSION == ".txt"


def test_default_configuration() -> None:
    """Default loader configuration should be valid."""
    assert constants.DEFAULT_DELIMITER == ","
    assert constants.DEFAULT_ENCODING == "utf-8"
    assert constants.DEFAULT_BATCH_SIZE > 0
    assert constants.DEFAULT_HAS_HEADER is True


def test_database_defaults() -> None:
    """Database defaults should be positive."""
    assert constants.DEFAULT_FETCH_SIZE > 0
    assert constants.DEFAULT_CONNECTION_TIMEOUT > 0


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_SOURCE == "source"
    assert constants.METADATA_LOADER == "loader"
    assert constants.METADATA_RECORD_COUNT == "record_count"
    assert constants.METADATA_ENCODING == "encoding"
    assert constants.METADATA_DURATION == "duration_ms"