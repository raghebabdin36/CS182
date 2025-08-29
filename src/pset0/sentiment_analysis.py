from typing import TypedDict
from enum import StrEnum


class Sentiment(StrEnum):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    NEUTRAL = "Neutral"


class SentimentSummary(TypedDict):
    sentiment: Sentiment
    positive_percentage: float
    negative_percentage: float
    most_positive_sentence: str
    most_negative_sentence: str


class SentimentAnalyzer:
    def __init__(
        self,
        positive_words: list[str],
        negative_words: list[str],
        negations: list[str],
        intensifiers: list[str],
    ):
        """
        Initializes the SentimentAnalyzer with lists of positive words, negative words, negations, and intensifiers.

        Parameters:
            positive_words (list[str]): A list of words considered positive.
            negative_words (list[str]): A list of words considered negative.
            negations (list[str]): A list of negation words that can invert sentiment.
            intensifiers (list[str]): A list of intensifier words that can amplify sentiment.
        """

        raise NotImplementedError

    def analyze_sentiment(self, sentence: str) -> int:
        punctuation = r"!#$%&'()*+,./:;<=>?@[]^_`{|}\~)"
        raise NotImplementedError

    def get_sentiment_summary(self, text: str) -> SentimentSummary:
        raise NotImplementedError
