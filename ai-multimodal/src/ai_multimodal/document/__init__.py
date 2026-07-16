"""
ai_multimodal.document

Enterprise document intelligence module for the AI Engineering Framework.

This package provides provider-independent abstractions for AI-powered
document processing including parsing, OCR, classification, summarization,
information extraction, and metadata retrieval.

Modules
-------
constants
    Document-related constants and defaults.

exceptions
    Document-specific exception hierarchy.

operations
    High-level document operations.

Design Goals
------------
- Framework independent
- SOLID compliant
- Fully typed
- Enterprise documented
- Production ready
"""

from ai_multimodal.document.operations import (
    classify_document,
    extract_document_data,
    get_document_metadata,
    parse_document,
    summarize_document,
)

__all__ = [
    "parse_document",
    "classify_document",
    "summarize_document",
    "extract_document_data",
    "get_document_metadata",
]