from __future__ import annotations

from app.models.ticket import Priority
from app.repositories.base import BaseRepository
from sqlalchemy.orm import Session


class PriorityRepository(BaseRepository[Priority]):
    def __init__(self, session: Session) -> None:
        super().__init__(session, Priority)
