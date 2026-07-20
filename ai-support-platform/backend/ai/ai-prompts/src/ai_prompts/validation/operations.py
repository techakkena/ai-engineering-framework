from __future__ import annotations

"""Operations for prompt validation."""

from __future__ import annotations

from ai_prompts.variables import (
    extract_variables,
    is_valid_variable_name,
)

import re

from .constants import (
    MAX_TEMPLATE_LENGTH,
    MAX_VARIABLE_COUNT,
    MIN_TEMPLATE_LENGTH,
)


def validate_template(template: str) -> bool:
    """Validate a prompt template."""

    length = len(template)

    return MIN_TEMPLATE_LENGTH <= length <= MAX_TEMPLATE_LENGTH


def validate_variable_names(template: str) -> bool:
    """Validate all variable names in a template."""

    variables = extract_raw_variables(template)

    return all(is_valid_variable_name(variable) for variable in variables)


def validate_variable_count(template: str) -> bool:
    """Validate variable count."""

    return len(extract_variables(template)) <= MAX_VARIABLE_COUNT


def validate_variables(
    variables: dict[str, object],
) -> bool:
    """Validate a variables dictionary."""

    return all(is_valid_variable_name(name) for name in variables)


def extract_raw_variables(template: str) -> list[str]:
    """Extract every placeholder, valid or invalid."""

    return re.findall(
        r"\{\{\s*(.*?)\s*\}\}",
        template,
    )


__all__ = [
    "validate_template",
    "validate_variable_names",
    "validate_variable_count",
    "validate_variables",
]
