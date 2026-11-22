from app.nlp.tokenizer import split_sentences
from app.services.summarizers.base import sentences_to_keep
from app.services.summarizers.textrank import TextRankSummarizer
from tests.sample_texts import ARTICLE

summarizer = TextRankSummarizer()


def test_every_sentence_gets_a_score_between_zero_and_one():
    sentences = split_sentences(ARTICLE)
    ranked = summarizer.rank(sentences, ratio=30)

    assert [s.text for s in ranked] == sentences
    assert all(0 <= s.score <= 1 for s in ranked)
    assert max(s.score for s in ranked) == 1


def test_selects_number_of_sentences_by_ratio():
    sentences = split_sentences(ARTICLE)

    for ratio in (10, 30, 60):
        ranked = summarizer.rank(sentences, ratio)
        assert sum(s.selected for s in ranked) == sentences_to_keep(len(sentences), ratio)


def test_selected_sentences_have_highest_scores():
    ranked = summarizer.rank(split_sentences(ARTICLE), ratio=30)
    lowest_selected = min(s.score for s in ranked if s.selected)
    highest_skipped = max(s.score for s in ranked if not s.selected)

    assert lowest_selected >= highest_skipped


def test_single_sentence_is_its_own_summary():
    ranked = summarizer.rank(["Ovo je jedina rečenica."], ratio=10)

    assert len(ranked) == 1
    assert ranked[0].selected
