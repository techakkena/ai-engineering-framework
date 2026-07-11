"""
Formatter implementations for the logging package.

This module provides formatter factories used by the logging subsystem.
"""

from __future__ import annotations

import json
import logging
from typing import Any

from ai_utils.logging.config import LoggingConfig

__all__ = [
    "JsonFormatter",
    "create_formatter",
]


class JsonFormatter(logging.Formatter):
    """Formatter that outputs log records as JSON."""

    def format(self, record: logging.LogRecord) -> str:
        """Format a log record as a JSON string."""

        log_record: dict[str, Any] = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }

        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_record, ensure_ascii=False)


def create_formatter(config: LoggingConfig) -> logging.Formatter:
    """
    Create the standard formatter.

    Parameters
    ----------
    config
        Logging configuration.

    Returns
    -------
    logging.Formatter
        Configured formatter instance.
    """

    return logging.Formatter(
        fmt=config.log_format,
        datefmt=config.date_format,
    )
