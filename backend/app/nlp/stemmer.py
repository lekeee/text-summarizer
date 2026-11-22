from threading import Lock

import snowballstemmer

_stemmer = snowballstemmer.stemmer("serbian")
_lock = Lock()


def stem(word: str) -> str:
    with _lock:
        return _stemmer.stemWord(word.lower())
