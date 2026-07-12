"""
Tests for environment.exceptions.
"""

import pytest

from ai_config.environment.exceptions import (
    EnvironmentError,
    EnvironmentFileNotFoundError,
    EnvironmentValueError,
    EnvironmentVariableNotFoundError,
)


def test_environment_error() -> None:
    with pytest.raises(EnvironmentError):
        raise EnvironmentError("Environment error")


def test_environment_file_not_found_error() -> None:
    with pytest.raises(EnvironmentFileNotFoundError):
        raise EnvironmentFileNotFoundError("File not found")


def test_environment_variable_not_found_error() -> None:
    with pytest.raises(EnvironmentVariableNotFoundError):
        raise EnvironmentVariableNotFoundError("Variable missing")


def test_environment_value_error() -> None:
    with pytest.raises(EnvironmentValueError):
        raise EnvironmentValueError("Invalid value")
