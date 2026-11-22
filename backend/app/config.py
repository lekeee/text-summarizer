from dataclasses import dataclass, field


@dataclass(frozen=True)
class Settings:
    app_name: str = "Sistem za sažimanje teksta"
    cors_origins: list[str] = field(default_factory=lambda: ["http://localhost:5173"])
    max_file_size_mb: int = 5
    max_pages: int = 5
    words_per_page: int = 300
    min_ratio: int = 10
    max_ratio: int = 60


settings = Settings()
