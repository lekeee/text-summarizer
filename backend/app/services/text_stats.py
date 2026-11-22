import math

from app.config import settings
from app.nlp.tokenizer import split_words


def count_words(text: str) -> int:
    return len(split_words(text))


def estimate_pages(word_count: int) -> int:
    return math.ceil(word_count / settings.words_per_page)
