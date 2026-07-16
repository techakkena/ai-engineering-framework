"""
Unit tests for ai_multimodal.speech.exceptions.
"""

from __future__ import annotations

import pytest

from ai_multimodal.speech.exceptions import (
    SpeechError,
    SpeechProcessingError,
    SpeechProviderError,
    SpeechValidationError,
    SSMLSynthesisError,
    StreamingSpeechError,
    TextToSpeechError,
    UnsupportedAudioFormatError,
    UnsupportedLanguageError,
    UnsupportedVoiceError,
    VoiceCloningError,
    VoiceListingError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        SpeechValidationError,
        UnsupportedAudioFormatError,
        UnsupportedLanguageError,
        UnsupportedVoiceError,
        SpeechProcessingError,
        TextToSpeechError,
        StreamingSpeechError,
        SSMLSynthesisError,
        VoiceCloningError,
        VoiceListingError,
        SpeechProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[SpeechError],
) -> None:
    """Every custom exception should inherit from SpeechError."""
    assert issubclass(exception_class, SpeechError)


def test_exception_message() -> None:
    """Exception message should be preserved."""
    with pytest.raises(SpeechError, match="speech failure"):
        raise SpeechError("speech failure")