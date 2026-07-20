from __future__ import annotations

from ai_prompts.validation.exceptions import (
    InvalidTemplateError,
    InvalidVariablesError,
    ValidationError,
)


def test_validation_error():
    assert issubclass(
        ValidationError,
        Exception,
    )


def test_invalid_template_error():
    assert issubclass(
        InvalidTemplateError,
        ValidationError,
    )


def test_invalid_variables_error():
    assert issubclass(
        InvalidVariablesError,
        ValidationError,
    )
