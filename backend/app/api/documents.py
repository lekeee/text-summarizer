from fastapi import APIRouter, HTTPException, UploadFile

from app.config import settings
from app.nlp.tokenizer import split_sentences
from app.schemas.documents import ExtractResponse
from app.services.extraction import ExtractionError, extract_text
from app.services.text_stats import count_words, estimate_pages

router = APIRouter(prefix="/documents", tags=["dokumenti"])

MAX_FILE_SIZE = settings.max_file_size_mb * 1024 * 1024


@router.post("/extract", response_model=ExtractResponse)
def extract(file: UploadFile) -> ExtractResponse:
    content = file.file.read(MAX_FILE_SIZE + 1)
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(status_code=413, detail=f"Fajl je veći od {settings.max_file_size_mb} MB.")

    try:
        text = extract_text(file.filename or "", content)
    except ExtractionError as error:
        raise HTTPException(status_code=400, detail=str(error))

    words = count_words(text)
    pages = estimate_pages(words)
    if pages > settings.max_pages:
        raise HTTPException(status_code=400, detail=f"Dokument je duži od {settings.max_pages} strana.")

    return ExtractResponse(
        file_name=file.filename or "",
        text=text,
        words=words,
        sentences=len(split_sentences(text)),
        pages=pages,
    )
