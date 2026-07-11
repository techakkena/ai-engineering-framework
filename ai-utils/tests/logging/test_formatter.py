"""
Unit tests for logging formatters.
"""

from __future__ import annotations

import json
import logging
import sys

from ai_utils.logging.config import LoggingConfig
from ai_utils.logging.formatter import JsonFormatter, create_formatter


def test_create_formatter_returns_formatter() -> None:
    """create_formatter should return a logging.Formatter instance."""

    config = LoggingConfig()

    formatter = create_formatter(config)

    assert isinstance(formatter, logging.Formatter)


def test_formatter_formats_message() -> None:
    """Standard formatter should format log records."""

    config = LoggingConfig()

    formatter = create_formatter(config)

    record = logging.LogRecord(
        name="test_logger",
        level=logging.INFO,
        pathname=__file__,
        lineno=10,
        msg="Hello World",
        args=(),
        exc_info=sys.exc_info(),
    )

    output = formatter.format(record)

    assert "Hello World" in output
    assert "INFO" in output


def test_json_formatter_returns_json() -> None:
    """JsonFormatter should return valid JSON."""

    formatter = JsonFormatter()

    record = logging.LogRecord(
        name="test_logger",
        level=logging.INFO,
        pathname=__file__,
        lineno=10,
        msg="Hello JSON",
        args=(),
        exc_info=sys.exc_info(),
    )

    output = formatter.format(record)

    parsed = json.loads(output)

    assert isinstance(parsed, dict)


def test_json_formatter_contains_level() -> None:
    """JSON output should contain the log level."""

    formatter = JsonFormatter()

    record = logging.LogRecord(
        name="test_logger",
        level=logging.WARNING,
        pathname=__file__,
        lineno=20,
        msg="Warning message",
        args=(),
        exc_info=sys.exc_info(),
    )

    parsed = json.loads(formatter.format(record))

    assert parsed["level"] == "WARNING"


def test_json_formatter_contains_message() -> None:
    """JSON output should contain the log message."""

    formatter = JsonFormatter()

    record = logging.LogRecord(
        name="test_logger",
        level=logging.INFO,
        pathname=__file__,
        lineno=30,
        msg="Framework Test",
        args=(),
        exc_info=sys.exc_info(),
    )

    parsed = json.loads(formatter.format(record))

    assert parsed["message"] == "Framework Test"


def test_json_formatter_handles_exception() -> None:
    """JSON formatter should include exception information."""

    formatter = JsonFormatter()

    try:
        raise ValueError("Sample error")
    except ValueError:
        record = logging.LogRecord(
            name="test_logger",
            level=logging.ERROR,
            pathname=__file__,
            lineno=40,
            msg="An error occurred",
            args=(),
            exc_info=sys.exc_info(),
        )

        # record.exc_info = __import__("sys").exc_info()

    parsed = json.loads(formatter.format(record))

    assert "exception" in parsed
    assert "ValueError" in parsed["exception"]
