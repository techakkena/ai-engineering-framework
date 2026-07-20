from __future__ import annotations

"""Authentication dependencies."""

from typing import Annotated

from app.auth.service import AuthenticationService
from app.core.dependencies import DatabaseDependency
from app.core.exceptions import AuthenticationException
from app.models.user import User
from app.repositories.user import UserRepository
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login",
)


def get_authentication_service(
    db: DatabaseDependency,
) -> AuthenticationService:
    """Return the authentication service.

    Args:
        db: Database session.

    Returns:
        Authentication service instance.
    """
    repository = UserRepository(db)

    return AuthenticationService(repository)


AuthenticationServiceDependency = Annotated[
    AuthenticationService,
    Depends(get_authentication_service),
]

async def get_current_active_user(
    current_user: CurrentUserDependency,
) -> User:
    """Return the current active user.

    Args:
        current_user: Authenticated user.

    Returns:
        Active user.

    Raises:
        AuthenticationException: If the user is inactive.
    """
    if not current_user.is_active:
        raise AuthenticationException(
            "User account is inactive.",
        )

    return current_user


CurrentActiveUserDependency = Annotated[
    User,
    Depends(get_current_active_user),
]


async def get_current_superuser(
    current_user: CurrentActiveUserDependency,
) -> User:
    """Return the current superuser.

    Args:
        current_user: Authenticated active user.

    Returns:
        Superuser.

    Raises:
        AuthenticationException: If the user is not a superuser.
    """
    if not current_user.is_superuser:
        raise AuthenticationException(
            "Superuser privileges are required.",
        )

    return current_user


CurrentUserDependency = CurrentActiveUserDependency