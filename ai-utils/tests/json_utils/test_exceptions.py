"""
Unit tests for JSON exceptions.
"""

from __future__ import annotations

import pytest

from ai_utils.json_utils.exceptions import (
    JsonDecodeError,
    JsonReadError,
    JsonUtilsError,
    JsonWriteError,
)


def test_json_utils_error_is_exception() -> None:
    assert issubclass(JsonUtilsError, Exception)


def test_json_read_error_inherits_base() -> None:
    assert issubclass(JsonReadError, JsonUtilsError)


def test_json_write_error_inherits_base() -> None:
    assert issubclass(JsonWriteError, JsonUtilsError)


def test_json_decode_error_inherits_base() -> None:
    assert issubclass(JsonDecodeError, JsonUtilsError)


@pytest.mark.parametrize(
    "exception_class",
    [
        JsonUtilsError,
        JsonReadError,
        JsonWriteError,
        JsonDecodeError,
    ],
)
def test_exception_can_be_raised(
    exception_class: type[Exception],
) -> None:
    with pytest.raises(exception_class):
        raise exception_class("Test")
