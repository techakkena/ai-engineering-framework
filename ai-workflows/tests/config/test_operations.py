import pytest

from ai_workflows.config.operations import (
    WorkflowConfig,
)


def test_default_config() -> None:
    config = WorkflowConfig()

    assert config.timeout == 60
    assert config.max_retries == 3
    assert config.fail_fast is True


def test_validate_success() -> None:
    WorkflowConfig().validate()


def test_invalid_timeout() -> None:
    config = WorkflowConfig(
        timeout=0,
    )

    with pytest.raises(ValueError):
        config.validate()


def test_invalid_retries() -> None:
    config = WorkflowConfig(
        max_retries=-1,
    )

    with pytest.raises(ValueError):
        config.validate()
