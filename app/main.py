from fastapi import APIRouter, FastAPI

def create_app() -> FastAPI:
    app = FastAPI(
        title="CloudTicket API",
        version="0.1.0",
        description="API for managing cloud-based ticketing systems using postgres and FastAPI.",
    )

    api_v1_router = APIRouter(prefix="/api/v1")

    @api_v1_router.get("/health", tags=["Health"])
    async def health_check():
        return {"status": "ok"}

    app.include_router(api_v1_router)
    return app

app = create_app()