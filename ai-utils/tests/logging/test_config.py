"""
Unit tests for LoggingConfig.
"""

from __future__ import annotations

from typing import Any, cast

import pytest

from ai_utils.logging.config import LoggingConfig
from ai_utils.logging.exceptions import LoggingConfigurationError


def test_default_configuration() -> None:
    config = LoggingConfig()

    assert config.level == "INFO"
    assert config.console_enabled is True
    assert config.file_enabled is False


def test_log_level_is_normalized() -> None:
    config = LoggingConfig(level="debug")

    assert config.level == "DEBUG"


@pytest.mark.parametrize(
    ("kwargs", "message"),
    [
        ({"level": ""}, "Log level"),
        ({"log_directory": ""}, "Log directory"),
        ({"log_filename": ""}, "Log filename"),
        ({"max_bytes": 0}, "max_bytes"),
        ({"backup_count": -1}, "backup_count"),
        ({"encoding": ""}, "Encoding"),
        ({"log_format": ""}, "Log format"),
        ({"date_format": ""}, "Date format"),
    ],
)
def test_invalid_configuration(
    kwargs: dict[str, Any],
    message: str,
) -> None:
    with pytest.raises(LoggingConfigurationError, match=message):
        LoggingConfig(**cast(dict[str, Any], kwargs))
