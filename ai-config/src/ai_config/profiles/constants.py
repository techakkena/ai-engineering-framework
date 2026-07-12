"""
Constants for the profiles module.

Author: TECHAKKENA
"""

from typing import Final

DEFAULT_PROFILE: Final[str] = "default"

PROFILE_SEPARATOR: Final[str] = "."

SUPPORTED_PROFILES: Final[tuple[str, ...]] = (
    "default",
    "development",
    "testing",
    "staging",
    "production",
)
