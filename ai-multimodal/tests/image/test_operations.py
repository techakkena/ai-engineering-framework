"""
Unit tests for ai_multimodal.image.operations.
"""

from __future__ import annotations

import pytest

from ai_multimodal.image.exceptions import (
    ImageAnalysisError,
    ImageEditingError,
    ImageGenerationError,
    ImageMetadataError,
    ImageOptimizationError,
    ImageSizeError,
    UnsupportedImageFormatError,
)
from ai_multimodal.image.operations import (
    ImageResult,
    analyze_image,
    edit_image,
    generate_image,
    get_image_metadata,
    optimize_image,
)


def test_generate_image_success() -> None:
    """Image generation should succeed with valid input."""
    result = generate_image("A mountain at sunrise")

    assert isinstance(result, ImageResult)
    assert result.success is True
    assert result.operation == "generate"


def test_generate_image_invalid_format() -> None:
    """Unsupported formats should raise."""
    with pytest.raises(UnsupportedImageFormatError):
        generate_image("test", image_format="svg")


def test_generate_image_invalid_size() -> None:
    """Invalid dimensions should raise."""
    with pytest.raises(ImageSizeError):
        generate_image("test", width=0)


def test_generate_image_empty_prompt() -> None:
    """Empty prompt should raise."""
    with pytest.raises(ImageGenerationError):
        generate_image("   ")


def test_edit_image_success() -> None:
    """Image editing should succeed."""
    result = edit_image("image.png", "remove background")

    assert result.success is True
    assert result.operation == "edit"


def test_edit_image_invalid_path() -> None:
    """Empty path should raise."""
    with pytest.raises(ImageEditingError):
        edit_image("", "prompt")


def test_edit_image_invalid_prompt() -> None:
    """Empty prompt should raise."""
    with pytest.raises(ImageEditingError):
        edit_image("image.png", "")


def test_analyze_image_success() -> None:
    """Image analysis should succeed."""
    result = analyze_image("image.png")

    assert result.success is True
    assert result.operation == "analyze"


def test_analyze_image_invalid_path() -> None:
    """Invalid path should raise."""
    with pytest.raises(ImageAnalysisError):
        analyze_image("")


def test_optimize_image_success() -> None:
    """Optimization should succeed."""
    result = optimize_image("image.png")

    assert result.success is True
    assert result.operation == "optimize"


def test_optimize_image_invalid_path() -> None:
    """Invalid path should raise."""
    with pytest.raises(ImageOptimizationError):
        optimize_image("")


def test_optimize_image_invalid_size() -> None:
    """Invalid target size should raise."""
    with pytest.raises(ImageOptimizationError):
        optimize_image("image.png", max_size_mb=0)


def test_get_image_metadata_success() -> None:
    """Metadata retrieval should succeed."""
    result = get_image_metadata("image.png")

    assert result.success is True
    assert result.operation == "metadata"


def test_get_image_metadata_invalid_path() -> None:
    """Invalid metadata path should raise."""
    with pytest.raises(ImageMetadataError):
        get_image_metadata("")