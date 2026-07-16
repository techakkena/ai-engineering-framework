"""
Unit tests for ai_multimodal.video.operations.
"""

from __future__ import annotations

import pytest

from ai_multimodal.video.exceptions import (
    FrameExtractionError,
    UnsupportedLanguageError,
    UnsupportedVideoFormatError,
    VideoAnalysisError,
    VideoValidationError,
)
from ai_multimodal.video.operations import (
    VideoResult,
    analyze_video,
    extract_frames,
    generate_video_summary,
    get_video_metadata,
    transcribe_video,
)


def test_analyze_video_success() -> None:
    """Video analysis should succeed."""
    result = analyze_video("video.mp4")

    assert isinstance(result, VideoResult)
    assert result.success is True
    assert result.task == "analysis"


def test_analyze_invalid_format() -> None:
    """Unsupported formats should raise."""
    with pytest.raises(UnsupportedVideoFormatError):
        analyze_video(
            "video.xyz",
            video_format="xyz",
        )


def test_analyze_invalid_threshold() -> None:
    """Invalid threshold should raise."""
    with pytest.raises(VideoAnalysisError):
        analyze_video(
            "video.mp4",
            confidence_threshold=2.0,
        )


def test_analyze_empty_path() -> None:
    """Empty video path should raise."""
    with pytest.raises(VideoValidationError):
        analyze_video("")


def test_generate_summary_success() -> None:
    """Video summarization should succeed."""
    result = generate_video_summary("video.mp4")

    assert result.success is True
    assert result.task == "summarization"


def test_extract_frames_success() -> None:
    """Frame extraction should succeed."""
    result = extract_frames("video.mp4")

    assert result.success is True
    assert result.task == "frame_extraction"


def test_extract_frames_invalid_interval() -> None:
    """Invalid frame interval should raise."""
    with pytest.raises(FrameExtractionError):
        extract_frames(
            "video.mp4",
            interval_seconds=0,
        )


def test_transcribe_video_success() -> None:
    """Video transcription should succeed."""
    result = transcribe_video("video.mp4")

    assert result.success is True
    assert result.task == "transcription"


def test_transcribe_invalid_language() -> None:
    """Unsupported language should raise."""
    with pytest.raises(UnsupportedLanguageError):
        transcribe_video(
            "video.mp4",
            language="xx",
        )


def test_get_video_metadata_success() -> None:
    """Metadata retrieval should succeed."""
    result = get_video_metadata("video.mp4")

    assert result.success is True
    assert result.task == "metadata"