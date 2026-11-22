from app.nlp.stemmer import stem
from app.nlp.stopwords import load_stopwords


def test_word_forms_share_the_same_stem():
    assert stem("rečenica") == stem("rečenice") == stem("rečenicama")
    assert stem("metode") == stem("metodama")


def test_stem_ignores_case():
    assert stem("Dokumentu") == stem("dokumentu")


def test_common_words_are_stopwords():
    stopwords = load_stopwords()
    assert {"i", "u", "je", "se", "koji", "zbog"} <= stopwords
    assert "sažimanje" not in stopwords
