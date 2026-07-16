"""
Unit tests for ai_multimodal.document.constants.
"""

from __future__ import annotations

from ai_multimodal.document import constants


def test_supported_document_formats() -> None:
    """Supported document formats should contain common formats."""
    assert "pdf" in constants.SUPPORTED_DOCUMENT_FORMATS
    assert "docx" in constants.SUPPORTED_DOCUMENT_FORMATS
    assert "txt" in constants.SUPPORTED_DOCUMENT_FORMATS
    assert "md" in constants.SUPPORTED_DOCUMENT_FORMATS


def test_default_document_format() -> None:
    """Default document format should be supported."""
    assert constants.DEFAULT_DOCUMENT_FORMAT == "pdf"
    assert (
        constants.DEFAULT_DOCUMENT_FORMAT
        in constants.SUPPORTED_DOCUMENT_FORMATS
    )


def test_supported_tasks() -> None:
    """Supported tasks should contain all exported tasks."""
    assert constants.TASK_PARSE in constants.SUPPORTED_TASKS
    assert constants.TASK_CLASSIFICATION in constants.SUPPORTED_TASKS
    assert constants.TASK_SUMMARIZATION in constants.SUPPORTED_TASKS
    assert constants.TASK_EXTRACTION in constants.SUPPORTED_TASKS
    assert constants.TASK_METADATA in constants.SUPPORTED_TASKS


def test_default_language() -> None:
    """Default language should be supported."""
    assert constants.DEFAULT_LANGUAGE == "en"
    assert constants.DEFAULT_LANGUAGE in constants.SUPPORTED_LANGUAGES


def test_document_limits() -> None:
    """Document limits should be positive."""
    assert constants.MAX_DOCUMENT_SIZE_MB > 0
    assert constants.MAX_DOCUMENT_PAGES > 0


def test_chunk_configuration() -> None:
    """Chunk configuration should be valid."""
    assert constants.DEFAULT_CHUNK_SIZE > 0
    assert constants.DEFAULT_CHUNK_OVERLAP >= 0
    assert (
        constants.DEFAULT_CHUNK_OVERLAP
        < constants.DEFAULT_CHUNK_SIZE
    )


def test_confidence_thresholds() -> None:
    """Confidence thresholds should be valid."""
    assert constants.MIN_CONFIDENCE_THRESHOLD == 0.0
    assert constants.DEFAULT_CONFIDENCE_THRESHOLD == 0.5
    assert constants.MAX_CONFIDENCE_THRESHOLD == 1.0


def test_metadata_keys() -> None:
    """Metadata keys should match expected values."""
    assert constants.METADATA_PROVIDER == "provider"
    assert constants.METADATA_MODEL == "model"
    assert constants.METADATA_PAGE_COUNT == "page_count"
    assert constants.METADATA_LANGUAGE == "language"
    assert constants.METADATA_LATENCY == "latency_ms"