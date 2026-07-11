"""
Unit tests for logger creation.
"""

from __future__ import annotations

import logging

from ai_utils.logging.config import LoggingConfig
from ai_utils.logging.logger import create_logger, get_logger


def test_get_logger_returns_logger() -> None:
    logger = get_logger("test_logger")

    assert isinstance(logger, logging.Logger)


def test_create_logger_returns_logger() -> None:
    logger = create_logger("custom_logger")

    assert isinstance(logger, logging.Logger)


def test_logger_name() -> None:
    logger = get_logger("sample")

    assert logger.name == "sample"


def test_duplicate_handlers_are_not_created() -> None:
    logger1 = get_logger("duplicate")

    handler_count = len(logger1.handlers)

    logger2 = get_logger("duplicate")

    assert logger1 is logger2
    assert len(logger2.handlers) == handler_count


def test_console_handler_enabled() -> None:
    config = LoggingConfig(console_enabled=True)

    logger = create_logger("console_logger", config)

    assert len(logger.handlers) >= 1
