"""Constants for the ai_plugins.sandbox module."""

from __future__ import annotations

from typing import Final

# Default sandbox configuration.
DEFAULT_SANDBOX_NAME: Final[str] = "sandbox"
DEFAULT_SANDBOX_MODE: Final[str] = "isolated"
DEFAULT_ENABLED: Final[bool] = True

# Supported sandbox modes.
ISOLATED_MODE: Final[str] = "isolated"
PROCESS_MODE: Final[str] = "process"
CONTAINER_MODE: Final[str] = "container"
VM_MODE: Final[str] = "virtual_machine"

SUPPORTED_SANDBOX_MODES: Final[frozenset[str]] = frozenset(
    {
        ISOLATED_MODE,
        PROCESS_MODE,
        CONTAINER_MODE,
        VM_MODE,
    }
)

# Validation.
MIN_SANDBOX_NAME_LENGTH: Final[int] = 1
MAX_SANDBOX_NAME_LENGTH: Final[int] = 255

# Metadata keys.
NAME_KEY: Final[str] = "name"
MODE_KEY: Final[str] = "mode"
MEMORY_LIMIT_KEY: Final[str] = "memory_limit"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "CONTAINER_MODE",
    "DEFAULT_ENABLED",
    "DEFAULT_SANDBOX_MODE",
    "DEFAULT_SANDBOX_NAME",
    "DESCRIPTION_KEY",
    "ENABLED_KEY",
    "ISOLATED_MODE",
    "MAX_SANDBOX_NAME_LENGTH",
    "MEMORY_LIMIT_KEY",
    "MIN_SANDBOX_NAME_LENGTH",
    "MODE_KEY",
    "NAME_KEY",
    "PROCESS_MODE",
    "SUPPORTED_SANDBOX_MODES",
    "VM_MODE",
]