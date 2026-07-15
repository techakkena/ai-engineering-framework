"""
Tests for ai_deployment.versioning.operations.
"""

import pytest

from ai_deployment.versioning.operations import (
    SemanticVersion,
    VersionService,
)


def test_parse() -> None:
    version = VersionService.parse("1.2.3")

    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3


def test_initial() -> None:
    version = VersionService.initial()

    assert str(version) == "0.1.0"


def test_bump_major() -> None:
    version = SemanticVersion(1, 2, 3)

    assert str(
        VersionService.bump_major(version)
    ) == "2.0.0"


def test_bump_minor() -> None:
    version = SemanticVersion(1, 2, 3)

    assert str(
        VersionService.bump_minor(version)
    ) == "1.3.0"


def test_bump_patch() -> None:
    version = SemanticVersion(1, 2, 3)

    assert str(
        VersionService.bump_patch(version)
    ) == "1.2.4"


def test_invalid_version() -> None:
    with pytest.raises(ValueError):
        VersionService.parse("1.2")


def test_version_ordering() -> None:
    assert SemanticVersion(
        1,
        0,
        0,
    ) < SemanticVersion(
        1,
        0,
        1,
    )