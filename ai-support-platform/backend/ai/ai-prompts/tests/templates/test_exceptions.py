from __future__ import annotations

from ai_prompts.templates.exceptions import (
    InvalidTemplateError,
    TemplateError,
    TemplateNotFoundError,
)


def test_template_error():
    assert issubclass(TemplateError, Exception)


def test_invalid_template_error():
    assert issubclass(
        InvalidTemplateError,
        TemplateError,
    )


def test_template_not_found_error():
    assert issubclass(
        TemplateNotFoundError,
        TemplateError,
    )
