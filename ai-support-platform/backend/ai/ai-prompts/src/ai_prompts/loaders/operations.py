from __future__ import annotations

"""Operations for prompt loaders."""

from __future__ import annotations

from pathlib import Path

from .constants import (
    DEFAULT_ENCODING,
    SUPPORTED_LOAD_EXTENSIONS,
)


def load_prompt(path: str | Path) -> str:
    """Load a prompt from disk."""

    return Path(path).read_text(
        encoding=DEFAULT_ENCODING,
    )


def load_prompt_from_string(prompt: str) -> str:
    """Return a prompt string."""

    return prompt


def is_supported_prompt_file(path: str | Path) -> bool:
    """Return True if the prompt file is supported."""

    return Path(path).suffix in SUPPORTED_LOAD_EXTENSIONS


__all__ = [
    "load_prompt",
    "load_prompt_from_string",
    "is_supported_prompt_file",
]
