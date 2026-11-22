from app.schemas.methods import SummaryMethod
from app.services.summarizers.base import Summarizer
from app.services.summarizers.textrank import TextRankSummarizer

METHODS = [
    SummaryMethod(
        id="textrank",
        name="TextRank",
        description="Graf rečenica i PageRank biraju rečenice koje najbolje predstavljaju tekst.",
        kind="ekstraktivni",
        available=True,
    ),
    SummaryMethod(
        id="metoda-2",
        name="Metoda 2",
        description="Biće dodata kasnije.",
        kind=None,
        available=False,
    ),
    SummaryMethod(
        id="metoda-3",
        name="Metoda 3",
        description="Biće dodata kasnije.",
        kind=None,
        available=False,
    ),
]

SUMMARIZERS: dict[str, Summarizer] = {
    "textrank": TextRankSummarizer(),
}


def get_summarizer(method_id: str) -> Summarizer | None:
    return SUMMARIZERS.get(method_id)
