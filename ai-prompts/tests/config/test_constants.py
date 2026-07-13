from ai_prompts.config.constants import (
    DEFAULT_PROMPT_DIRECTORY,
    DEFAULT_PROMPT_EXTENSION,
    DEFAULT_TEMPLATE_ENCODING,
)


def test_default_prompt_directory():
    assert DEFAULT_PROMPT_DIRECTORY == "prompts"


def test_default_prompt_extension():
    assert DEFAULT_PROMPT_EXTENSION == ".txt"


def test_default_template_encoding():
    assert DEFAULT_TEMPLATE_ENCODING == "utf-8"
