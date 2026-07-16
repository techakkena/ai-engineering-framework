"""
Constants for the ai_multimodal.vision module.

This module contains framework-independent constants used by vision
operations throughout the AI Engineering Framework.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Supported image formats
# ---------------------------------------------------------------------------

SUPPORTED_IMAGE_FORMATS: Final[tuple[str, ...]] = (
    "png",
    "jpg",
    "jpeg",
    "webp",
    "bmp",
    "gif",
    "tiff",
)

# ---------------------------------------------------------------------------
# Vision task names
# ---------------------------------------------------------------------------

TASK_CLASSIFICATION: Final[str] = "classification"
TASK_OBJECT_DETECTION: Final[str] = "object_detection"
TASK_IMAGE_CAPTIONING: Final[str] = "image_captioning"
TASK_OCR: Final[str] = "ocr"
TASK_VISUAL_QA: Final[str] = "visual_question_answering"

SUPPORTED_TASKS: Final[tuple[str, ...]] = (
    TASK_CLASSIFICATION,
    TASK_OBJECT_DETECTION,
    TASK_IMAGE_CAPTIONING,
    TASK_OCR,
    TASK_VISUAL_QA,
)

# ---------------------------------------------------------------------------
# Confidence thresholds
# ---------------------------------------------------------------------------

DEFAULT_CONFIDENCE_THRESHOLD: Final[float] = 0.50
MIN_CONFIDENCE_THRESHOLD: Final[float] = 0.00
MAX_CONFIDENCE_THRESHOLD: Final[float] = 1.00

# ---------------------------------------------------------------------------
# Image constraints
# ---------------------------------------------------------------------------

DEFAULT_MAX_IMAGE_SIZE_MB: Final[int] = 25
DEFAULT_MAX_WIDTH: Final[int] = 8192
DEFAULT_MAX_HEIGHT: Final[int] = 8192

# ---------------------------------------------------------------------------
# OCR
# ---------------------------------------------------------------------------

DEFAULT_LANGUAGE: Final[str] = "en"

SUPPORTED_LANGUAGES: Final[tuple[str, ...]] = (
    "en",
    "fr",
    "de",
    "es",
    "it",
    "pt",
    "ja",
    "ko",
    "zh",
)

# ---------------------------------------------------------------------------
# Response limits
# ---------------------------------------------------------------------------

DEFAULT_MAX_LABELS: Final[int] = 10
DEFAULT_MAX_OBJECTS: Final[int] = 100

# ---------------------------------------------------------------------------
# Metadata keys
# ---------------------------------------------------------------------------

METADATA_PROVIDER: Final[str] = "provider"
METADATA_MODEL: Final[str] = "model"
METADATA_LATENCY: Final[str] = "latency_ms"
METADATA_CONFIDENCE: Final[str] = "confidence"