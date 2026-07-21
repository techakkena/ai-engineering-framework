from __future__ import annotations

from app.models.ticket import Category  # Ensure this matches your category model path
from app.repositories.base import BaseRepository
from sqlalchemy.orm import Session


class CategoryRepository(BaseRepository[Category]):
    def __init__(self, session: Session) -> None:
        super().__init__(session, Category)
