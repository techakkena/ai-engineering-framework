"""Tests for ai_docs.generators.exceptions."""

from __future__ import annotations

import pytest

from ai_docs.generators.exceptions import (
    DuplicateGeneratorError,
    GeneratorError,
    GeneratorNotFoundError,
    GeneratorRegistrationError,
    GeneratorValidationError,
    UnsupportedGeneratorTypeError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        GeneratorValidationError,
        GeneratorError,
    )
    assert issubclass(
        GeneratorRegistrationError,
        GeneratorError,
    )
    assert issubclass(
        GeneratorNotFoundError,
        GeneratorRegistrationError,
    )
    assert issubclass(
        DuplicateGeneratorError,
        GeneratorRegistrationError,
    )
    assert issubclass(
        UnsupportedGeneratorTypeError,
        GeneratorValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (GeneratorError, "base"),
        (GeneratorValidationError, "validation"),
        (GeneratorRegistrationError, "registration"),
        (GeneratorNotFoundError, "missing"),
        (DuplicateGeneratorError, "duplicate"),
        (UnsupportedGeneratorTypeError, "type"),
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