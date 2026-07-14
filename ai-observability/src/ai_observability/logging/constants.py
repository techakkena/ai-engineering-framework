"""Logging constants."""

from enum import Enum


class LogLevel(str, Enum):
    """Supported log levels."""

    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"
