"""Tests for ai_enterprise.tenants.constants."""

from __future__ import annotations

from ai_enterprise.tenants import constants


def test_default_values() -> None:
    assert constants.DEFAULT_TENANT_NAME == "tenant"
    assert constants.DEFAULT_TENANT_PLAN == "standard"
    assert constants.DEFAULT_ENABLED is True


def test_supported_tenant_plans() -> None:
    assert constants.SUPPORTED_TENANT_PLANS == frozenset(
        {
            "standard",
            "professional",
            "enterprise",
            "trial",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_TENANT_NAME_LENGTH == 1
    assert constants.MAX_TENANT_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.PLAN_KEY == "plan"
    assert constants.ORGANIZATION_KEY == "organization"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"