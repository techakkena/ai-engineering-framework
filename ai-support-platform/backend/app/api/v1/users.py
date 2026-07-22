"""User API router."""

from __future__ import annotations

from typing import Annotated
from uuid import UUID

from app.auth.dependencies import get_current_user
from app.core.dependencies import DatabaseDependency
from app.core.exceptions import (
    ConflictException,
    ResourceNotFoundException,
)
from app.models.user import User
from app.organizations.repository import OrganizationRepository
from app.repositories.user import UserRepository
from app.users.schemas import (
    CreateUserRequest,
    UpdateUserRequest,
    UserListResponse,
    UserResponse,
)
from app.users.service import UserService
from fastapi import APIRouter, Depends, HTTPException, Query, Response, status

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


def get_user_service(
    db: DatabaseDependency,
) -> UserService:
    """Return a user service."""
    return UserService(
        user_repository=UserRepository(db),
        organization_repository=OrganizationRepository(db),
    )


UserServiceDependency = Annotated[
    UserService,
    Depends(get_user_service),
]

CurrentUserDependency = Annotated[
    User,
    Depends(get_current_user),
]


@router.get(
    "",
    response_model=UserListResponse,
    summary="List users",
)
async def list_users(
    _: CurrentUserDependency,
    service: UserServiceDependency,
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=100),
) -> UserListResponse:
    """Return users."""
    users = service.list_users(
        offset=offset,
        limit=limit,
    )

    return UserListResponse(
        total=len(users),
        users=[
            UserResponse.model_validate(user)
            for user in users
        ],
    )


@router.get(
    "/{user_id}",
    response_model=UserResponse,
    summary="Get user",
)
async def get_user(
    user_id: UUID,
    _: CurrentUserDependency,
    service: UserServiceDependency,
) -> UserResponse:
    """Return a user."""
    try:
        user = service.get_user(user_id)
        return UserResponse.model_validate(user)
    except ResourceNotFoundException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create user",
)
async def create_user(
    request: CreateUserRequest,
    _: CurrentUserDependency,
    service: UserServiceDependency,
) -> UserResponse:
    """Create a user."""
    try:
        user = service.create_user(request)
        return UserResponse.model_validate(user)
    except ConflictException as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc
    except ResourceNotFoundException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.patch(
    "/{user_id}",
    response_model=UserResponse,
    summary="Update user",
)
async def update_user(
    user_id: UUID,
    request: UpdateUserRequest,
    _: CurrentUserDependency,
    service: UserServiceDependency,
) -> UserResponse:
    """Update a user."""
    try:
        user = service.update_user(
            user_id=user_id,
            request=request,
        )

        return UserResponse.model_validate(user)

    except ConflictException as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc
    except ResourceNotFoundException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete user",
)
async def delete_user(
    user_id: UUID,
    _: CurrentUserDependency,
    service: UserServiceDependency,
) -> Response:
    """Delete a user."""
    try:
        service.delete_user(user_id)

        return Response(
            status_code=status.HTTP_204_NO_CONTENT,
        )
    except ResourceNotFoundException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
