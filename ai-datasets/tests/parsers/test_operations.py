"""
Unit tests for ai_datasets.parsers.operations.
"""

from __future__ import annotations

import pytest

from ai_datasets.parsers.exceptions import (
    CSVParserError,
    ParserValidationError,
)
from ai_datasets.parsers.operations import (
    ParserResult,
    parse_csv,
    parse_json,
    parse_jsonl,
    parse_parquet,
    parse_xml,
)


def test_parse_csv_success() -> None:
    """CSV parsing should succeed."""
    result = parse_csv("id,name\n1,Alice")

    assert isinstance(result, ParserResult)
    assert result.success is True
    assert result.task == "parse_csv"


def test_parse_csv_invalid_delimiter() -> None:
    """Empty delimiters should raise."""
    with pytest.raises(CSVParserError):
        parse_csv(
            "id,name",
            delimiter="",
        )


def test_parse_csv_empty_content() -> None:
    """Empty content should raise."""
    with pytest.raises(ParserValidationError):
        parse_csv("")


def test_parse_json_success() -> None:
    """JSON parsing should succeed."""
    result = parse_json('{"id": 1}')

    assert result.success is True
    assert result.task == "parse_json"


def test_parse_jsonl_success() -> None:
    """JSONL parsing should succeed."""
    result = parse_jsonl('{"id":1}')

    assert result.success is True
    assert result.task == "parse_jsonl"


def test_parse_parquet_success() -> None:
    """Parquet parsing should succeed."""
    result = parse_parquet("dataset.parquet")

    assert result.success is True
    assert result.task == "parse_parquet"


def test_parse_xml_success() -> None:
    """XML parsing should succeed."""
    result = parse_xml("<root></root>")

    assert result.success is True
    assert result.task == "parse_xml"


def test_parse_json_empty_content() -> None:
    """Empty JSON content should raise."""
    with pytest.raises(ParserValidationError):
        parse_json("")


def test_parse_jsonl_empty_content() -> None:
    """Empty JSONL content should raise."""
    with pytest.raises(ParserValidationError):
        parse_jsonl("")


def test_parse_xml_empty_content() -> None:
    """Empty XML content should raise."""
    with pytest.raises(ParserValidationError):
        parse_xml("")