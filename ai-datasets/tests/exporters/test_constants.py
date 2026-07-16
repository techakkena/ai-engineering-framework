"""
Unit tests for ai_datasets.exporters.constants.
"""

from __future__ import annotations

from ai_datasets.exporters import constants


def test_supported_export_formats() -> None:
    """Supported export formats should contain all export types."""
    assert constants.EXPORT_CSV in constants.SUPPORTED_EXPORT_FORMATS
    assert constants.EXPORT_JSON in constants.SUPPORTED_EXPORT_FORMATS
    assert constants.EXPORT_PARQUET in constants.SUPPORTED_EXPORT_FORMATS
    assert constants.EXPORT_EXCEL in constants.SUPPORTED_EXPORT_FORMATS


def test_default_configuration() -> None:
    """Default exporter configuration should be valid."""
    assert constants.DEFAULT_ENCODING == "utf-8"
    assert constants.DEFAULT_DELIMITER == ","
    assert constants.DEFAULT_OVERWRITE is False


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_FORMAT == "format"
    assert constants.METADATA_RECORD_COUNT == "record_count"
    assert constants.METADATA_OUTPUT_PATH == "output_path"
    assert constants.METADATA_DURATION == "duration_ms"