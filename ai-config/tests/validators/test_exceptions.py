"""
Unit tests for validators exceptions.

Author: TECHAKKENA
"""

from ai_config.validators.exceptions import (
    ChoiceValidationError,
    LengthValidationError,
    RangeValidationError,
    RegexValidationError,
    RequiredFieldError,
    TypeValidationError,
    ValidationError,
)


def test_validation_error() -> None:
    exception = ValidationError("error")

    assert isinstance(exception, Exception)


def test_required_field_error() -> None:
    exception = RequiredFieldError("missing")

    assert isinstance(exception, ValidationError)


def test_type_validation_error() -> None:
    exception = TypeValidationError("type")

    assert isinstance(exception, ValidationError)


def test_range_validation_error() -> None:
    exception = RangeValidationError("range")

    assert isinstance(exception, ValidationError)


def test_length_validation_error() -> None:
    exception = LengthValidationError("length")

    assert isinstance(exception, ValidationError)


def test_choice_validation_error() -> None:
    exception = ChoiceValidationError("choice")

    assert isinstance(exception, ValidationError)


def test_regex_validation_error() -> None:
    exception = RegexValidationError("regex")

    assert isinstance(exception, ValidationError)
