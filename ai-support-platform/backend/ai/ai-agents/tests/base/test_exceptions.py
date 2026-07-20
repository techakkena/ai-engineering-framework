from __future__ import annotations

import pytest

from ai_agents.base.exceptions import (
    AgentConfigurationError,
    AgentError,
    AgentExecutionError,
    AgentValidationError,
)


def test_base_exception() -> None:
    with pytest.raises(AgentError):
        raise AgentError()


def test_configuration_exception() -> None:
    with pytest.raises(AgentConfigurationError):
        raise AgentConfigurationError()


def test_execution_exception() -> None:
    with pytest.raises(AgentExecutionError):
        raise AgentExecutionError()


def test_validation_exception() -> None:
    with pytest.raises(AgentValidationError):
        raise AgentValidationError()
