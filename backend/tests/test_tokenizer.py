from app.nlp.tokenizer import split_sentences, split_words


def test_splits_on_sentence_marks():
    text = "Prva rečenica. Druga rečenica! Da li je ovo treća? Jeste."
    assert split_sentences(text) == [
        "Prva rečenica.",
        "Druga rečenica!",
        "Da li je ovo treća?",
        "Jeste.",
    ]


def test_does_not_split_after_abbreviations():
    text = "Postoje razne metode, npr. TextRank i LexRank. Rad je pregledao dr. Petrović."
    assert split_sentences(text) == [
        "Postoje razne metode, npr. TextRank i LexRank.",
        "Rad je pregledao dr. Petrović.",
    ]


def test_does_not_split_after_ordinal_numbers_and_initials():
    text = "Rad je odbranjen 12. juna 2024. godine. Mentor je bio M. Jovanović."
    assert split_sentences(text) == [
        "Rad je odbranjen 12. juna 2024. godine.",
        "Mentor je bio M. Jovanović.",
    ]


def test_paragraph_without_period_is_separate_sentence():
    text = "Uvod\n\nOvaj rad se bavi\nsažimanjem teksta."
    assert split_sentences(text) == ["Uvod", "Ovaj rad se bavi sažimanjem teksta."]


def test_empty_text_has_no_sentences():
    assert split_sentences("   \n\n ") == []


def test_words_are_lowercase_without_numbers_and_punctuation():
    assert split_words("Sažimanje (2024) je VAŽNO, zar ne?") == ["sažimanje", "je", "važno", "zar", "ne"]


def test_splits_after_serbian_closing_quote():
    text = "Rekao je: „Ovo je citat.“ Zatim je otišao."
    assert split_sentences(text) == ["Rekao je: „Ovo je citat.“", "Zatim je otišao."]
