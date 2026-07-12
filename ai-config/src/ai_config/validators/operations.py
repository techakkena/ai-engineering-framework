"""
Validation operations.

Author: TECHAKKENA
"""

from __future__ import annotations

import re
from typing import Any

from ai_config.validators.exceptions import (
    ChoiceValidationError,
    LengthValidationError,
    RangeValidationError,
    RegexValidationError,
    RequiredFieldError,
    TypeValidationError,
)


class Validator:
    """
    Generic validation helper.
    """

    def required(
        self,
        value: Any,
        name: str = "value",
    ) -> None:
        """
        Validate that a value exists.
        """
        if value is None:
            raise RequiredFieldError(f"{name} is required.")

    def type(
        self,
        value: Any,
        expected: type,
        name: str = "value",
    ) -> None:
        """
        Validate value type.
        """
        if not isinstance(value, expected):
            raise TypeValidationError(f"{name} must be of type {expected.__name__}.")

    def range(
        self,
        value: int | float,
        minimum: int | float,
        maximum: int | float,
        name: str = "value",
    ) -> None:
        """
        Validate numeric range.
        """
        if not minimum <= value <= maximum:
            raise RangeValidationError(
                f"{name} must be between {minimum} and {maximum}."
            )

    def length(
        self,
        value: str,
        minimum: int,
        maximum: int,
        name: str = "value",
    ) -> None:
        """
        Validate string length.
        """
        size = len(value)

        if not minimum <= size <= maximum:
            raise LengthValidationError(
                f"{name} length must be between {minimum} and {maximum}."
            )

    def choice(
        self,
        value: Any,
        choices: list[Any] | tuple[Any, ...],
        name: str = "value",
    ) -> None:
        """
        Validate allowed choices.
        """
        if value not in choices:
            raise ChoiceValidationError(f"{name} must be one of {choices}.")

    def regex(
        self,
        value: str,
        pattern: str,
        name: str = "value",
    ) -> None:
        """
        Validate regular expression.
        """
        if re.fullmatch(pattern, value) is None:
            raise RegexValidationError(f"{name} does not match '{pattern}'.")
