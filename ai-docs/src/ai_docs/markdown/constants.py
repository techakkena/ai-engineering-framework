"""Constants for the ai_docs.markdown module."""

from __future__ import annotations

from typing import Final

DEFAULT_MARKDOWN_NAME: Final[str] = "document"
DEFAULT_MARKDOWN_FORMAT: Final[str] = "github"
DEFAULT_ENABLED: Final[bool] = True

GITHUB_FORMAT: Final[str] = "github"
COMMONMARK_FORMAT: Final[str] = "commonmark"
GITLAB_FORMAT: Final[str] = "gitlab"
MARKDOWN_EXTRA_FORMAT: Final[str] = "markdown_extra"

SUPPORTED_MARKDOWN_FORMATS: Final[frozenset[str]] = frozenset(
    {
        GITHUB_FORMAT,
        COMMONMARK_FORMAT,
        GITLAB_FORMAT,
        MARKDOWN_EXTRA_FORMAT,
    }
)

MIN_MARKDOWN_NAME_LENGTH: Final[int] = 3
MAX_MARKDOWN_NAME_LENGTH: Final[int] = 255

NAME_KEY: Final[str] = "name"
FORMAT_KEY: Final[str] = "format"
CONTENT_KEY: Final[str] = "content"
ENABLED_KEY: Final[str] = "enabled"

__all__ = [
    "COMMONMARK_FORMAT",
    "CONTENT_KEY",
    "DEFAULT_ENABLED",
    "DEFAULT_MARKDOWN_FORMAT",
    "DEFAULT_MARKDOWN_NAME",
    "FORMAT_KEY",
    "GITHUB_FORMAT",
    "GITLAB_FORMAT",
    "MARKDOWN_EXTRA_FORMAT",
    "MAX_MARKDOWN_NAME_LENGTH",
    "MIN_MARKDOWN_NAME_LENGTH",
    "NAME_KEY",
    "SUPPORTED_MARKDOWN_FORMATS",
    "ENABLED_KEY",
]