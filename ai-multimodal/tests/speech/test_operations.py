"""
Unit tests for ai_multimodal.speech.operations.
"""

from __future__ import annotations

import pytest

from ai_multimodal.speech.exceptions import (
    SSMLSynthesisError,
    SpeechValidationError,
    TextToSpeechError,
    UnsupportedAudioFormatError,
    UnsupportedLanguageError,
    VoiceCloningError,
)
from ai_multimodal.speech.operations import (
    SpeechResult,
    clone_voice,
    generate_speech,
    list_available_voices,
    stream_speech,
    synthesize_ssml,
)


def test_generate_speech_success() -> None:
    """Speech generation should succeed."""
    result = generate_speech("Hello World")

    assert isinstance(result, SpeechResult)
    assert result.success is True
    assert result.task == "text_to_speech"


def test_generate_invalid_audio_format() -> None:
    """Unsupported formats should raise."""
    with pytest.raises(UnsupportedAudioFormatError):
        generate_speech(
            "Hello",
            audio_format="xyz",
        )


def test_generate_invalid_language() -> None:
    """Unsupported languages should raise."""
    with pytest.raises(UnsupportedLanguageError):
        generate_speech(
            "Hello",
            language="xx",
        )


def test_generate_invalid_rate() -> None:
    """Invalid speech rate should raise."""
    with pytest.raises(TextToSpeechError):
        generate_speech(
            "Hello",
            speech_rate=5.0,
        )


def test_generate_empty_text() -> None:
    """Empty text should raise."""
    with pytest.raises(SpeechValidationError):
        generate_speech("")


def test_stream_speech_success() -> None:
    """Streaming speech should succeed."""
    result = stream_speech("Streaming text")

    assert result.success is True
    assert result.task == "streaming"


def test_synthesize_ssml_success() -> None:
    """SSML synthesis should succeed."""
    result = synthesize_ssml("<speak>Hello</speak>")

    assert result.success is True
    assert result.task == "ssml"


def test_synthesize_empty_ssml() -> None:
    """Empty SSML should raise."""
    with pytest.raises(SSMLSynthesisError):
        synthesize_ssml("")


def test_clone_voice_success() -> None:
    """Voice cloning should succeed."""
    result = clone_voice(
        "Assistant",
        "sample.wav",
    )

    assert result.success is True
    assert result.task == "voice_cloning"


def test_clone_voice_invalid_inputs() -> None:
    """Invalid cloning inputs should raise."""
    with pytest.raises(VoiceCloningError):
        clone_voice("", "sample.wav")


def test_list_available_voices() -> None:
    """Voice listing should succeed."""
    result = list_available_voices()

    assert result.success is True
    assert result.task == "list_voices"