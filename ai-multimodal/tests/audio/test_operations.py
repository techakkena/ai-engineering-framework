"""
Unit tests for ai_multimodal.audio.operations.
"""

from __future__ import annotations

import pytest

from ai_multimodal.audio.exceptions import (
    AudioClassificationError,
    AudioValidationError,
    UnsupportedAudioFormatError,
    UnsupportedLanguageError,
)
from ai_multimodal.audio.operations import (
    AudioResult,
    analyze_audio,
    classify_audio,
    extract_audio_metadata,
    transcribe_audio,
    translate_audio,
)


def test_transcribe_audio_success() -> None:
    """Audio transcription should succeed."""
    result = transcribe_audio("audio.mp3")

    assert isinstance(result, AudioResult)
    assert result.success is True
    assert result.task == "transcription"


def test_transcribe_invalid_format() -> None:
    """Unsupported audio formats should raise."""
    with pytest.raises(UnsupportedAudioFormatError):
        transcribe_audio(
            "audio.xyz",
            audio_format="xyz",
        )


def test_transcribe_invalid_language() -> None:
    """Unsupported languages should raise."""
    with pytest.raises(UnsupportedLanguageError):
        transcribe_audio(
            "audio.mp3",
            language="xx",
        )


def test_transcribe_empty_path() -> None:
    """Empty audio paths should raise."""
    with pytest.raises(AudioValidationError):
        transcribe_audio("")


def test_translate_audio_success() -> None:
    """Audio translation should succeed."""
    result = translate_audio("audio.mp3")

    assert result.success is True
    assert result.task == "translation"


def test_translate_invalid_language() -> None:
    """Invalid translation language should raise."""
    with pytest.raises(UnsupportedLanguageError):
        translate_audio(
            "audio.mp3",
            target_language="xx",
        )


def test_classify_audio_success() -> None:
    """Audio classification should succeed."""
    result = classify_audio("audio.mp3")

    assert result.success is True
    assert result.task == "classification"


def test_classify_invalid_threshold() -> None:
    """Invalid confidence threshold should raise."""
    with pytest.raises(AudioClassificationError):
        classify_audio(
            "audio.mp3",
            confidence_threshold=2.0,
        )


def test_analyze_audio_success() -> None:
    """Audio analysis should succeed."""
    result = analyze_audio("audio.mp3")

    assert result.success is True
    assert result.task == "analysis"


def test_extract_audio_metadata_success() -> None:
    """Metadata extraction should succeed."""
    result = extract_audio_metadata("audio.mp3")

    assert result.success is True
    assert result.task == "metadata"