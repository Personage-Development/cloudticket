from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    app_name: str = "CloudTicket API"
    environment: str = "local"

    secret_key: str = "change_me_please"
    access_token_expire_minutes: int = 60

    DATABASE_URL: str = "postgresql://cloudticket:cloudticket_password_change_me@localhost:5432/cloudticket"


    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    return Settings()