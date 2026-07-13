from ai_prompts.loaders.exceptions import (
    LoaderError,
    PromptFileNotFoundError,
    UnsupportedPromptFormatError,
)


def test_loader_error():
    assert issubclass(LoaderError, Exception)


def test_prompt_file_not_found_error():
    assert issubclass(
        PromptFileNotFoundError,
        LoaderError,
    )


def test_unsupported_prompt_format_error():
    assert issubclass(
        UnsupportedPromptFormatError,
        LoaderError,
    )
