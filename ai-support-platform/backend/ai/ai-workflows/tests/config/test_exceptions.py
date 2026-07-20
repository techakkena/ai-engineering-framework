from __future__ import annotations

import pytest

from ai_workflows.config.exceptions import (
    WorkflowConfigurationError,
)


def test_configuration_error() -> None:
    with pytest.raises(
        WorkflowConfigurationError,
    ):
        raise WorkflowConfigurationError()
