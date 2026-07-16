"""Constants for the ai_testing.data module."""

from __future__ import annotations

from typing import Final

DEFAULT_DATASET_NAME: Final[str] = "dataset"

DEFAULT_ENABLED: Final[bool] = True

MIN_DATASET_NAME_LENGTH: Final[int] = 1
MAX_DATASET_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
DATA_KEY: Final[str] = "data"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "DATA_KEY",
    "DEFAULT_DATASET_NAME",
    "DEFAULT_ENABLED",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "MAX_DATASET_NAME_LENGTH",
    "MIN_DATASET_NAME_LENGTH",
    "NAME_KEY",
]