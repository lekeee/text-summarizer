import re

ABBREVIATIONS = frozenset({
    "npr", "tj", "itd", "sl", "dr", "mr", "prof", "doc", "dipl", "ing",
    "gdin", "gđa", "gđica", "g", "br", "str", "st", "ul", "tzv", "odn",
    "sv", "god", "v", "vol", "red", "prim", "up", "min", "maks", "mil",
    "mlrd", "tel", "fak", "univ", "inž", "pok", "kap", "gen", "pr", "n",
    "e", "jan", "feb", "mar", "apr", "jun", "jul", "avg", "sep", "okt",
    "nov", "dec",
})

SENTENCE_END = re.compile(r"[.!?…]+[\"”“»')\]]*\s+")
PARAGRAPH_BREAK = re.compile(r"\n\s*\n")
WORD = re.compile(r"[^\W\d_]+")
OPENING_MARKS = "\"„“«(['‘–-"


def split_sentences(text: str) -> list[str]:
    sentences = []
    for paragraph in PARAGRAPH_BREAK.split(text):
        sentences.extend(_split_paragraph(" ".join(paragraph.split())))
    return sentences


def split_words(sentence: str) -> list[str]:
    return WORD.findall(sentence.lower())


def _split_paragraph(paragraph: str) -> list[str]:
    sentences = []
    start = 0
    for match in SENTENCE_END.finditer(paragraph):
        if _is_sentence_end(paragraph, match.start(), match.end()):
            sentences.append(paragraph[start:match.end()].strip())
            start = match.end()
    rest = paragraph[start:].strip()
    if rest:
        sentences.append(rest)
    return sentences


def _is_sentence_end(paragraph: str, mark_position: int, next_position: int) -> bool:
    next_char = paragraph[next_position]
    if not (next_char.isupper() or next_char.isdigit() or next_char in OPENING_MARKS):
        return False
    if paragraph[mark_position] != ".":
        return True
    previous_word = paragraph[:mark_position].rsplit(" ", 1)[-1].lstrip(OPENING_MARKS)
    if previous_word.lower() in ABBREVIATIONS:
        return False
    return not (len(previous_word) == 1 and previous_word.isupper())
