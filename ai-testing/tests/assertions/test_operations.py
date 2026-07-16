"""Tests for ai_testing.assertions.operations."""

from __future__ import annotations

import pytest

from ai_testing.assertions.constants import (
    STATUS_FAILED,
    STATUS_PASSED,
)
from ai_testing.assertions.exceptions import AssertionValidationError
from ai_testing.assertions.operations import (
    AssertionRunner,
    assert_equal,
)


def test_assertion_runner_success() -> None:
    runner = AssertionRunner()

    result = runner.evaluate(
        name="equal",
        expected=1,
        actual=1,
    )

    assert result.name == "equal"
    assert result.passed is True
    assert result.status() == STATUS_PASSED
    assert result.expected == 1
    assert result.actual == 1
    assert result.message == ""


def test_assertion_runner_failure() -> None:
    runner = AssertionRunner()

    result = runner.evaluate(
        name="equal",
        expected=1,
        actual=2,
    )

    assert result.passed is False
    assert result.status() == STATUS_FAILED
    assert result.message == "Assertion failed."


def test_runner_trims_name() -> None:
    runner = AssertionRunner()

    result = runner.evaluate(
        name="  sample  ",
        expected=1,
        actual=1,
    )

    assert result.name == "sample"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_runner_invalid_name(name: str) -> None:
    runner = AssertionRunner()

    with pytest.raises(AssertionValidationError):
        runner.evaluate(
            name=name,
            expected=1,
            actual=1,
        )


def test_non_strict_comparison() -> None:
    result = assert_equal(
        name="compare",
        expected=1,
        actual="1",
        strict=False,
    )

    assert result.passed is True


def test_strict_comparison_failure() -> None:
    result = assert_equal(
        name="compare",
        expected=1,
        actual="1",
        strict=True,
    )

    assert result.passed is False


def test_assert_equal_success() -> None:
    result = assert_equal(
        name="numbers",
        expected=100,
        actual=100,
    )

    assert result.status() == STATUS_PASSED


def test_assert_equal_failure() -> None:
    result = assert_equal(
        name="numbers",
        expected=100,
        actual=101,
    )

    assert result.status() == STATUS_FAILED