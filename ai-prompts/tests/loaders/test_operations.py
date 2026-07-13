from pathlib import Path

from ai_prompts.loaders.operations import (
    is_supported_prompt_file,
    load_prompt,
    load_prompt_from_string,
)


def test_load_prompt_from_string():
    assert load_prompt_from_string("Hello") == "Hello"


def test_supported_prompt_file():
    assert is_supported_prompt_file("chat.prompt")


def test_unsupported_prompt_file():
    assert not is_supported_prompt_file("chat.pdf")


def test_load_prompt(tmp_path: Path):
    file = tmp_path / "prompt.txt"

    file.write_text(
        "Hello AI",
        encoding="utf-8",
    )

    assert load_prompt(file) == "Hello AI"
