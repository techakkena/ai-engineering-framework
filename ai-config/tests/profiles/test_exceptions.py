"""
Unit tests for profile constants.
"""

from ai_config.profiles.constants import (
    DEFAULT_PROFILE,
    PROFILE_SEPARATOR,
    SUPPORTED_PROFILES,
)


def test_default_profile() -> None:
    assert DEFAULT_PROFILE == "default"


def test_profile_separator() -> None:
    assert PROFILE_SEPARATOR == "."


def test_supported_profiles() -> None:
    assert "development" in SUPPORTED_PROFILES
    assert "production" in SUPPORTED_PROFILES
