"""
Tests for ai_deployment.versioning.constants.
"""

from ai_deployment.versioning.constants import (
    DEFAULT_INITIAL_VERSION,
    DEFAULT_VERSION_SEPARATOR,
    SEMVER_PARTS,
)


def test_default_initial_version() -> None:
    assert DEFAULT_INITIAL_VERSION == "0.1.0"


def test_default_separator() -> None:
    assert DEFAULT_VERSION_SEPARATOR == "."


def test_semver_parts() -> None:
    assert SEMVER_PARTS == (
        "major",
        "minor",
        "patch",
    )