"""Tests for ai_cloud.networking.constants."""

from __future__ import annotations

from ai_cloud.networking import constants


def test_default_values() -> None:
    assert constants.DEFAULT_NETWORK_NAME == "network"
    assert constants.DEFAULT_NETWORK_TYPE == "private"
    assert constants.DEFAULT_ENABLED is True


def test_supported_network_types() -> None:
    assert constants.SUPPORTED_NETWORK_TYPES == frozenset(
        {
            "private",
            "public",
            "hybrid",
            "vpc",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_NETWORK_NAME_LENGTH == 1
    assert constants.MAX_NETWORK_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.TYPE_KEY == "type"
    assert constants.CIDR_KEY == "cidr"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"