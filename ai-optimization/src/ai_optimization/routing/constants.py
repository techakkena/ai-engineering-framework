"""Constants for the ai_optimization.routing module."""

from __future__ import annotations

from typing import Final

# Default routing configuration.
DEFAULT_ROUTE_NAME: Final[str] = "route"
DEFAULT_ROUTING_STRATEGY: Final[str] = "round_robin"
DEFAULT_ENABLED: Final[bool] = True

# Supported routing strategies.
ROUND_ROBIN_STRATEGY: Final[str] = "round_robin"
LEAST_LOADED_STRATEGY: Final[str] = "least_loaded"
WEIGHTED_STRATEGY: Final[str] = "weighted"
RANDOM_STRATEGY: Final[str] = "random"

SUPPORTED_ROUTING_STRATEGIES: Final[frozenset[str]] = frozenset(
    {
        ROUND_ROBIN_STRATEGY,
        LEAST_LOADED_STRATEGY,
        WEIGHTED_STRATEGY,
        RANDOM_STRATEGY,
    }
)

# Validation.
MIN_ROUTE_NAME_LENGTH: Final[int] = 1
MAX_ROUTE_NAME_LENGTH: Final[int] = 255

# Metadata keys.
NAME_KEY: Final[str] = "name"
STRATEGY_KEY: Final[str] = "strategy"
WEIGHT_KEY: Final[str] = "weight"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "DEFAULT_ENABLED",
    "DEFAULT_ROUTE_NAME",
    "DEFAULT_ROUTING_STRATEGY",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "LEAST_LOADED_STRATEGY",
    "MAX_ROUTE_NAME_LENGTH",
    "MIN_ROUTE_NAME_LENGTH",
    "NAME_KEY",
    "RANDOM_STRATEGY",
    "ROUND_ROBIN_STRATEGY",
    "STRATEGY_KEY",
    "SUPPORTED_ROUTING_STRATEGIES",
    "WEIGHT_KEY",
    "WEIGHTED_STRATEGY",
]