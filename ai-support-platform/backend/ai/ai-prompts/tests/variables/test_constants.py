from __future__ import annotations

from ai_prompts.variables.constants import (
    MAX_VARIABLE_NAME_LENGTH,
    RESERVED_VARIABLES,
    VARIABLE_PATTERN,
)


def test_variable_pattern():
    assert VARIABLE_PATTERN == r"\{\{\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*\}\}"


def test_max_variable_length():
    assert MAX_VARIABLE_NAME_LENGTH == 64


def test_reserved_variables():
    assert "system" in RESERVED_VARIABLES
