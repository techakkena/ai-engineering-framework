"""Tests for ai_optimization.compression.exceptions."""

from __future__ import annotations

import pytest

from ai_optimization.compression.exceptions import (
    CompressionError,
    CompressionNotFoundError,
    CompressionRegistrationError,
    CompressionValidationError,
    DuplicateCompressionError,
    UnsupportedCompressionTypeError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        CompressionValidationError,
        CompressionError,
    )
    assert issubclass(
        CompressionRegistrationError,
        CompressionError,
    )
    assert issubclass(
        CompressionNotFoundError,
        CompressionRegistrationError,
    )
    assert issubclass(
        DuplicateCompressionError,
        CompressionRegistrationError,
    )
    assert issubclass(
        UnsupportedCompressionTypeError,
        CompressionValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (CompressionError, "base"),
        (CompressionValidationError, "validation"),
        (CompressionRegistrationError, "registration"),
        (CompressionNotFoundError, "missing"),
        (DuplicateCompressionError, "duplicate"),
        (UnsupportedCompressionTypeError, "type"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)