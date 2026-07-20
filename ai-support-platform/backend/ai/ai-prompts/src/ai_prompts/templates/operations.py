from __future__ import annotations

"""Operations for prompt templates."""

from __future__ import annotations

from ai_prompts.variables import extract_variables

from .constants import SUPPORTED_TEMPLATE_EXTENSIONS


def is_supported_template(filename: str) -> bool:
    """Return True if the template extension is supported."""

    return any(
        filename.endswith(extension) for extension in SUPPORTED_TEMPLATE_EXTENSIONS
    )


def get_template_name(filename: str) -> str:
    """Return the template name without its extension."""

    return filename.rsplit(".", 1)[0]


def get_template_variables(template: str) -> list[str]:
    """Return variables contained in a template."""

    return extract_variables(template)


def validate_template(template: str) -> bool:
    """Validate a template."""

    return bool(template.strip())


__all__ = [
    "is_supported_template",
    "get_template_name",
    "get_template_variables",
    "validate_template",
]
