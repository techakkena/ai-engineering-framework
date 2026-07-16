"""Tests for ai_testing.assertions.constants."""

from __future__ import annotations

from ai_testing.assertions import constants


def test_default_assertion_name() -> None:
    assert constants.DEFAULT_ASSERTION_NAME == "assertion"


def test_default_strict() -> None:
    assert constants.DEFAULT_STRICT is True


def test_supported_statuses() -> None:
    assert constants.SUPPORTED_ASSERTION_STATUSES == frozenset(
        {
            constants.STATUS_PASSED,
            constants.STATUS_FAILED,
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_ASSERTION_NAME_LENGTH == 1
    assert constants.MAX_ASSERTION_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.STATUS_KEY == "status"
    assert constants.MESSAGE_KEY == "message"
    assert constants.EXPECTED_KEY == "expected"
    assert constants.ACTUAL_KEY == "actual"