"""
ai_datasets.augmenters

Enterprise dataset augmentation module for the AI Engineering Framework.

This package provides provider-independent dataset augmentation
capabilities for text, image, audio, and tabular datasets.

Modules
-------
constants
    Augmenter-specific constants.

exceptions
    Augmenter-specific exception hierarchy.

operations
    High-level dataset augmentation operations.

Design Goals
------------
- Framework independent
- SOLID compliant
- Fully typed
- Enterprise documented
- Production ready
"""

from ai_datasets.augmenters.operations import (
    augment_audio,
    augment_image,
    augment_tabular,
    augment_text,
    augment_dataset,
)

__all__ = [
    "augment_dataset",
    "augment_text",
    "augment_image",
    "augment_audio",
    "augment_tabular",
]