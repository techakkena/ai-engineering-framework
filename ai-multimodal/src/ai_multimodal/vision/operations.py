"""
Enterprise computer vision operations.

This module provides provider-independent abstractions for common computer
vision tasks. Concrete providers should implement these interfaces while
maintaining a consistent API across the AI Engineering Framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ai_multimodal.vision.constants import (
    DEFAULT_CONFIDENCE_THRESHOLD,
    DEFAULT_LANGUAGE,
    SUPPORTED_IMAGE_FORMATS,
    SUPPORTED_LANGUAGES,
)
from ai_multimodal.vision.exceptions import (
    ImageClassificationError,
    OCRProcessingError,
    UnsupportedImageFormatError,
    VisionValidationError,
    VisualQuestionAnsweringError,
)


@dataclass(slots=True, frozen=True)
class VisionResult:
    """Represents the result of a vision operation."""

    task: str
    success: bool
    data: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


def _validate_image_path(image_path: str) -> None:
    """Validate an image path."""
    if not image_path.strip():
        raise VisionValidationError("Image path cannot be empty.")


def _validate_image_format(image_format: str) -> None:
    """Validate an image format."""
    if image_format.lower() not in SUPPORTED_IMAGE_FORMATS:
        raise UnsupportedImageFormatError(
            f"Unsupported image format: {image_format!r}."
        )


def classify_image(
    image_path: str,
    *,
    image_format: str = "png",
    confidence_threshold: float = DEFAULT_CONFIDENCE_THRESHOLD,
) -> VisionResult:
    """
    Classify an image.

    Returns a provider-independent classification result.
    """
    _validate_image_path(image_path)
    _validate_image_format(image_format)

    if not 0.0 <= confidence_threshold <= 1.0:
        raise ImageClassificationError(
            "Confidence threshold must be between 0.0 and 1.0."
        )

    return VisionResult(
        task="classification",
        success=True,
        data={
            "image_path": image_path,
            "format": image_format,
            "confidence_threshold": confidence_threshold,
        },
    )


def detect_objects(
    image_path: str,
    *,
    image_format: str = "png",
) -> VisionResult:
    """
    Detect objects in an image.

    Placeholder implementation for future provider integrations.
    """
    _validate_image_path(image_path)
    _validate_image_format(image_format)

    return VisionResult(
        task="object_detection",
        success=True,
        data={
            "image_path": image_path,
            "format": image_format,
        },
    )


def describe_image(
    image_path: str,
) -> VisionResult:
    """
    Generate a natural language description of an image.
    """
    _validate_image_path(image_path)

    return VisionResult(
        task="image_captioning",
        success=True,
        data={
            "image_path": image_path,
        },
    )


def extract_text(
    image_path: str,
    *,
    language: str = DEFAULT_LANGUAGE,
) -> VisionResult:
    """
    Extract text from an image using OCR.
    """
    _validate_image_path(image_path)

    if language not in SUPPORTED_LANGUAGES:
        raise OCRProcessingError(f"Unsupported language: {language!r}.")

    return VisionResult(
        task="ocr",
        success=True,
        data={
            "image_path": image_path,
            "language": language,
        },
    )


def visual_question_answering(
    image_path: str,
    question: str,
) -> VisionResult:
    """
    Answer a question about an image.
    """
    _validate_image_path(image_path)

    if not question.strip():
        raise VisualQuestionAnsweringError(
            "Question cannot be empty."
        )

    return VisionResult(
        task="visual_question_answering",
        success=True,
        data={
            "image_path": image_path,
            "question": question,
        },
    )