from app.nlp.transliteration import cyrillic_to_latin


def test_converts_cyrillic_sentence():
    assert cyrillic_to_latin("Ћирилица и ђак читају књигу.") == "Ćirilica i đak čitaju knjigu."


def test_digraphs_respect_case():
    assert cyrillic_to_latin("Љубав") == "Ljubav"
    assert cyrillic_to_latin("ЉУБАВ") == "LJUBAV"
    assert cyrillic_to_latin("Џеп и њива") == "Džep i njiva"


def test_latin_text_stays_the_same():
    text = "Ovo je već latinica, 2024. godine."
    assert cyrillic_to_latin(text) == text
