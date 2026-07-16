"""
Unit tests for ai_multimodal.utils.operations.
"""

from __future__ import annotations

import pytest

from ai_multimodal.utils.constants import (
    CONTENT_TYPE_IMAGE,
    CONTENT_TYPE_UNKNOWN,
)
from ai_multimodal.utils.exceptions import (
    FileFormatDetectionError,
    FileValidationError,
)
from ai_multimodal.utils.operations import (
    UtilityResult,
    detect_content_type,
    detect_file_format,
    generate_content_identifier,
    get_file_metadata,
    validate_file_path,
)


def test_validate_file_path_success() -> None:
    """File validation should succeed."""
    result = validate_file_path("image.png")

    assert isinstance(result, UtilityResult)
    assert result.success is True


def test_validate_file_path_empty() -> None:
    """Empty file paths should raise."""
    with pytest.raises(FileValidationError):
        validate_file_path("")


def test_detect_file_format_success() -> None:
    """File format detection should succeed."""
    result = detect_file_format("image.png")

    assert result.success is True
    assert result.data["extension"] == ".png"


def test_detect_file_format_invalid() -> None:
    """Files without extensions should raise."""
    with pytest.raises(FileFormatDetectionError):
        detect_file_format("image")


def test_detect_content_type_image() -> None:
    """Image content type should be detected."""
    result = detect_content_type("photo.jpg")

    assert result.data["content_type"] == CONTENT_TYPE_IMAGE


def test_detect_content_type_unknown() -> None:
    """Unknown content types should be returned."""
    result = detect_content_type("archive.xyz")

    assert result.data["content_type"] == CONTENT_TYPE_UNKNOWN


def test_get_file_metadata_success() -> None:
    """Metadata retrieval should succeed."""
    result = get_file_metadata("image.png")

    assert result.success is True
    assert result.data["filename"] == "image.png"


def test_generate_content_identifier() -> None:
    """Identifier generation should succeed."""
    result = generate_content_identifier()

    assert result.success is True
    assert isinstance(result.data["identifier"], str)
    assert len(result.data["identifier"]) > 0