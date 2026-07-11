"""
Logger creation utilities for the logging package.

This module provides factory functions for creating configured
Python loggers used throughout the AI Engineering Framework.
"""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from ai_utils.logging.config import LoggingConfig
from ai_utils.logging.formatter import create_formatter

__all__ = [
    "create_logger",
    "get_logger",
]


def create_logger(
    name: str,
    config: LoggingConfig | None = None,
) -> logging.Logger:
    """
    Create and configure a logger.

    Parameters
    ----------
    name
        Logger name.

    config
        Optional logging configuration.

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """

    if config is None:
        config = LoggingConfig()

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(config.level)
    logger.propagate = False

    formatter = create_formatter(config)

    if config.console_enabled:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if config.file_enabled:
        log_directory = Path(config.log_directory)
        log_directory.mkdir(parents=True, exist_ok=True)

        file_handler = RotatingFileHandler(
            filename=log_directory / config.log_filename,
            maxBytes=config.max_bytes,
            backupCount=config.backup_count,
            encoding=config.encoding,
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def get_logger(name: str) -> logging.Logger:
    """
    Return a logger using the default configuration.

    Parameters
    ----------
    name
        Logger name.

    Returns
    -------
    logging.Logger
        Configured logger.
    """

    return create_logger(name)
