from __future__ import annotations

import pytest

from ai_utils.datetime_utils.exceptions import (
    DateTimeFormatError,
    DateTimeParseError,
    DateTimeUtilsError,
)


def test_base_exception() -> None:
    assert issubclass(DateTimeUtilsError, Exception)


def test_parse_exception() -> None:
    assert issubclass(DateTimeParseError, DateTimeUtilsError)


def test_format_exception() -> None:
    assert issubclass(DateTimeFormatError, DateTimeUtilsError)


@pytest.mark.parametrize(
    "exception_class",
    [
        DateTimeUtilsError,
        DateTimeParseError,
        DateTimeFormatError,
    ],
)
def test_exception_can_be_raised(
    exception_class: type[Exception],
) -> None:
    with pytest.raises(exception_class):
        raise exception_class("Test")
