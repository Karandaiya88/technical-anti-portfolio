"""
Application settings, loaded from environment variables (.env).
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://postgres:postgres@localhost:5432/anti_portfolio"
    github_client_id: str = ""
    github_client_secret: str = ""
    github_callback_url: str = "http://localhost:8000/auth/github/callback"
    secret_key: str = "dev-secret-change-me"
    frontend_url: str = "http://localhost:3000"
    max_diff_size_kb: int = 250

    class Config:
        env_file = ".env"


settings = Settings()
