from __future__ import annotations

from ai_prompts.variables.operations import (
    extract_variables,
    has_duplicate_variables,
    is_valid_variable_name,
)


def test_extract_variables():
    variables = extract_variables("Hello {{name}}, welcome to {{company}}.")

    assert variables == ["name", "company"]


def test_valid_variable_name():
    assert is_valid_variable_name("username")


def test_invalid_variable_name():
    assert not is_valid_variable_name("123name")


def test_reserved_variable():
    assert not is_valid_variable_name("system")


def test_duplicate_variables():
    assert has_duplicate_variables("{{name}} {{name}}")


def test_unique_variables():
    assert not has_duplicate_variables("{{name}} {{age}}")
