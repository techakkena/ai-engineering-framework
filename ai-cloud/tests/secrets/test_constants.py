"""Tests for ai_cloud.secrets.constants."""

from __future__ import annotations

from ai_cloud.secrets import constants


def test_default_values() -> None:
    assert constants.DEFAULT_SECRET_NAME == "secret"
    assert constants.DEFAULT_SECRET_TYPE == "api_key"
    assert constants.DEFAULT_ENABLED is True


def test_supported_secret_types() -> None:
    assert constants.SUPPORTED_SECRET_TYPES == frozenset(
        {
            "api_key",
            "token",
            "password",
            "certificate",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_SECRET_NAME_LENGTH == 1
    assert constants.MAX_SECRET_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.TYPE_KEY == "type"
    assert constants.VALUE_KEY == "value"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"