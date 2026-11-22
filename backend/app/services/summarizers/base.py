from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class RankedSentence:
    index: int
    text: str
    score: float
    selected: bool


class Summarizer(Protocol):
    def rank(self, sentences: list[str], ratio: int) -> list[RankedSentence]: ...


def sentences_to_keep(total: int, ratio: int) -> int:
    return max(1, round(total * ratio / 100))


def select_best(sentences: list[str], scores: list[float], ratio: int) -> list[RankedSentence]:
    keep = sentences_to_keep(len(sentences), ratio)
    best = set(sorted(range(len(sentences)), key=lambda i: scores[i], reverse=True)[:keep])
    top_score = max(scores, default=0) or 1

    return [
        RankedSentence(
            index=i,
            text=sentence,
            score=round(scores[i] / top_score, 4),
            selected=i in best,
        )
        for i, sentence in enumerate(sentences)
    ]
