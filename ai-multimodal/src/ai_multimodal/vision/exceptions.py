"""
Exceptions for the ai_multimodal.vision package.

This module defines the exception hierarchy for provider-independent
computer vision operations.
"""

from __future__ import annotations


class VisionError(Exception):
    """Base exception for all vision-related errors."""


class VisionValidationError(VisionError):
    """Raised when input validation fails."""


class UnsupportedVisionTaskError(VisionValidationError):
    """Raised when an unsupported vision task is requested."""


class UnsupportedImageFormatError(VisionValidationError):
    """Raised when an unsupported image format is provided."""


class VisionProcessingError(VisionError):
    """Raised when a vision processing operation fails."""


class ImageClassificationError(VisionProcessingError):
    """Raised when image classification fails."""


class ObjectDetectionError(VisionProcessingError):
    """Raised when object detection fails."""


class ImageCaptionError(VisionProcessingError):
    """Raised when image caption generation fails."""


class OCRProcessingError(VisionProcessingError):
    """Raised when optical character recognition (OCR) fails."""


class VisualQuestionAnsweringError(VisionProcessingError):
    """Raised when visual question answering fails."""


class VisionProviderError(VisionError):
    """Raised when the underlying vision provider returns an error."""