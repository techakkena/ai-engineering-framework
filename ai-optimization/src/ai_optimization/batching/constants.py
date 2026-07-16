"""Constants for the ai_optimization.batching module."""

from __future__ import annotations

from typing import Final

# Default batching configuration.
DEFAULT_BATCH_NAME: Final[str] = "batch"
DEFAULT_BATCH_STRATEGY: Final[str] = "fixed"
DEFAULT_ENABLED: Final[bool] = True

# Supported batching strategies.
FIXED_STRATEGY: Final[str] = "fixed"
DYNAMIC_STRATEGY: Final[str] = "dynamic"
ADAPTIVE_STRATEGY: Final[str] = "adaptive"
STREAMING_STRATEGY: Final[str] = "streaming"

SUPPORTED_BATCH_STRATEGIES: Final[frozenset[str]] = frozenset(
    {
        FIXED_STRATEGY,
        DYNAMIC_STRATEGY,
        ADAPTIVE_STRATEGY,
        STREAMING_STRATEGY,
    }
)

# Validation.
MIN_BATCH_NAME_LENGTH: Final[int] = 1
MAX_BATCH_NAME_LENGTH: Final[int] = 255

# Metadata keys.
NAME_KEY: Final[str] = "name"
STRATEGY_KEY: Final[str] = "strategy"
SIZE_KEY: Final[str] = "size"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "ADAPTIVE_STRATEGY",
    "DEFAULT_BATCH_NAME",
    "DEFAULT_BATCH_STRATEGY",
    "DEFAULT_ENABLED",
    "DESCRIPTION_KEY",
    "DYNAMIC_STRATEGY",
    "ENABLED_KEY",
    "FIXED_STRATEGY",
    "MAX_BATCH_NAME_LENGTH",
    "MIN_BATCH_NAME_LENGTH",
    "NAME_KEY",
    "SIZE_KEY",
    "STREAMING_STRATEGY",
    "STRATEGY_KEY",
    "SUPPORTED_BATCH_STRATEGIES",
]