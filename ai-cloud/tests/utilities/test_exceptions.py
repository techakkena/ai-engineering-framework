"""Tests for ai_cloud.utilities.exceptions."""

from __future__ import annotations

import pytest

from ai_cloud.utilities.exceptions import (
    UtilityError,
    UtilityValidationError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(
        UtilityValidationError,
        UtilityError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (UtilityError, "base"),
        (UtilityValidationError, "validation"),
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