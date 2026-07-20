from __future__ import annotations

import pytest
from fastapi import HTTPException

from app.auth.dependencies import get_current_user
from app.auth.jwt import create_access_token


def test_get_current_user_success(
    db_session,
    user,
):
    token = create_access_token(str(user.id))

    current_user = get_current_user(
        token=token,
        db=db_session,
    )

    assert current_user.id == user.id


def test_invalid_token(
    db_session,
):
    with pytest.raises(HTTPException):
        get_current_user(
            token="invalid-token",
            db=db_session,
        )