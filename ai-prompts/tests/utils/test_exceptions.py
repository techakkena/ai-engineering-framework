from ai_prompts.utils.exceptions import (
    EmptyTextError,
    InvalidTextError,
    UtilityError,
)


def test_utility_error():
    assert issubclass(
        UtilityError,
        Exception,
    )


def test_invalid_text_error():
    assert issubclass(
        InvalidTextError,
        UtilityError,
    )


def test_empty_text_error():
    assert issubclass(
        EmptyTextError,
        UtilityError,
    )
