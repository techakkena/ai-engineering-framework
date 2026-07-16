"""Tests for ai_testing.pytest.constants."""

from __future__ import annotations

from ai_testing.pytest import constants


def test_default_values() -> None:
    assert constants.DEFAULT_TEST_PATH == "tests"
    assert constants.DEFAULT_VERBOSE is False
    assert constants.DEFAULT_FAIL_FAST is False


def test_configuration_name_limits() -> None:
    assert constants.MIN_CONFIGURATION_NAME_LENGTH == 1
    assert constants.MAX_CONFIGURATION_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.TEST_PATH_KEY == "test_path"
    assert constants.VERBOSE_KEY == "verbose"
    assert constants.FAIL_FAST_KEY == "fail_fast"