"""
Tests for ai_deployment.packaging.constants.
"""

from ai_deployment.packaging.constants import (
    DEFAULT_BUILD_DIRECTORY,
    DEFAULT_PACKAGE_FORMAT,
    SUPPORTED_PACKAGE_FORMATS,
)


def test_default_build_directory() -> None:
    assert DEFAULT_BUILD_DIRECTORY == "dist"


def test_default_package_format() -> None:
    assert DEFAULT_PACKAGE_FORMAT == "wheel"


def test_supported_package_formats() -> None:
    assert "wheel" in SUPPORTED_PACKAGE_FORMATS
    assert "sdist" in SUPPORTED_PACKAGE_FORMATS
    assert "docker" in SUPPORTED_PACKAGE_FORMATS