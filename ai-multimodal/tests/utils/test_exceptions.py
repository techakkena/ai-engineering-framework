"""
Unit tests for ai_multimodal.utils.exceptions.
"""

from __future__ import annotations

import pytest

from ai_multimodal.utils.exceptions import (
    ContentTypeDetectionError,
    FileFormatDetectionError,
    FileValidationError,
    IdentifierGenerationError,
    InvalidFilePathError,
    MetadataExtractionError,
    MultimodalUtilityError,
    UnsupportedFileTypeError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        FileValidationError,
        UnsupportedFileTypeError,
        InvalidFilePathError,
        MetadataExtractionError,
        ContentTypeDetectionError,
        FileFormatDetectionError,
        IdentifierGenerationError,
    ],
)
def test_exception_inheritance(
    exception_class: type[MultimodalUtilityError],
) -> None:
    """Every custom exception should inherit from MultimodalUtilityError."""
    assert issubclass(
        exception_class,
        MultimodalUtilityError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        MultimodalUtilityError,
        match="utility failure",
    ):
        raise MultimodalUtilityError(
            "utility failure",
        )