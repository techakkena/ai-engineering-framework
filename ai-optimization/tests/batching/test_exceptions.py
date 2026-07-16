"""Tests for ai_optimization.batching.exceptions."""

from __future__ import annotations

import pytest

from ai_optimization.batching.exceptions import (
    BatchError,
    BatchNotFoundError,
    BatchRegistrationError,
    BatchValidationError,
    DuplicateBatchError,
    UnsupportedBatchStrategyError,
)


def test_exception_hierarchy() -> None:
    assert issubclass(BatchValidationError, BatchError)
    assert issubclass(BatchRegistrationError, BatchError)
    assert issubclass(
        BatchNotFoundError,
        BatchRegistrationError,
    )
    assert issubclass(
        DuplicateBatchError,
        BatchRegistrationError,
    )
    assert issubclass(
        UnsupportedBatchStrategyError,
        BatchValidationError,
    )


@pytest.mark.parametrize(
    ("exception_class", "message"),
    [
        (BatchError, "base"),
        (BatchValidationError, "validation"),
        (BatchRegistrationError, "registration"),
        (BatchNotFoundError, "missing"),
        (DuplicateBatchError, "duplicate"),
        (UnsupportedBatchStrategyError, "strategy"),
    ],
)
def test_exception_messages(
    exception_class: type[Exception],
    message: str,
) -> None:
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)