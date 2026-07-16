"""Constants for the ai_plugins.loading module."""

from __future__ import annotations

from typing import Final

# Default loader configuration.
DEFAULT_LOADER_NAME: Final[str] = "loader"
DEFAULT_LOADING_MODE: Final[str] = "lazy"
DEFAULT_ENABLED: Final[bool] = True

# Supported loading modes.
LAZY_MODE: Final[str] = "lazy"
EAGER_MODE: Final[str] = "eager"
ON_DEMAND_MODE: Final[str] = "on_demand"
ISOLATED_MODE: Final[str] = "isolated"

SUPPORTED_LOADING_MODES: Final[frozenset[str]] = frozenset(
    {
        LAZY_MODE,
        EAGER_MODE,
        ON_DEMAND_MODE,
        ISOLATED_MODE,
    }
)

# Validation.
MIN_LOADER_NAME_LENGTH: Final[int] = 1
MAX_LOADER_NAME_LENGTH: Final[int] = 255

# Metadata keys.
NAME_KEY: Final[str] = "name"
MODE_KEY: Final[str] = "mode"
TIMEOUT_KEY: Final[str] = "timeout"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "DEFAULT_ENABLED",
    "DEFAULT_LOADER_NAME",
    "DEFAULT_LOADING_MODE",
    "DESCRIPTION_KEY",
    "EAGER_MODE",
    "ENABLED_KEY",
    "ISOLATED_MODE",
    "LAZY_MODE",
    "MAX_LOADER_NAME_LENGTH",
    "MIN_LOADER_NAME_LENGTH",
    "MODE_KEY",
    "NAME_KEY",
    "ON_DEMAND_MODE",
    "SUPPORTED_LOADING_MODES",
    "TIMEOUT_KEY",
]