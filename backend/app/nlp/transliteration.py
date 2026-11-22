CYRILLIC_TO_LATIN = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "ђ": "đ", "е": "e",
    "ж": "ž", "з": "z", "и": "i", "ј": "j", "к": "k", "л": "l", "љ": "lj",
    "м": "m", "н": "n", "њ": "nj", "о": "o", "п": "p", "р": "r", "с": "s",
    "т": "t", "ћ": "ć", "у": "u", "ф": "f", "х": "h", "ц": "c", "ч": "č",
    "џ": "dž", "ш": "š",
}

DIGRAPHS = {"Љ": ("Lj", "LJ"), "Њ": ("Nj", "NJ"), "Џ": ("Dž", "DŽ")}


def cyrillic_to_latin(text: str) -> str:
    result = []
    for position, char in enumerate(text):
        if char in DIGRAPHS:
            next_char = text[position + 1] if position + 1 < len(text) else ""
            title_case, upper_case = DIGRAPHS[char]
            result.append(upper_case if next_char.isupper() else title_case)
        elif char.lower() in CYRILLIC_TO_LATIN:
            latin = CYRILLIC_TO_LATIN[char.lower()]
            result.append(latin.upper() if char.isupper() else latin)
        else:
            result.append(char)
    return "".join(result)
