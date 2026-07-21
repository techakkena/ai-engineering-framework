from __future__ import annotations

from app.models.ticket import Status
from app.repositories.base import BaseRepository
from sqlalchemy.orm import Session


class StatusRepository(BaseRepository[Status]):
    def __init__(self, session: Session) -> None:
        super().__init__(session, Status)
