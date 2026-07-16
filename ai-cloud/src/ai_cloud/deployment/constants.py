"""Constants for the ai_cloud.deployment module."""

from __future__ import annotations

from typing import Final

DEFAULT_DEPLOYMENT_NAME: Final[str] = "deployment"
DEFAULT_DEPLOYMENT_STRATEGY: Final[str] = "rolling"
DEFAULT_ENABLED: Final[bool] = True

ROLLING_STRATEGY: Final[str] = "rolling"
BLUE_GREEN_STRATEGY: Final[str] = "blue_green"
CANARY_STRATEGY: Final[str] = "canary"
RECREATE_STRATEGY: Final[str] = "recreate"

SUPPORTED_DEPLOYMENT_STRATEGIES: Final[frozenset[str]] = frozenset(
    {
        ROLLING_STRATEGY,
        BLUE_GREEN_STRATEGY,
        CANARY_STRATEGY,
        RECREATE_STRATEGY,
    }
)

MIN_DEPLOYMENT_NAME_LENGTH: Final[int] = 1
MAX_DEPLOYMENT_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
STRATEGY_KEY: Final[str] = "strategy"
REPLICAS_KEY: Final[str] = "replicas"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "BLUE_GREEN_STRATEGY",
    "CANARY_STRATEGY",
    "DEFAULT_DEPLOYMENT_NAME",
    "DEFAULT_DEPLOYMENT_STRATEGY",
    "DEFAULT_ENABLED",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "MAX_DEPLOYMENT_NAME_LENGTH",
    "MIN_DEPLOYMENT_NAME_LENGTH",
    "NAME_KEY",
    "RECREATE_STRATEGY",
    "REPLICAS_KEY",
    "ROLLING_STRATEGY",
    "STRATEGY_KEY",
    "SUPPORTED_DEPLOYMENT_STRATEGIES",
]