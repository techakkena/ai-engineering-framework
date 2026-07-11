"""
Unit tests for environment operations.
"""

from __future__ import annotations

import os

import pytest

from ai_utils.env_utils.exceptions import (
    EnvironmentVariableError,
)
from ai_utils.env_utils.operations import (
    get_env,
    get_required_env,
    has_env,
    remove_env,
    set_env,
)


def test_set_and_get_env() -> None:
    key = "AI_UTILS_TEST"

    set_env(key, "value")

    assert get_env(key) == "value"

    remove_env(key)


def test_has_env() -> None:
    key = "AI_UTILS_EXISTS"

    set_env(key, "exists")

    assert has_env(key) is True

    remove_env(key)


def test_remove_env() -> None:
    key = "AI_UTILS_REMOVE"

    set_env(key, "remove")

    remove_env(key)

    assert has_env(key) is False


def test_get_env_default() -> None:
    assert get_env("UNKNOWN_KEY", "default") == "default"


def test_get_required_env() -> None:
    key = "AI_UTILS_REQUIRED"

    set_env(key, "required")

    assert get_required_env(key) == "required"

    remove_env(key)


def test_missing_required_env() -> None:
    key = "AI_UTILS_MISSING"

    os.environ.pop(key, None)

    with pytest.raises(EnvironmentVariableError):
        get_required_env(key)
