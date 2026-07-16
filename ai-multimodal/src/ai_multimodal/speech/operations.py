"""
Enterprise speech operations for the ai_multimodal.speech package.

This module provides provider-independent abstractions for text-to-speech,
speech streaming, SSML synthesis, voice cloning, and voice discovery.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_multimodal.speech.constants import (
    DEFAULT_AUDIO_FORMAT,
    DEFAULT_LANGUAGE,
    DEFAULT_PITCH,
    DEFAULT_SPEECH_RATE,
    DEFAULT_VOICE,
    DEFAULT_VOLUME,
    MAX_PITCH,
    MAX_SPEECH_RATE,
    MAX_VOLUME,
    MIN_PITCH,
    MIN_SPEECH_RATE,
    MIN_VOLUME,
    SUPPORTED_AUDIO_FORMATS,
    SUPPORTED_LANGUAGES,
)
from ai_multimodal.speech.exceptions import (
    SSMLSynthesisError,
    SpeechValidationError,
    TextToSpeechError,
    UnsupportedAudioFormatError,
    UnsupportedLanguageError,
    VoiceCloningError,
)


@dataclass(slots=True, frozen=True)
class SpeechResult:
    """Represents the result of a speech operation."""

    task: str
    success: bool
    data: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


def _validate_text(text: str) -> None:
    """Validate text input."""
    if not text.strip():
        raise SpeechValidationError("Text cannot be empty.")


def _validate_audio_format(audio_format: str) -> None:
    """Validate an audio output format."""
    if audio_format.lower() not in SUPPORTED_AUDIO_FORMATS:
        raise UnsupportedAudioFormatError(
            f"Unsupported audio format: {audio_format!r}."
        )


def _validate_language(language: str) -> None:
    """Validate a language code."""
    if language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageError(
            f"Unsupported language: {language!r}."
        )


def generate_speech(
    text: str,
    *,
    voice: str = DEFAULT_VOICE,
    language: str = DEFAULT_LANGUAGE,
    audio_format: str = DEFAULT_AUDIO_FORMAT,
    speech_rate: float = DEFAULT_SPEECH_RATE,
    volume: float = DEFAULT_VOLUME,
    pitch: float = DEFAULT_PITCH,
) -> SpeechResult:
    """
    Generate speech from text.
    """
    _validate_text(text)
    _validate_audio_format(audio_format)
    _validate_language(language)

    if not MIN_SPEECH_RATE <= speech_rate <= MAX_SPEECH_RATE:
        raise TextToSpeechError("Invalid speech rate.")

    if not MIN_VOLUME <= volume <= MAX_VOLUME:
        raise TextToSpeechError("Invalid volume.")

    if not MIN_PITCH <= pitch <= MAX_PITCH:
        raise TextToSpeechError("Invalid pitch.")

    return SpeechResult(
        task="text_to_speech",
        success=True,
        data={
            "text": text,
            "voice": voice,
            "language": language,
            "audio_format": audio_format,
        },
    )


def stream_speech(text: str) -> SpeechResult:
    """
    Stream synthesized speech.
    """
    _validate_text(text)

    return SpeechResult(
        task="streaming",
        success=True,
        data={"text": text},
    )


def synthesize_ssml(ssml: str) -> SpeechResult:
    """
    Synthesize speech from SSML.
    """
    if not ssml.strip():
        raise SSMLSynthesisError("SSML cannot be empty.")

    return SpeechResult(
        task="ssml",
        success=True,
        data={"ssml": ssml},
    )


def clone_voice(
    voice_name: str,
    sample_audio_path: str,
) -> SpeechResult:
    """
    Clone a voice from an audio sample.
    """
    if not voice_name.strip():
        raise VoiceCloningError("Voice name cannot be empty.")

    if not sample_audio_path.strip():
        raise VoiceCloningError("Sample audio path cannot be empty.")

    return SpeechResult(
        task="voice_cloning",
        success=True,
        data={
            "voice_name": voice_name,
            "sample_audio_path": sample_audio_path,
        },
    )


def list_available_voices() -> SpeechResult:
    """
    Return the list of available voices.

    Placeholder implementation for provider integrations.
    """
    return SpeechResult(
        task="list_voices",
        success=True,
        data={
            "voices": [
                DEFAULT_VOICE,
            ],
        },
    )