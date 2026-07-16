"""Constants for the ai_plugins.lifecycle module."""

from __future__ import annotations

from typing import Final

# Default lifecycle configuration.
DEFAULT_LIFECYCLE_NAME: Final[str] = "lifecycle"
DEFAULT_PHASE: Final[str] = "initialize"
DEFAULT_ENABLED: Final[bool] = True

# Supported lifecycle phases.
INITIALIZE_PHASE: Final[str] = "initialize"
START_PHASE: Final[str] = "start"
STOP_PHASE: Final[str] = "stop"
DESTROY_PHASE: Final[str] = "destroy"

SUPPORTED_LIFECYCLE_PHASES: Final[frozenset[str]] = frozenset(
    {
        INITIALIZE_PHASE,
        START_PHASE,
        STOP_PHASE,
        DESTROY_PHASE,
    }
)

# Validation.
MIN_LIFECYCLE_NAME_LENGTH: Final[int] = 1
MAX_LIFECYCLE_NAME_LENGTH: Final[int] = 255

# Metadata keys.
NAME_KEY: Final[str] = "name"
PHASE_KEY: Final[str] = "phase"
ORDER_KEY: Final[str] = "order"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "DEFAULT_ENABLED",
    "DEFAULT_LIFECYCLE_NAME",
    "DEFAULT_PHASE",
    "DESCRIPTION_KEY",
    "DESTROY_PHASE",
    "ENABLED_KEY",
    "INITIALIZE_PHASE",
    "MAX_LIFECYCLE_NAME_LENGTH",
    "MIN_LIFECYCLE_NAME_LENGTH",
    "NAME_KEY",
    "ORDER_KEY",
    "PHASE_KEY",
    "START_PHASE",
    "STOP_PHASE",
    "SUPPORTED_LIFECYCLE_PHASES",
]