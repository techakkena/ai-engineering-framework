"""
Unit tests for ai_multimodal.vision.exceptions.
"""

from __future__ import annotations

import pytest

from ai_multimodal.vision.exceptions import (
    ImageCaptionError,
    ImageClassificationError,
    ObjectDetectionError,
    OCRProcessingError,
    UnsupportedImageFormatError,
    UnsupportedVisionTaskError,
    VisionError,
    VisionProcessingError,
    VisionProviderError,
    VisionValidationError,
    VisualQuestionAnsweringError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        VisionValidationError,
        UnsupportedVisionTaskError,
        UnsupportedImageFormatError,
        VisionProcessingError,
        ImageClassificationError,
        ObjectDetectionError,
        ImageCaptionError,
        OCRProcessingError,
        VisualQuestionAnsweringError,
        VisionProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[VisionError],
) -> None:
    """Every custom exception should inherit from VisionError."""
    assert issubclass(exception_class, VisionError)


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(VisionError, match="vision failure"):
        raise VisionError("vision failure")