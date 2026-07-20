from __future__ import annotations

import pytest

from ai_workflows.utils.exceptions import (
    UtilityError,
)


def test_utility_error() -> None:
    with pytest.raises(
        UtilityError,
    ):
        raise UtilityError()
