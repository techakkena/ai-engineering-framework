"""Tests for ai_optimization.caching.constants."""

from __future__ import annotations

from ai_optimization.caching import constants


def test_default_values() -> None:
    assert constants.DEFAULT_CACHE_NAME == "cache"
    assert constants.DEFAULT_CACHE_BACKEND == "memory"
    assert constants.DEFAULT_ENABLED is True


def test_supported_cache_backends() -> None:
    assert constants.SUPPORTED_CACHE_BACKENDS == frozenset(
        {
            "memory",
            "redis",
            "disk",
            "hybrid",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_CACHE_NAME_LENGTH == 1
    assert constants.MAX_CACHE_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.BACKEND_KEY == "backend"
    assert constants.CAPACITY_KEY == "capacity"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"