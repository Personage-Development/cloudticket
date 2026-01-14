from fastapi import APIRouter, FastAPI
from app.core.config import get_settings
import psycopg


def create_app() -> FastAPI:
    Settings = get_settings()

    app = FastAPI(
        title="CloudTicket API",
        version="0.1.0",
        description="API for managing cloud-based ticketing systems using postgres and FastAPI.",
    )

    api_v1_router = APIRouter(prefix="/api/v1")

    @api_v1_router.get("/health", tags=["Health"])
    async def health_check():
        return {"status": "ok"}
    
    @api_v1_router.get("/ready", tags=["health"])
    def readiness_check():
        settings = get_settings()
        try:
            with psycopg.connect(settings.DATABASE_URL, connect_timeout=3) as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT 1;")
                    cur.fetchone()
        except Exception as exc:
            return {"status": "not_ready", "detail": str(exc)}

        return {"status": "ready"}

    app.include_router(api_v1_router)
    return app

app = create_app()