"""
Tests for environment.operations.
"""

import os

from ai_config.environment.operations import EnvironmentLoader


def test_get_existing_variable() -> None:
    os.environ["TEST_KEY"] = "test-value"

    env = EnvironmentLoader()

    assert env.get("TEST_KEY") == "test-value"


def test_get_default_value() -> None:
    env = EnvironmentLoader()

    assert env.get("UNKNOWN_KEY", "default") == "default"


def test_exists_true() -> None:
    os.environ["EXISTS_KEY"] = "exists"

    env = EnvironmentLoader()

    assert env.exists("EXISTS_KEY") is True


def test_exists_false() -> None:
    env = EnvironmentLoader()

    assert env.exists("MISSING_KEY") is False


def test_require_existing_variable() -> None:
    os.environ["REQUIRED_KEY"] = "required"

    env = EnvironmentLoader()

    assert env.require("REQUIRED_KEY") == "required"


def test_all_returns_dictionary() -> None:
    env = EnvironmentLoader()

    result = env.all()

    assert isinstance(result, dict)
