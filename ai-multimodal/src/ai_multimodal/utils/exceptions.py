"""
Exceptions for the ai_multimodal.utils package.

This module defines the exception hierarchy for shared multimodal utility
operations.
"""

from __future__ import annotations


class MultimodalUtilityError(Exception):
    """Base exception for multimodal utility errors."""


class FileValidationError(MultimodalUtilityError):
    """Raised when file validation fails."""


class UnsupportedFileTypeError(FileValidationError):
    """Raised when an unsupported file type is encountered."""


class InvalidFilePathError(FileValidationError):
    """Raised when a file path is invalid."""


class MetadataExtractionError(MultimodalUtilityError):
    """Raised when metadata extraction fails."""


class ContentTypeDetectionError(MultimodalUtilityError):
    """Raised when content type detection fails."""


class FileFormatDetectionError(MultimodalUtilityError):
    """Raised when file format detection fails."""


class IdentifierGenerationError(MultimodalUtilityError):
    """Raised when content identifier generation fails."""