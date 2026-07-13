"""Tests for base operations."""

from ai_prompts.base.operations import (
    is_supported_prompt_format,
    is_valid_prompt_name,
)


def test_valid_prompt_name() -> None:
    assert is_valid_prompt_name("system")


def test_invalid_prompt_name() -> None:
    assert not is_valid_prompt_name("")
    assert not is_valid_prompt_name("   ")


def test_supported_prompt_format() -> None:
    assert is_supported_prompt_format("text")
    assert is_supported_prompt_format("chat")


def test_unsupported_prompt_format() -> None:
    assert not is_supported_prompt_format("xml")
