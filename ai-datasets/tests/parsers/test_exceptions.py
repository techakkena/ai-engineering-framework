"""
Unit tests for ai_datasets.parsers.exceptions.
"""

from __future__ import annotations

import pytest

from ai_datasets.parsers.exceptions import (
    CSVParserError,
    DatasetParserError,
    DatasetParsingError,
    DatasetSchemaError,
    JSONLParserError,
    JSONParserError,
    ParserValidationError,
    ParquetParserError,
    UnsupportedParserError,
    XMLParserError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        ParserValidationError,
        UnsupportedParserError,
        DatasetParsingError,
        CSVParserError,
        JSONParserError,
        JSONLParserError,
        ParquetParserError,
        XMLParserError,
        DatasetSchemaError,
    ],
)
def test_exception_inheritance(
    exception_class: type[DatasetParserError],
) -> None:
    """Every custom exception should inherit from DatasetParserError."""
    assert issubclass(
        exception_class,
        DatasetParserError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        DatasetParserError,
        match="parser failure",
    ):
        raise DatasetParserError(
            "parser failure",
        )