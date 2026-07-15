"""
Tests for ai_deployment.utils.exceptions.
"""

from ai_deployment.utils.exceptions import (
    DeploymentUtilityError,
    ValidationError,
)


def test_deployment_utility_error() -> None:
    error = DeploymentUtilityError("error")

    assert str(error) == "error"


def test_validation_error() -> None:
    assert isinstance(
        ValidationError("validation"),
        DeploymentUtilityError,
    )