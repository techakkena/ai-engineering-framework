"""
Unit tests for ai_multimodal.utils.constants.
"""

from __future__ import annotations

from ai_multimodal.utils import constants


def test_supported_content_types() -> None:
    """Supported content types should contain all modalities."""
    assert constants.CONTENT_TYPE_TEXT in constants.SUPPORTED_CONTENT_TYPES
    assert constants.CONTENT_TYPE_IMAGE in constants.SUPPORTED_CONTENT_TYPES
    assert constants.CONTENT_TYPE_AUDIO in constants.SUPPORTED_CONTENT_TYPES
    assert constants.CONTENT_TYPE_VIDEO in constants.SUPPORTED_CONTENT_TYPES
    assert constants.CONTENT_TYPE_DOCUMENT in constants.SUPPORTED_CONTENT_TYPES


def test_image_extensions() -> None:
    """Image extensions should contain common formats."""
    assert ".png" in constants.IMAGE_EXTENSIONS
    assert ".jpg" in constants.IMAGE_EXTENSIONS
    assert ".jpeg" in constants.IMAGE_EXTENSIONS


def test_audio_extensions() -> None:
    """Audio extensions should contain common formats."""
    assert ".mp3" in constants.AUDIO_EXTENSIONS
    assert ".wav" in constants.AUDIO_EXTENSIONS


def test_video_extensions() -> None:
    """Video extensions should contain common formats."""
    assert ".mp4" in constants.VIDEO_EXTENSIONS
    assert ".mov" in constants.VIDEO_EXTENSIONS


def test_document_extensions() -> None:
    """Document extensions should contain common formats."""
    assert ".pdf" in constants.DOCUMENT_EXTENSIONS
    assert ".docx" in constants.DOCUMENT_EXTENSIONS
    assert ".txt" in constants.DOCUMENT_EXTENSIONS


def test_file_limits() -> None:
    """File limits should be positive."""
    assert constants.MAX_FILE_SIZE_MB > 0
    assert constants.MAX_FILENAME_LENGTH > 0


def test_metadata_keys() -> None:
    """Metadata constants should match expected values."""
    assert constants.METADATA_FILENAME == "filename"
    assert constants.METADATA_EXTENSION == "extension"
    assert constants.METADATA_SIZE == "size_bytes"
    assert constants.METADATA_CONTENT_TYPE == "content_type"
    assert constants.METADATA_CREATED_AT == "created_at"