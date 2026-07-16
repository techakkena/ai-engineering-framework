"""
Exceptions for the ai_datasets.augmenters package.
"""

from __future__ import annotations


class DatasetAugmenterError(Exception):
    """Base exception for dataset augmentation."""


class AugmentationValidationError(DatasetAugmenterError):
    """Raised when augmentation input is invalid."""


class UnsupportedAugmentationError(AugmentationValidationError):
    """Raised for unsupported augmentation types."""


class DatasetAugmentationError(DatasetAugmenterError):
    """Raised when augmentation fails."""


class TextAugmentationError(DatasetAugmentationError):
    """Raised for text augmentation failures."""


class ImageAugmentationError(DatasetAugmentationError):
    """Raised for image augmentation failures."""


class AudioAugmentationError(DatasetAugmentationError):
    """Raised for audio augmentation failures."""


class TabularAugmentationError(DatasetAugmentationError):
    """Raised for tabular augmentation failures."""


class AugmenterProviderError(DatasetAugmenterError):
    """Raised when an augmentation provider fails."""