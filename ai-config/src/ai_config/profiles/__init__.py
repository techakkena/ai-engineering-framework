"""
Profiles module.

Author: TECHAKKENA
"""

from ai_config.profiles.constants import (
    DEFAULT_PROFILE,
    PROFILE_SEPARATOR,
    SUPPORTED_PROFILES,
)
from ai_config.profiles.exceptions import (
    DuplicateProfileError,
    InvalidProfileError,
    ProfileError,
    ProfileNotFoundError,
)
from ai_config.profiles.operations import ProfileManager

__all__ = [
    "DEFAULT_PROFILE",
    "PROFILE_SEPARATOR",
    "SUPPORTED_PROFILES",
    "ProfileManager",
    "ProfileError",
    "ProfileNotFoundError",
    "DuplicateProfileError",
    "InvalidProfileError",
]
