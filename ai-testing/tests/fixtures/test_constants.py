"""Tests for ai_testing.fixtures.constants."""

from __future__ import annotations

from ai_testing.fixtures import constants


def test_default_fixture_name() -> None:
    assert constants.DEFAULT_FIXTURE_NAME == "fixture"


def test_default_fixture_scope() -> None:
    assert constants.DEFAULT_FIXTURE_SCOPE == "function"


def test_supported_fixture_scopes() -> None:
    assert constants.SUPPORTED_FIXTURE_SCOPES == frozenset(
        {
            "function",
            "class",
            "module",
            "package",
            "session",
        }
    )


def test_default_autouse() -> None:
    assert constants.DEFAULT_AUTOUSE is False


def test_default_cache_enabled() -> None:
    assert constants.DEFAULT_CACHE_ENABLED is True


def test_fixture_name_length_limits() -> None:
    assert constants.MIN_FIXTURE_NAME_LENGTH == 1
    assert constants.MAX_FIXTURE_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.SCOPE_KEY == "scope"
    assert constants.AUTOUSE_KEY == "autouse"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.TAGS_KEY == "tags"
    assert constants.CACHE_KEY == "cache"