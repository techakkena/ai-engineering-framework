"""
Exceptions for the ai_multimodal.audio package.

This module defines the exception hierarchy for provider-independent
audio processing operations.
"""

from __future__ import annotations


class AudioError(Exception):
    """Base exception for all audio-related errors."""


class AudioValidationError(AudioError):
    """Raised when audio input validation fails."""


class UnsupportedAudioFormatError(AudioValidationError):
    """Raised when an unsupported audio format is provided."""


class UnsupportedLanguageError(AudioValidationError):
    """Raised when an unsupported language is specified."""


class AudioProcessingError(AudioError):
    """Base exception for audio processing failures."""


class AudioTranscriptionError(AudioProcessingError):
    """Raised when audio transcription fails."""


class AudioTranslationError(AudioProcessingError):
    """Raised when audio translation fails."""


class AudioClassificationError(AudioProcessingError):
    """Raised when audio classification fails."""


class AudioAnalysisError(AudioProcessingError):
    """Raised when audio analysis fails."""


class AudioMetadataError(AudioProcessingError):
    """Raised when audio metadata extraction fails."""


class AudioProviderError(AudioError):
    """Raised when an underlying audio provider returns an error."""