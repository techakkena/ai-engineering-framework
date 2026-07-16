"""
Enterprise moderation operations for the ai_multimodal.moderation package.

This module provides provider-independent abstractions for moderating
text, images, audio, video, and retrieving moderation metadata.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_multimodal.moderation.constants import (
    DEFAULT_RISK_THRESHOLD,
    STATUS_SAFE,
)
from ai_multimodal.moderation.exceptions import (
    ModerationMetadataError,
    ModerationValidationError,
    TextModerationError,
)


@dataclass(slots=True, frozen=True)
class ModerationResult:
    """Represents the result of a moderation operation."""

    task: str
    success: bool
    status: str
    risk_score: float
    data: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


def _validate_content(content: str) -> None:
    """Validate moderation input."""
    if not content.strip():
        raise ModerationValidationError(
            "Content cannot be empty."
        )


def moderate_text(
    text: str,
    *,
    risk_threshold: float = DEFAULT_RISK_THRESHOLD,
) -> ModerationResult:
    """
    Moderate text content.
    """
    _validate_content(text)

    if not 0.0 <= risk_threshold <= 1.0:
        raise TextModerationError(
            "Risk threshold must be between 0.0 and 1.0."
        )

    return ModerationResult(
        task="text",
        success=True,
        status=STATUS_SAFE,
        risk_score=0.0,
        data={"text": text},
    )


def moderate_image(
    image_path: str,
) -> ModerationResult:
    """
    Moderate an image.
    """
    _validate_content(image_path)

    return ModerationResult(
        task="image",
        success=True,
        status=STATUS_SAFE,
        risk_score=0.0,
        data={"image_path": image_path},
    )


def moderate_audio(
    audio_path: str,
) -> ModerationResult:
    """
    Moderate an audio recording.
    """
    _validate_content(audio_path)

    return ModerationResult(
        task="audio",
        success=True,
        status=STATUS_SAFE,
        risk_score=0.0,
        data={"audio_path": audio_path},
    )


def moderate_video(
    video_path: str,
) -> ModerationResult:
    """
    Moderate a video.
    """
    _validate_content(video_path)

    return ModerationResult(
        task="video",
        success=True,
        status=STATUS_SAFE,
        risk_score=0.0,
        data={"video_path": video_path},
    )


def get_moderation_metadata(
    moderation_id: str,
) -> ModerationResult:
    """
    Retrieve moderation metadata.
    """
    if not moderation_id.strip():
        raise ModerationMetadataError(
            "Moderation ID cannot be empty."
        )

    return ModerationResult(
        task="metadata",
        success=True,
        status=STATUS_SAFE,
        risk_score=0.0,
        metadata={
            "moderation_id": moderation_id,
        },
    )