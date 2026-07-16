"""
Constants for the ai_multimodal.image module.

This module contains framework-independent defaults and configuration values
used by image operations.
"""

from __future__ import annotations

from typing import Final

# ---------------------------------------------------------------------------
# Supported image formats
# ---------------------------------------------------------------------------

SUPPORTED_IMAGE_FORMATS: Final[tuple[str, ...]] = (
    "png",
    "jpeg",
    "jpg",
    "webp",
    "gif",
    "bmp",
    "tiff",
)

DEFAULT_IMAGE_FORMAT: Final[str] = "png"

# ---------------------------------------------------------------------------
# Image generation defaults
# ---------------------------------------------------------------------------

DEFAULT_IMAGE_WIDTH: Final[int] = 1024
DEFAULT_IMAGE_HEIGHT: Final[int] = 1024
DEFAULT_IMAGE_QUALITY: Final[str] = "standard"

SUPPORTED_IMAGE_QUALITIES: Final[tuple[str, ...]] = (
    "low",
    "standard",
    "high",
)

# ---------------------------------------------------------------------------
# Image editing defaults
# ---------------------------------------------------------------------------

DEFAULT_MASK_FORMAT: Final[str] = "png"
DEFAULT_BACKGROUND_COLOR: Final[str] = "transparent"

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

DEFAULT_DPI: Final[int] = 72

SUPPORTED_COLOR_MODES: Final[tuple[str, ...]] = (
    "RGB",
    "RGBA",
    "L",
    "CMYK",
)

# ---------------------------------------------------------------------------
# Limits
# ---------------------------------------------------------------------------

MAX_IMAGE_SIZE_MB: Final[int] = 25
MAX_IMAGE_WIDTH: Final[int] = 8192
MAX_IMAGE_HEIGHT: Final[int] = 8192

# ---------------------------------------------------------------------------
# Operation names
# ---------------------------------------------------------------------------

OPERATION_GENERATE: Final[str] = "generate"
OPERATION_EDIT: Final[str] = "edit"
OPERATION_ANALYZE: Final[str] = "analyze"
OPERATION_OPTIMIZE: Final[str] = "optimize"
OPERATION_METADATA: Final[str] = "metadata"