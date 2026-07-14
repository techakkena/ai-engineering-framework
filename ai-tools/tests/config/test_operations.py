import pytest

from ai_tools.config.operations import (
    ToolConfig,
)


def test_default_config() -> None:
    config = ToolConfig()

    assert config.timeout == 30
    assert config.retry_count == 3
    assert config.user_agent == "ai-tools"
    assert config.verify_ssl is True


def test_validate_success() -> None:
    ToolConfig().validate()


def test_invalid_timeout() -> None:
    config = ToolConfig(
        timeout=0,
    )

    with pytest.raises(ValueError):
        config.validate()


def test_invalid_retry_count() -> None:
    config = ToolConfig(
        retry_count=-1,
    )

    with pytest.raises(ValueError):
        config.validate()


def test_invalid_user_agent() -> None:
    config = ToolConfig(
        user_agent="",
    )

    with pytest.raises(ValueError):
        config.validate()
