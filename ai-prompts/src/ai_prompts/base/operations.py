"""Operations for the base prompt module."""

from .constants import SUPPORTED_PROMPT_FORMATS


def is_valid_prompt_name(name: str) -> bool:
    """Return True if the prompt name is valid."""
    return isinstance(name, str) and bool(name.strip())


def is_supported_prompt_format(prompt_format: str) -> bool:
    """Return True if the prompt format is supported."""
    return prompt_format in SUPPORTED_PROMPT_FORMATS
