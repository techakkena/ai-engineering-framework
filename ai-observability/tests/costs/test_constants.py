from ai_observability.costs.constants import (
    DEFAULT_CURRENCY,
)


def test_default_currency() -> None:
    assert DEFAULT_CURRENCY == "USD"
