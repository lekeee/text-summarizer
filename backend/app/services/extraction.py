import re
from io import BytesIO
from pathlib import Path

from docx import Document
from pypdf import PdfReader

SUPPORTED_EXTENSIONS = {".txt", ".docx", ".pdf"}
TEXT_ENCODINGS = ("utf-8-sig", "cp1250")
HYPHENATED_LINE_BREAK = re.compile(r"(\w)-\n(\w)")


class ExtractionError(Exception):
    pass


def extract_text(file_name: str, content: bytes) -> str:
    extension = Path(file_name).suffix.lower()
    if extension not in SUPPORTED_EXTENSIONS:
        raise ExtractionError("Podržani su samo TXT, DOCX i PDF fajlovi.")

    readers = {".txt": _read_txt, ".docx": _read_docx, ".pdf": _read_pdf}
    text = readers[extension](content).strip()
    if not text:
        raise ExtractionError("U dokumentu nije pronađen tekst.")
    return text


def _read_txt(content: bytes) -> str:
    for encoding in TEXT_ENCODINGS:
        try:
            return content.decode(encoding)
        except UnicodeDecodeError:
            continue
    raise ExtractionError("Kodiranje tekstualnog fajla nije prepoznato.")


def _read_docx(content: bytes) -> str:
    try:
        document = Document(BytesIO(content))
    except Exception as error:
        raise ExtractionError("DOCX fajl nije moguće otvoriti.") from error
    paragraphs = [paragraph.text.strip() for paragraph in document.paragraphs]
    return "\n\n".join(paragraph for paragraph in paragraphs if paragraph)


def _read_pdf(content: bytes) -> str:
    try:
        reader = PdfReader(BytesIO(content))
        pages = [page.extract_text() or "" for page in reader.pages]
    except Exception as error:
        raise ExtractionError("PDF fajl nije moguće otvoriti.") from error
    text = "\n\n".join(page.strip() for page in pages if page.strip())
    return HYPHENATED_LINE_BREAK.sub(r"\1\2", text)
