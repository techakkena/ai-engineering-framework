"""Tests for base constants."""

from ai_prompts.base.constants import (
    DEFAULT_PROMPT_NAME,
    DEFAULT_PROMPT_VERSION,
    SUPPORTED_PROMPT_FORMATS,
)


def test_default_prompt_name() -> None:
    assert DEFAULT_PROMPT_NAME == "default"


def test_default_prompt_version() -> None:
    assert DEFAULT_PROMPT_VERSION == "1.0"


def test_supported_prompt_formats() -> None:
    assert "text" in SUPPORTED_PROMPT_FORMATS
    assert "chat" in SUPPORTED_PROMPT_FORMATS
