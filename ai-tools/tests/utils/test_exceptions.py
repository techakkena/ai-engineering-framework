import pytest

from ai_tools.utils.exceptions import (
    UtilityError,
)


def test_utility_error() -> None:
    with pytest.raises(
        UtilityError,
    ):
        raise UtilityError()
