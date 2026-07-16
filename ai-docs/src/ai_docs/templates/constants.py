"""Constants for the ai_docs.templates module."""

from __future__ import annotations

from typing import Final

DEFAULT_TEMPLATE_NAME: Final[str] = "template"
DEFAULT_TEMPLATE_TYPE: Final[str] = "markdown"
DEFAULT_ENABLED: Final[bool] = True

MARKDOWN_TEMPLATE: Final[str] = "markdown"
HTML_TEMPLATE: Final[str] = "html"
EMAIL_TEMPLATE: Final[str] = "email"
PROMPT_TEMPLATE: Final[str] = "prompt"

SUPPORTED_TEMPLATE_TYPES: Final[frozenset[str]] = frozenset(
    {
        MARKDOWN_TEMPLATE,
        HTML_TEMPLATE,
        EMAIL_TEMPLATE,
        PROMPT_TEMPLATE,
    }
)

MIN_TEMPLATE_NAME_LENGTH: Final[int] = 3
MAX_TEMPLATE_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
TYPE_KEY: Final[str] = "type"
CONTENT_KEY: Final[str] = "content"
DESCRIPTION_KEY: Final[str] = "description"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "CONTENT_KEY",
    "DEFAULT_ENABLED",
    "DEFAULT_TEMPLATE_NAME",
    "DEFAULT_TEMPLATE_TYPE",
    "DESCRIPTION_KEY",
    "EMAIL_TEMPLATE",
    "ENABLED_KEY",
    "HTML_TEMPLATE",
    "MARKDOWN_TEMPLATE",
    "MAX_TEMPLATE_NAME_LENGTH",
    "MIN_TEMPLATE_NAME_LENGTH",
    "NAME_KEY",
    "PROMPT_TEMPLATE",
    "SUPPORTED_TEMPLATE_TYPES",
    "TYPE_KEY",
]