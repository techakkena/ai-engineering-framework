"""
Tests for ai_deployment.release.constants.
"""

from ai_deployment.release.constants import (
    DEFAULT_RELEASE_CHANNEL,
    DEFAULT_VERSION_PREFIX,
    SUPPORTED_RELEASE_CHANNELS,
)


def test_default_release_channel() -> None:
    assert DEFAULT_RELEASE_CHANNEL == "stable"


def test_default_version_prefix() -> None:
    assert DEFAULT_VERSION_PREFIX == "v"


def test_supported_release_channels() -> None:
    assert "alpha" in SUPPORTED_RELEASE_CHANNELS
    assert "beta" in SUPPORTED_RELEASE_CHANNELS
    assert "rc" in SUPPORTED_RELEASE_CHANNELS
    assert "stable" in SUPPORTED_RELEASE_CHANNELS