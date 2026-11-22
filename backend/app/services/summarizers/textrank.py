from sumy.models.dom import ObjectDocumentModel, Paragraph, Sentence
from sumy.summarizers.text_rank import TextRankSummarizer as SumyTextRank

from app.nlp.stemmer import stem
from app.nlp.stopwords import load_stopwords
from app.nlp.tokenizer import split_words
from app.services.summarizers.base import RankedSentence, select_best


class SerbianWordTokenizer:
    def to_words(self, sentence: str) -> list[str]:
        return split_words(sentence)


class TextRankSummarizer:
    def __init__(self):
        self._tokenizer = SerbianWordTokenizer()
        self._textrank = SumyTextRank(stem)
        self._textrank.stop_words = load_stopwords()

    def rank(self, sentences: list[str], ratio: int) -> list[RankedSentence]:
        document = self._build_document(sentences)
        ratings = self._textrank.rate_sentences(document)
        scores = [float(ratings[sentence]) for sentence in document.sentences]
        return select_best(sentences, scores, ratio)

    def _build_document(self, sentences: list[str]) -> ObjectDocumentModel:
        paragraph = Paragraph(Sentence(text, self._tokenizer) for text in sentences)
        return ObjectDocumentModel([paragraph])
