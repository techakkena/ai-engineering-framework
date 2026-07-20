from app.auth.router import router as auth_router
from app.users.router import router as user_router
from fastapi import APIRouter

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(auth_router)
api_router.include_router(user_router)