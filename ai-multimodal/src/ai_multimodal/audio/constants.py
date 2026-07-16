"""
Constants for the ai_multimodal.audio module.

This module defines framework-independent constants used by audio
operations throughout the AI Engineering Framework.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Supported audio formats
# ---------------------------------------------------------------------------

SUPPORTED_AUDIO_FORMATS: Final[tuple[str, ...]] = (
    "mp3",
    "wav",
    "flac",
    "aac",
    "ogg",
    "m4a",
    "webm",
)

DEFAULT_AUDIO_FORMAT: Final[str] = "mp3"

# ---------------------------------------------------------------------------
# Audio tasks
# ---------------------------------------------------------------------------

TASK_TRANSCRIPTION: Final[str] = "transcription"
TASK_TRANSLATION: Final[str] = "translation"
TASK_CLASSIFICATION: Final[str] = "classification"
TASK_ANALYSIS: Final[str] = "analysis"
TASK_METADATA: Final[str] = "metadata"

SUPPORTED_TASKS: Final[tuple[str, ...]] = (
    TASK_TRANSCRIPTION,
    TASK_TRANSLATION,
    TASK_CLASSIFICATION,
    TASK_ANALYSIS,
    TASK_METADATA,
)

# ---------------------------------------------------------------------------
# Language defaults
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
# Audio constraints
# ---------------------------------------------------------------------------

DEFAULT_SAMPLE_RATE: Final[int] = 16000
DEFAULT_BIT_DEPTH: Final[int] = 16
DEFAULT_CHANNELS: Final[int] = 1

MAX_AUDIO_DURATION_SECONDS: Final[int] = 3600
MAX_AUDIO_SIZE_MB: Final[int] = 100

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
METADATA_SAMPLE_RATE: Final[str] = "sample_rate"
METADATA_LATENCY: Final[str] = "latency_ms"