"""
Enterprise video operations for the ai_multimodal.video package.

This module provides provider-independent abstractions for video analysis,
summarization, frame extraction, transcription, and metadata retrieval.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_multimodal.video.constants import (
    DEFAULT_CONFIDENCE_THRESHOLD,
    DEFAULT_FRAME_INTERVAL_SECONDS,
    DEFAULT_LANGUAGE,
    DEFAULT_VIDEO_FORMAT,
    MAX_VIDEO_DURATION_SECONDS,
    SUPPORTED_LANGUAGES,
    SUPPORTED_VIDEO_FORMATS,
)
from ai_multimodal.video.exceptions import (
    FrameExtractionError,
    UnsupportedLanguageError,
    UnsupportedVideoFormatError,
    VideoAnalysisError,
    VideoValidationError,
)


@dataclass(slots=True, frozen=True)
class VideoResult:
    """Represents the result of a video operation."""

    task: str
    success: bool
    data: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


def _validate_video_path(video_path: str) -> None:
    """Validate a video path."""
    if not video_path.strip():
        raise VideoValidationError("Video path cannot be empty.")


def _validate_video_format(video_format: str) -> None:
    """Validate a video format."""
    if video_format.lower() not in SUPPORTED_VIDEO_FORMATS:
        raise UnsupportedVideoFormatError(
            f"Unsupported video format: {video_format!r}."
        )


def analyze_video(
    video_path: str,
    *,
    video_format: str = DEFAULT_VIDEO_FORMAT,
    confidence_threshold: float = DEFAULT_CONFIDENCE_THRESHOLD,
) -> VideoResult:
    """
    Analyze a video.

    Returns a provider-independent analysis result.
    """
    _validate_video_path(video_path)
    _validate_video_format(video_format)

    if not 0.0 <= confidence_threshold <= 1.0:
        raise VideoAnalysisError(
            "Confidence threshold must be between 0.0 and 1.0."
        )

    return VideoResult(
        task="analysis",
        success=True,
        data={
            "video_path": video_path,
            "video_format": video_format,
            "confidence_threshold": confidence_threshold,
        },
    )


def generate_video_summary(video_path: str) -> VideoResult:
    """
    Generate a summary of a video.
    """
    _validate_video_path(video_path)

    return VideoResult(
        task="summarization",
        success=True,
        data={
            "video_path": video_path,
        },
    )


def extract_frames(
    video_path: str,
    *,
    interval_seconds: int = DEFAULT_FRAME_INTERVAL_SECONDS,
) -> VideoResult:
    """
    Extract frames from a video.
    """
    _validate_video_path(video_path)

    if interval_seconds <= 0:
        raise FrameExtractionError(
            "Frame interval must be greater than zero."
        )

    return VideoResult(
        task="frame_extraction",
        success=True,
        data={
            "video_path": video_path,
            "interval_seconds": interval_seconds,
        },
    )


def transcribe_video(
    video_path: str,
    *,
    language: str = DEFAULT_LANGUAGE,
) -> VideoResult:
    """
    Transcribe speech contained in a video.
    """
    _validate_video_path(video_path)

    if language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageError(
            f"Unsupported language: {language!r}."
        )

    return VideoResult(
        task="transcription",
        success=True,
        data={
            "video_path": video_path,
            "language": language,
        },
    )


def get_video_metadata(video_path: str) -> VideoResult:
    """
    Retrieve metadata from a video.
    """
    _validate_video_path(video_path)

    return VideoResult(
        task="metadata",
        success=True,
        metadata={
            "video_path": video_path,
            "max_duration_seconds": MAX_VIDEO_DURATION_SECONDS,
        },
    )