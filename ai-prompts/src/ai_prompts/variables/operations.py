"""Operations for prompt variables."""

from __future__ import annotations

import re

from .constants import (
    MAX_VARIABLE_NAME_LENGTH,
    RESERVED_VARIABLES,
    VARIABLE_PATTERN,
)


def extract_variables(template: str) -> list[str]:
    """Extract variables from a template."""

    return re.findall(VARIABLE_PATTERN, template)


def is_valid_variable_name(name: str) -> bool:
    """Validate a variable name."""

    if not name:
        return False

    if len(name) > MAX_VARIABLE_NAME_LENGTH:
        return False

    if name in RESERVED_VARIABLES:
        return False

    return bool(re.fullmatch(r"[a-zA-Z_][a-zA-Z0-9_]*", name))


def has_duplicate_variables(template: str) -> bool:
    """Check for duplicate variables."""

    variables = extract_variables(template)
    return len(variables) != len(set(variables))


__all__ = [
    "extract_variables",
    "is_valid_variable_name",
    "has_duplicate_variables",
]
