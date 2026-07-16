"""
Exceptions for the ai_multimodal.moderation package.

This module defines the exception hierarchy for provider-independent
moderation operations.
"""

from __future__ import annotations


class ModerationError(Exception):
    """Base exception for all moderation-related errors."""


class ModerationValidationError(ModerationError):
    """Raised when moderation input validation fails."""


class UnsupportedContentTypeError(ModerationValidationError):
    """Raised when an unsupported content type is provided."""


class UnsupportedModerationCategoryError(ModerationValidationError):
    """Raised when an unsupported moderation category is requested."""


class ModerationProcessingError(ModerationError):
    """Base exception for moderation processing failures."""


class TextModerationError(ModerationProcessingError):
    """Raised when text moderation fails."""


class ImageModerationError(ModerationProcessingError):
    """Raised when image moderation fails."""


class AudioModerationError(ModerationProcessingError):
    """Raised when audio moderation fails."""


class VideoModerationError(ModerationProcessingError):
    """Raised when video moderation fails."""


class DocumentModerationError(ModerationProcessingError):
    """Raised when document moderation fails."""


class ModerationMetadataError(ModerationProcessingError):
    """Raised when moderation metadata retrieval fails."""


class ModerationProviderError(ModerationError):
    """Raised when an underlying moderation provider returns an error."""