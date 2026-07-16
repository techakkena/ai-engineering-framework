"""
Constants for the ai_multimodal.video module.

This module contains framework-independent constants used by video
operations throughout the AI Engineering Framework.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Supported video formats
# ---------------------------------------------------------------------------

SUPPORTED_VIDEO_FORMATS: Final[tuple[str, ...]] = (
    "mp4",
    "mov",
    "avi",
    "mkv",
    "webm",
    "mpeg",
)

DEFAULT_VIDEO_FORMAT: Final[str] = "mp4"

# ---------------------------------------------------------------------------
# Video tasks
# ---------------------------------------------------------------------------

TASK_ANALYSIS: Final[str] = "analysis"
TASK_SUMMARIZATION: Final[str] = "summarization"
TASK_FRAME_EXTRACTION: Final[str] = "frame_extraction"
TASK_TRANSCRIPTION: Final[str] = "transcription"
TASK_METADATA: Final[str] = "metadata"

SUPPORTED_TASKS: Final[tuple[str, ...]] = (
    TASK_ANALYSIS,
    TASK_SUMMARIZATION,
    TASK_FRAME_EXTRACTION,
    TASK_TRANSCRIPTION,
    TASK_METADATA,
)

# ---------------------------------------------------------------------------
# Video constraints
# ---------------------------------------------------------------------------

DEFAULT_FRAME_RATE: Final[int] = 30
DEFAULT_FRAME_INTERVAL_SECONDS: Final[int] = 1

MAX_VIDEO_DURATION_SECONDS: Final[int] = 7200
MAX_VIDEO_SIZE_MB: Final[int] = 1024

DEFAULT_MAX_FRAMES: Final[int] = 1000

# ---------------------------------------------------------------------------
# Transcription
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
# Confidence thresholds
# ---------------------------------------------------------------------------

DEFAULT_CONFIDENCE_THRESHOLD: Final[float] = 0.50
MIN_CONFIDENCE_THRESHOLD: Final[float] = 0.00
MAX_CONFIDENCE_THRESHOLD: Final[float] = 1.00

# ---------------------------------------------------------------------------
# Metadata keys
# ---------------------------------------------------------------------------

METADATA_PROVIDER: Final[str] = "provider"
METADATA_MODEL: Final[str] = "model"
METADATA_DURATION: Final[str] = "duration_seconds"
METADATA_FRAME_RATE: Final[str] = "frame_rate"
METADATA_LATENCY: Final[str] = "latency_ms"