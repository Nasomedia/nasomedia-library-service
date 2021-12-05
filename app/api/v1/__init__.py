from fastapi import APIRouter

from app.api.v1.endpoints import history
from app.api.v1.endpoints import liked
from app.api.v1.endpoints import purchased

api_router = APIRouter()
api_router.include_router(history.router, prefix="/library/history", tags=["history"])
api_router.include_router(liked.router, prefix="/library/liked", tags=["liked"])
api_router.include_router(purchased.router, prefix="/library/purchased", tags=["purchased"])