"""
Unit tests for environment exceptions.
"""

from __future__ import annotations

import pytest

from ai_utils.env_utils.exceptions import (
    EnvironmentVariableError,
    EnvUtilsError,
)


def test_base_exception() -> None:
    assert issubclass(EnvUtilsError, Exception)


def test_environment_variable_error() -> None:
    assert issubclass(EnvironmentVariableError, EnvUtilsError)


@pytest.mark.parametrize(
    "exception_class",
    [
        EnvUtilsError,
        EnvironmentVariableError,
    ],
)
def test_exception_can_be_raised(
    exception_class: type[Exception],
) -> None:
    with pytest.raises(exception_class):
        raise exception_class("Test")
