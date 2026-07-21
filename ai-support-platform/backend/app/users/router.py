from __future__ import annotations

"""User API router."""

from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Response, status
from app.users.dependencies import (
    UserServiceDependency,
    get_user_service,
)
from app.core.dependencies import DatabaseDependency
from app.models.user import User
from app.organizations.repository import OrganizationRepository
from app.rbac.dependencies import require_permission
from app.repositories.user import UserRepository
from app.users.schemas import (
    CreateUserRequest,
    UpdateUserRequest,
    UserListResponse,
    UserResponse,
)
from app.users.service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


def get_user_service(
    db: DatabaseDependency,
) -> UserService:
    """Return a user service."""
    user_repository = UserRepository(db)
    organization_repository = OrganizationRepository(db)

    return UserService(
        user_repository=user_repository,
        organization_repository=organization_repository,
    )

UserServiceDependency = Annotated[
    UserService,
    Depends(get_user_service),
]

CreateUserPermission = Annotated[
    User,
    Depends(require_permission("user", "create")),
]

ViewUserPermission = Annotated[
    User,
    Depends(require_permission("user", "view")),
]

UpdateUserPermission = Annotated[
    User,
    Depends(require_permission("user", "update")),
]

DeleteUserPermission = Annotated[
    User,
    Depends(require_permission("user", "delete")),
]


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create user",
)
async def create_user(
    request: CreateUserRequest,
    _: CreateUserPermission,
    service: UserServiceDependency,
) -> UserResponse:
    """Create a new user."""
    user = service.create_user(request)

    return UserResponse.model_validate(user)


@router.get(
    "",
    response_model=UserListResponse,
    summary="List users",
)
async def list_users(
    _: ViewUserPermission,
    service: UserServiceDependency,
    offset: int = 0,
    limit: int = 100,
) -> UserListResponse:
    """Return all users."""
    users = service.list_users(
        skip=skip,
        limit=limit,
    )

    return UserListResponse(
        users=[
            UserResponse.model_validate(user)
            for user in users
        ],
        total=len(users),
    )


@router.get(
    "/{user_id}",
    response_model=UserResponse,
    summary="Get user",
)
async def get_user(
    user_id: UUID,
    _: ViewUserPermission,
    service: UserServiceDependency,
) -> UserResponse:
    """Return a user."""
    user = service.get_user(user_id)

    return UserResponse.model_validate(user)


@router.patch(
    "/{user_id}",
    response_model=UserResponse,
    summary="Update user",
)
async def update_user(
    user_id: UUID,
    request: UpdateUserRequest,
    _: UpdateUserPermission,
    service: UserServiceDependency,
) -> UserResponse:
    """Update an existing user."""
    user = service.update_user(
        user_id=user_id,
        request=request,
    )

    return UserResponse.model_validate(user)


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete user",
)
async def delete_user(
    user_id: UUID,
    _: DeleteUserPermission,
    service: UserServiceDependency,
) -> Response:
    """Delete a user."""
    service.delete_user(user_id)

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )