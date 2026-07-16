"""
Unit tests for ai_multimodal.vision.operations.
"""

from __future__ import annotations

import pytest

from ai_multimodal.vision.exceptions import (
    ImageClassificationError,
    OCRProcessingError,
    UnsupportedImageFormatError,
    VisionValidationError,
    VisualQuestionAnsweringError,
)
from ai_multimodal.vision.operations import (
    VisionResult,
    classify_image,
    describe_image,
    detect_objects,
    extract_text,
    visual_question_answering,
)


def test_classify_image_success() -> None:
    """Classification should succeed."""
    result = classify_image("image.png")

    assert isinstance(result, VisionResult)
    assert result.success is True
    assert result.task == "classification"


def test_classify_invalid_format() -> None:
    """Unsupported formats should raise."""
    with pytest.raises(UnsupportedImageFormatError):
        classify_image("image.png", image_format="svg")


def test_classify_invalid_threshold() -> None:
    """Threshold outside range should raise."""
    with pytest.raises(ImageClassificationError):
        classify_image(
            "image.png",
            confidence_threshold=2.0,
        )


def test_classify_empty_path() -> None:
    """Empty image path should raise."""
    with pytest.raises(VisionValidationError):
        classify_image("")


def test_detect_objects_success() -> None:
    """Object detection should succeed."""
    result = detect_objects("image.png")

    assert result.success is True
    assert result.task == "object_detection"


def test_describe_image_success() -> None:
    """Caption generation should succeed."""
    result = describe_image("image.png")

    assert result.success is True
    assert result.task == "image_captioning"


def test_extract_text_success() -> None:
    """OCR should succeed."""
    result = extract_text("image.png")

    assert result.success is True
    assert result.task == "ocr"


def test_extract_text_invalid_language() -> None:
    """Unsupported OCR language should raise."""
    with pytest.raises(OCRProcessingError):
        extract_text("image.png", language="xx")


def test_visual_question_answering_success() -> None:
    """Visual QA should succeed."""
    result = visual_question_answering(
        "image.png",
        "What is in this image?",
    )

    assert result.success is True
    assert result.task == "visual_question_answering"


def test_visual_question_answering_empty_question() -> None:
    """Empty questions should raise."""
    with pytest.raises(VisualQuestionAnsweringError):
        visual_question_answering(
            "image.png",
            "",
        )