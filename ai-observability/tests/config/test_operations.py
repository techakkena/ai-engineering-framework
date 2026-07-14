import pytest

from ai_observability.config.operations import (
    ObservabilityConfig,
)


def test_default_config() -> None:
    config = ObservabilityConfig()

    assert config.enabled is True
    assert config.export_interval == 60
    assert config.log_level == "INFO"
    assert config.sampling_rate == 1.0


def test_validate_success() -> None:
    ObservabilityConfig().validate()


def test_invalid_export_interval() -> None:
    config = ObservabilityConfig(
        export_interval=0,
    )

    with pytest.raises(ValueError):
        config.validate()


def test_invalid_sampling_rate() -> None:
    config = ObservabilityConfig(
        sampling_rate=2.0,
    )

    with pytest.raises(ValueError):
        config.validate()


def test_invalid_log_level() -> None:
    config = ObservabilityConfig(
        log_level="",
    )

    with pytest.raises(ValueError):
        config.validate()
