"""
Tests for ai_deployment.release.exceptions.
"""

from ai_deployment.release.exceptions import (
    ReleaseConfigurationError,
    ReleaseError,
    ReleaseValidationError,
)


def test_release_error() -> None:
    error = ReleaseError("error")

    assert str(error) == "error"


def test_configuration_error() -> None:
    assert isinstance(
        ReleaseConfigurationError("config"),
        ReleaseError,
    )


def test_validation_error() -> None:
    assert isinstance(
        ReleaseValidationError("validation"),
        ReleaseError,
    )