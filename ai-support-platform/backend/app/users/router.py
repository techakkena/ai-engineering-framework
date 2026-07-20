"""Ticket API router."""

from __future__ import annotations

from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Response, status

from app.core.dependencies import DatabaseDependency
from app.models.user import User
from app.rbac.dependencies import require_permission
from app.tickets.schemas import (
    CreateTicketRequest,
    TicketListResponse,
    TicketResponse,
    UpdateTicketRequest,
)
from app.tickets.service import TicketService

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"],
)


def get_ticket_service(
    db: DatabaseDependency,
) -> TicketService:
    """Return a ticket service."""
    return TicketService(db)


TicketServiceDependency = Annotated[
    TicketService,
    Depends(get_ticket_service),
]

CreateTicketUser = Annotated[
    User,
    Depends(require_permission("ticket", "create")),
]

ViewTicketUser = Annotated[
    User,
    Depends(require_permission("ticket", "view")),
]

UpdateTicketUser = Annotated[
    User,
    Depends(require_permission("ticket", "update")),
]

DeleteTicketUser = Annotated[
    User,
    Depends(require_permission("ticket", "delete")),
]


@router.post(
    "",
    response_model=TicketResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create ticket",
)
async def create_ticket(
    request: CreateTicketRequest,
    current_user: CreateTicketUser,
    service: TicketServiceDependency,
) -> TicketResponse:
    """Create a ticket."""
    ticket = service.create_ticket(
        organization_id=current_user.organization_id,
        created_by_id=current_user.id,
        request=request,
    )

    return TicketResponse.model_validate(ticket)


@router.get(
    "",
    response_model=TicketListResponse,
    summary="List tickets",
)
async def list_tickets(
    current_user: ViewTicketUser,
    service: TicketServiceDependency,
) -> TicketListResponse:
    """Return all tickets."""
    tickets = service.list_tickets(
        organization_id=current_user.organization_id,
    )

    return TicketListResponse(
        tickets=[
            TicketResponse.model_validate(ticket)
            for ticket in tickets
        ],
        total=len(tickets), 
    )


@router.get(
    "/{ticket_id}",
    response_model=TicketResponse,
    summary="Get ticket",
)
async def get_ticket(
    ticket_id: UUID,
    _: ViewTicketUser,
    service: TicketServiceDependency,
) -> TicketResponse:
    """Return a ticket."""
    ticket = service.get_ticket(ticket_id)

    return TicketResponse.model_validate(ticket)


@router.patch(
    "/{ticket_id}",
    response_model=TicketResponse,
    summary="Update ticket",
)
async def update_ticket(
    ticket_id: UUID,
    request: UpdateTicketRequest,
    _: UpdateTicketUser,
    service: TicketServiceDependency,
) -> TicketResponse:
    """Update a ticket."""
    ticket = service.update_ticket(
        ticket_id,
        request,
    )

    return TicketResponse.model_validate(ticket)


@router.delete(
    "/{ticket_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete ticket",
)
async def delete_ticket(
    ticket_id: UUID,
    _: DeleteTicketUser,
    service: TicketServiceDependency,
) -> Response:
    """Delete a ticket."""
    service.delete_ticket(ticket_id)

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )
