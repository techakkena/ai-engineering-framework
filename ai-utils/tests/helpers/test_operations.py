from __future__ import annotations

from ai_utils.helpers.operations import (
    batched,
    chunk_list,
    flatten_list,
    generate_random_string,
    generate_uuid,
    identity,
    noop,
    safe_cast,
)


def test_generate_uuid() -> None:
    assert isinstance(generate_uuid(), str)


def test_generate_random_string() -> None:
    value = generate_random_string()

    assert len(value) == 16


def test_chunk_list() -> None:
    data = [1, 2, 3, 4, 5]

    assert chunk_list(data, 2) == [
        [1, 2],
        [3, 4],
        [5],
    ]


def test_flatten_list() -> None:
    data = [
        [1, 2],
        [3, 4],
    ]

    assert flatten_list(data) == [1, 2, 3, 4]


def test_safe_cast_success() -> None:
    assert safe_cast("123", int) == 123


def test_safe_cast_failure() -> None:
    assert safe_cast("abc", int) is None


def test_noop() -> None:
    noop()


def test_identity() -> None:
    assert identity("OpenAI") == "OpenAI"


def test_batched() -> None:
    data = list(batched(range(5), 2))

    assert data == [
        [0, 1],
        [2, 3],
        [4],
    ]
