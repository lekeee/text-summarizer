from fastapi.testclient import TestClient

from app.config import settings
from app.main import app
from tests.sample_texts import ARTICLE

client = TestClient(app)

TOO_MANY_WORDS = settings.max_pages * settings.words_per_page + 1


def test_summarize_returns_summary_scores_and_stats():
    response = client.post("/api/summarize", json={"text": ARTICLE, "method": "textrank", "ratio": 30})
    body = response.json()

    assert response.status_code == 200
    assert body["summary"] == " ".join(s["text"] for s in body["sentences"] if s["selected"])
    assert body["stats"]["original_sentences"] == 13
    assert body["stats"]["summary_sentences"] == 4
    assert body["stats"]["summary_words"] < body["stats"]["original_words"]


def test_cyrillic_text_is_summarized_in_latin():
    response = client.post("/api/summarize", json={"text": "Ово је прва реченица. Ово је друга реченица.", "ratio": 50})

    assert response.status_code == 200
    assert response.json()["summary"].startswith("Ovo je")


def test_unavailable_method_is_rejected():
    response = client.post("/api/summarize", json={"text": ARTICLE, "method": "metoda-2"})

    assert response.status_code == 400


def test_blank_text_and_ratio_out_of_range_are_rejected():
    assert client.post("/api/summarize", json={"text": "   "}).status_code == 422
    assert client.post("/api/summarize", json={"text": ARTICLE, "ratio": 90}).status_code == 422


def test_text_longer_than_page_limit_is_rejected():
    response = client.post("/api/summarize", json={"text": "Reč. " * TOO_MANY_WORDS})

    assert response.status_code == 400
