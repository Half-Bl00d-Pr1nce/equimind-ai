from fastapi import APIRouter
from app.routers.health import router as health_router
from app.routers.sec import router as sec_router
from app.routers.parser import router as parser_router
from app.routers.embedding import router as embedding_router
from app.routers.vector import router as vector_router
from app.routers.chat import router as chat_router

api_router = APIRouter()

api_router.include_router(health_router)

api_router.include_router(sec_router)

api_router.include_router(parser_router)
api_router.include_router(embedding_router)
api_router.include_router(vector_router)
api_router.include_router(chat_router)