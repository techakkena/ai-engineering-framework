"""
Exceptions for the ai_multimodal.video package.

This module defines the exception hierarchy for provider-independent
video processing operations.
"""

from __future__ import annotations


class VideoError(Exception):
    """Base exception for all video-related errors."""


class VideoValidationError(VideoError):
    """Raised when video input validation fails."""


class UnsupportedVideoFormatError(VideoValidationError):
    """Raised when an unsupported video format is provided."""


class UnsupportedLanguageError(VideoValidationError):
    """Raised when an unsupported language is specified."""


class VideoProcessingError(VideoError):
    """Base exception for video processing failures."""


class VideoAnalysisError(VideoProcessingError):
    """Raised when video analysis fails."""


class VideoSummarizationError(VideoProcessingError):
    """Raised when video summarization fails."""


class FrameExtractionError(VideoProcessingError):
    """Raised when frame extraction fails."""


class VideoTranscriptionError(VideoProcessingError):
    """Raised when video transcription fails."""


class VideoMetadataError(VideoProcessingError):
    """Raised when video metadata extraction fails."""


class VideoProviderError(VideoError):
    """Raised when an underlying video provider returns an error."""