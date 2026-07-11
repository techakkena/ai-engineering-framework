"""
Retry operations for the AI Engineering Framework.
"""

from __future__ import annotations

import time
from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar

from ai_utils.retry.constants import (
    DEFAULT_DELAY_SECONDS,
    DEFAULT_MAX_ATTEMPTS,
)
from ai_utils.retry.exceptions import RetryError

F = TypeVar("F", bound=Callable[..., Any])

__all__ = [
    "retry",
    "retry_on_exception",
]


def retry(
    max_attempts: int = DEFAULT_MAX_ATTEMPTS,
    delay: float = DEFAULT_DELAY_SECONDS,
) -> Callable[[F], F]:
    """
    Retry a function when an exception occurs.
    """

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception: Exception | None = None

            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)

                except Exception as exc:
                    last_exception = exc

                    if attempt < max_attempts - 1:
                        time.sleep(delay)

            raise RetryError(
                f"{func.__name__} failed after {max_attempts} attempts."
            ) from last_exception

        return wrapper  # type: ignore[return-value]

    return decorator


def retry_on_exception(
    func: Callable[..., Any],
    *args: Any,
    max_attempts: int = DEFAULT_MAX_ATTEMPTS,
    delay: float = DEFAULT_DELAY_SECONDS,
    **kwargs: Any,
) -> Any:
    """
    Retry a callable directly.
    """
    decorated = retry(
        max_attempts=max_attempts,
        delay=delay,
    )(func)

    return decorated(*args, **kwargs)
