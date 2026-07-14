from ai_observability.config.constants import (
    DEFAULT_ENABLED,
    DEFAULT_EXPORT_INTERVAL,
    DEFAULT_LOG_LEVEL,
    DEFAULT_SAMPLING_RATE,
)


def test_defaults() -> None:
    assert DEFAULT_ENABLED is True
    assert DEFAULT_EXPORT_INTERVAL == 60
    assert DEFAULT_LOG_LEVEL == "INFO"
    assert DEFAULT_SAMPLING_RATE == 1.0
