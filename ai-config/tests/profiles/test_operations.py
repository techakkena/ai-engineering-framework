"""
Unit tests for profile operations.
"""

import pytest

from ai_config.profiles.constants import DEFAULT_PROFILE
from ai_config.profiles.exceptions import (
    DuplicateProfileError,
    ProfileNotFoundError,
)
from ai_config.profiles.operations import ProfileManager


def test_default_profile_exists() -> None:
    manager = ProfileManager()

    assert manager.exists(DEFAULT_PROFILE)


def test_add_profile() -> None:
    manager = ProfileManager()

    manager.add("development")

    assert manager.exists("development")


def test_duplicate_profile() -> None:
    manager = ProfileManager()

    with pytest.raises(DuplicateProfileError):
        manager.add(DEFAULT_PROFILE)


def test_get_profile() -> None:
    manager = ProfileManager()

    manager.add("development", {"debug": True})

    assert manager.get("development") == {"debug": True}


def test_missing_profile() -> None:
    manager = ProfileManager()

    with pytest.raises(ProfileNotFoundError):
        manager.get("missing")


def test_remove_profile() -> None:
    manager = ProfileManager()

    manager.add("development")
    manager.remove("development")

    assert not manager.exists("development")


def test_activate_profile() -> None:
    manager = ProfileManager()

    manager.add("development")
    manager.activate("development")

    assert manager.active_profile() == "development"


def test_list_profiles() -> None:
    manager = ProfileManager()

    manager.add("development")

    assert "development" in manager.list()


def test_clear_profiles() -> None:
    manager = ProfileManager()

    manager.add("development")
    manager.clear()

    assert manager.list() == [DEFAULT_PROFILE]


def test_to_dict() -> None:
    manager = ProfileManager()

    data = manager.to_dict()

    assert isinstance(data, dict)
