import os

import pytest

from pset0.sentiment_analysis import Sentiment, SentimentAnalyzer, SentimentSummary


def test_sentiment_analysis():
    POSITIVE_WORDS_PATH = os.path.join("data", "positive_words.txt")
    NEGATIVE_WORDS_PATH = os.path.join("data", "negative_words.txt")
    NEGATIONS_PATH = os.path.join("data", "negations.txt")
    INTENSIFIERS_PATH = os.path.join("data", "intensifiers.txt")
    COMMENTS_PATH = os.path.join("data", "comments.txt")

    with open(POSITIVE_WORDS_PATH, "r") as f:
        positive_words = [line.strip() for line in f if line.strip() and not line.startswith(";")]

    with open(NEGATIVE_WORDS_PATH, "r") as f:
        negative_words = [line.strip() for line in f if line.strip() and not line.startswith(";")]

    with open(NEGATIONS_PATH, "r") as f:
        negations = [line.strip() for line in f if line.strip() and not line.startswith(";")]

    with open(INTENSIFIERS_PATH, "r") as f:
        intensifiers = [line.strip() for line in f if line.strip() and not line.startswith(";")]

    with open(COMMENTS_PATH, "r") as f:
        comments = " ".join([line.strip() for line in f if line.strip()])

    test_analyzer = SentimentAnalyzer(positive_words, negative_words, negations, intensifiers)

    assert test_analyzer.analyze_sentiment("HUDS food is delicious.") == 1
    assert test_analyzer.analyze_sentiment("The movie was fun, but the dinner was dissappointing") == 0
    assert test_analyzer.analyze_sentiment("Today drained me.") == -1
    assert test_analyzer.analyze_sentiment("I'm not satisfied with your answer.") == -1
    assert test_analyzer.analyze_sentiment("Remy is a really cute cat.") == 2
    assert test_analyzer.analyze_sentiment("Spot is not a puppy anymore, but still adorable.") == 1

    example_target_summary: SentimentSummary = {
        "sentiment": Sentiment.POSITIVE,
        "positive_percentage": 0.6,
        "negative_percentage": 0.2,
        "most_positive_sentence": "The professors are SERIOUSLY INCREDIBLE, like so overqualified, inspiring, accomplished, and sufficiently engaging",
        "most_negative_sentence": "It was by far the most time-consuming and difficult, out of four undergraduate computer science department classes I took this semester",
    }

    analyzer_summary = test_analyzer.get_sentiment_summary(comments)

    assert analyzer_summary["sentiment"] == example_target_summary["sentiment"]
    assert analyzer_summary["positive_percentage"] == pytest.approx(example_target_summary["positive_percentage"])
    assert analyzer_summary["negative_percentage"] == pytest.approx(example_target_summary["negative_percentage"])
    assert test_analyzer.analyze_sentiment(analyzer_summary["most_positive_sentence"]) == 6
    assert test_analyzer.analyze_sentiment(analyzer_summary["most_negative_sentence"]) == -2