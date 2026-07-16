"""Tests for ai_testing.snapshots.constants."""

from __future__ import annotations

from ai_testing.snapshots import constants


def test_default_snapshot_name() -> None:
    assert constants.DEFAULT_SNAPSHOT_NAME == "snapshot"


def test_default_values() -> None:
    assert constants.DEFAULT_FORMAT == "json"
    assert constants.DEFAULT_ENABLED is True


def test_supported_formats() -> None:
    assert constants.SUPPORTED_FORMATS == frozenset(
        {
            "json",
            "yaml",
            "text",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_SNAPSHOT_NAME_LENGTH == 1
    assert constants.MAX_SNAPSHOT_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.FORMAT_KEY == "format"
    assert constants.CONTENT_KEY == "content"
    assert constants.ENABLED_KEY == "enabled"