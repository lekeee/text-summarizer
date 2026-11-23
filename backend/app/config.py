import os
from dataclasses import dataclass, field

DEFAULT_CORS_ORIGINS = "http://localhost:5173"


def read_cors_origins() -> list[str]:
    value = os.environ.get("CORS_ORIGINS", DEFAULT_CORS_ORIGINS)
    return [origin.strip().rstrip("/") for origin in value.split(",") if origin.strip()]


@dataclass(frozen=True)
class Settings:
    app_name: str = "Sistem za sažimanje teksta"
    cors_origins: list[str] = field(default_factory=read_cors_origins)
    max_file_size_mb: int = 5
    max_pages: int = 10
    words_per_page: int = 300
    min_ratio: int = 10
    max_ratio: int = 60


settings = Settings()
