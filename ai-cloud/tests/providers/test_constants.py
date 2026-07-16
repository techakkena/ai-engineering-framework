"""Tests for ai_cloud.providers.constants."""

from __future__ import annotations

from ai_cloud.providers import constants


def test_default_values() -> None:
    assert constants.DEFAULT_PROVIDER_NAME == "provider"
    assert constants.DEFAULT_PROVIDER_TYPE == "aws"
    assert constants.DEFAULT_ENABLED is True


def test_supported_provider_types() -> None:
    assert constants.SUPPORTED_PROVIDER_TYPES == frozenset(
        {
            "aws",
            "azure",
            "gcp",
            "oci",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_PROVIDER_NAME_LENGTH == 1
    assert constants.MAX_PROVIDER_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.TYPE_KEY == "type"
    assert constants.REGION_KEY == "region"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"