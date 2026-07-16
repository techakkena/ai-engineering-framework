"""Tests for ai_enterprise.organizations.constants."""

from __future__ import annotations

from ai_enterprise.organizations import constants


def test_default_values() -> None:
    assert constants.DEFAULT_ORGANIZATION_NAME == "organization"
    assert constants.DEFAULT_ORGANIZATION_TYPE == "enterprise"
    assert constants.DEFAULT_ENABLED is True


def test_supported_organization_types() -> None:
    assert constants.SUPPORTED_ORGANIZATION_TYPES == frozenset(
        {
            "enterprise",
            "business",
            "startup",
            "government",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_ORGANIZATION_NAME_LENGTH == 1
    assert constants.MAX_ORGANIZATION_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.TYPE_KEY == "type"
    assert constants.DOMAIN_KEY == "domain"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"