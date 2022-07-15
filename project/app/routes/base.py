from fastapi import APIRouter

from homepage import home_pages_router
from ws import websockets_router

router = APIRouter()

api_router.include_router(home_pages_router, prefix="", tags=["home-page"])