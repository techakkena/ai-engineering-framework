"""Constants for the ai_testing.fixtures module."""

from __future__ import annotations

from typing import Final

# Default fixture metadata.
DEFAULT_FIXTURE_NAME: Final[str] = "fixture"
DEFAULT_FIXTURE_SCOPE: Final[str] = "function"

# Supported pytest fixture scopes.
FUNCTION_SCOPE: Final[str] = "function"
CLASS_SCOPE: Final[str] = "class"
MODULE_SCOPE: Final[str] = "module"
PACKAGE_SCOPE: Final[str] = "package"
SESSION_SCOPE: Final[str] = "session"

SUPPORTED_FIXTURE_SCOPES: Final[frozenset[str]] = frozenset(
    {
        FUNCTION_SCOPE,
        CLASS_SCOPE,
        MODULE_SCOPE,
        PACKAGE_SCOPE,
        SESSION_SCOPE,
    }
)

# Fixture behavior.
DEFAULT_AUTOUSE: Final[bool] = False
DEFAULT_CACHE_ENABLED: Final[bool] = True

# Validation.
MIN_FIXTURE_NAME_LENGTH: Final[int] = 1
MAX_FIXTURE_NAME_LENGTH: Final[int] = 255

# Metadata keys.
NAME_KEY: Final[str] = "name"
SCOPE_KEY: Final[str] = "scope"
AUTOUSE_KEY: Final[str] = "autouse"
DESCRIPTION_KEY: Final[str] = "description"
TAGS_KEY: Final[str] = "tags"
CACHE_KEY: Final[str] = "cache"

__all__ = [
    "AUTOUSE_KEY",
    "CACHE_KEY",
    "CLASS_SCOPE",
    "DEFAULT_AUTOUSE",
    "DEFAULT_CACHE_ENABLED",
    "DEFAULT_FIXTURE_NAME",
    "DEFAULT_FIXTURE_SCOPE",
    "DESCRIPTION_KEY",
    "FUNCTION_SCOPE",
    "MAX_FIXTURE_NAME_LENGTH",
    "MIN_FIXTURE_NAME_LENGTH",
    "MODULE_SCOPE",
    "NAME_KEY",
    "PACKAGE_SCOPE",
    "SESSION_SCOPE",
    "SCOPE_KEY",
    "SUPPORTED_FIXTURE_SCOPES",
    "TAGS_KEY",
]