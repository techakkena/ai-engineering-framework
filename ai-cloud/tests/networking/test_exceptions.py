"""Tests for ai_cloud.networking.exceptions."""

from __future__ import annotations

import pytest

from ai_cloud.networking.exceptions import (
    DuplicateNetworkError,
    NetworkError,
    NetworkNotFoundError,
    NetworkRegistrationError,
    NetworkValidationError,
    UnsupportedNetworkTypeError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        NetworkValidationError,
        NetworkError,
    )
    assert issubclass(
        NetworkRegistrationError,
        NetworkError,
    )
    assert issubclass(
        NetworkNotFoundError,
        NetworkRegistrationError,
    )
    assert issubclass(
        DuplicateNetworkError,
        NetworkRegistrationError,
    )
    assert issubclass(
        UnsupportedNetworkTypeError,
        NetworkValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (NetworkError, "base"),
        (NetworkValidationError, "validation"),
        (NetworkRegistrationError, "registration"),
        (NetworkNotFoundError, "missing"),
        (DuplicateNetworkError, "duplicate"),
        (UnsupportedNetworkTypeError, "network"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)