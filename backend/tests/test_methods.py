from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_methods_list_contains_textrank_as_only_available_method():
    response = client.get("/api/methods")
    methods = response.json()

    assert response.status_code == 200
    assert [m["id"] for m in methods] == ["textrank", "metoda-2", "metoda-3"]
    assert [m["id"] for m in methods if m["available"]] == ["textrank"]
