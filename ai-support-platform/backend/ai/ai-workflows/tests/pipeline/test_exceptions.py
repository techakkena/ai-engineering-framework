from __future__ import annotations

import pytest

from ai_workflows.pipeline.exceptions import (
    PipelineExecutionError,
)


def test_pipeline_execution_error() -> None:
    with pytest.raises(PipelineExecutionError):
        raise PipelineExecutionError()
