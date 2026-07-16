"""Constants for the ai_plugins.discovery module."""

from __future__ import annotations

from typing import Final

# Default discovery configuration.
DEFAULT_DISCOVERY_NAME: Final[str] = "discovery"
DEFAULT_DISCOVERY_STRATEGY: Final[str] = "filesystem"
DEFAULT_ENABLED: Final[bool] = True

# Supported discovery strategies.
FILESYSTEM_STRATEGY: Final[str] = "filesystem"
ENTRY_POINTS_STRATEGY: Final[str] = "entry_points"
PACKAGE_SCAN_STRATEGY: Final[str] = "package_scan"
MANUAL_STRATEGY: Final[str] = "manual"

SUPPORTED_DISCOVERY_STRATEGIES: Final[frozenset[str]] = frozenset(
    {
        FILESYSTEM_STRATEGY,
        ENTRY_POINTS_STRATEGY,
        PACKAGE_SCAN_STRATEGY,
        MANUAL_STRATEGY,
    }
)

# Validation.
MIN_DISCOVERY_NAME_LENGTH: Final[int] = 1
MAX_DISCOVERY_NAME_LENGTH: Final[int] = 255

# Metadata keys.
NAME_KEY: Final[str] = "name"
STRATEGY_KEY: Final[str] = "strategy"
PATH_KEY: Final[str] = "path"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "DEFAULT_DISCOVERY_NAME",
    "DEFAULT_DISCOVERY_STRATEGY",
    "DEFAULT_ENABLED",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "ENTRY_POINTS_STRATEGY",
    "FILESYSTEM_STRATEGY",
    "MANUAL_STRATEGY",
    "MAX_DISCOVERY_NAME_LENGTH",
    "MIN_DISCOVERY_NAME_LENGTH",
    "NAME_KEY",
    "PACKAGE_SCAN_STRATEGY",
    "PATH_KEY",
    "STRATEGY_KEY",
    "SUPPORTED_DISCOVERY_STRATEGIES",
]