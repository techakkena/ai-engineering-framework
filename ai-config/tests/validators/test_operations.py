"""
Unit tests for validators operations.

Author: TECHAKKENA
"""

import pytest

from ai_config.validators.exceptions import (
    ChoiceValidationError,
    LengthValidationError,
    RangeValidationError,
    RegexValidationError,
    RequiredFieldError,
    TypeValidationError,
)
from ai_config.validators.operations import Validator


def test_required_success() -> None:
    validator = Validator()

    validator.required("value")


def test_required_failure() -> None:
    validator = Validator()

    with pytest.raises(RequiredFieldError):
        validator.required(None)


def test_type_success() -> None:
    validator = Validator()

    validator.type(10, int)


def test_type_failure() -> None:
    validator = Validator()

    with pytest.raises(TypeValidationError):
        validator.type("10", int)


def test_range_success() -> None:
    validator = Validator()

    validator.range(5, 1, 10)


def test_range_failure() -> None:
    validator = Validator()

    with pytest.raises(RangeValidationError):
        validator.range(20, 1, 10)


def test_length_success() -> None:
    validator = Validator()

    validator.length("hello", 1, 10)


def test_length_failure() -> None:
    validator = Validator()

    with pytest.raises(LengthValidationError):
        validator.length("hello world", 1, 5)


def test_choice_success() -> None:
    validator = Validator()

    validator.choice("dev", ["dev", "test", "prod"])


def test_choice_failure() -> None:
    validator = Validator()

    with pytest.raises(ChoiceValidationError):
        validator.choice("local", ["dev", "test", "prod"])


def test_regex_success() -> None:
    validator = Validator()

    validator.regex("abc123", r"^[a-z0-9]+$")


def test_regex_failure() -> None:
    validator = Validator()

    with pytest.raises(RegexValidationError):
        validator.regex("ABC!", r"^[a-z0-9]+$")
