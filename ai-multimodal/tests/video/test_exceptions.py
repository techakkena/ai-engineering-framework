"""
Unit tests for ai_multimodal.video.exceptions.
"""

from __future__ import annotations

import pytest

from ai_multimodal.video.exceptions import (
    FrameExtractionError,
    UnsupportedLanguageError,
    UnsupportedVideoFormatError,
    VideoAnalysisError,
    VideoError,
    VideoMetadataError,
    VideoProcessingError,
    VideoProviderError,
    VideoSummarizationError,
    VideoTranscriptionError,
    VideoValidationError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        VideoValidationError,
        UnsupportedVideoFormatError,
        UnsupportedLanguageError,
        VideoProcessingError,
        VideoAnalysisError,
        VideoSummarizationError,
        FrameExtractionError,
        VideoTranscriptionError,
        VideoMetadataError,
        VideoProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[VideoError],
) -> None:
    """Every custom exception should inherit from VideoError."""
    assert issubclass(exception_class, VideoError)


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(VideoError, match="video failure"):
        raise VideoError("video failure")