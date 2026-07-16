"""
Custom exceptions for the ai_multimodal.image module.

This module defines the exception hierarchy used by image operations.
"""

from __future__ import annotations


class ImageError(Exception):
    """Base exception for all image-related errors."""


class ImageValidationError(ImageError):
    """Raised when image input validation fails."""


class UnsupportedImageFormatError(ImageValidationError):
    """Raised when an unsupported image format is supplied."""


class ImageSizeError(ImageValidationError):
    """Raised when image dimensions or file size exceed supported limits."""


class ImageGenerationError(ImageError):
    """Raised when image generation fails."""


class ImageEditingError(ImageError):
    """Raised when an image editing operation fails."""


class ImageAnalysisError(ImageError):
    """Raised when image analysis fails."""


class ImageOptimizationError(ImageError):
    """Raised when image optimization fails."""


class ImageMetadataError(ImageError):
    """Raised when image metadata cannot be retrieved or processed."""


class ImageProviderError(ImageError):
    """Raised when an underlying image provider returns an error."""