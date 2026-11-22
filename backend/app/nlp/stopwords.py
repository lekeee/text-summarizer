from functools import cache
from pathlib import Path

STOPWORDS_FILE = Path(__file__).with_name("stopwords_sr.txt")


@cache
def load_stopwords() -> frozenset[str]:
    lines = STOPWORDS_FILE.read_text(encoding="utf-8").splitlines()
    return frozenset(line.strip().lower() for line in lines if line.strip())
