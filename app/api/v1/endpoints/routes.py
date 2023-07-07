from fastapi import APIRouter

from app.api.v1.endpoints import words

api_router = APIRouter()

api_router.include_router(words.router, prefix="/words", tags=['words'])
