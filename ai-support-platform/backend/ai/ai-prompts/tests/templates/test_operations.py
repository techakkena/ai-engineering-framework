from __future__ import annotations

from ai_prompts.templates.operations import (
    get_template_name,
    get_template_variables,
    is_supported_template,
    validate_template,
)


def test_supported_template():
    assert is_supported_template("prompt.md")


def test_unsupported_template():
    assert not is_supported_template("prompt.pdf")


def test_get_template_name():
    assert get_template_name("chat.prompt") == "chat"


def test_template_variables():
    variables = get_template_variables("Hello {{name}}, welcome to {{company}}.")

    assert variables == ["name", "company"]


def test_validate_template():
    assert validate_template("Hello {{name}}")


def test_empty_template():
    assert not validate_template("   ")
