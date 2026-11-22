from app.config import read_cors_origins


def test_uses_localhost_when_variable_is_missing(monkeypatch):
    monkeypatch.delenv("CORS_ORIGINS", raising=False)

    assert read_cors_origins() == ["http://localhost:5173"]


def test_reads_comma_separated_origins_without_trailing_slash(monkeypatch):
    monkeypatch.setenv("CORS_ORIGINS", "https://sazimanje.vercel.app/, http://localhost:5173")

    assert read_cors_origins() == ["https://sazimanje.vercel.app", "http://localhost:5173"]
