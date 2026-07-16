"""
Constants for the ai_multimodal.document module.

This module defines framework-independent constants used by document
processing operations throughout the AI Engineering Framework.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Supported document formats
# ---------------------------------------------------------------------------

SUPPORTED_DOCUMENT_FORMATS: Final[tuple[str, ...]] = (
    "pdf",
    "docx",
    "doc",
    "txt",
    "rtf",
    "odt",
    "html",
    "md",
)

DEFAULT_DOCUMENT_FORMAT: Final[str] = "pdf"

# ---------------------------------------------------------------------------
# Document tasks
# ---------------------------------------------------------------------------

TASK_PARSE: Final[str] = "parse"
TASK_CLASSIFICATION: Final[str] = "classification"
TASK_SUMMARIZATION: Final[str] = "summarization"
TASK_EXTRACTION: Final[str] = "extraction"
TASK_METADATA: Final[str] = "metadata"

SUPPORTED_TASKS: Final[tuple[str, ...]] = (
    TASK_PARSE,
    TASK_CLASSIFICATION,
    TASK_SUMMARIZATION,
    TASK_EXTRACTION,
    TASK_METADATA,
)

# ---------------------------------------------------------------------------
# OCR
# ---------------------------------------------------------------------------

DEFAULT_LANGUAGE: Final[str] = "en"

SUPPORTED_LANGUAGES: Final[tuple[str, ...]] = (
    "en",
    "es",
    "fr",
    "de",
    "it",
    "pt",
    "ja",
    "ko",
    "zh",
)

# ---------------------------------------------------------------------------
# Limits
# ---------------------------------------------------------------------------

MAX_DOCUMENT_SIZE_MB: Final[int] = 100
MAX_DOCUMENT_PAGES: Final[int] = 5000

DEFAULT_CHUNK_SIZE: Final[int] = 1000
DEFAULT_CHUNK_OVERLAP: Final[int] = 200

# ---------------------------------------------------------------------------
# Confidence
# ---------------------------------------------------------------------------

DEFAULT_CONFIDENCE_THRESHOLD: Final[float] = 0.50
MIN_CONFIDENCE_THRESHOLD: Final[float] = 0.00
MAX_CONFIDENCE_THRESHOLD: Final[float] = 1.00

# ---------------------------------------------------------------------------
# Metadata keys
# ---------------------------------------------------------------------------

METADATA_PROVIDER: Final[str] = "provider"
METADATA_MODEL: Final[str] = "model"
METADATA_PAGE_COUNT: Final[str] = "page_count"
METADATA_LANGUAGE: Final[str] = "language"
METADATA_LATENCY: Final[str] = "latency_ms"