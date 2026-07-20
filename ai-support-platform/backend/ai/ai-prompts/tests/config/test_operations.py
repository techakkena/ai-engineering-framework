from __future__ import annotations

from ai_prompts.config.constants import (
    DEFAULT_PROMPT_DIRECTORY,
)
from ai_prompts.config.operations import (
    get_all_config,
    get_config,
    reset_config,
    set_config,
)


def setup_function():
    reset_config()


def test_get_default_config():
    assert get_config("prompt_directory") == DEFAULT_PROMPT_DIRECTORY


def test_set_config():
    set_config(
        "prompt_directory",
        "templates",
    )

    assert get_config("prompt_directory") == "templates"


def test_reset_config():
    set_config(
        "prompt_directory",
        "templates",
    )

    reset_config()

    assert get_config("prompt_directory") == DEFAULT_PROMPT_DIRECTORY


def test_get_all_config():
    config = get_all_config()

    assert isinstance(
        config,
        dict,
    )

    assert "prompt_directory" in config
