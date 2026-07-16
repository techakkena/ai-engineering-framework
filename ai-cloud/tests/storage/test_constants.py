"""Tests for ai_cloud.storage.constants."""

from __future__ import annotations

from ai_cloud.storage import constants


def test_default_values() -> None:
    assert constants.DEFAULT_STORAGE_NAME == "storage"
    assert constants.DEFAULT_STORAGE_TYPE == "object"
    assert constants.DEFAULT_ENABLED is True


def test_supported_storage_types() -> None:
    assert constants.SUPPORTED_STORAGE_TYPES == frozenset(
        {
            "object",
            "block",
            "file",
            "archive",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_STORAGE_NAME_LENGTH == 1
    assert constants.MAX_STORAGE_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.TYPE_KEY == "type"
    assert constants.CAPACITY_KEY == "capacity"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"