from __future__ import annotations

from ai_prompts.rendering.operations import (
    count_variables,
    has_unresolved_variables,
    render_prompt,
)


def test_render_prompt():
    result = render_prompt(
        "Hello {{name}}",
        {"name": "John"},
    )

    assert result == "Hello John"


def test_render_multiple_variables():
    result = render_prompt(
        "{{greeting}} {{name}}",
        {
            "greeting": "Hello",
            "name": "John",
        },
    )

    assert result == "Hello John"


def test_missing_variable():
    result = render_prompt(
        "Hello {{name}}",
        {},
    )

    assert result == "Hello "


def test_count_variables():
    assert count_variables("{{a}} {{b}} {{c}}") == 3


def test_has_unresolved_variables():
    assert has_unresolved_variables("{{name}}")


def test_no_variables():
    assert not has_unresolved_variables("Hello World")
