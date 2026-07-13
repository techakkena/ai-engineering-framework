"""Tests for base exceptions."""

from ai_prompts.base.exceptions import (
    InvalidPromptError,
    PromptError,
    PromptNotFoundError,
)


def test_prompt_error() -> None:
    assert issubclass(PromptError, Exception)


def test_invalid_prompt_error() -> None:
    assert issubclass(InvalidPromptError, PromptError)


def test_prompt_not_found_error() -> None:
    assert issubclass(PromptNotFoundError, PromptError)
