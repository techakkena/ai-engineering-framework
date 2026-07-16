"""
Unit tests for ai_multimodal.speech.constants.
"""

from __future__ import annotations

from ai_multimodal.speech import constants


def test_supported_audio_formats() -> None:
    """Supported audio formats should contain common formats."""
    assert "mp3" in constants.SUPPORTED_AUDIO_FORMATS
    assert "wav" in constants.SUPPORTED_AUDIO_FORMATS
    assert "pcm" in constants.SUPPORTED_AUDIO_FORMATS


def test_default_audio_format() -> None:
    """Default audio format should be supported."""
    assert constants.DEFAULT_AUDIO_FORMAT == "mp3"


def test_supported_tasks() -> None:
    """All speech tasks should be registered."""
    assert constants.TASK_TEXT_TO_SPEECH in constants.SUPPORTED_TASKS
    assert constants.TASK_STREAMING in constants.SUPPORTED_TASKS
    assert constants.TASK_SSML in constants.SUPPORTED_TASKS
    assert constants.TASK_VOICE_CLONING in constants.SUPPORTED_TASKS
    assert constants.TASK_LIST_VOICES in constants.SUPPORTED_TASKS


def test_default_language() -> None:
    """Default language should be supported."""
    assert constants.DEFAULT_LANGUAGE == "en"
    assert constants.DEFAULT_LANGUAGE in constants.SUPPORTED_LANGUAGES


def test_voice_defaults() -> None:
    """Voice defaults should be valid."""
    assert constants.DEFAULT_VOICE == "default"
    assert "male" in constants.SUPPORTED_GENDERS
    assert "female" in constants.SUPPORTED_GENDERS
    assert "neutral" in constants.SUPPORTED_GENDERS


def test_speech_rate_limits() -> None:
    """Speech rate values should be valid."""
    assert (
        constants.MIN_SPEECH_RATE
        < constants.DEFAULT_SPEECH_RATE
        < constants.MAX_SPEECH_RATE
    )


def test_volume_limits() -> None:
    """Volume values should be valid."""
    assert (
        constants.MIN_VOLUME
        <= constants.DEFAULT_VOLUME
        <= constants.MAX_VOLUME
    )


def test_pitch_limits() -> None:
    """Pitch values should be valid."""
    assert (
        constants.MIN_PITCH
        <= constants.DEFAULT_PITCH
        <= constants.MAX_PITCH
    )


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_PROVIDER == "provider"
    assert constants.METADATA_MODEL == "model"
    assert constants.METADATA_DURATION == "duration_seconds"
    assert constants.METADATA_LATENCY == "latency_ms"