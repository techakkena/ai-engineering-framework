"""API V1 router for all modules."""

from app.auth.router import router as auth_router
from app.comments.router import router as comment_router
from app.customers.router import router as customer_router
from app.knowledge.router import router as knowledge_router
from app.notifications.router import router as notification_router
from app.teams.router import router as teams_router
from app.tickets.router import router as ticket_router
from app.users.router import router as user_router
from fastapi import APIRouter

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(auth_router)
api_router.include_router(user_router)
api_router.include_router(teams_router)
api_router.include_router(ticket_router)
api_router.include_router(customer_router)
api_router.include_router(comment_router)
api_router.include_router(knowledge_router)
api_router.include_router(notification_router)