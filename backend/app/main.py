from contextlib import asynccontextmanager

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifecycle manager.
    Executes startup logic before the application begins serving requests
    and shutdown logic before the application exits.
    """

    # Startup
    print("Starting EquiMind AI Backend...")

    yield

    # Shutdown
    print("Shutting down EquiMind AI Backend...")


app = FastAPI(
    title="EquiMind AI",
    description="AI-Powered Equity Research Platform",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)