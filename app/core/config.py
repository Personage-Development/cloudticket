from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
        )

    APP_NAME: str = "CloudTicket API"
    ENVIRONMENT: str = "local"

    # Security
    SECRET_KEY: str = "change-me"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60


    DATABASE_URL: str = "postgresql://cloudticket:cloudticket_password_change_me@localhost:5432/cloudticket"

@lru_cache()
def get_settings() -> Settings:
    return Settings()