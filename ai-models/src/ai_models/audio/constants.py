"""
Constants for ai_models.audio.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Defaults
# ============================================================================

DEFAULT_AUDIO_MODEL: Final[str] = "gpt-4o-mini-transcribe"

DEFAULT_AUDIO_PROVIDER: Final[str] = "openai"

DEFAULT_AUDIO_RESPONSE_FORMAT: Final[str] = "text"

# ============================================================================
# Providers
# ============================================================================

OPENAI: Final[str] = "openai"

ELEVENLABS: Final[str] = "elevenlabs"

ASSEMBLYAI: Final[str] = "assemblyai"

DEEPGRAM: Final[str] = "deepgram"

GOOGLE: Final[str] = "google"

AZURE: Final[str] = "azure"

SUPPORTED_AUDIO_PROVIDERS: Final[frozenset[str]] = frozenset(
    {
        OPENAI,
        ELEVENLABS,
        ASSEMBLYAI,
        DEEPGRAM,
        GOOGLE,
        AZURE,
    }
)

# ============================================================================
# Audio Formats
# ============================================================================

TEXT_FORMAT: Final[str] = "text"

JSON_FORMAT: Final[str] = "json"

SRT_FORMAT: Final[str] = "srt"

VTT_FORMAT: Final[str] = "vtt"

SUPPORTED_AUDIO_RESPONSE_FORMATS: Final[
    frozenset[str]
] = frozenset(
    {
        TEXT_FORMAT,
        JSON_FORMAT,
        SRT_FORMAT,
        VTT_FORMAT,
    }
)

# ============================================================================
# Configuration
# ============================================================================

DEFAULT_TIMEOUT: Final[int] = 60

DEFAULT_RETRIES: Final[int] = 3

DEFAULT_SAMPLE_RATE: Final[int] = 16000