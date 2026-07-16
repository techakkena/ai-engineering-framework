"""
Unit tests for ai_multimodal.image.exceptions.
"""

from __future__ import annotations

import pytest

from ai_multimodal.image.exceptions import (
    ImageAnalysisError,
    ImageEditingError,
    ImageError,
    ImageGenerationError,
    ImageMetadataError,
    ImageOptimizationError,
    ImageProviderError,
    ImageSizeError,
    ImageValidationError,
    UnsupportedImageFormatError,
)


@pytest.mark.parametrize(
    "exception_type",
    [
        ImageValidationError,
        UnsupportedImageFormatError,
        ImageSizeError,
        ImageGenerationError,
        ImageEditingError,
        ImageAnalysisError,
        ImageOptimizationError,
        ImageMetadataError,
        ImageProviderError,
    ],
)
def test_exceptions_inherit_from_image_error(
    exception_type: type[ImageError],
) -> None:
    """All image exceptions should inherit from ImageError."""
    assert issubclass(exception_type, ImageError)


def test_image_error_message() -> None:
    """Exception message should be preserved."""
    message = "image failure"

    with pytest.raises(ImageError, match=message):
        raise ImageError(message)