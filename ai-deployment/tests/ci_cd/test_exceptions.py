"""
Tests for ai_deployment.ci_cd.exceptions.
"""

from ai_deployment.ci_cd.exceptions import (
    CICDConfigurationError,
    CICDError,
    CICDPipelineError,
)


def test_cicd_error() -> None:
    error = CICDError("error")
    assert str(error) == "error"


def test_configuration_error() -> None:
    assert isinstance(
        CICDConfigurationError("config"),
        CICDError,
    )


def test_pipeline_error() -> None:
    assert isinstance(
        CICDPipelineError("pipeline"),
        CICDError,
    )