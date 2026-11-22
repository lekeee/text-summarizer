from pydantic import BaseModel, Field, field_validator

from app.config import settings


class SummarizeRequest(BaseModel):
    text: str
    method: str = "textrank"
    ratio: int = Field(default=30, ge=settings.min_ratio, le=settings.max_ratio)

    @field_validator("text")
    @classmethod
    def text_must_not_be_blank(cls, text: str) -> str:
        if not text.strip():
            raise ValueError("Tekst ne sme biti prazan.")
        return text


class SentenceScore(BaseModel):
    index: int
    text: str
    score: float
    selected: bool


class SummaryStats(BaseModel):
    original_words: int
    summary_words: int
    original_sentences: int
    summary_sentences: int


class SummarizeResponse(BaseModel):
    method: str
    ratio: int
    summary: str
    sentences: list[SentenceScore]
    stats: SummaryStats
    elapsed_ms: int
