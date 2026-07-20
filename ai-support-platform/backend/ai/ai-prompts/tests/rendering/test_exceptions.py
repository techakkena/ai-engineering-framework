from __future__ import annotations

from ai_prompts.rendering.exceptions import (
    InvalidTemplateSyntaxError,
    MissingVariableError,
    RenderingError,
)


def test_rendering_error():
    assert issubclass(RenderingError, Exception)


def test_missing_variable_error():
    assert issubclass(
        MissingVariableError,
        RenderingError,
    )


def test_invalid_template_syntax_error():
    assert issubclass(
        InvalidTemplateSyntaxError,
        RenderingError,
    )
