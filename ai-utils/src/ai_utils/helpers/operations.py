"""
Generic helper utilities for the AI Engineering Framework.
"""

from __future__ import annotations

import secrets
import string
import uuid
from collections.abc import Callable, Iterable
from itertools import islice
from typing import Any, TypeVar

from ai_utils.helpers.constants import DEFAULT_RANDOM_LENGTH

T = TypeVar("T")

__all__ = [
    "batched",
    "chunk_list",
    "flatten_list",
    "generate_random_string",
    "generate_uuid",
    "identity",
    "noop",
    "safe_cast",
]


def generate_uuid() -> str:
    """
    Generate a UUID4 string.

    Returns
    -------
    str
        A randomly generated UUID4 string.
    """
    return str(uuid.uuid4())


def generate_random_string(
    length: int = DEFAULT_RANDOM_LENGTH,
) -> str:
    """
    Generate a cryptographically secure random string.

    Parameters
    ----------
    length
        Length of the generated string.

    Returns
    -------
    str
        Random alphanumeric string.

    Raises
    ------
    ValueError
        If length is less than or equal to zero.
    """
    if length <= 0:
        raise ValueError("length must be greater than zero")

    alphabet = string.ascii_letters + string.digits

    return "".join(secrets.choice(alphabet) for _ in range(length))


def chunk_list(
    items: list[T],
    size: int,
) -> list[list[T]]:
    """
    Split a list into equally sized chunks.

    Parameters
    ----------
    items
        List to split.

    size
        Chunk size.

    Returns
    -------
    list[list[T]]
        List of chunks.

    Raises
    ------
    ValueError
        If size is less than or equal to zero.
    """
    if size <= 0:
        raise ValueError("size must be greater than zero")

    return [items[index : index + size] for index in range(0, len(items), size)]


def flatten_list(
    items: list[list[T]],
) -> list[T]:
    """
    Flatten a nested list.

    Parameters
    ----------
    items
        Nested list.

    Returns
    -------
    list[T]
        Flattened list.
    """
    return [item for sublist in items for item in sublist]


def safe_cast(
    value: Any,
    target_type: Callable[[Any], T],
    default: T | None = None,
) -> T | None:
    """
    Safely cast a value.

    Parameters
    ----------
    value
        Value to cast.

    target_type
        Callable used for casting.

    default
        Default value returned if casting fails.

    Returns
    -------
    T | None
        Converted value or default.
    """
    try:
        return target_type(value)
    except TypeError, ValueError:
        return default


def noop(
    *args: Any,
    **kwargs: Any,
) -> None:
    """
    Perform no operation.

    Accepts any positional and keyword arguments and
    intentionally does nothing.
    """
    return None


def identity(
    value: T,
) -> T:
    """
    Return the supplied value unchanged.

    Parameters
    ----------
    value
        Input value.

    Returns
    -------
    T
        Same value.
    """
    return value


def batched(
    iterable: Iterable[T],
    size: int,
) -> Iterable[list[T]]:
    """
    Yield batches from an iterable.

    Parameters
    ----------
    iterable
        Input iterable.

    size
        Batch size.

    Yields
    ------
    list[T]
        Batch of items.

    Raises
    ------
    ValueError
        If size is less than or equal to zero.
    """
    if size <= 0:
        raise ValueError("size must be greater than zero")

    iterator = iter(iterable)

    while True:
        batch = list(islice(iterator, size))

        if not batch:
            break

        yield batch
