from ai_prompts.variables.exceptions import (
    DuplicateVariableError,
    InvalidVariableError,
    VariableError,
)


def test_variable_error():
    assert issubclass(VariableError, Exception)


def test_invalid_variable_error():
    assert issubclass(InvalidVariableError, VariableError)


def test_duplicate_variable_error():
    assert issubclass(DuplicateVariableError, VariableError)
