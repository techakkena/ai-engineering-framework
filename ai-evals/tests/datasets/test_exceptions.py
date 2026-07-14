import pytest

from ai_evals.datasets.exceptions import (
    DatasetError,
)


def test_dataset_error() -> None:
    with pytest.raises(DatasetError):
        raise DatasetError()
