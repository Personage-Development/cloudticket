from fastapi import FastAPI
from app.core.config import get_settings
from app.api.v1.routes import health



def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title="CloudTicket API",
        version="0.1.0",
        description="API for managing cloud-based ticketing systems using postgres and FastAPI.",
    )

    app.include_router(health.router, prefix="/api/v1")

    return app

app = create_app()