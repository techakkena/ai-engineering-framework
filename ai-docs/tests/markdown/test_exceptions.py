"""Tests for ai_docs.markdown.exceptions."""

from __future__ import annotations

import pytest

from ai_docs.markdown.exceptions import (
    DuplicateMarkdownError,
    MarkdownError,
    MarkdownNotFoundError,
    MarkdownRegistrationError,
    MarkdownValidationError,
    UnsupportedMarkdownFormatError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        MarkdownValidationError,
        MarkdownError,
    )
    assert issubclass(
        MarkdownRegistrationError,
        MarkdownError,
    )
    assert issubclass(
        MarkdownNotFoundError,
        MarkdownRegistrationError,
    )
    assert issubclass(
        DuplicateMarkdownError,
        MarkdownRegistrationError,
    )
    assert issubclass(
        UnsupportedMarkdownFormatError,
        MarkdownValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (MarkdownError, "base"),
        (MarkdownValidationError, "validation"),
        (MarkdownRegistrationError, "registration"),
        (MarkdownNotFoundError, "missing"),
        (DuplicateMarkdownError, "duplicate"),
        (UnsupportedMarkdownFormatError, "format"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(
        exception_class,
        match=message,
    ):
        raise exception_class(message)