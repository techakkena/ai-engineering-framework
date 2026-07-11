"""
Logging constants for the AI Engineering Framework.

This module defines the default configuration values used throughout
the logging package. Keeping these values centralized ensures
consistency, maintainability, and avoids hard-coded "magic" values
across the codebase.
"""

from __future__ import annotations

__all__ = [
    "DEFAULT_LOG_LEVEL",
    "DEFAULT_LOG_FORMAT",
    "DEFAULT_DATE_FORMAT",
    "DEFAULT_LOG_DIRECTORY",
    "DEFAULT_LOG_FILENAME",
    "DEFAULT_MAX_BYTES",
    "DEFAULT_BACKUP_COUNT",
    "DEFAULT_ENCODING",
    "LOGGER_NAME_SEPARATOR",
]

# ---------------------------------------------------------------------
# Logging Defaults
# ---------------------------------------------------------------------

DEFAULT_LOG_LEVEL: str = "INFO"

DEFAULT_LOG_FORMAT: str = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"

DEFAULT_DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"

# ---------------------------------------------------------------------
# File Logging
# ---------------------------------------------------------------------

DEFAULT_LOG_DIRECTORY: str = "logs"

DEFAULT_LOG_FILENAME: str = "application.log"

DEFAULT_MAX_BYTES: int = 10 * 1024 * 1024  # 10 MB

DEFAULT_BACKUP_COUNT: int = 5

DEFAULT_ENCODING: str = "utf-8"

# ---------------------------------------------------------------------
# Miscellaneous
# ---------------------------------------------------------------------

LOGGER_NAME_SEPARATOR: str = "."
