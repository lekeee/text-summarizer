from time import perf_counter

from app.config import settings
from app.nlp.tokenizer import split_sentences
from app.nlp.transliteration import cyrillic_to_latin
from app.schemas.summarize import SentenceScore, SummarizeResponse, SummaryStats
from app.services.summarizers.registry import get_summarizer
from app.services.text_stats import count_words, estimate_pages


class SummarizationError(Exception):
    pass


def summarize_text(text: str, method: str, ratio: int) -> SummarizeResponse:
    summarizer = get_summarizer(method)
    if summarizer is None:
        raise SummarizationError(f"Metod „{method}“ nije dostupan.")

    text = cyrillic_to_latin(text)
    original_words = count_words(text)
    if estimate_pages(original_words) > settings.max_pages:
        raise SummarizationError(f"Tekst je duži od {settings.max_pages} strana.")

    started = perf_counter()
    ranked = summarizer.rank(split_sentences(text), ratio)
    elapsed_ms = round((perf_counter() - started) * 1000)

    selected = [sentence.text for sentence in ranked if sentence.selected]
    summary = " ".join(selected)

    return SummarizeResponse(
        method=method,
        ratio=ratio,
        summary=summary,
        sentences=[SentenceScore(**vars(sentence)) for sentence in ranked],
        stats=SummaryStats(
            original_words=original_words,
            summary_words=count_words(summary),
            original_sentences=len(ranked),
            summary_sentences=len(selected),
        ),
        elapsed_ms=elapsed_ms,
    )
