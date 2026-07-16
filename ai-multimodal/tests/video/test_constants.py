"""
Unit tests for ai_multimodal.video.constants.
"""

from __future__ import annotations

from ai_multimodal.video import constants


def test_supported_video_formats() -> None:
    """Supported video formats should contain common formats."""
    assert "mp4" in constants.SUPPORTED_VIDEO_FORMATS
    assert "mov" in constants.SUPPORTED_VIDEO_FORMATS
    assert "avi" in constants.SUPPORTED_VIDEO_FORMATS
    assert "webm" in constants.SUPPORTED_VIDEO_FORMATS


def test_default_video_format() -> None:
    """Default video format should be supported."""
    assert constants.DEFAULT_VIDEO_FORMAT == "mp4"
    assert (
        constants.DEFAULT_VIDEO_FORMAT
        in constants.SUPPORTED_VIDEO_FORMATS
    )


def test_supported_tasks() -> None:
    """Supported tasks should contain all exported tasks."""
    assert constants.TASK_ANALYSIS in constants.SUPPORTED_TASKS
    assert constants.TASK_SUMMARIZATION in constants.SUPPORTED_TASKS
    assert constants.TASK_FRAME_EXTRACTION in constants.SUPPORTED_TASKS
    assert constants.TASK_TRANSCRIPTION in constants.SUPPORTED_TASKS
    assert constants.TASK_METADATA in constants.SUPPORTED_TASKS


def test_video_defaults() -> None:
    """Video defaults should be positive."""
    assert constants.DEFAULT_FRAME_RATE > 0
    assert constants.DEFAULT_FRAME_INTERVAL_SECONDS > 0


def test_video_limits() -> None:
    """Video limits should be positive."""
    assert constants.MAX_VIDEO_DURATION_SECONDS > 0
    assert constants.MAX_VIDEO_SIZE_MB > 0
    assert constants.DEFAULT_MAX_FRAMES > 0


def test_default_language() -> None:
    """Default language should be supported."""
    assert constants.DEFAULT_LANGUAGE == "en"
    assert constants.DEFAULT_LANGUAGE in constants.SUPPORTED_LANGUAGES


def test_confidence_thresholds() -> None:
    """Confidence thresholds should be valid."""
    assert constants.MIN_CONFIDENCE_THRESHOLD == 0.0
    assert constants.DEFAULT_CONFIDENCE_THRESHOLD == 0.5
    assert constants.MAX_CONFIDENCE_THRESHOLD == 1.0


def test_metadata_keys() -> None:
    """Metadata keys should match expected values."""
    assert constants.METADATA_PROVIDER == "provider"
    assert constants.METADATA_MODEL == "model"
    assert constants.METADATA_DURATION == "duration_seconds"
    assert constants.METADATA_FRAME_RATE == "frame_rate"
    assert constants.METADATA_LATENCY == "latency_ms"