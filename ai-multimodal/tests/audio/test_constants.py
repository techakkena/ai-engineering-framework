"""
Unit tests for ai_multimodal.audio.constants.
"""

from __future__ import annotations

from ai_multimodal.audio import constants


def test_supported_audio_formats() -> None:
    """Supported audio formats should contain common formats."""
    assert "mp3" in constants.SUPPORTED_AUDIO_FORMATS
    assert "wav" in constants.SUPPORTED_AUDIO_FORMATS
    assert "flac" in constants.SUPPORTED_AUDIO_FORMATS
    assert "m4a" in constants.SUPPORTED_AUDIO_FORMATS


def test_default_audio_format() -> None:
    """Default audio format should be supported."""
    assert constants.DEFAULT_AUDIO_FORMAT == "mp3"
    assert (
        constants.DEFAULT_AUDIO_FORMAT
        in constants.SUPPORTED_AUDIO_FORMATS
    )


def test_supported_tasks() -> None:
    """Supported tasks should contain all exported tasks."""
    assert constants.TASK_TRANSCRIPTION in constants.SUPPORTED_TASKS
    assert constants.TASK_TRANSLATION in constants.SUPPORTED_TASKS
    assert constants.TASK_CLASSIFICATION in constants.SUPPORTED_TASKS
    assert constants.TASK_ANALYSIS in constants.SUPPORTED_TASKS
    assert constants.TASK_METADATA in constants.SUPPORTED_TASKS


def test_default_language() -> None:
    """Default language should be valid."""
    assert constants.DEFAULT_LANGUAGE == "en"
    assert constants.DEFAULT_LANGUAGE in constants.SUPPORTED_LANGUAGES


def test_audio_defaults() -> None:
    """Audio defaults should be positive."""
    assert constants.DEFAULT_SAMPLE_RATE > 0
    assert constants.DEFAULT_BIT_DEPTH > 0
    assert constants.DEFAULT_CHANNELS > 0


def test_audio_limits() -> None:
    """Audio limits should be positive."""
    assert constants.MAX_AUDIO_DURATION_SECONDS > 0
    assert constants.MAX_AUDIO_SIZE_MB > 0


def test_confidence_thresholds() -> None:
    """Confidence thresholds should be valid."""
    assert constants.MIN_CONFIDENCE_THRESHOLD == 0.0
    assert constants.DEFAULT_CONFIDENCE_THRESHOLD == 0.5
    assert constants.MAX_CONFIDENCE_THRESHOLD == 1.0


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_PROVIDER == "provider"
    assert constants.METADATA_MODEL == "model"
    assert constants.METADATA_DURATION == "duration_seconds"
    assert constants.METADATA_SAMPLE_RATE == "sample_rate"
    assert constants.METADATA_LATENCY == "latency_ms"