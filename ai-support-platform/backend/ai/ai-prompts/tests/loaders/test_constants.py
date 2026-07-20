from __future__ import annotations

from ai_prompts.loaders.constants import (
    DEFAULT_ENCODING,
    SUPPORTED_LOAD_EXTENSIONS,
)


def test_default_encoding():
    assert DEFAULT_ENCODING == "utf-8"


def test_supported_extensions():
    assert ".txt" in SUPPORTED_LOAD_EXTENSIONS


def test_prompt_extension():
    assert ".prompt" in SUPPORTED_LOAD_EXTENSIONS
