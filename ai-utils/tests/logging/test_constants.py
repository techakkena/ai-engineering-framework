"""
Unit tests for logging constants.
"""

from __future__ import annotations

from ai_utils.logging import constants


def test_default_log_level() -> None:
    assert constants.DEFAULT_LOG_LEVEL == "INFO"


def test_default_log_directory() -> None:
    assert constants.DEFAULT_LOG_DIRECTORY == "logs"


def test_default_log_filename() -> None:
    assert constants.DEFAULT_LOG_FILENAME == "application.log"


def test_default_max_bytes() -> None:
    assert constants.DEFAULT_MAX_BYTES > 0


def test_default_backup_count() -> None:
    assert constants.DEFAULT_BACKUP_COUNT >= 0


def test_default_encoding() -> None:
    assert constants.DEFAULT_ENCODING == "utf-8"


def test_default_log_format_is_not_empty() -> None:
    assert constants.DEFAULT_LOG_FORMAT


def test_default_date_format_is_not_empty() -> None:
    assert constants.DEFAULT_DATE_FORMAT
