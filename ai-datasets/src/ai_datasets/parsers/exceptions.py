"""
Exceptions for the ai_datasets.parsers package.

This module defines the exception hierarchy for provider-independent
dataset parsing operations.
"""

from __future__ import annotations


class DatasetParserError(Exception):
    """Base exception for all dataset parser errors."""


class ParserValidationError(DatasetParserError):
    """Raised when parser input validation fails."""


class UnsupportedParserError(ParserValidationError):
    """Raised when an unsupported parser is requested."""


class DatasetParsingError(DatasetParserError):
    """Base exception for dataset parsing failures."""


class CSVParserError(DatasetParsingError):
    """Raised when CSV parsing fails."""


class JSONParserError(DatasetParsingError):
    """Raised when JSON parsing fails."""


class JSONLParserError(DatasetParsingError):
    """Raised when JSONL parsing fails."""


class ParquetParserError(DatasetParsingError):
    """Raised when Parquet parsing fails."""


class XMLParserError(DatasetParsingError):
    """Raised when XML parsing fails."""


class DatasetSchemaError(DatasetParserError):
    """Raised when dataset schema validation fails."""