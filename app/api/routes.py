from fastapi import APIRouter

from app.api.endpoints import address

api_router = APIRouter()

api_router.include_router(address.router, prefix="/address")