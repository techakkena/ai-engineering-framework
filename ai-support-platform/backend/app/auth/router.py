from __future__ import annotations

"""Authentication API router."""

from app.auth.dependencies import (
    AuthenticationServiceDependency,
    CurrentActiveUserDependency,
)
from app.auth.schemas import (
    CurrentUserResponse,
    LoginRequest,
    TokenResponse,
    UserResponse,
)
from app.config.constants import BEARER_TOKEN_TYPE
from app.config.settings import settings
from fastapi import APIRouter, status

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
    summary="Authenticate user",
)
async def login(
    request: LoginRequest,
    auth_service: AuthenticationServiceDependency,
) -> TokenResponse:
    """Authenticate a user and issue an access token.

    Args:
        request: Login request.
        auth_service: Authentication service.

    Returns:
        JWT access token response.
    """
    user = auth_service.authenticate(
        email=request.email,
        password=request.password,
    )

    access_token = auth_service.create_token(user)

    return TokenResponse(
        access_token=access_token,
        token_type=BEARER_TOKEN_TYPE,
        expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
    )


@router.get(
    "/me",
    response_model=CurrentUserResponse,
    status_code=status.HTTP_200_OK,
    summary="Current authenticated user",
)
async def me(
    current_user: CurrentActiveUserDependency,
) -> CurrentUserResponse:
    """Return the authenticated user.

    Args:
        current_user: Authenticated active user.

    Returns:
        Current authenticated user.
    """
    return CurrentUserResponse(
        user=UserResponse.model_validate(current_user),
    )


@router.post(
    "/logout",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Logout",
)
async def logout() -> None:
    """Logout the current user.

    Token revocation will be implemented in a future sprint.
    """
    return None