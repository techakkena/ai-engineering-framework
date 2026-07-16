"""
Unit tests for ai_multimodal.audio.exceptions.
"""

from __future__ import annotations

import pytest

from ai_multimodal.audio.exceptions import (
    AudioAnalysisError,
    AudioClassificationError,
    AudioError,
    AudioMetadataError,
    AudioProcessingError,
    AudioProviderError,
    AudioTranscriptionError,
    AudioTranslationError,
    AudioValidationError,
    UnsupportedAudioFormatError,
    UnsupportedLanguageError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        AudioValidationError,
        UnsupportedAudioFormatError,
        UnsupportedLanguageError,
        AudioProcessingError,
        AudioTranscriptionError,
        AudioTranslationError,
        AudioClassificationError,
        AudioAnalysisError,
        AudioMetadataError,
        AudioProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[AudioError],
) -> None:
    """Every custom exception should inherit from AudioError."""
    assert issubclass(exception_class, AudioError)


def test_exception_message() -> None:
    """Exception message should be preserved."""
    with pytest.raises(AudioError, match="audio failure"):
        raise AudioError("audio failure")