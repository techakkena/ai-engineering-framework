from ai_observability.token_usage.operations import (
    TokenUsage,
    TokenUsageRegistry,
)


def test_total_tokens() -> None:
    usage = TokenUsage(
        prompt_tokens=100,
        completion_tokens=50,
    )

    assert usage.total_tokens == 150


def test_registry_totals() -> None:
    registry = TokenUsageRegistry()

    registry.add(
        TokenUsage(
            prompt_tokens=10,
            completion_tokens=5,
        )
    )

    registry.add(
        TokenUsage(
            prompt_tokens=20,
            completion_tokens=15,
        )
    )

    assert registry.count == 2
    assert registry.total_prompt_tokens == 30
    assert registry.total_completion_tokens == 20
    assert registry.total_tokens == 50


def test_default_model() -> None:
    usage = TokenUsage()

    assert usage.model == "unknown"
