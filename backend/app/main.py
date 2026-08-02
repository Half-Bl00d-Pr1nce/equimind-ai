from contextlib import asynccontextmanager
from app.config.settings import settings
from fastapi import FastAPI
from app.config.logging import configure_logging
import logging
from app.routers.api import api_router





@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifecycle manager.
    Executes startup logic before the application begins serving requests
    and shutdown logic before the application exits.
    """
    logger = logging.getLogger(__name__)
    
    # Startup
    logger.info("Starting EquiMind AI Backend...")

    yield

    # Shutdown
    logger.info("Shutting down EquiMind AI Backend...")


configure_logging()

app = FastAPI(
    title=settings.APP_NAME,
    description="AI-Powered Equity Research Platform",
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

app.include_router(
    api_router,
    prefix=settings.API_V1_PREFIX,
)