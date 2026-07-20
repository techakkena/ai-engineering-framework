from __future__ import annotations

import pytest

from ai_workflows.state.exceptions import StateError


def test_state_error() -> None:
    with pytest.raises(StateError):
        raise StateError()
