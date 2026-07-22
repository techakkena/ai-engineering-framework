"""API v1 router."""

from __future__ import annotations

from app.api.v1.tickets import router as ticket_router
from app.auth.router import router as auth_router
from app.customers.router import router as customer_router
from app.teams.router import router as teams_router
from app.users.router import router as user_router
from fastapi import APIRouter

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(auth_router)
api_router.include_router(user_router)
api_router.include_router(teams_router)
api_router.include_router(ticket_router)
api_router.include_router(customer_router)