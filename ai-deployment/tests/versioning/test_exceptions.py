"""
Tests for ai_deployment.versioning.exceptions.
"""

from ai_deployment.versioning.exceptions import (
    VersionError,
    VersionFormatError,
    VersionValidationError,
)


def test_version_error() -> None:
    error = VersionError("error")

    assert str(error) == "error"


def test_format_error() -> None:
    assert isinstance(
        VersionFormatError("format"),
        VersionError,
    )


def test_validation_error() -> None:
    assert isinstance(
        VersionValidationError("validation"),
        VersionError,
    )