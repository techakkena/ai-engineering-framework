"""Tests for ai_enterprise.roles.constants."""

from __future__ import annotations

from ai_enterprise.roles import constants


def test_default_values() -> None:
    assert constants.DEFAULT_ROLE_NAME == "user"
    assert constants.DEFAULT_ENABLED is True


def test_supported_role_names() -> None:
    assert constants.SUPPORTED_ROLE_NAMES == frozenset(
        {
            "admin",
            "manager",
            "user",
            "viewer",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_ROLE_NAME_LENGTH == 3
    assert constants.MAX_ROLE_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.PERMISSIONS_KEY == "permissions"
    assert constants.ENABLED_KEY == "enabled"