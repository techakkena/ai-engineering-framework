"""Tests for ai_testing.pytest.operations."""

from __future__ import annotations

import pytest

from ai_testing.pytest.constants import (
    DEFAULT_FAIL_FAST,
    DEFAULT_TEST_PATH,
    DEFAULT_VERBOSE,
)
from ai_testing.pytest.exceptions import PytestValidationError
from ai_testing.pytest.operations import (
    PytestConfiguration,
    PytestRunner,
    build_configuration,
)


def test_configuration_defaults() -> None:
    configuration = PytestConfiguration(name="default")

    assert configuration.name == "default"
    assert configuration.test_path == DEFAULT_TEST_PATH
    assert configuration.verbose is DEFAULT_VERBOSE
    assert configuration.fail_fast is DEFAULT_FAIL_FAST


def test_configuration_trims_values() -> None:
    configuration = PytestConfiguration(
        name="  integration  ",
        test_path="  tests/integration  ",
    )

    assert configuration.name == "integration"
    assert configuration.test_path == "tests/integration"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_configuration_name(name: str) -> None:
    with pytest.raises(PytestValidationError):
        PytestConfiguration(name=name)


@pytest.mark.parametrize(
    "path",
    [
        "",
        "   ",
    ],
)
def test_invalid_test_path(path: str) -> None:
    with pytest.raises(PytestValidationError):
        PytestConfiguration(
            name="config",
            test_path=path,
        )


def test_build_configuration() -> None:
    configuration = build_configuration(
        name="integration",
        test_path="tests/integration",
        verbose=True,
        fail_fast=True,
    )

    assert configuration.name == "integration"
    assert configuration.test_path == "tests/integration"
    assert configuration.verbose is True
    assert configuration.fail_fast is True


def test_build_configuration_defaults() -> None:
    configuration = build_configuration(name="default")

    assert configuration.test_path == DEFAULT_TEST_PATH
    assert configuration.verbose is DEFAULT_VERBOSE
    assert configuration.fail_fast is DEFAULT_FAIL_FAST


def test_runner_default_command() -> None:
    runner = PytestRunner()

    configuration = build_configuration(name="default")

    assert runner.build_command(configuration) == (
        "pytest",
        "tests",
    )


def test_runner_verbose_command() -> None:
    runner = PytestRunner()

    configuration = build_configuration(
        name="verbose",
        verbose=True,
    )

    assert runner.build_command(configuration) == (
        "pytest",
        "tests",
        "-v",
    )


def test_runner_fail_fast_command() -> None:
    runner = PytestRunner()

    configuration = build_configuration(
        name="fail-fast",
        fail_fast=True,
    )

    assert runner.build_command(configuration) == (
        "pytest",
        "tests",
        "-x",
    )


def test_runner_full_command() -> None:
    runner = PytestRunner()

    configuration = build_configuration(
        name="full",
        test_path="tests/unit",
        verbose=True,
        fail_fast=True,
    )

    assert runner.build_command(configuration) == (
        "pytest",
        "tests/unit",
        "-v",
        "-x",
    )