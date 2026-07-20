from __future__ import annotations

from ai_prompts.validation.operations import (
    validate_template,
    validate_variable_count,
    validate_variable_names,
    validate_variables,
)


def test_validate_template():
    assert validate_template("Hello {{name}}")


def test_empty_template():
    assert not validate_template("")


def test_validate_variable_names():
    assert validate_variable_names("Hello {{name}}")


def test_invalid_variable_names():
    assert not validate_variable_names("Hello {{123name}}")


def test_validate_variable_count():
    assert validate_variable_count("{{a}} {{b}} {{c}}")


def test_validate_variables():
    assert validate_variables(
        {
            "name": "John",
            "age": 25,
        }
    )


def test_invalid_variables():
    assert not validate_variables(
        {
            "123name": "John",
        }
    )
