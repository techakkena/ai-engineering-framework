"""
Unit tests for ai_multimodal.moderation.operations.
"""

from __future__ import annotations

import pytest

from ai_multimodal.moderation.exceptions import (
    ModerationMetadataError,
    ModerationValidationError,
    TextModerationError,
)
from ai_multimodal.moderation.operations import (
    ModerationResult,
    get_moderation_metadata,
    moderate_audio,
    moderate_image,
    moderate_text,
    moderate_video,
)


def test_moderate_text_success() -> None:
    """Text moderation should succeed."""
    result = moderate_text("Hello world")

    assert isinstance(result, ModerationResult)
    assert result.success is True
    assert result.task == "text"


def test_moderate_text_invalid_threshold() -> None:
    """Invalid threshold should raise."""
    with pytest.raises(TextModerationError):
        moderate_text(
            "Hello",
            risk_threshold=2.0,
        )


def test_moderate_text_empty() -> None:
    """Empty text should raise."""
    with pytest.raises(ModerationValidationError):
        moderate_text("")


def test_moderate_image_success() -> None:
    """Image moderation should succeed."""
    result = moderate_image("image.png")

    assert result.success is True
    assert result.task == "image"


def test_moderate_audio_success() -> None:
    """Audio moderation should succeed."""
    result = moderate_audio("audio.mp3")

    assert result.success is True
    assert result.task == "audio"


def test_moderate_video_success() -> None:
    """Video moderation should succeed."""
    result = moderate_video("video.mp4")

    assert result.success is True
    assert result.task == "video"


def test_get_moderation_metadata_success() -> None:
    """Metadata retrieval should succeed."""
    result = get_moderation_metadata("moderation-1")

    assert result.success is True
    assert result.task == "metadata"


def test_get_moderation_metadata_invalid_identifier() -> None:
    """Empty moderation identifiers should raise."""
    with pytest.raises(ModerationMetadataError):
        get_moderation_metadata("")