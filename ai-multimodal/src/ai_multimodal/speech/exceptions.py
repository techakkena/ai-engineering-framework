"""
Exceptions for the ai_multimodal.speech package.

This module defines the exception hierarchy for provider-independent
speech synthesis operations.
"""

from __future__ import annotations


class SpeechError(Exception):
    """Base exception for all speech-related errors."""


class SpeechValidationError(SpeechError):
    """Raised when speech input validation fails."""


class UnsupportedAudioFormatError(SpeechValidationError):
    """Raised when an unsupported audio output format is requested."""


class UnsupportedLanguageError(SpeechValidationError):
    """Raised when an unsupported language is specified."""


class UnsupportedVoiceError(SpeechValidationError):
    """Raised when an unsupported voice is requested."""


class SpeechProcessingError(SpeechError):
    """Base exception for speech processing failures."""


class TextToSpeechError(SpeechProcessingError):
    """Raised when text-to-speech synthesis fails."""


class StreamingSpeechError(SpeechProcessingError):
    """Raised when streaming speech generation fails."""


class SSMLSynthesisError(SpeechProcessingError):
    """Raised when SSML synthesis fails."""


class VoiceCloningError(SpeechProcessingError):
    """Raised when voice cloning fails."""


class VoiceListingError(SpeechProcessingError):
    """Raised when retrieving available voices fails."""


class SpeechProviderError(SpeechError):
    """Raised when an underlying speech provider returns an error."""