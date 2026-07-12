"""
Tests for settings constants.
"""

from ai_config.settings.constants import (
    DEFAULT_COPY_ON_MERGE,
    DEFAULT_SEPARATOR,
    DEFAULT_SETTINGS,
)


def test_default_settings() -> None:
    assert DEFAULT_SETTINGS == {}


def test_default_separator() -> None:
    assert DEFAULT_SEPARATOR == "."


def test_default_copy_on_merge() -> None:
    assert DEFAULT_COPY_ON_MERGE is True
