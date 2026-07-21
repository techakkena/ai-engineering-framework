from __future__ import annotations

"""Organization API router."""

from typing import Annotated
from uuid import UUID

from app.auth.dependencies import get_current_user
from app.core.exceptions import (
    ConflictException,
    ResourceNotFoundException,
)
from app.models.user import User
from app.organizations.dependencies import (
    OrganizationServiceDependency,
)
from app.organizations.schemas import (
    CreateOrganizationRequest,
    OrganizationListResponse,
    OrganizationResponse,
    UpdateOrganizationRequest,
)
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Response,
    status,
)

router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"],
)

CurrentUserDependency = Annotated[
    User,
    Depends(get_current_user),
]


@router.post(
    "",
    response_model=OrganizationResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create organization",
)
async def create_organization(
    request: CreateOrganizationRequest,
    _: CurrentUserDependency = None,
    service: OrganizationServiceDependency = None,
) -> OrganizationResponse:
    """Create an organization."""
    try:
        organization = service.create_organization(request)

        return OrganizationResponse.model_validate(
            organization,
        )

    except ConflictException as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc


@router.get(
    "",
    response_model=OrganizationListResponse,
    summary="List organizations",
)
async def list_organizations(
    skip: int = 0,
    limit: int = 100,
    _: CurrentUserDependency = None,
    service: OrganizationServiceDependency = None,
) -> OrganizationListResponse:
    """Return organizations."""
    organizations = service.list_organizations(
        skip=skip,
        limit=limit,
    )

    return OrganizationListResponse(
        organizations=[
            OrganizationResponse.model_validate(org) for org in organizations
        ],
    )


@router.get(
    "/{organization_id}",
    response_model=OrganizationResponse,
    summary="Get organization",
)
async def get_organization(
    organization_id: UUID,
    _: CurrentUserDependency = None,
    service: OrganizationServiceDependency = None,
) -> OrganizationResponse:
    """Return an organization."""
    try:
        organization = service.get_organization(
            organization_id,
        )

        return OrganizationResponse.model_validate(
            organization,
        )

    except ResourceNotFoundException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.patch(
    "/{organization_id}",
    response_model=OrganizationResponse,
    summary="Update organization",
)
async def update_organization(
    organization_id: UUID,
    request: UpdateOrganizationRequest,
    _: CurrentUserDependency = None,
    service: OrganizationServiceDependency = None,
) -> OrganizationResponse:
    """Update an organization."""
    try:
        organization = service.update_organization(
            organization_id=organization_id,
            request=request,
        )

        return OrganizationResponse.model_validate(
            organization,
        )

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
    "/{organization_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete organization",
)
async def delete_organization(
    organization_id: UUID,
    _: CurrentUserDependency = None,
    service: OrganizationServiceDependency = None,
) -> Response:
    """Delete an organization."""
    try:
        service.delete_organization(organization_id)

        return Response(
            status_code=status.HTTP_204_NO_CONTENT,
        )

    except ResourceNotFoundException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
