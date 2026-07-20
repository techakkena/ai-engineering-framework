from __future__ import annotations

import pytest

from ai_tools.github.exceptions import (
    GitHubToolError,
)


def test_github_tool_error() -> None:
    with pytest.raises(GitHubToolError):
        raise GitHubToolError()
