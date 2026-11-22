from fastapi.testclient import TestClient

from app.main import app
from tests.sample_files import make_docx, make_pdf

client = TestClient(app)


def upload(file_name: str, content: bytes):
    return client.post("/api/documents/extract", files={"file": (file_name, content)})


def test_extracts_utf8_txt():
    response = upload("rad.txt", "Prva rečenica. Druga rečenica.".encode("utf-8"))
    body = response.json()

    assert response.status_code == 200
    assert body["text"] == "Prva rečenica. Druga rečenica."
    assert body["words"] == 4
    assert body["sentences"] == 2
    assert body["pages"] == 1


def test_extracts_windows_1250_txt():
    response = upload("rad.txt", "Šuma i čvor.".encode("cp1250"))

    assert response.json()["text"] == "Šuma i čvor."


def test_extracts_docx_paragraphs():
    content = make_docx(["Naslov", "Prvi pasus. Drugi deo pasusa."])
    response = upload("rad.docx", content)

    assert response.status_code == 200
    assert response.json()["text"] == "Naslov\n\nPrvi pasus. Drugi deo pasusa."
    assert response.json()["sentences"] == 3


def test_extracts_pdf_and_joins_hyphenated_words():
    content = make_pdf(["Automatsko sa-", "zimanje teksta je korisno."])
    response = upload("rad.pdf", content)

    assert response.status_code == 200
    assert "sazimanje" in response.json()["text"]


def test_rejects_unsupported_extension():
    response = upload("slika.png", b"\x89PNG")

    assert response.status_code == 400
    assert "TXT, DOCX i PDF" in response.json()["detail"]


def test_rejects_broken_pdf_and_empty_file():
    assert upload("rad.pdf", b"ovo nije pdf").status_code == 400
    assert upload("prazan.txt", b"   ").status_code == 400


def test_rejects_document_longer_than_page_limit():
    response = upload("dug.txt", ("Reč. " * 2000).encode("utf-8"))

    assert response.status_code == 400
