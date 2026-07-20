from __future__ import annotations

from ai_tools.database.operations import (
    DatabaseClient,
    QueryResult,
)


def test_empty_result() -> None:
    result = QueryResult()

    assert result.rows == []
    assert result.row_count == 0


def test_register_and_execute() -> None:
    client = DatabaseClient()

    expected = QueryResult(
        rows=[
            {"id": 1, "name": "Alice"},
        ]
    )

    client.register_result(
        "SELECT * FROM users",
        expected,
    )

    result = client.execute(
        "SELECT * FROM users",
    )

    assert result.row_count == 1
    assert result.rows[0]["name"] == "Alice"


def test_unknown_query() -> None:
    client = DatabaseClient()

    result = client.execute(
        "SELECT * FROM missing",
    )

    assert result.row_count == 0
