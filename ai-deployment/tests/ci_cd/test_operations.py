"""
Tests for ai_deployment.ci_cd.operations.
"""

import pytest

from ai_deployment.ci_cd.exceptions import (
    CICDConfigurationError,
    CICDPipelineError,
)
from ai_deployment.ci_cd.operations import (
    Pipeline,
    PipelineService,
)


def test_run_pipeline() -> None:
    service = PipelineService()

    pipeline = Pipeline(name="build")

    assert service.run(pipeline)


def test_validate_pipeline() -> None:
    service = PipelineService()

    pipeline = Pipeline()

    assert service.validate(pipeline)


def test_cancel_pipeline() -> None:
    service = PipelineService()

    pipeline = Pipeline(name="deploy")

    assert service.cancel(pipeline)


def test_invalid_pipeline_name() -> None:
    service = PipelineService()

    pipeline = Pipeline(name="")

    with pytest.raises(CICDConfigurationError):
        service.run(pipeline)


def test_invalid_branch() -> None:
    service = PipelineService()

    pipeline = Pipeline(
        name="build",
        branch="",
    )

    with pytest.raises(CICDConfigurationError):
        service.validate(pipeline)


def test_cancel_invalid_pipeline() -> None:
    service = PipelineService()

    pipeline = Pipeline(name="")

    with pytest.raises(CICDPipelineError):
        service.cancel(pipeline)