"""Operations for prompt rendering."""

from __future__ import annotations

from ai_prompts.variables import extract_variables


def render_prompt(
    template: str,
    variables: dict[str, str],
) -> str:
    """Render a prompt template."""

    rendered = template

    for variable in extract_variables(template):
        placeholder = f"{{{{{variable}}}}}"

        rendered = rendered.replace(
            placeholder,
            str(variables.get(variable, "")),
        )

    return rendered


def has_unresolved_variables(template: str) -> bool:
    """Return True if unresolved variables exist."""

    return bool(extract_variables(template))


def count_variables(template: str) -> int:
    """Return number of variables."""

    return len(extract_variables(template))


__all__ = [
    "render_prompt",
    "has_unresolved_variables",
    "count_variables",
]
