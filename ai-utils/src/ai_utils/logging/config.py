"""
Configuration models for the logging package.

This module defines the configuration object used to initialize and
customize logging throughout the AI Engineering Framework.
"""

from __future__ import annotations

from dataclasses import dataclass

from ai_utils.logging.constants import (
    DEFAULT_BACKUP_COUNT,
    DEFAULT_DATE_FORMAT,
    DEFAULT_ENCODING,
    DEFAULT_LOG_DIRECTORY,
    DEFAULT_LOG_FILENAME,
    DEFAULT_LOG_FORMAT,
    DEFAULT_LOG_LEVEL,
    DEFAULT_MAX_BYTES,
)
from ai_utils.logging.exceptions import LoggingConfigurationError

__all__ = ["LoggingConfig"]


@dataclass(slots=True)
class LoggingConfig:
    """Configuration for application logging."""

    level: str = DEFAULT_LOG_LEVEL

    console_enabled: bool = True

    file_enabled: bool = False

    log_directory: str = DEFAULT_LOG_DIRECTORY

    log_filename: str = DEFAULT_LOG_FILENAME

    max_bytes: int = DEFAULT_MAX_BYTES

    backup_count: int = DEFAULT_BACKUP_COUNT

    encoding: str = DEFAULT_ENCODING

    log_format: str = DEFAULT_LOG_FORMAT

    date_format: str = DEFAULT_DATE_FORMAT

    def __post_init__(self) -> None:
        """Validate configuration values after initialization."""

        self.level = self.level.upper().strip()

        if not self.level:
            raise LoggingConfigurationError("Log level cannot be empty.")

        if not self.log_directory.strip():
            raise LoggingConfigurationError("Log directory cannot be empty.")

        if not self.log_filename.strip():
            raise LoggingConfigurationError("Log filename cannot be empty.")

        if self.max_bytes <= 0:
            raise LoggingConfigurationError("max_bytes must be greater than zero.")

        if self.backup_count < 0:
            raise LoggingConfigurationError("backup_count cannot be negative.")

        if not self.encoding.strip():
            raise LoggingConfigurationError("Encoding cannot be empty.")

        if not self.log_format.strip():
            raise LoggingConfigurationError("Log format cannot be empty.")

        if not self.date_format.strip():
            raise LoggingConfigurationError("Date format cannot be empty.")
