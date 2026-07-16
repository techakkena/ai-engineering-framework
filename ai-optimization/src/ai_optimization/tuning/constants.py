"""Constants for the ai_optimization.tuning module."""

from __future__ import annotations

from typing import Final

# Default tuning configuration.
DEFAULT_TUNING_NAME: Final[str] = "tuning"
DEFAULT_TUNING_STRATEGY: Final[str] = "grid"
DEFAULT_ENABLED: Final[bool] = True

# Supported tuning strategies.
GRID_STRATEGY: Final[str] = "grid"
RANDOM_STRATEGY: Final[str] = "random"
BAYESIAN_STRATEGY: Final[str] = "bayesian"
EVOLUTIONARY_STRATEGY: Final[str] = "evolutionary"

SUPPORTED_TUNING_STRATEGIES: Final[frozenset[str]] = frozenset(
    {
        GRID_STRATEGY,
        RANDOM_STRATEGY,
        BAYESIAN_STRATEGY,
        EVOLUTIONARY_STRATEGY,
    }
)

# Validation.
MIN_TUNING_NAME_LENGTH: Final[int] = 1
MAX_TUNING_NAME_LENGTH: Final[int] = 255

# Metadata keys.
NAME_KEY: Final[str] = "name"
STRATEGY_KEY: Final[str] = "strategy"
ITERATIONS_KEY: Final[str] = "iterations"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "BAYESIAN_STRATEGY",
    "DEFAULT_ENABLED",
    "DEFAULT_TUNING_NAME",
    "DEFAULT_TUNING_STRATEGY",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "EVOLUTIONARY_STRATEGY",
    "GRID_STRATEGY",
    "ITERATIONS_KEY",
    "MAX_TUNING_NAME_LENGTH",
    "MIN_TUNING_NAME_LENGTH",
    "NAME_KEY",
    "RANDOM_STRATEGY",
    "STRATEGY_KEY",
    "SUPPORTED_TUNING_STRATEGIES",
]