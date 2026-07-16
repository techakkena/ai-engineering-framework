"""
ai_datasets.parsers

Enterprise dataset parser module for the AI Engineering Framework.

This package provides provider-independent parsing capabilities for
structured and semi-structured datasets including CSV, JSON, JSONL,
Parquet, XML, and custom formats.

Modules
-------
constants
    Parser-specific constants.

exceptions
    Parser-specific exception hierarchy.

operations
    High-level dataset parsing operations.

Design Goals
------------
- Framework independent
- SOLID compliant
- Fully typed
- Enterprise documented
- Production ready
"""

from ai_datasets.parsers.operations import (
    parse_csv,
    parse_json,
    parse_jsonl,
    parse_parquet,
    parse_xml,
)

__all__ = [
    "parse_csv",
    "parse_json",
    "parse_jsonl",
    "parse_parquet",
    "parse_xml",
]