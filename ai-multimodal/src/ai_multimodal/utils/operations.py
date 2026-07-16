"""
Enterprise utility operations for the ai_multimodal.utils package.

This module provides provider-independent helper functions shared across
all multimodal modules.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from uuid import uuid4

from ai_multimodal.utils.constants import (
    AUDIO_EXTENSIONS,
    CONTENT_TYPE_AUDIO,
    CONTENT_TYPE_DOCUMENT,
    CONTENT_TYPE_IMAGE,
    CONTENT_TYPE_TEXT,
    CONTENT_TYPE_UNKNOWN,
    CONTENT_TYPE_VIDEO,
    DOCUMENT_EXTENSIONS,
    IMAGE_EXTENSIONS,
    METADATA_CONTENT_TYPE,
    METADATA_EXTENSION,
    METADATA_FILENAME,
    VIDEO_EXTENSIONS,
)
from ai_multimodal.utils.exceptions import (
    FileFormatDetectionError,
    FileValidationError,
    IdentifierGenerationError,
)


@dataclass(slots=True, frozen=True)
class UtilityResult:
    """Represents the result of a utility operation."""

    success: bool
    data: dict[str, Any] = field(default_factory=dict)


def validate_file_path(file_path: str) -> UtilityResult:
    """
    Validate a file path.
    """
    if not file_path.strip():
        raise FileValidationError("File path cannot be empty.")

    return UtilityResult(
        success=True,
        data={"file_path": file_path},
    )


def detect_file_format(file_path: str) -> UtilityResult:
    """
    Detect a file format from its extension.
    """
    validate_file_path(file_path)

    extension = Path(file_path).suffix.lower()

    if not extension:
        raise FileFormatDetectionError(
            "Unable to determine file format."
        )

    return UtilityResult(
        success=True,
        data={"extension": extension},
    )


def detect_content_type(file_path: str) -> UtilityResult:
    """
    Detect the multimodal content type.
    """
    extension = Path(file_path).suffix.lower()

    if extension in IMAGE_EXTENSIONS:
        content_type = CONTENT_TYPE_IMAGE
    elif extension in AUDIO_EXTENSIONS:
        content_type = CONTENT_TYPE_AUDIO
    elif extension in VIDEO_EXTENSIONS:
        content_type = CONTENT_TYPE_VIDEO
    elif extension in DOCUMENT_EXTENSIONS:
        content_type = CONTENT_TYPE_DOCUMENT
    elif extension == ".txt":
        content_type = CONTENT_TYPE_TEXT
    else:
        content_type = CONTENT_TYPE_UNKNOWN

    return UtilityResult(
        success=True,
        data={
            "content_type": content_type,
        },
    )


def get_file_metadata(file_path: str) -> UtilityResult:
    """
    Retrieve basic metadata for a file.
    """
    validate_file_path(file_path)

    path = Path(file_path)

    return UtilityResult(
        success=True,
        data={
            METADATA_FILENAME: path.name,
            METADATA_EXTENSION: path.suffix.lower(),
            METADATA_CONTENT_TYPE: detect_content_type(
                file_path,
            ).data["content_type"],
        },
    )


def generate_content_identifier() -> UtilityResult:
    """
    Generate a unique content identifier.
    """
    identifier = str(uuid4())

    if not identifier:
        raise IdentifierGenerationError(
            "Unable to generate identifier."
        )

    return UtilityResult(
        success=True,
        data={
            "identifier": identifier,
        },
    )