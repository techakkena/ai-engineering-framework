from __future__ import annotations

import pytest

from ai_workflows.scheduler.exceptions import (
    SchedulerError,
)


def test_scheduler_error() -> None:
    with pytest.raises(SchedulerError):
        raise SchedulerError()
