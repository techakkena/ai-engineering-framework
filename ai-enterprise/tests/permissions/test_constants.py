"""Tests for ai_enterprise.permissions.constants."""

from __future__ import annotations

from ai_enterprise.permissions import constants


def test_default_values() -> None:
    assert constants.DEFAULT_PERMISSION_NAME == "read"
    assert constants.DEFAULT_RESOURCE == "resource"
    assert constants.DEFAULT_ENABLED is True


def test_supported_permissions() -> None:
    assert constants.SUPPORTED_PERMISSION_NAMES == frozenset(
        {
            "read",
            "write",
            "update",
            "delete",
            "admin",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_PERMISSION_NAME_LENGTH == 4
    assert constants.MAX_PERMISSION_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.RESOURCE_KEY == "resource"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"