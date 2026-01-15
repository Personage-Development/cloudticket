from fastapi import APIRouter

import psycopg
from app.db.session import get_db


router = APIRouter(prefix="/health", tags=["Health"])
                   
                   
@router.get("")
def health_check() -> dict:
    return {"status": "ok"}

@router.get("/ready")
def readiness_check() -> dict:
    try:
        db_gen = get_db()
        conn = next(db_gen)
        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            cur.fetchone()
    except Exception as exc:
        return {"status": "not_ready", "detail": str(exc)}
    finally:
        try:
            conn.close()
        except Exception:
            pass

    return {"status": "ready"}