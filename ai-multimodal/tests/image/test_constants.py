"""
Unit tests for ai_multimodal.image.constants.
"""

from __future__ import annotations

from ai_multimodal.image import constants


def test_supported_image_formats() -> None:
    """SUPPORTED_IMAGE_FORMATS should contain expected formats."""
    assert "png" in constants.SUPPORTED_IMAGE_FORMATS
    assert "jpeg" in constants.SUPPORTED_IMAGE_FORMATS
    assert "jpg" in constants.SUPPORTED_IMAGE_FORMATS
    assert "webp" in constants.SUPPORTED_IMAGE_FORMATS


def test_default_image_format() -> None:
    """DEFAULT_IMAGE_FORMAT should be valid."""
    assert constants.DEFAULT_IMAGE_FORMAT == "png"
    assert (
        constants.DEFAULT_IMAGE_FORMAT
        in constants.SUPPORTED_IMAGE_FORMATS
    )


def test_default_dimensions() -> None:
    """Default dimensions should be positive."""
    assert constants.DEFAULT_IMAGE_WIDTH > 0
    assert constants.DEFAULT_IMAGE_HEIGHT > 0


def test_supported_qualities() -> None:
    """Supported image qualities should contain defaults."""
    assert constants.DEFAULT_IMAGE_QUALITY in (
        constants.SUPPORTED_IMAGE_QUALITIES
    )
    assert "low" in constants.SUPPORTED_IMAGE_QUALITIES
    assert "standard" in constants.SUPPORTED_IMAGE_QUALITIES
    assert "high" in constants.SUPPORTED_IMAGE_QUALITIES


def test_default_mask_format() -> None:
    """Mask format should be PNG."""
    assert constants.DEFAULT_MASK_FORMAT == "png"


def test_background_color() -> None:
    """Default background should be transparent."""
    assert constants.DEFAULT_BACKGROUND_COLOR == "transparent"


def test_default_dpi() -> None:
    """DPI should be positive."""
    assert constants.DEFAULT_DPI > 0


def test_supported_color_modes() -> None:
    """Color modes should contain common values."""
    assert "RGB" in constants.SUPPORTED_COLOR_MODES
    assert "RGBA" in constants.SUPPORTED_COLOR_MODES
    assert "CMYK" in constants.SUPPORTED_COLOR_MODES


def test_image_limits() -> None:
    """Image limits should be positive."""
    assert constants.MAX_IMAGE_SIZE_MB > 0
    assert constants.MAX_IMAGE_WIDTH > 0
    assert constants.MAX_IMAGE_HEIGHT > 0


def test_operation_constants() -> None:
    """Operation names should match expected values."""
    assert constants.OPERATION_GENERATE == "generate"
    assert constants.OPERATION_EDIT == "edit"
    assert constants.OPERATION_ANALYZE == "analyze"
    assert constants.OPERATION_OPTIMIZE == "optimize"
    assert constants.OPERATION_METADATA == "metadata"