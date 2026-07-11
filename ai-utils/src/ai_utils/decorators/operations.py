"""
Decorator implementations for the AI Engineering Framework.
"""

from __future__ import annotations

import threading
import time
import warnings
from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar

from ai_utils.decorators.constants import (
    DEFAULT_DEPRECATION_MESSAGE,
)

F = TypeVar("F", bound=Callable[..., Any])

__all__ = [
    "deprecated",
    "singleton",
    "synchronized",
    "timer",
]


def timer(func: F) -> F:
    """
    Measure execution time of a function.
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()

        print(f"{func.__name__} executed in {end - start:.6f} seconds")

        return result

    return wrapper  # type: ignore[return-value]


def deprecated(
    message: str = DEFAULT_DEPRECATION_MESSAGE,
) -> Callable[[F], F]:
    """
    Mark a function as deprecated.
    """

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            warnings.warn(
                message,
                category=DeprecationWarning,
                stacklevel=2,
            )
            return func(*args, **kwargs)

        return wrapper  # type: ignore[return-value]

    return decorator


def singleton(cls: type[Any]) -> type[Any]:
    """
    Singleton class decorator.
    """

    instances: dict[type[Any], Any] = {}

    @wraps(cls)
    def get_instance(*args: Any, **kwargs: Any) -> Any:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)

        return instances[cls]

    return get_instance  # type: ignore[return-value]


def synchronized(func: F) -> F:
    """
    Thread-safe decorator.
    """

    lock = threading.Lock()

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        with lock:
            return func(*args, **kwargs)

    return wrapper  # type: ignore[return-value]
