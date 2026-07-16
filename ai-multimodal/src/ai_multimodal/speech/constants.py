"""
Constants for the ai_multimodal.speech module.

This module contains framework-independent constants used by speech synthesis
operations throughout the AI Engineering Framework.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Supported audio output formats
# ---------------------------------------------------------------------------

SUPPORTED_AUDIO_FORMATS: Final[tuple[str, ...]] = (
    "mp3",
    "wav",
    "pcm",
    "opus",
    "aac",
    "flac",
)

DEFAULT_AUDIO_FORMAT: Final[str] = "mp3"

# ---------------------------------------------------------------------------
# Supported synthesis tasks
# ---------------------------------------------------------------------------

TASK_TEXT_TO_SPEECH: Final[str] = "text_to_speech"
TASK_STREAMING: Final[str] = "streaming"
TASK_SSML: Final[str] = "ssml"
TASK_VOICE_CLONING: Final[str] = "voice_cloning"
TASK_LIST_VOICES: Final[str] = "list_voices"

SUPPORTED_TASKS: Final[tuple[str, ...]] = (
    TASK_TEXT_TO_SPEECH,
    TASK_STREAMING,
    TASK_SSML,
    TASK_VOICE_CLONING,
    TASK_LIST_VOICES,
)

# ---------------------------------------------------------------------------
# Voice defaults
# ---------------------------------------------------------------------------

DEFAULT_VOICE: Final[str] = "default"

SUPPORTED_GENDERS: Final[tuple[str, ...]] = (
    "male",
    "female",
    "neutral",
)

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
# Speech configuration
# ---------------------------------------------------------------------------

DEFAULT_SAMPLE_RATE: Final[int] = 24000

DEFAULT_SPEECH_RATE: Final[float] = 1.0
MIN_SPEECH_RATE: Final[float] = 0.5
MAX_SPEECH_RATE: Final[float] = 2.0

DEFAULT_VOLUME: Final[float] = 1.0
MIN_VOLUME: Final[float] = 0.0
MAX_VOLUME: Final[float] = 2.0

DEFAULT_PITCH: Final[float] = 0.0
MIN_PITCH: Final[float] = -20.0
MAX_PITCH: Final[float] = 20.0

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

METADATA_PROVIDER: Final[str] = "provider"
METADATA_MODEL: Final[str] = "model"
METADATA_DURATION: Final[str] = "duration_seconds"
METADATA_LATENCY: Final[str] = "latency_ms"