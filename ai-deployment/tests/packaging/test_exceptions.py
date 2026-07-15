"""
Tests for ai_deployment.packaging.exceptions.
"""

from ai_deployment.packaging.exceptions import (
    PackageBuildError,
    PackagingConfigurationError,
    PackagingError,
)


def test_packaging_error() -> None:
    error = PackagingError("error")
    assert str(error) == "error"


def test_configuration_error() -> None:
    assert isinstance(
        PackagingConfigurationError("config"),
        PackagingError,
    )


def test_build_error() -> None:
    assert isinstance(
        PackageBuildError("build"),
        PackagingError,
    )