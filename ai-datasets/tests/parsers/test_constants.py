"""
Unit tests for ai_datasets.parsers.constants.
"""

from __future__ import annotations

from ai_datasets.parsers import constants


def test_supported_parsers() -> None:
    """Supported parsers should contain all parser types."""
    assert constants.PARSER_CSV in constants.SUPPORTED_PARSERS
    assert constants.PARSER_JSON in constants.SUPPORTED_PARSERS
    assert constants.PARSER_JSONL in constants.SUPPORTED_PARSERS
    assert constants.PARSER_PARQUET in constants.SUPPORTED_PARSERS
    assert constants.PARSER_XML in constants.SUPPORTED_PARSERS


def test_default_configuration() -> None:
    """Default parser configuration should be valid."""
    assert constants.DEFAULT_DELIMITER == ","
    assert constants.DEFAULT_ENCODING == "utf-8"
    assert constants.DEFAULT_BATCH_SIZE > 0
    assert constants.DEFAULT_INDENT > 0
    assert constants.DEFAULT_STRICT_MODE is True


def test_default_xml_root() -> None:
    """XML root should be configured."""
    assert constants.DEFAULT_XML_ROOT == "root"


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_SOURCE == "source"
    assert constants.METADATA_PARSER == "parser"
    assert constants.METADATA_RECORD_COUNT == "record_count"
    assert constants.METADATA_ENCODING == "encoding"
    assert constants.METADATA_DURATION == "duration_ms"