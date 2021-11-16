from fastapi import APIRouter

from app.api.v1.endpoints import api_frame

api_router = APIRouter()
api_router.include_router(api_frame.router, prefix="/test", tags=["test"])