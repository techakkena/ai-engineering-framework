from __future__ import annotations

import pytest

from ai_agents.tools.exceptions import ToolExecutionError


def test_tool_execution_error() -> None:
    with pytest.raises(ToolExecutionError):
        raise ToolExecutionError()
