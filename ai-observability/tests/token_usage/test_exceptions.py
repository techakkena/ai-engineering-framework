import pytest

from ai_observability.token_usage.exceptions import (
    TokenUsageError,
)


def test_token_usage_error() -> None:
    with pytest.raises(
        TokenUsageError,
    ):
        raise TokenUsageError()
