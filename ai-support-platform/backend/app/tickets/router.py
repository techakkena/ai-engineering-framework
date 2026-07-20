from __future__ import annotations

from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Response, status

from app.core.dependencies import DatabaseDependency
from app.models import User
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

@router.post(
    "",
    response_model=TicketResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create ticket",
)
async def create_ticket(
    request: CreateTicketRequest,
    current_user: User = Depends(
        require_permission(
            "ticket",
            "create",
        ),
    ),
    service: TicketServiceDependency,
) -> TicketResponse:
    """Create a ticket."""

    ticket = service.create_ticket(
        organization_id=current_user.organization_id,
        created_by_id=current_user.id,
        request=request,
    )
    return TicketResponse.model_validate(ticket)