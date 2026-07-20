from __future__ import annotations

from ai_tools.search.operations import (
    SearchClient,
    SearchResult,
)


def test_register_and_search() -> None:
    client = SearchClient()

    expected = [
        SearchResult(
            title="OpenAI",
            url="https://openai.com",
            snippet="AI research.",
        ),
    ]

    client.register_results(
        "openai",
        expected,
    )

    results = client.search("openai")

    assert len(results) == 1
    assert results[0].title == "OpenAI"


def test_unknown_query() -> None:
    client = SearchClient()

    results = client.search("missing")

    assert results == []


def test_search_result_fields() -> None:
    result = SearchResult(
        title="Example",
        url="https://example.com",
        snippet="Example snippet.",
    )

    assert result.title == "Example"
    assert result.url == "https://example.com"
    assert result.snippet == "Example snippet."
