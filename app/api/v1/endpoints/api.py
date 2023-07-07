from fastapi import APIRouter

from app.api.v1.endpoints.words import router as words_router

api_router = APIRouter()

api_router.include_router(words_router, prefix="/words", tags=['words'])
