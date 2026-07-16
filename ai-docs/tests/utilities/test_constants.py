"""Tests for ai_docs.utilities.constants."""

from __future__ import annotations

from ai_docs.utilities import constants


def test_default_values() -> None:
    assert constants.DEFAULT_VERSION == "1.0.0"
    assert constants.DEFAULT_AUTHOR == "Unknown"


def test_name_limits() -> None:
    assert constants.MIN_NAME_LENGTH == 1
    assert constants.MAX_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.VERSION_KEY == "version"
    assert constants.AUTHOR_KEY == "author"
    assert constants.DESCRIPTION_KEY == "description"