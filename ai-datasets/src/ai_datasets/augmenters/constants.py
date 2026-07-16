"""
Constants for the ai_datasets.augmenters module.
"""

from __future__ import annotations

from typing import Final

# Supported augmentation types

AUGMENT_TEXT: Final[str] = "text"
AUGMENT_IMAGE: Final[str] = "image"
AUGMENT_AUDIO: Final[str] = "audio"
AUGMENT_TABULAR: Final[str] = "tabular"

SUPPORTED_AUGMENTATIONS: Final[tuple[str, ...]] = (
    AUGMENT_TEXT,
    AUGMENT_IMAGE,
    AUGMENT_AUDIO,
    AUGMENT_TABULAR,
)

# Defaults

DEFAULT_AUGMENTATIONS: Final[int] = 1
DEFAULT_RANDOM_SEED: Final[int] = 42

# Metadata

METADATA_TYPE: Final[str] = "augmentation_type"
METADATA_COUNT: Final[str] = "augmentation_count"
METADATA_DURATION: Final[str] = "duration_ms"