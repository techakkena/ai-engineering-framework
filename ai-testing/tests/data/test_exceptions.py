"""Tests for ai_testing.data.exceptions."""

from __future__ import annotations

import pytest

from ai_testing.data.exceptions import (
    DataError,
    DataNotFoundError,
    DataRegistrationError,
    DataValidationError,
    DuplicateDataError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(DataValidationError, DataError)
    assert issubclass(DataRegistrationError, DataError)
    assert issubclass(DataNotFoundError, DataRegistrationError)
    assert issubclass(DuplicateDataError, DataRegistrationError)


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (DataError, "base"),
        (DataValidationError, "validation"),
        (DataRegistrationError, "registration"),
        (DataNotFoundError, "missing"),
        (DuplicateDataError, "duplicate"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)