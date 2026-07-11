"""
Unit tests for decorators.
"""

from __future__ import annotations

import warnings

from ai_utils.decorators.operations import (
    deprecated,
    singleton,
    synchronized,
    timer,
)


def test_timer() -> None:
    @timer
    def add(a: int, b: int) -> int:
        return a + b

    assert add(2, 3) == 5


def test_deprecated() -> None:
    @deprecated("Deprecated")
    def old_function() -> int:
        return 10

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")

        assert old_function() == 10

        assert len(caught) == 1
        assert issubclass(
            caught[0].category,
            DeprecationWarning,
        )


def test_singleton() -> None:
    @singleton
    class Test:
        pass

    a = Test()
    b = Test()

    assert a is b


def test_synchronized() -> None:
    @synchronized
    def increment(value: int) -> int:
        return value + 1

    assert increment(1) == 2
