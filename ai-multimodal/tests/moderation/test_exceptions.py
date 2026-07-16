"""
Unit tests for ai_multimodal.moderation.exceptions.
"""

from __future__ import annotations

import pytest

from ai_multimodal.moderation.exceptions import (
    AudioModerationError,
    DocumentModerationError,
    ImageModerationError,
    ModerationError,
    ModerationMetadataError,
    ModerationProcessingError,
    ModerationProviderError,
    ModerationValidationError,
    TextModerationError,
    UnsupportedContentTypeError,
    UnsupportedModerationCategoryError,
    VideoModerationError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        ModerationValidationError,
        UnsupportedContentTypeError,
        UnsupportedModerationCategoryError,
        ModerationProcessingError,
        TextModerationError,
        ImageModerationError,
        AudioModerationError,
        VideoModerationError,
        DocumentModerationError,
        ModerationMetadataError,
        ModerationProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[ModerationError],
) -> None:
    """Every custom exception should inherit from ModerationError."""
    assert issubclass(exception_class, ModerationError)


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(ModerationError, match="moderation failure"):
        raise ModerationError("moderation failure")