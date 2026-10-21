"""Lesson 3 — pydantic-settings, modeled on Spigot's app/config.py."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    database_url: str
    redis_url: str = "redis://localhost:6379/0"
    jwt_secret: str = Field(min_length=32)
    jwt_expire_minutes: int = Field(default=60, ge=1)
    frontend_origin: str = "http://localhost:5173"
    login_rate_limit_per_min: int = Field(default=10, ge=1)
