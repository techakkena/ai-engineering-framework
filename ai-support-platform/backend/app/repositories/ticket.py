from __future__ import annotations

from uuid import UUID

from app.models import Ticket
from app.models.ticket import Ticket
from app.repositories.base import BaseRepository
from sqlalchemy.orm import Session


class TicketRepository(BaseRepository[Ticket]):
    def __init__(self, session: Session) -> None:
        super().__init__(session, Ticket)

    def list_by_organization(self, organization_id: UUID) -> list[Ticket]:
        """Return a list of tickets belonging to an organization."""
        return (
            self.session.query(self._model)
            .filter(self._model.organization_id == organization_id)
            .all()
        )
