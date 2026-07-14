from ai_observability.logging.constants import (
    LogLevel,
)


def test_log_levels() -> None:
    assert LogLevel.INFO.value == "info"
    assert LogLevel.ERROR.value == "error"


def test_log_level_count() -> None:
    assert len(LogLevel) == 5
