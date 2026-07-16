"""
Unit tests for ai_multimodal.vision.constants.
"""

from __future__ import annotations

from ai_multimodal.vision import constants


def test_supported_image_formats() -> None:
    """Supported image formats should contain common formats."""
    assert "png" in constants.SUPPORTED_IMAGE_FORMATS
    assert "jpg" in constants.SUPPORTED_IMAGE_FORMATS
    assert "jpeg" in constants.SUPPORTED_IMAGE_FORMATS
    assert "webp" in constants.SUPPORTED_IMAGE_FORMATS


def test_supported_tasks() -> None:
    """Supported tasks should contain all exported tasks."""
    assert constants.TASK_CLASSIFICATION in constants.SUPPORTED_TASKS
    assert constants.TASK_OBJECT_DETECTION in constants.SUPPORTED_TASKS
    assert constants.TASK_IMAGE_CAPTIONING in constants.SUPPORTED_TASKS
    assert constants.TASK_OCR in constants.SUPPORTED_TASKS
    assert constants.TASK_VISUAL_QA in constants.SUPPORTED_TASKS


def test_confidence_thresholds() -> None:
    """Confidence threshold values should be valid."""
    assert constants.MIN_CONFIDENCE_THRESHOLD == 0.0
    assert constants.DEFAULT_CONFIDENCE_THRESHOLD == 0.5
    assert constants.MAX_CONFIDENCE_THRESHOLD == 1.0


def test_image_limits() -> None:
    """Image limits should be positive."""
    assert constants.DEFAULT_MAX_IMAGE_SIZE_MB > 0
    assert constants.DEFAULT_MAX_WIDTH > 0
    assert constants.DEFAULT_MAX_HEIGHT > 0


def test_default_language() -> None:
    """Default language should be supported."""
    assert constants.DEFAULT_LANGUAGE == "en"
    assert constants.DEFAULT_LANGUAGE in constants.SUPPORTED_LANGUAGES


def test_supported_languages() -> None:
    """Language list should contain common languages."""
    assert "en" in constants.SUPPORTED_LANGUAGES
    assert "ja" in constants.SUPPORTED_LANGUAGES
    assert "zh" in constants.SUPPORTED_LANGUAGES


def test_response_limits() -> None:
    """Response limits should be positive."""
    assert constants.DEFAULT_MAX_LABELS > 0
    assert constants.DEFAULT_MAX_OBJECTS > 0


def test_metadata_keys() -> None:
    """Metadata keys should match expected values."""
    assert constants.METADATA_PROVIDER == "provider"
    assert constants.METADATA_MODEL == "model"
    assert constants.METADATA_LATENCY == "latency_ms"
    assert constants.METADATA_CONFIDENCE == "confidence"