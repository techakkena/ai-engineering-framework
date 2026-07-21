from __future__ import annotations

"""Authentication dependencies."""

from typing import Annotated
from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.auth.jwt import decode_access_token
from app.auth.service import AuthenticationService
from app.database import get_db
from app.models.user import User
from app.repositories.user import UserRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    """Return the authenticated user."""
    try:
        payload = decode_access_token(token)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials.",
        ) from exc

    user_id = UUID(payload["sub"])

    repository = UserRepository(db)
    user = repository.get_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found.",
        )

    return user


CurrentActiveUserDependency = Annotated[
    User,
    Depends(get_current_user),
]


def get_authentication_service(
    db: Session = Depends(get_db),
) -> AuthenticationService:
    """Return the authentication service."""
    repository = UserRepository(db)
    return AuthenticationService(repository)