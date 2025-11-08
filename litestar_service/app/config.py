from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    DEBUG: int

    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int

    DB_NAME_DEV: str
    DB_USER_DEV: str
    DB_PASSWORD_DEV: str
    DB_HOST_DEV: str
    DB_PORT_DEV: int

    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 5000

    @property
    def DB_URL(self) -> str:
        if self.DEBUG == 1:
            return f"postgresql+asyncpg://{self.DB_USER_DEV}:{self.DB_PASSWORD_DEV}@{self.DB_HOST_DEV}:{self.DB_PORT_DEV}/{self.DB_NAME_DEV}"
        else:
            return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
