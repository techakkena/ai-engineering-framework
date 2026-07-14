import pytest

from ai_observability.costs.exceptions import (
    CostError,
)


def test_cost_error() -> None:
    with pytest.raises(CostError):
        raise CostError()
