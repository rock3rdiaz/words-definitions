from fastapi import FastAPI, Request, Response, APIRouter
from functools import lru_cache

from app.src.core.database import SessionLocal, engine
from app.src.core.database import Base
from app.api.v1.endpoints.api import api_router

Base.metadata.create_all(bind=engine)


@lru_cache(maxsize=None)
def get_application() -> FastAPI:
    application = FastAPI(
        title='A translation tool!',
        description='Just give me a word and i\'ll do magic!',
        version='0.1'
    )
    application.include_router(api_router, prefix='/api/v1')
    return application


app = get_application()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


async def get_db():
    return request.state.db